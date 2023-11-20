import sys

#Python prpgram fo calculating Collatz chains.
#Program defines a helper function as well as a Node and Chain object 
#Program will output intial value, max value and length of chain for each intial value from 1 until and user defined int
#AUTHOR: davissmith1

#helper funtion for determining if num is odd or even
#returns True if odd, False if even
def isOdd(num):
    return num % 2 != 0

#represents a node in the chain
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.value)

#represents a chain of nodes
class Chain:
    def __init__(self, intialValue):
        self.initial = None
        self.current = None
        #total number of steps until value == 1
        self.size = 0
        #max value in chain
        self.maxValue = intialValue
        #creates node with intial value
        self.add(intialValue)
        self.createChain()

    #function to create chain
    def createChain(self):
        val = self.initial.value
        if val == 0:
            print('ERROR: value cannot be 0')
        
        while val != 1:
            if isOdd(val) :
                newVal = ((3*val) + 1)
                #updates maxVal is applicable
                if newVal > self.maxValue:
                    self.maxValue = newVal
                #creates new node with calculated newVal
                self.add(newVal)
                
            else:
                newVal = val/2
                self.add(newVal)
            
            #iteates value to continue adding nodes
            val = self.current.value
            



    
    def add(self, value):
        if self.initial == None:
            self.initial = Node(value, None)
            self.current = self.initial
        else:
            self.current.next = Node(value, None)
            self.current = self.current.next
        self.size += 1

    def __str__(self):
        if self.initial == None:
            return "Empty Chain"
        chain = ""


def main(numChains):
    #list to hold all chains between 1 and user inputed value
    chains = []
    #creates chains
    for i in range(numChains):
        newChain = Chain(i+1)
        chains.append(newChain)
    for currentChain in chains:
        value = currentChain.initial.value
        maxValue = currentChain.maxValue
        size = currentChain.size
        #print(value+ ") max vale: " + maxValue + ", chain length: " + size, sep='/n')
        print("%d) Max Value: %d, Nodes to termination: %d" % (value, maxValue, size))
    print("End of chains")

if __name__ == "__main__":
    #checks for correct number of arguments
    
    numberOfChains = 10

main(numberOfChains)
    
