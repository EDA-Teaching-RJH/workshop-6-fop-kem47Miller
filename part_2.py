rover_status = {
    "Battery": int(100),
    "Heater" :str("Off"), 
    "Camera":str("Standby")
    
}
for h in rover_status:
    print(rover_status["Battery"])
    
    
    
rover_status = {
    "Battery": 100, 
    "Heater": "Off",
    "Camera": "Standby"
    
}
print("Current status:", rover_status)
rover_status["Battery"] = 85
rover_status["Heater"] = "On"
rover_status["Speed"] = 5  
print("New status:", rover_status)



mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False},
    {"Site": "Dune B", "Radiation": "High", "Water": True}
]
print("\nMission Log Radiation Report:")
for site_data in mission_log:
    site_name = site_data["Site"]
    radiation_level = site_data["Radiation"]
    print(f"Site {site_name} has {radiation_level} radiation.")
    
