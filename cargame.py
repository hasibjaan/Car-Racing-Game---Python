
user_command = ""
car_started = False 
while True:
    user_command = input(">").upper()
    if user_command == 'HELP':
        print ("""
Start - to start the car
Stop - to stop the car
Quit - to exit the game
        """)
    elif user_command == 'START':
        if not car_started:
            print ("Car started.... Ready to go!")
            car_started = True
        else:
            print ("Car is already started")
    elif user_command == 'STOP':
        if car_started:
            print ("Car stopped")
            car_started = False
        else:
            print ("Car is already stopped")
    elif user_command == 'QUIT':
        break
    else:
        print ("I dont understand it")
        
