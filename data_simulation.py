import random

def simulate_telemetry_data():
    return {
        "battery_voltage": round(random.uniform(7.0, 12.0), 2),
        "imu_roll": round(random.uniform(-180, 180), 2),
        "imu_pitch": round(random.uniform(-90, 90), 2),
        "imu_yaw": round(random.uniform(-180, 180), 2),
        "temperature": round(random.uniform(20.0, 60.0), 2),
        "altitude": round(random.uniform(100, 500), 2),
        "gps_lat": round(random.uniform(12.0, 13.0), 6),
        "gps_long": round(random.uniform(77.0, 78.0), 6),
        "gps_alt": round(random.uniform(100, 200), 2),
        "connection_health": random.choice(["Excellent", "Good", "Poor", "No Signal"])
    }
