"""user_input = input("Enter Motor Speed: ")
try:
    speed = int(user_input)
    if 0 <= speed <= 100:
        print(f"Speed set to {speed}.")
    else:
        print(f"Error: Speed {speed} isn't in range (0-100).")
        
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")"""

    
"""def get_coordinate():
   
    while True: 
        try:
            user_input = input("Enter X-coordinate: ")
            coordinate = int(user_input)
            print(f"Coordinate {coordinate} accepted.")
            break
         
        except ValueError:
            print("Invalid coordinate.")
    return coordinate
print("Testing get_coordinate() function:")
x = get_coordinate()
print(f"Final coordinate received: {x}")"""


"""def get_safe_coordinate():
    while True:
        try:
            user_input = input("Enter X-coordinate (-100 to 100): ")
            coordinate = int(user_input)
            if coordinate < -100 or coordinate > 100:
                print("Coordinate out of range. Please enter a value between -100 and 100.")
                continue  
            print(f"Coordinate {coordinate} accepted and is within safe range.")
            return coordinate
            
        except ValueError:
            print("Invalid coordinate. Please enter a valid integer.")
print("Testing get_safe_coordinate() function:")
safe_coord = get_safe_coordinate()
print(f"Final safe coordinate: {safe_coord}")"""