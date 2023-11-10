
#import numpy as np
from tkinter import *
from tkinter import ttk
import customtkinter

# Class that deals with Binary Inputs
class BinaryEntered:

    def __init__(self, inputNum):
        self.inputNum = inputNum

    def signedMagnitude(self):
        bitList = []
        binaryNum = self.inputNum
        for bit in binaryNum:
            bitList.append(bit)
        if bitList[0] == "1":
            bitList.pop(0)
            newBin = ''.join(bitList)
            binaryToInt = int(newBin, 2)
            binaryToInt = -abs(binaryToInt)
        else:
            binaryToInt = int(binaryNum, 2)
        return "Signed Magnitude: " + str(binaryToInt)

    def onesComplement(self):
        binaryInt = self.inputNum
        bit_list = []
        for bit in binaryInt:
            if bit == "0":
                bit = "1"
            elif bit == "1":
                bit = "0"
            bit_list.append(bit)

        onesComp = ''.join(bit_list)
        onesCompInt = int(onesComp, 2)
        if bit_list[0] == "0":
            onesCompInt = -abs(onesCompInt)
        return "Ones Complement: " + str(onesCompInt)

    def twosComplement(self):
        compliment = ""
        bit_list = []

        for bit in self.inputNum:
            bit_list.append(bit)

        for i in range(len(self.inputNum)):
            if self.inputNum[i] == '0':
                compliment = compliment + '1'
            else:
                compliment = compliment + '0'

        inputBit = compliment
        carry = 1
        compliment = ""
        compInt = 0

        for i in range(len(inputBit) - 1, -1, -1):
            if inputBit[i] == '0':
                if carry == 1:
                    compliment = '1' + compliment
                    carry = 0
                else:
                    compliment = inputBit[i] + compliment
            elif inputBit[i] == '1':
                if carry == 1:
                    compliment = '0' + compliment
                else:
                    compliment = inputBit[i] + compliment
            else:
                compliment = inputBit[i] + compliment
            compInt = int(compliment, 2)
            if bit_list[0] == "1":
                compInt = -abs(compInt)
        return "Twos Complement: " + str(compInt)

    def excess128Notation(self):
        intVal = int(self.inputNum, 2)
        excessValue = 0
        if intVal < 128:
            excessValue = intVal + 128
        elif intVal > 128:
            excessValue = intVal - 128
        return "Excess 128 Notation: " + str(excessValue)


# Class that deals with Integer inputs
class IntEntered:

    def __init__(self, inputNum):
        self.inputNum = inputNum

    def signedMagnitude(self):
        a = format(int(self.inputNum), '08b')
        bit_list = []
        for bit in a:
            bit_list.append(bit)
        if int(self.inputNum) < 0:
            bit_list[0] = '1'
        else:
            bit_list[0] = '0'
        signedNum = ''.join(bit_list)
        return "Signed Magnitude: " + signedNum

    def binaryInt(self):
        a = format(self.inputNum, '08b')
        return a

    def onesComplement(self):
        a = format(int(self.inputNum), '08b')
        bit_list = []
        for bit in a:
            if bit == '0':
                bit = '1'
            elif bit == '1':
                bit = '0'
            bit_list.append(bit)
        if int(self.inputNum) < 0:
            bit_list[0] = '1'
        elif int(self.inputNum) > 0:
            bit_list[0] = '0'
        onesComp = ''.join(bit_list)
        return "Ones Complement: " + str(onesComp)

    def twosComplement(self):
        return "Twos Complement: " + str(np.binary_repr(int(self.inputNum)))

    def excess128Notation(self):
        intVal = int(self.inputNum)
        excessValue = 0
        if intVal < 128:
            excessValue = intVal + 128
        elif intVal > 128:
            excessValue = intVal - 128
        excessBinaryValue = format(excessValue, '08b')
        return "Excess-128 Notation: " + excessBinaryValue


run = False

# while loop that runs all the classes and performs a check on the binary input
while run:

    BinOrInt = input("Press 1 to enter a Binary number and 2 to enter an Integer: ")
    innerRun = True

    while innerRun:
        if BinOrInt == "1":
            inputBin = input("Enter a binary number: ")

            try:     
                binaryEntered = BinaryEntered(inputBin)
                print(binaryEntered.signedMagnitude())
                print(binaryEntered.onesComplement())
                print(binaryEntered.twosComplement())
                print(binaryEntered.excess128Notation())
            except ValueError:
                print("Invalid Input a Binary Number Consists of 1's and 0's")
                continue

        if BinOrInt == "2":
            inputInt = input("Enter an Integer: ")
            intEntered = IntEntered(inputInt)
            print(intEntered.signedMagnitude())
            print(intEntered.onesComplement())
            print(intEntered.twosComplement())
            print(intEntered.excess128Notation())
        innerRun = False

    runAgain = input("Do you want to run it again (Y/N)? ")

    if runAgain.lower() == "n":
        run = False

#GUI for the program

root = Tk()
root.title("Binary Converter")
root.geometry("800x400")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NSEW")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

inputNum = StringVar()
# outputs
signedMag = StringVar()
onesComp = StringVar()
twosComp = StringVar()
excess128 = StringVar()
BinOrInt = IntVar()
errorMsg = StringVar()

#checkbox to select binary or integer
ttk.Checkbutton(mainframe, text="Binary", variable=BinOrInt).grid(column=3, row=1, sticky="NSEW")
ttk.Label(mainframe).grid(column=3, row=0, sticky="NSEW")

#textbox to display an error message
ttk.Label(mainframe, textvariable=errorMsg).grid(column=2, row=0, sticky="NSEW")

# Function that converts the binary input to the different types
def convert():
    try:
        inputValue = inputNum.get()
        if inputValue == "":
            pass
        else:
            if BinOrInt.get() == 1:
                binaryEntered = BinaryEntered(inputValue)
                signedMag.set(binaryEntered.signedMagnitude())
                onesComp.set(binaryEntered.onesComplement())
                twosComp.set(binaryEntered.twosComplement())
                excess128.set(binaryEntered.excess128Notation())
            else:
                intEntered = IntEntered(inputValue)
                signedMag.set(intEntered.signedMagnitude())
                onesComp.set(intEntered.onesComplement())
                twosComp.set(intEntered.twosComplement())
                excess128.set(intEntered.excess128Notation())
    except ValueError:
        # Error message if the input is not a binary or integer
        errorMsg.set("Invalid Input a Binary Number Consists of 1's and 0's")
        #display the error message for 5 seconds
        root.after(5000, lambda: errorMsg.set(""))
        return

# Labels and buttons for the GUI
ttk.Label(mainframe, text="Enter a Number").grid(column=2, row=1, sticky="NSEW")
ttk.Label(mainframe, text="Number: ").grid(column=1, row=2, sticky="NSEW")
inputNumEntry = ttk.Entry(mainframe, width=7, textvariable=inputNum)
inputNumEntry.grid(column=2, row=2, sticky="NSEW")

ttk.Label(mainframe).grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, textvariable=signedMag).grid(column=2, row=3, sticky="NSEW")
ttk.Label(mainframe).grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, textvariable=onesComp).grid(column=2, row=4, sticky="NSEW")
ttk.Label(mainframe).grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, textvariable=twosComp).grid(column=2, row=5, sticky="NSEW")
ttk.Label(mainframe).grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, textvariable=excess128).grid(column=2, row=6, sticky="NSEW")

ttk.Button(mainframe, text="Convert", command=convert).grid(column=3, row=2, sticky="NSEW")

root.mainloop()
