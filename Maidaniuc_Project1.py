import math
import numpy as np


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
        return "Twos Complement: " + str(np.binary_repr(int(self.inputNum), width=8))

    def excess128Notation(self):
        intVal = int(self.inputNum)
        excessValue = 0
        if intVal < 128:
            excessValue = intVal + 128
        elif intVal > 128:
            excessValue = intVal - 128
        excessBinaryValue = format(excessValue, '08b')
        return "Excess-128 Notation: " + excessBinaryValue


run = True

# while loop that runs all the classes and performs a check on the binary input
while run:

    BinOrInt = input("Press 1 to enter a Binary number and 2 to enter an Integer: ")
    innerRun = True

    while innerRun:
        if BinOrInt == "1":
            inputBin = input("Enter an 8-bit String: ")
            if len(inputBin) > 8 or len(inputBin) < 8:
                continue
            else:
                binaryEntered = BinaryEntered(inputBin)
                print(binaryEntered.signedMagnitude())
                print(binaryEntered.onesComplement())
                print(binaryEntered.twosComplement())
                print(binaryEntered.excess128Notation())
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
