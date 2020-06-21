import random
import time
while True:
    print("WELCOME TO THE WAITING GAME")
    print("The WAITING GAME IS WAITING FOR YOU ")
    print(" YOU TARGET TIME IS 4 SECONDS , LET'S GO !!!")
    input ("Press ENTER to start")
    waitingTime = random.randint(4,4)
    start = time.time()
    input("...Press ENTER again after 4 seconds...")
    end = time.time()
    elapsed = end - start
    difference = round(waitingTime - elapsed,2)
    print("\n" "elapsed time: " + str(elapsed) + " seconds")
    if difference < 0.1:
        print("You pushed  in "+ str(difference) + " seconds very slow")
    elif difference > 0.1:
        print( "You pushed  in " + str(difference) + " seconds very fast")
    else:
        print("YOU WIN!!!!! ")
input("Press ENTER to try again")
