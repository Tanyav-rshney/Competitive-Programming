#function with argument
def goodDay(name): #argument: name
    print("Hello,"  + name)

goodDay("Kaya")



def goodDay(name, ending): # arugements: name, ending
    print("Hello,"  + name)
    print(ending)

goodDay("Kaya", "Thank you")    
goodDay("Tanay", "Thanks")    


#function with return type
def goodDay(name): 
    print("Hello,"  + name)

a=goodDay("Kaya")
print(a) #output: return none


def goodDay(name): 
    print("Hello,"  + name)
    return "bye"

a=goodDay("Kaya")
print(a) #output: bye