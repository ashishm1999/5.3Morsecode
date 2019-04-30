#Import the needed resources
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

#Set up the system
GPIO.setmode(GPIO.BCM)
led = LED(17)

#Create the window
win = Tk()
win.title("LED Morse")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

#Create the lable
L1 = Label(win, text="Enter:")
L1.pack()

#Limit the input to 12 characters
var = StringVar()
max_char=12
def limit_char(*args):
    input=var.get()
    if len(input)>max_char:
        var.set(input[:max_char])
var.trace_variable("w", limit_char)

#Create the input box
textBox = Entry(win, bd=5, textvariable=var)
textBox.pack(side=RIGHT)

#For short blink in Morse code
def shortBlink():
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.25)

#For long blink in Morse code
def longBlink():
    led.on()
    time.sleep(1.75)
    led.off()
    time.sleep(0.25)

#The Morse code for each letter
def blink(letter):
    if letter == "a":
        shortBlink()
        longBlink()
    if letter == "b":
        longBlink()
        shortBlink()
        shortBlink()
        shortBlink()
    if letter == "c":
        shortBlink()
        longBlink()
        shortBlink()
        longBlink()
    if letter == "d":
        longBlink()
        shortBlink()
        shortBlink()
    if letter == "e":
        shortBlink()
    if letter == "f":
        shortBlink()
        shortBlink()
        longBlink()
        shortBlink()
    if letter == "g":
        longBlink()
        longBlink()
        shortBlink()
    if letter == "h":
        shortBlink()
        shortBlink()
        shortBlink()
        shortBlink()
    if letter == "i":
        shortBlink()
        shortBlink()
    if letter == "j":
        shortBlink()
        longBlink()
        longBlink()
        longBlink()
    if letter == "k":
        longBlink()
        shortBlink()
        longBlink()
    if letter == "l":
        shortBlink()
        longBlink()
        shortBlink()
        shortBlink()
    if letter == "m":
        longBlink()
        longBlink()
    if letter == "n":
        longBlink()
        shortBlink()
    if letter == "o":
        longBlink()
        longBlink()
        longBlink()
    if letter == "p":
        shortBlink()
        longBlink()
        longBlink()
        shortBlink()
    if letter == "q":
        longBlink()
        longBlink()
        shortBlink()
        longBlink()
    if letter == "r":
        shortBlink()
        longBlink()
        shortBlink()
    if letter == "s":
        shortBlink()
        shortBlink()
        shortBlink()
    if letter == "t":
        longBlink()
    if letter == "u":
        shortBlink()
        shortBlink()
        longBlink()
    if letter == "v":
        shortBlink()
        shortBlink()
        shortBlink()
        longBlink()
    if letter == "w":
        shortBlink()
        longBlink()
        longBlink()
    if letter == "x":
        longBlink()
        shortBlink()
        shortBlink()
        longBlink()
    if letter == "y":
        longBlink()
        shortBlink()
        longBlink()
        longBlink()
    if letter == "z":
        longBlink()
        longBlink()
        shortBlink()
        shortBlink()

#Run the program that blink the input word in Morse code
def runProgram():
    text = textBox.get()
    for x in text.lower():
        blink(x)

#Exit the program
def exitProgram():
    GPIO.cleanup()
    win.quit()

#Create run button
runButton = Button (win, text = "Run", font = myFont, command = runProgram, height = 1, width = 5)
runButton.pack(side=BOTTOM)

#Create exit button
exitButton = Button (win, text = "Exit", font = myFont, command = exitProgram, height = 1, width = 5)
exitButton.pack(side=LEFT)

#Start the program
mainloop()


