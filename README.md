# Industrial IoT Sensor Analytics Pipeline



##  Overview
Manufacturing plants and chemical engineering labs collect millions of data points from physical sensors, but rarely utilize this raw data to predict equipment failures. 

This project bridges the gap between physical thermodynamics and digital data infrastructure. It is an automated, end-to-end pipeline that ingests noisy IoT sensor data from fluid mechanics tables and distillation columns, engineers time-series features, and deploys a machine learning classification model to predict imminent system anomalies before a catastrophic failure occurs.

##  The Physics & Domain Logic
Unlike standard generic datasets, the data flowing through this pipeline is grounded in physical realities:
* **Fluid Mechanics Constraints:** Pipe length parameters ($L$) are strictly standardized to exactly 186 cm across test cases.
* **Mass Transfer:** Distillation supply feed calculations specifically track the mass of impurities ($M$) in grams, utilizing rate-of-change gradients to detect fouling or blockages.
* **Realistic Sensor Noise:** The data simulates real-world industrial environments by accounting for gradual sensor drift, latent heat delays, and minor calibration errors, preventing the model from relying on artificial, perfectly linear splits.

##  Pipeline Architecture

### 1. Data Mocking & Ingestion (`data_generator.py`)
Generates 10,000 rows of time-series IoT logs tracking temperature, pressure, and impurity mass. Injects subtle, sub-threshold anomalies to simulate early-warning equipment failures (e.g., slow valve leaks) rather than obvious catastrophic bursts.

### 2. ETL & Feature Engineering (`etl_pipeline.py`)
Processes the raw CSV data using **Pandas**. 
* Calculates 5-minute rolling averages for heat and pressure.
* Computes gradients (rate of change) for the mass of impurities.
* Cleans null values and loads the processed features into a local **SQLite** database (`sensor_features` table) for efficient querying.

### 3. Predictive Maintenance Model (`train_model.py`)
Queries the SQLite database and trains a **Scikit-Learn Logistic Regression** model. By analyzing the engineered time-series features alongside raw inputs, the model successfully identifies overlapping, non-obvious equipment anomalies, outputting a comprehensive classification report (Precision, Recall, F1-Score).

##  Tech Stack
* **Data Engineering & ETL:** Python, Pandas, NumPy
* **Database:** SQLite
* **Machine Learning:** Scikit-Learn

##  How to Run Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/shaivatva-shukla/Industrial-iot-sensor.git](https://github.com/shaivatva-shukla/Industrial-iot-sensor.git)
cd Industrial-iot-sensor
