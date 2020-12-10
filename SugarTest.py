import random as rand
import time    # this class imported for accessing the current date and time of a system
from threading import Timer   # this class imported that here Timer class imported from threading package

def testing():
 try:

    GetTimeDecemalNo= time.time()              # This function is getting the system time

    FinalValue= time.ctime( GetTimeDecemalNo)   # Here is Converting that date and time value understandable form

    saveFile = open('Loggs.doc', 'a')  # here creating File to store log

    for lopcounter in range(5):

        randomnumber = rand.randint(0, 5); # here is generating the Random number

        if( randomnumber >=0 and  randomnumber <=1 ): # here this condition is checking level that is low
           print("Your Sugar Level is too low Take some sweet to maintain your suger Level ")
           test="Your Sugar Level is too low Take some sweet to maintain your suger Level. \n Your suger level is right now: ";
           saveFile.write(test)
           saveFile.write(str( randomnumber )+"\n")
           saveFile.write( FinalValue)
           saveFile.write("\n*******************************************************************************\n")
           break;
        elif( randomnumber ==2): # here this condition is checking sugar level is normal
            print("Stay calm, your Suger level is normal");
            test="Sugar level is Normal.\n which is right now: ";
            saveFile.write(test)
            saveFile.write(str( randomnumber )+"\n") # here writing the sugar level
            saveFile.write( FinalValue) # this condition is writing the Date and time
            saveFile.write("\n*******************************************************************************\n")
            break;
        elif( randomnumber >=3 and  randomnumber <=5):  # this condition is checking the sugar level is very high
            print("Sugar Level is very High inject insuline.")
            test="Sugar Level is very High inject insuline.\n Your suger level is right now: ";
            saveFile.write(test)
            saveFile.write(str( randomnumber ))
            # inner if condition here this condtion checking how many insuline injected

            if  randomnumber ==3:  # this condition is checking sugar is equal three then insert one insuline
                saveFile.write("\ninjected insuline 1Mg"+"\n")
                saveFile.write("  Now Sugar Level is Normal "+str(randomnumber - 1)+"\n")
                saveFile.write( FinalValue)
                saveFile.write("\n*******************************************************************************\n")
                break

            elif  randomnumber ==4:# this condition is checking sugar is equal 4 then insert 2 insuline
                saveFile.write("\ninjected insuline  2Mg"+"\n")
                saveFile.write("Now Sugar Level is Normal "+str(randomnumber - 2)+"\n")
                saveFile.write(FinalValue)
                saveFile.write("\n*******************************************************************************\n")
                break;

            elif randomnumber==5: # this condition is checking sugar is equal 5 then insert 3 insuline
                saveFile.write("\nInjected Insuline "+" 3Mg"+"\n")
                saveFile.write("Now Sugar Level is Normal "+str(randomnumber - 3)+"\n")
                saveFile.write(FinalValue)
                saveFile.write("\n*******************************************************************************\n")
                break;
    print("cheking Your Suger Level.....");  # this message is showng that ur sugar level is being check every five second
    Timer(5,testing).start();   # Here is Timer to call the function every 5 second

 except: # try catch block that control the error of program
     print("There is a problem");
     saveFile.close()

testing() # Here is main body that first time progam execute
