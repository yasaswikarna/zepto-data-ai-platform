import joblib
import pandas as pd

# Load the saved model
model = joblib.load(
    "titanic_survival_pipeline.joblib"
)

# Example passenger
passenger = pd.DataFrame([{
    "pclass": 2,
    "sex": "female",
    "age": 25,
    "sibsp": 0,
    "parch": 0,
    "fare": 30.0,
    "embarked": "S"
}])

prediction = model.predict(passenger)[0]

print("Prediction:", prediction)

if prediction == 1:
    print("Predicted outcome: Survived")
else:
    print("Predicted outcome: Did not survive")