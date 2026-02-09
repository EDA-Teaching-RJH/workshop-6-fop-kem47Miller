rover_status = {"Power": 100, "Samples": 0}
inventory = []

while True:
    print("1. Dig for Sample")
    print("2. Report Status")
    print("3. Emergency Stop")
    
    try:
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            sample_name = input("Enter sample name: ")
            if sample_name:
                inventory.append(sample_name)
                rover_status["Samples"] += 1
                rover_status["Power"] -= 10
                print(f"Sample '{sample_name}' collected.")
        
        elif choice == 2:
            print(f"Status: {rover_status}")
            print(f"Inventory: {inventory}")
        
        elif choice == 3:
            print("Emergency Stop activated.")
            break
        
        else:
            print("Invalid choice. Enter 1, 2, or 3.")
            
    except ValueError:
        print("Invalid input. Enter a number.")
        
        
        
    

command_batch = [
    "MOVE 10",
    "TURN LEFT",
    "MOVE 5",
    "MOVE five",
    "DIG",
    "MOVE 20",
    "XÆA-12",
    "RETURN",
    "MOVE 15"
]

rover_state = {"x": 0, "y": 0, "samples": 0}

for command in command_batch:
    parts = command.split()
    
    if not parts:
        continue
    
    action = parts[0]
    
    if action == "MOVE":
        if len(parts) < 2:
            print("Error: Invalid distance ignored")
            continue
        
        try:
            distance = int(parts[1])
            rover_state["y"] += distance
        except ValueError:
            print("Error: Invalid distance ignored")
    
    elif action == "DIG":
        rover_state["samples"] += 1
    
    elif action == "TURN":
        print("Turning...")
    
    else:
        print("Error: Unknown command sequence")
print(rover_state)
