import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sensor_data(file_path='sensor_data.csv', n_rows=10000):
    print(f"Generating {n_rows} rows of mock sensor data...")
    np.random.seed(42)  # For reproducibility
    
    # 1. Generate time series (1 reading per minute)
    start_time = datetime.now()
    timestamps = [start_time + timedelta(minutes=i) for i in range(n_rows)]
    
    # 2. Fluid Mechanics constraint: Pipe length (L) strictly 186 cm
    L = np.full(n_rows, 186.0) 
    
    # 3. Distillation constraint: Mass of impurities (M) in grams
    M = np.random.uniform(0.5, 25.0, n_rows) 
    
    # 4. Base physical sensor readings (normal operation)
    # INCREASED NOISE: Higher standard deviations represent real-world sensor fluctuations
    temperature = np.random.normal(75.0, 8.0, n_rows)  # Std dev increased from 3.0 to 8.0
    pressure = np.random.normal(101.3, 5.0, n_rows)    # Std dev increased from 1.5 to 5.0
    
    # 5. Inject physical anomalies (Subtle Spikes)
    anomaly_detected = np.zeros(n_rows, dtype=int)
    num_anomalies = int(n_rows * 0.04)
    anomaly_indices = np.random.choice(n_rows, num_anomalies, replace=False)
    
    for idx in anomaly_indices:
        # DECREASED SPIKES: These values now overlap with the natural noise (the upper tails)
        # of the normal data, forcing the model to rely on combinations of features.
        temperature[idx] += np.random.uniform(6.0, 12.0) 
        pressure[idx] += np.random.uniform(4.0, 9.0)
        M[idx] += np.random.uniform(3.0, 8.0)
        anomaly_detected[idx] = 1

    # Compile into DataFrame
    df = pd.DataFrame({
        'timestamp': timestamps,
        'pipe_length_cm': L,
        'impurity_mass_g': M,
        'temperature_c': temperature,
        'pressure_kpa': pressure,
        'anomaly_detected': anomaly_detected
    })
    
    # Save to CSV
    df.to_csv(file_path, index=False)
    print(f"Success! Data saved to {file_path}")

if __name__ == "__main__":
    generate_sensor_data(file_path='sample_sensor_data.csv', n_rows=50)