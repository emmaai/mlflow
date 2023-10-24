import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

import mlflow.sklearn
from mlflow.models import infer_signature

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment(experiment_id="2")
mlflow.autolog()

db = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

# Create and train models.
rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
rf.fit(X_train, y_train)

# Use the model to make predictions on the test dataset.
predictions = rf.predict(X_test)
signature = infer_signature(X_test, predictions)

mlflow.sklearn.log_model(
    sk_model=rf,
    artifact_path="sklearn-model",
    signature=signature,
    registered_model_name="sk-learn-random-forest-reg-model",
)

print(f"default artifacts URI: '{mlflow.get_artifact_uri()}'")
