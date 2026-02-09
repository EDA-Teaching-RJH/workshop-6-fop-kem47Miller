travel_log = []
while True:
    user_input = input("Sensor Reading (Slope Angle): ")
    
    if user_input.lower() == 'exit':
        print("Navigation terminated.")
        break
    
    try:
        angle = float(user_input)
        
        if angle > 45:
            print("CRITICAL TILT! HALTING.")
            break
        else:
            travel_log.append(angle)
            print("Path Stable. Moving forward.")
            
    except ValueError:
        print("Sensor Glitch")

travel_log = []
while True:
    user_input = input("Sensor Reading (Slope Angle): ")
    
    if user_input.lower() == 'exit':
        print("Navigation terminated.")
        break
    
    try:
        angle = float(user_input)
        
        if angle > 45:
            print("CRITICAL TILT! HALTING.")
            break
        else:
            travel_log.append(angle)
            print("Path Stable. Moving forward.")
            
    except ValueError:
        print("Sensor Glitch")

print("Mission Terminated.")
print(f"Total steps taken: {len(travel_log)}")
print(f"Travel Log: {travel_log}")