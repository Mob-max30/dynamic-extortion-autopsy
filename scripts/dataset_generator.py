"""
Dynamic Extortion Autopsy
Dataset Generator for Bangalore Ride Pricing Forensics

Synthesizes high fidelity ride telemetry bridging physical road conditions
with predatory pricing triggers like battery drain and app refresh frequency.
"""

import numpy as np
import pandas as pd


def generate_ride_forensics_dataset(n_samples=50000, random_seed=42):
    np.random.seed(random_seed)

    # Spatial and Temporal Features
    locations = np.array([
        "Koramangala", "Indiranagar", "Whitefield", "Electronic City",
        "HSR Layout", "Bellandur", "Marathahalli", "MG Road", "Hebbal", "JP Nagar"
    ])
    pickup_locations = locations[np.random.randint(0, len(locations), size=n_samples)]
    drop_locations = locations[np.random.randint(0, len(locations), size=n_samples)]

    hour_of_day = np.random.randint(0, 24, size=n_samples)
    is_peak_hour = np.where(
        ((hour_of_day >= 8) & (hour_of_day <= 11)) | ((hour_of_day >= 17) & (hour_of_day <= 21)),
        1,
        0
    )

    # Physical Environment
    trip_distance_km = np.round(np.random.uniform(2.0, 35.0, size=n_samples), 2)
    rainfall_mm = np.round(np.random.exponential(scale=12.0, size=n_samples), 1)
    is_monsoon_rain = np.where(rainfall_mm > 15.0, 1, 0)

    base_traffic_index = np.random.uniform(1.0, 5.0, size=n_samples)
    traffic_multiplier = base_traffic_index + (is_peak_hour * 2.5) + (is_monsoon_rain * 2.0)
    traffic_multiplier = np.clip(traffic_multiplier, 1.0, 10.0)

    # Digital Telemetry and User Desperation Indicators
    battery_percentage = np.random.beta(a=2.0, b=2.0, size=n_samples) * 100
    battery_percentage = np.round(np.clip(battery_percentage, 1.0, 100.0), 1)
    is_critical_battery = np.where(battery_percentage <= 15.0, 1, 0)

    app_reopen_count = np.random.poisson(lam=2.5, size=n_samples)
    app_reopen_count = np.where(is_critical_battery == 1, app_reopen_count + np.random.poisson(lam=3.0, size=n_samples), app_reopen_count)
    app_reopen_count = np.clip(app_reopen_count, 1, 25)

    # Device Profiling (0 for Budget, 1 for Midrange, 2 for Premium)
    device_tier_code = np.random.choice([0, 1, 2], size=n_samples, p=[0.45, 0.35, 0.20])
    device_tier_names = np.array(["Budget Android", "Midrange Android", "Premium Flagship iPhone"])
    device_tier = device_tier_names[device_tier_code]

    # Baseline Financial Calculations
    base_fare_inr = 50.0 + (trip_distance_km * 14.5)

    # Physical Demand Surge
    traffic_surge = 1.0 + (traffic_multiplier * 0.12)
    weather_surge = 1.0 + (is_monsoon_rain * 0.35)

    # Algorithmic Predatory Markup Factors
    # Battery exploitation: Lower battery unlocks steeper pricing penalty
    battery_desperation_factor = np.where(
        battery_percentage <= 10.0,
        0.45,
        np.where(
            battery_percentage <= 20.0,
            0.25,
            0.0
        )
    )

    # Reopen exploitation: Repeated searching signals captive demand
    reopen_desperation_factor = np.clip((app_reopen_count - 2) * 0.04, 0.0, 0.40)

    # Device tier markup: Hardware profiling penalty
    device_markup_factor = np.where(
        device_tier_code == 2,
        0.30,
        np.where(
            device_tier_code == 1,
            0.10,
            0.0
        )
    )

    # Total Multiplier
    predatory_multiplier = 1.0 + battery_desperation_factor + reopen_desperation_factor + device_markup_factor
    physical_multiplier = traffic_surge * weather_surge
    total_surge_multiplier = np.round(physical_multiplier * predatory_multiplier, 2)
    total_surge_multiplier = np.clip(total_surge_multiplier, 1.0, 5.0)

    quoted_fare_inr = np.round(base_fare_inr * total_surge_multiplier, 2)
    algorithmic_markup_inr = np.round(quoted_fare_inr - (base_fare_inr * physical_multiplier), 2)
    algorithmic_markup_inr = np.clip(algorithmic_markup_inr, 0.0, None)

    # Ride Status Simulation
    status_codes = np.array(["Completed", "Cancelled by Driver", "Cancelled by User", "Timeout"])
    cancellation_risk = (
        (quoted_fare_inr / base_fare_inr) * 0.15 +
        (traffic_multiplier * 0.05) +
        (is_critical_battery * 0.10)
    )
    cancellation_risk = np.clip(cancellation_risk, 0.05, 0.85)

    random_uniform = np.random.uniform(0.0, 1.0, size=n_samples)
    ride_status_indices = np.where(
        random_uniform < (1.0 - cancellation_risk),
        0,
        np.where(
            random_uniform < (1.0 - (cancellation_risk * 0.5)),
            1,
            np.where(
                random_uniform < (1.0 - (cancellation_risk * 0.2)),
                2,
                3
            )
        )
    )
    ride_status = status_codes[ride_status_indices]

    dataset = pd.DataFrame({
        "trip_id": np.arange(100001, 100001 + n_samples),
        "pickup_location": pickup_locations,
        "drop_location": drop_locations,
        "hour_of_day": hour_of_day,
        "is_peak_hour": is_peak_hour,
        "trip_distance_km": trip_distance_km,
        "rainfall_mm": rainfall_mm,
        "is_monsoon_rain": is_monsoon_rain,
        "traffic_multiplier": np.round(traffic_multiplier, 2),
        "battery_percentage": battery_percentage,
        "is_critical_battery": is_critical_battery,
        "app_reopen_count": app_reopen_count,
        "device_tier": device_tier,
        "base_fare_inr": np.round(base_fare_inr, 2),
        "total_surge_multiplier": total_surge_multiplier,
        "quoted_fare_inr": quoted_fare_inr,
        "algorithmic_markup_inr": algorithmic_markup_inr,
        "ride_status": ride_status
    })

    return dataset


if __name__ == "__main__":
    df = generate_ride_forensics_dataset(n_samples=50000)
    
    # Save output for forensics verification
    output_path = "data/Bangalore_Advanced_Ride_Forensics_2.csv"
    df.to_csv(output_path, index=False)
    print(f"Synthesized dataset saved to: {output_path}")
    
    # Critical vs Safe battery statistical analysis
    critical_group = df[df["is_critical_battery"] == 1]["algorithmic_markup_inr"]
    safe_group = df[df["is_critical_battery"] == 0]["algorithmic_markup_inr"]

    mean_critical = critical_group.mean()
    var_critical = critical_group.var()
    std_critical = critical_group.std()

    mean_safe = safe_group.mean()
    var_safe = safe_group.var()
    std_safe = safe_group.std()

    print("=" * 70)
    print("ALGORITHMIC SURGE MARKUP STATISTICAL ANALYSIS")
    print("=" * 70)
    print("Group: Critical Battery Level (<= 15%)")
    print(f"  Mean Algorithmic Markup:    INR {mean_critical:.2f}")
    print(f"  Variance:                   {var_critical:.2f}")
    print(f"  Standard Deviation:         INR {std_critical:.2f}")
    print("=" * 70)
    print("Group: Safe Battery Level (> 15%)")
    print(f"  Mean Algorithmic Markup:    INR {mean_safe:.2f}")
    print(f"  Variance:                   {var_safe:.2f}")
    print(f"  Standard Deviation:         INR {std_safe:.2f}")
    print("=" * 70)
