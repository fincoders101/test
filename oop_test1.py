#!/usr/bin/python
# Coder : Anindya Ghosh

class Bird:
    att1 = "Lays eggs."
    att2 = "Has wings."
    
    __init__(self, name, colour):
        self.name = name
        self.colour = colour
        
####### Driver Code #########

bird1 = Bird("Blu", "Blue");
bird2 = Bird("Chucky", "Yellow")

print("The first bird is: " + bird1.name)
        

