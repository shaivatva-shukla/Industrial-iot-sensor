import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_and_evaluate():
    print("Loading data from SQLite database...")
    
    # 1. Connect to the database and query the features
    db_name = 'sensor_database.db'
    with sqlite3.connect(db_name) as conn:
        df = pd.read_sql_query("SELECT * FROM sensor_features", conn)
        
    print(f"Dataset loaded successfully with {len(df)} rows.")

    # 2. Define Features (X) and Target (y)
    # We drop the timestamp (not a numeric feature) and our target label
    # Notice we are including the specific physical constraint (pipe_length_cm) 
    # and our engineered features (temp_5min_ma, pressure_5min_ma, impurity_mass_gradient)
    X = df.drop(columns=['timestamp', 'anomaly_detected'])
    y = df['anomaly_detected']

    # 3. Split the data (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training set: {len(X_train)} rows | Testing set: {len(X_test)} rows")

    # 4. Initialize and Train the Model
    print("\nTraining Logistic Regression model...")
    # max_iter=1000 ensures the gradient descent converges properly
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # 5. Predict and Evaluate
    print("Evaluating model performance on test data:\n")
    y_pred = model.predict(X_test)
    
    # The classification report shows Precision, Recall, and F1-Score
    report = classification_report(y_test, y_pred, target_names=["Normal (0)", "Anomaly (1)"])
    print(report)

if __name__ == "__main__":
    train_and_evaluate()