# Zepto Support Assistant

A context-aware support assistant that answers questions about Zepto policies using retrieved document context.

## Project Structure

```text
.
├── main.py
├── prompts.py
├── requirements.txt
└── README.md
```

## Structured Prompt

The structured prompt in `prompts.py` follows these sections:

1. **Role**
2. **Context**
3. **Task**
4. **Format**
5. **Length**

It also contains a negative constraint preventing answers from using information outside the provided context, along with a few-shot example.

## API

Start the server:

```powershell
$env:MOCK_LLM="1"
uvicorn main:app --reload
```

The API will start locally and can be accessed through:

```text
http://127.0.0.1:8000
```

## Example Call 1

A question that can be answered using the retrieved context returns:

```json
{
  "answer": "Based on the retrieved context: Zepto delivers grocery and household essentials...",
  "sources": [
    "doc_01",
    "doc_04",
    "doc_05"
  ],
  "confidence": 1.0
}
```

## Example Call 2

A question outside the supported Zepto policy context returns:

```json
{
  "answer": "I can only answer questions about Zepto policies right now.",
  "sources": [],
  "confidence": 1.0
}
```

## Response Format

The API response contains three fields:

| Field        | Description                                      |
| ------------ | ------------------------------------------------ |
| `answer`     | The assistant's response to the user's question  |
| `sources`    | IDs of the documents used to generate the answer |
| `confidence` | Confidence value associated with the response    |

## Context Restriction

The assistant is designed to answer only from the retrieved context provided to it.

It should not introduce information that is not present in the supplied context.

For questions outside the supported Zepto policy information, the assistant returns the predefined fallback response.

## Running in Development

Run the following commands from the project directory:

```powershell
$env:MOCK_LLM="1"
uvicorn main:app --reload
```

After the server starts, use the API endpoint to send requests and inspect the JSON responses.

## Notes

* `MOCK_LLM="1"` enables the mock LLM behavior for local development.
* The API returns structured JSON responses.
* Source document IDs are included when retrieved context is used.
* Unsupported questions return an empty `sources` list.

### Example Call 1

```json
{
  "answer": "Based on the retrieved context: Zepto delivers grocery and household essentials to serviceable pin codes within 10 to 30 minutes of order confirmation, depending on the customer's delivery zone and current order volume. Standard del",
  "sources": [
    "doc_01"
  ],
  "confidence": 1.0
}
```
### Example Call 2

```json
{
  "answer": "I can only answer questions about Zepto policies right now.",
  "sources": [],
  "confidence": 1.0
}
```