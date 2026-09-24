
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/"
books = []

for page in range(1, 6):
    url = f"{BASE_URL}page-{page}.html"

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.select("article.product_pod"):
        title = item.select_one("h3 a")["title"]
        price = item.select_one(".price_color").get_text(strip=True)

        rating_classes = item.select_one(".star-rating")["class"]
        star_rating = next(
            (r for r in rating_classes if r != "star-rating"),
            None
        )

        availability = item.select_one(
            ".availability"
        ).get_text(" ", strip=True)

        # Open the individual book page to find its category.
        book_url = requests.compat.urljoin(
            url, item.select_one("h3 a")["href"]
        )

        detail_response = requests.get(book_url, timeout=20)
        detail_response.raise_for_status()

        detail_soup = BeautifulSoup(
            detail_response.text, "html.parser"
        )

        category = detail_soup.select(
            ".breadcrumb li a"
        )[-1].get_text(strip=True)

        books.append({
            "title": title,
            "price": price,
            "star_rating": star_rating,
            "availability": availability,
            "category": category
        })

    print(f"Finished page {page}")

df = pd.DataFrame(books)

print(df.head())
print("Total books:", len(df))
print("Categories:", df["category"].nunique())




# STEP 2: DATA CLEANING

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# Convert prices to numbers.
df["price_gbp"] = pd.to_numeric(
    df["price"].str.replace(
        r"[^0-9.]", "", regex=True
    ),
    errors="coerce"
)

# Convert text ratings into integers.
df["rating"] = df["star_rating"].map(rating_map)

# Convert availability into boolean values.
df["in_stock"] = df["availability"].apply(
    lambda x: (
        True if x.lower().startswith("in stock")
        else False if x.lower().startswith("out of stock")
        else None
    )
)

# Remove records with missing essential information.
df = df.dropna(
    subset=["title", "category", "rating", "in_stock"]
).copy()

df = df[
    (df["title"].str.strip() != "") &
    (df["category"].str.strip() != "")
].copy()

# Fill missing prices with the median.
median_price = df["price_gbp"].median()
df["price_gbp"] = df["price_gbp"].fillna(median_price)

# Convert ratings to integer and availability to boolean.
df["rating"] = df["rating"].astype(int)
df["in_stock"] = df["in_stock"].astype(bool)

# Fixed project-defined conversion rate.
GBP_TO_INR = 105.50

df["price_inr"] = (
    df["price_gbp"] * GBP_TO_INR
).round(2)

df = df.drop_duplicates(
    subset=["title", "category"]
).reset_index(drop=True)

# Validate the cleaned data.
assert len(df) >= 60, "Fewer than 60 books collected"
assert df["category"].nunique() >= 3
assert df["rating"].between(1, 5).all()
assert df["price_gbp"].notna().all()

print("\nCLEANED DATA")
print(df.head())
print(df.dtypes)
print("Total cleaned books:", len(df))

df.to_csv("data_pipeline/cleaned_books.csv", index=False)


# STEP 3: CREATE AND LOAD THE DATABASE

import sqlite3

# Create the database
conn = sqlite3.connect(
    "data_pipeline/zepto_books.db"
)

conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.cursor()

# Delete old tables if they exist
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("DROP TABLE IF EXISTS categories")

# Create categories table
cursor.execute("""
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL UNIQUE
)
""")

# Create books table
cursor.execute("""
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    price_gbp REAL NOT NULL,
    price_inr REAL NOT NULL,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    in_stock INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
)
""")

# Insert categories
categories = sorted(df["category"].unique())

cursor.executemany(
    "INSERT INTO categories (category_name) VALUES (?)",
    [(name,) for name in categories]
)

category_ids = dict(
    cursor.execute(
        "SELECT category_name, category_id FROM categories"
    ).fetchall()
)

# Insert cleaned books
records = [
    (
        row.title,
        float(row.price_gbp),
        float(row.price_inr),
        int(row.rating),
        int(row.in_stock),
        category_ids[row.category]
    )
    for row in df.itertuples(index=False)
]

cursor.executemany("""
INSERT INTO books (
    title, price_gbp, price_inr,
    rating, in_stock, category_id
)
VALUES (?, ?, ?, ?, ?, ?)
""", records)

conn.commit()

print("\nDATABASE CREATED")
print("Books inserted:", len(records))
print("Categories inserted:", len(categories))




# STEP 4: SQL QUERIES

queries = {
    "1_in_stock": """
        SELECT title, price_gbp
        FROM books
        WHERE in_stock = 1
        LIMIT 10
    """,

    "2_most_expensive": """
        SELECT title, price_gbp, price_inr
        FROM books
        ORDER BY price_gbp DESC
        LIMIT 10
    """,

    "3_distinct_categories": """
        SELECT DISTINCT category_name
        FROM categories
        ORDER BY category_name
    """,

    "4_price_range": """
        SELECT title, price_gbp
        FROM books
        WHERE price_gbp BETWEEN 20 AND 40
        ORDER BY price_gbp
    """,

    "5_high_ratings": """
        SELECT title, rating
        FROM books
        WHERE rating IN (4, 5)
        ORDER BY rating DESC, title
        LIMIT 10
    """,

    "6_join": """
        SELECT
            b.book_id,
            b.title,
            b.rating,
            c.category_name
        FROM books AS b
        JOIN categories AS c
            ON b.category_id = c.category_id
        ORDER BY b.book_id
    """
}

# Execute queries and save the results

with open(
    "data_pipeline/sql_results.md",
    "w",
    encoding="utf-8"
) as output:

    for name, sql in queries.items():

        result = pd.read_sql_query(sql, conn)

        print(f"\n{name}")
        print(result.to_string(index=False))

        output.write(f"## {name}\n\n")

        output.write(
            "```sql\n" + sql.strip() + "\n```\n\n"
        )

    
        output.write(
            "```text\n"
            + result.to_string(index=False)
            + "\n```\n\n"
        )

print("\nSQL query results saved.")


# STEP 5: SQL VS PANDAS

# Read two SQL query results into pandas
in_stock_df = pd.read_sql_query(
    queries["1_in_stock"], conn
)

sql_join_df = pd.read_sql_query(
    queries["6_join"], conn
)

# Read both complete database tables
books_df = pd.read_sql_query(
    "SELECT * FROM books", conn
)

categories_df = pd.read_sql_query(
    "SELECT * FROM categories", conn
)

# Reproduce the SQL JOIN using pandas
pandas_join_df = pd.merge(
    books_df,
    categories_df,
    on="category_id",
    how="inner"
)

# Select the same columns in the same order
columns = [
    "book_id", "title", "rating", "category_name"
]

pandas_join_df = (
    pandas_join_df[columns]
    .sort_values("book_id")
    .reset_index(drop=True)
)

sql_join_df = sql_join_df.reset_index(drop=True)

# Check whether both results match
pd.testing.assert_frame_equal(
    sql_join_df,
    pandas_join_df
)

print("\nSQL JOIN RESULT")
print(sql_join_df.head(10).to_string(index=False))

print("\nPANDAS MERGE RESULT")
print(pandas_join_df.head(10).to_string(index=False))

print("\nSUCCESS: SQL JOIN and pandas merge match!")

# Save the comparison results
with open(
    "data_pipeline/pandas_comparison.md",
    "w",
    encoding="utf-8"
) as output:

    output.write("# SQL and pandas comparison\n\n")

    output.write("## First SQL result: in-stock books\n\n")
    output.write(
        "```text\n"
        + in_stock_df.to_string(index=False)
        + "\n```\n\n"
    )

    output.write("## SQL JOIN result\n\n")
    output.write(
        "```text\n"
        + sql_join_df.to_string(index=False)
        + "\n```\n\n"
    )

    output.write("## pandas merge result\n\n")
    output.write(
        "```text\n"
        + pandas_join_df.to_string(index=False)
        + "\n```\n\n"
    )

    output.write(
        "Both results are equivalent. "
        "The comparison passed using "
        "pd.testing.assert_frame_equal().\n"
    )

# Close the database after completing all five steps
conn.close()
  

