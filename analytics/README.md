# Module 2: Titanic Data Analysis and Machine Learning

## 1. Project Overview

This project analyzes the Titanic passenger dataset and builds machine learning models to predict passenger survival. It also uses Linear Regression to predict ticket fares.

## 2. Technologies Used

* Python
* Pandas and NumPy
* Matplotlib and Seaborn
* Scikit-learn
* Imbalanced-learn
* Joblib
* Jupyter Notebook

## 3. Setup Instructions

Activate the existing virtual environment from the project root:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required libraries:

```powershell
python -m pip install -r requirements.txt
```

## 4. How to Run the Project

Run the notebooks in this order:

1. `01_eda.ipynb` — Data cleaning, analysis and visualization.
2. `02_modeling.ipynb` — Classification, regression, evaluation and model saving.

Both notebooks should run from the `analytics` directory. The original dataset is stored in `titanic.csv`.

To test the saved model:

```powershell
cd analytics
python test_model.py
```

## 5. Data Cleaning

The original dataset contains missing values.

| Column      | Missing percentage | Cleaning decision    |
| ----------- | -----------------: | -------------------- |
| Age         |     [Your result]% | Median imputation    |
| Embarked    |     [Your result]% | Remove affected rows |
| Embark town |     [Your result]% | Remove affected rows |
| Deck        |     [Your result]% | Remove column        |

The original dataset was preserved as `titanic.csv`. A separate `titanic_cleaned.csv` was created for EDA.

During modeling, the original CSV was used so that missing ages could be imputed using training data only.

## 6. Exploratory Data Analysis

### Univariate Analysis

* Age outliers: [Your result]
* Fare outliers: [Your result]
* Mean fare: [Your result]
* Median fare: [Your result]
* Mode fare: [Your result]

Fare distribution: [Explain whether it is right-skewed, left-skewed or approximately symmetric.]

### Survival Analysis

| Group        |  Survival rate |
| ------------ | -------------: |
| Female       | [Your result]% |
| Male         | [Your result]% |
| First class  | [Your result]% |
| Second class | [Your result]% |
| Third class  | [Your result]% |

### Correlation Analysis

The two strongest correlations were:

1. [First variable pair]: [Correlation coefficient and interpretation]
2. [Second variable pair]: [Correlation coefficient and interpretation]

Correlation does not establish causation.

### Chart Interpretations

**Chart 1 — Survival by Sex**

[Write 2–4 sentences describing your observations.]

**Chart 2 — Survival by Class and Sex**

[Write 2–4 sentences describing your observations.]

**Chart 3 — Age and Survival**

[Write 2–4 sentences describing your observations.]

**Chart 4 — Fare, Class and Survival**

[Write 2–4 sentences describing your observations.]

## 7. Classification Models

Three models were trained:

* Logistic Regression
* Decision Tree
* Random Forest

| Model               | Accuracy | Precision | Recall |  F1 | AUC |
| ------------------- | -------: | --------: | -----: | --: | --: |
| Logistic Regression |      [ ] |       [ ] |    [ ] | [ ] | [ ] |
| Decision Tree       |      [ ] |       [ ] |    [ ] | [ ] | [ ] |
| Random Forest       |      [ ] |       [ ] |    [ ] | [ ] | [ ] |

## 8. Class-Imbalance Comparison

| Strategy         | Precision | Recall |  F1 |
| ---------------- | --------: | -----: | --: |
| Baseline         |       [ ] |    [ ] | [ ] |
| Balanced weights |       [ ] |    [ ] | [ ] |
| SMOTE            |       [ ] |    [ ] | [ ] |

[Explain the observed differences and the trade-off between precision and recall.]

## 9. Random Forest Tuning

* Best parameters: [Your result]
* Cross-validation F1: [Your result]
* OOB score: [Your result]

[Explain whether tuning improved the results compared with the original Random Forest.]

## 10. Ticket Fare Regression

Linear Regression was used to predict ticket fares.

| Metric      | Result |
| ----------- | -----: |
| MAE         |    [ ] |
| RMSE        |    [ ] |
| R²          |    [ ] |
| Adjusted R² |    [ ] |

**Residual plot interpretation:** [Describe whether the residuals show constant spread, increasing spread or another pattern.]

## 11. Final Model Selection

Selected classifier: [Model name]

[Write 3–5 sentences explaining your selection using actual accuracy, precision, recall, F1 and AUC results. Discuss relevant trade-offs.]

## 12. Model Saving and Verification

The selected classifier and its preprocessing pipeline were saved as `titanic_survival_pipeline.joblib`.

The saved model was reloaded successfully, and its predictions matched those of the original pipeline.

The independent `test_model.py` script also successfully loaded the model and generated a prediction.

## 13. Conclusion

This module demonstrates data cleaning, exploratory data analysis, classification, class-imbalance handling, hyperparameter tuning, regression and model persistence.
