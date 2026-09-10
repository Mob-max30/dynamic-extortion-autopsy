import pandas as pd
import numpy as np
import os
import uuid
from datetime import datetime, timedelta

def generate_hybrid_pricing_data(n_rows=35000):
    """
    Generates a 21-dimensional hybrid-synthetic dataset for Bangalore ride-hailing forensics.
    Utilizes pure vectorized NumPy array operations to simulate complex physical logistics
    and algorithmic behavioral pricing (digital telemetry exploitation).
    """
    
    # 1. INITIALIZATION & SEEDING
    # Setting seed ensures the random distributions remain reproducible across different machines
    np.random.seed(42)
    print(f"Initializing data synthesis for {n_rows} ride queries...")
    
    # 2. GEOSPATIAL & TEMPORAL BASELINE
    hubs = [
        'Whitefield', 'Koramangala', 'Indiranagar', 'Electronic_City', 
        'HSR_Layout', 'Bellandur', 'Marathahalli', 'Peenya', 'Hebbal', 'Malleshwaram'
    ]
    pickup_hubs = np.random.choice(hubs, n_rows)
    drop_hubs = np.random.choice(hubs, n_rows)

    # Vectorized cleanup: Prevent pickup and drop from being the exact same hub
    mask = pickup_hubs == drop_hubs
    drop_hubs[mask] = np.roll(drop_hubs, 1)[mask]

    # Distance generation using a Gamma distribution for organic, right-skewed realistic distances
    distances = np.round(np.random.gamma(shape=3.0, scale=3.5, size=n_rows) + 1.5, 1)
    distances = np.clip(distances, 2.0, 35.0)

    # Time distribution (Bimodal: peaking at morning office hours and evening rush)
    hour_probabilities = [0.01, 0.01, 0.01, 0.01, 0.02, 0.04, 0.06, 0.07, 0.10, 0.08, 
                          0.05, 0.04, 0.04, 0.04, 0.04, 0.05, 0.06, 0.09, 0.09, 0.05, 
                          0.02, 0.01, 0.01, 0.00]
    
    hours = np.random.choice(np.arange(24), n_rows, p=hour_probabilities)
    minutes = np.random.randint(0, 60, n_rows)
    days = np.random.randint(0, 180, n_rows)

    start_date = np.datetime64('2026-03-01')
    timestamps = start_date + days.astype('timedelta64[D]') + hours.astype('timedelta64[h]') + minutes.astype('timedelta64[m]')
    days_of_week = (days + 6) % 7 

    # 3. DYNAMIC PHYSICAL CONSTRAINTS (Traffic & Weather)
    traffic_conditions = np.where(
        (hours >= 8) & (hours <= 10) | (hours >= 17) & (hours <= 20), 
        np.random.choice(['Gridlock', 'Heavy', 'Moderate'], n_rows, p=[0.4, 0.5, 0.1]),
        np.random.choice(['Moderate', 'Free_Flow', 'Light'], n_rows, p=[0.2, 0.6, 0.2])
    )

    weather = np.random.choice(
        ['Clear', 'Light_Rain', 'Heavy_Downpour', 'Thunderstorm'], 
        n_rows, 
        p=[0.75, 0.15, 0.08, 0.02]
    )

    # Calculating time penalties based on physical constraints
    traffic_penalties = np.where(traffic_conditions == 'Gridlock', 4.5,
                        np.where(traffic_conditions == 'Heavy', 3.0,
                        np.where(traffic_conditions == 'Moderate', 1.5, 0.0)))
    
    rain_penalties = np.where(weather == 'Heavy_Downpour', 2.0,
                     np.where(weather == 'Thunderstorm', 3.5, 0.0))

    # Base duration calculation with organic statistical noise added
    ride_duration_min = np.round((distances * 3.0) + (distances * traffic_penalties) + (distances * rain_penalties) + np.random.normal(0, 3, n_rows))
    ride_duration_min = np.clip(ride_duration_min, 5, 180).astype(int)

    # 4. DIGITAL TELEMETRY (User & Device Profiling)
    device_os = np.random.choice(['iOS', 'Android'], n_rows, p=[0.35, 0.65])
    
    # Nested conditional to assign device tiers logically based on OS
    device_tier = np.where(device_os == 'iOS', 
                           np.random.choice(['Premium', 'Mid_Range'], n_rows, p=[0.8, 0.2]),
                           np.random.choice(['Premium', 'Mid_Range', 'Budget'], n_rows, p=[0.2, 0.5, 0.3]))

    battery_pct = np.random.randint(1, 101, n_rows)
    
    # App open counts spike dynamically if the user is stuck in bad traffic or rain (Poisson distribution)
    app_open_count = np.where((traffic_conditions == 'Gridlock') | (weather == 'Heavy_Downpour'),
                              np.random.poisson(lam=4, size=n_rows) + 1,
                              np.random.poisson(lam=1.5, size=n_rows) + 1)
    
    account_tenure_months = np.random.randint(1, 48, n_rows)
    
    # Historical elasticity: Older accounts are modeled to be slightly more tolerant of surges
    historical_acceptance = np.clip(np.random.normal(0.6, 0.2, n_rows) + (account_tenure_months * 0.005), 0.1, 0.9)

    # 5. THE ALGORITHMIC PRICING ENGINE (Vectorized Logic)
    print("Applying vectorized pricing algorithms and behavioral surcharges...")
    legal_meter = 30.0 + np.maximum(0, (distances - 2.0) * 15.0)

    algo_multiplier = np.ones(n_rows)
    
    # Stacking physical environment surcharges
    algo_multiplier += np.where(traffic_conditions == 'Gridlock', 0.45, 0)
    algo_multiplier += np.where(traffic_conditions == 'Heavy', 0.25, 0)
    algo_multiplier += np.where(weather == 'Thunderstorm', 0.80, 0)
    algo_multiplier += np.where(weather == 'Heavy_Downpour', 0.50, 0)
    
    # Stacking digital telemetry and profiling surcharges
    algo_multiplier += np.where(device_tier == 'Premium', 0.12, 0)
    algo_multiplier -= np.where(device_tier == 'Budget', 0.08, 0)
    algo_multiplier += np.where((battery_pct <= 15) & (app_open_count > 3), 0.35, 0) 
    algo_multiplier += np.where(historical_acceptance > 0.75, 0.10, 0) 

    # Adding continuous normal noise to prevent perfectly flat chart lines in EDA
    algo_multiplier *= np.random.normal(1.0, 0.05, n_rows)
    algo_multiplier = np.clip(algo_multiplier, 0.9, 3.5)
    
    app_quoted_fare = np.round(legal_meter * algo_multiplier, 0)
    competitor_diff = np.round(np.random.normal(0, 20, n_rows), 0) 

    # 6. MARKET CHURN SIMULATION (User & Driver Behavior)
    # User acceptance probability drops if surge is high, unless desperate
    prob_accept = 0.8 - (algo_multiplier * 0.15) 
    prob_accept += np.where(battery_pct <= 15, 0.25, 0)
    prob_accept += np.where(weather == 'Heavy_Downpour', 0.20, 0)
    prob_accept += np.where(competitor_diff > 30, 0.20, 0) 
    prob_accept = np.clip(prob_accept, 0.05, 0.95)

    # Driver cancellation probability spikes for short distances in massive gridlock
    prob_cancel = np.where((distances < 5.0) & (traffic_conditions == 'Gridlock'), 0.60, 0.10)
    
    random_draw = np.random.rand(n_rows)
    final_status = np.where(random_draw < prob_accept,
                            np.where(np.random.rand(n_rows) < prob_cancel, 'Cancelled_By_Driver', 'Ride_Accepted'),
                            'User_Abandoned_App')

    # 7. ASSEMBLE DATAFRAME
    df = pd.DataFrame({
        'Query_ID': [str(uuid.uuid4())[:8] for _ in range(n_rows)],
        'Query_Timestamp': timestamps,
        'Day_of_Week': days_of_week,
        'Hour_of_Day': hours,
        'Pickup_Hub': pickup_hubs,
        'Drop_Hub': drop_hubs,
        'Base_Distance_KM': distances,
        'Est_Ride_Duration_Min': ride_duration_min,
        'Traffic_Condition': traffic_conditions,
        'Weather_Condition': weather,
        'User_Device_OS': device_os,
        'Device_Model_Tier': device_tier,
        'Battery_Level_Pct': battery_pct,
        'App_Open_Count_Last_1hr': app_open_count,
        'User_Account_Tenure_Months': account_tenure_months,
        'Historical_Acceptance_Rate': np.round(historical_acceptance, 2),
        'Legal_Meter_Fare_INR': legal_meter,
        'Surge_Multiplier_Applied': np.round(algo_multiplier, 2),
        'App_Quoted_Fare_INR': app_quoted_fare,
        'Competitor_Price_Diff_INR': competitor_diff,
        'Final_Ride_Status': final_status
    })

    # 8. EXPORT TO CSV
    output_filename = 'Bangalore_Advanced_Ride_Forensics.csv'
    df.to_csv(output_filename, index=False)
    file_size_mb = os.path.getsize(output_filename) / (1024 * 1024)
    print(f"Success! Dataset exported as {output_filename} ({file_size_mb:.2f} MB)")

    # 9. STATISTICAL PROOF OUTPUT
    df['Algorithmic_Markup_INR'] = df['App_Quoted_Fare_INR'] - df['Legal_Meter_Fare_INR']
    critical_battery = df[df['Battery_Level_Pct'] <= 15]['Algorithmic_Markup_INR']
    safe_battery = df[df['Battery_Level_Pct'] > 15]['Algorithmic_Markup_INR']

    print("\n" + "="*45)
    print("   ALGORITHMIC SURGE FORENSICS (PROOF)")
    print("="*45)
    print(f"Average Extra Markup (Safe Battery):     {safe_battery.mean():.2f} INR")
    print(f"Average Extra Markup (Critical Battery): {critical_battery.mean():.2f} INR")
    print("-" * 45)
    print(f"Markup Variance (Critical Battery):      {critical_battery.var():.2f}")
    print(f"Standard Deviation (Critical Battery):   {critical_battery.std():.2f}")
    print("="*45 + "\n")

if __name__ == "__main__":
    generate_hybrid_pricing_data()
