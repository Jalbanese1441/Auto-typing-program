import keyboard # This allows me to use the “keyboard” library 
import time # This allows me to add in time delays to avoid errors due to slow computer speeds
import os 
import os.path 
# These two allow me to work with files
cls = lambda: os.system("cls")
# This line allows me to use “cls” to clean the console

def getText():
	file=open("text.txt","r")
	textFromFile=file.read()
	text=textFromFile.splitlines()
	return text
# This open and reads the contents from the text file, saves it to a string then breaks apart the string
# The result is a list containing every line of text form the script



while True: # This keeps the user inside a loop until the program can find the text file
	cls()
	print("Welcome to the auto typing program")
	print("This program is designed to type out the contents of a text file line by line into an instant messaging program.\nNote: make sure that the program of your choice is set up so that when you press enter the message is sent.\nAlso, I am not at all responsible for what you do with this program.\nMake sure to check the program that you are using to see if you are able to send mass messages as some program may suspend your account due to spam.")
	print("\nPress enter for the program to search for text file, if you have not created it yet, the program will give you instructions of how to do so")
	input()
	if os.path.isfile("text.txt"):
		cls()
		print("File found!\nPress enter to continue")
		input()
		break
	    # If the file is found, then this allows the program to move on
	else:
		cls()
		print("File not found!\nEach new line of text in the file will be a new line typed, empty lines will not be ignored")
		print("Enter the text that you want typed into a text file called \"text\"")
		print("Then put the text file the same folder that this program is being run out of. Close out of this program and then reopen it, if the file is found then the program will move on")
		print("Alternatively, type open and press enter, then enter the text into the file, close and save the file, then close and reopen this program.")
		print("\nType \"e\" to exit this program")
		x=input()
		if x=="e": exit(0) # Closes the program
		if x=="open":
			file=open("text.txt","w+")
			file.close()
			time.sleep(.2)
			os.startfile("text.txt")
			time.sleep(.2)
			exit(0)
			# If the files do not exist, then the program will cerate and open a new file as well as close the program. 
			# Also, the sleep commands prevents the program from crashing on old or slow computers.
		else:
			cls()
			print("\"",x,"\"Is not a vailed response, press enter to rerun this program")
			input()

while True: # This keeps the user inside a loop until the user enters a valid input
	cls()
	print("Type the number before the bracket to run the corresponding action")
	print("1) Run the program as normal (time between messages: .5 seconds)\n2) Run the program on slow computer or slow internet connection (time between messages: .7 seconds)")
	print("3) Run the program with random timings between messages(time between messages: .7 seconds - 300 seconds")
	print("4) exit the program")
	x=input()
	if x=="4": exit(0)
	if x=="1": 
		timeDelay =.5
		break
	if x=="2":
	   timeDelay =.7
	   break
	if x=="3":
		print("\nPlease type in a time below between .7 and 300 seconds")
		y=input()
		if y.isalnum()== False and y.isalpha()==False:
			y=float(y)
			if y>= .7 and y <=300:
				timeDelay=y
				break
	else:
		cls()
		print("\"",x,"\"Is not a vailed response, press enter to try again ")
		input()
# This bit allows the user to set their desired time delay between messages
# Once the have a proper delay time the program moves out of the loop a and into the next block of code
text=[] 
text = getText()
# This calls on a method that is able to get all of the text that this program will use
cls()
print("Read everything first!\n")
print("Instructions: Minimize this program and go to where you want the text typed and type \"a\" (No need to press enter, also \"a\" won't be sent)")
print("After that the program will automatically type and send each line of text from the file")
print("Note: The program will automatically stop once all of the text has been sent, however you can press \"e\" any time to stop it (You may need to press and hold \"e\")")

keyboard.wait("a")  # Once the user presses a then the program will begin typing out code
keyboard.send("backspace") # Removes the “a” that was typed to start the program
time.sleep(.2)

for i in range(len(text)): # Will loop this code until all text is printed
	if keyboard.is_pressed("e"): break # If the user presses e then the program will stop 
	keyboard.write(text[i]) # This will make the program type out the contents of text at the current line
	time.sleep(timeDelay)
	keyboard.press_and_release("enter") # This will simulate the keyboard pressing "enter", this sends the message
	time.sleep(timeDelay)
	# The time delays make it so that the computer doesn’t type two sentence in a row or send empty messages 
cls()
print("Done!\nPress any key to exit the program ")
exit(0)
