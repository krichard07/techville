

def move_forward():
    print("Moving forward.")

def turn(direction):
    print(f"Turning {direction}.")

def start_engine():
    print("Stating engine.")

def stop_engine():
    print("Stopping engine.")

def follow_roundabout(exit_number):
    print(f"Taking the exit number {exit_number} from the roundabout.")

start_engine()

destination = input("Where do you want to go? ")
if destination == "library":
    move_forward()
    turn("left")
    print("We arrived at the library!")
    stop_engine()
elif destination == "tech park":
    move_forward()
    turn("right")
    print("We arrived at the tech park!")
    stop_engine()
elif destination in ["hospital", "mall", "airport"]:
    move_forward()
    print("Entering the roundabout.")
    if destination == "hospital":
        follow_roundabout("1")
        print("We are arrived at the hospital!")
        stop_engine()
    elif destination == "mall":
        follow_roundabout("2")
        move_forward()
        turn("right")
        print("We arrived at the mall!")
        stop_engine()
    elif destination == "airport":
        follow_roundabout("3")
        print("We arrived at the airport!")
        stop_engine()
elif destination == "university" or "stadium":
    follow_roundabout("4")
    if destination == "university":
        turn("left")
        print("We arrived at the university!")
        stop_engine()
    else: 
        turn("right")
        print("We arrived at the stadium!")
        stop_engine()
else: 
    print("Error! Invalid destination adress!")