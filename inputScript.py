##Import the regular expression module.
import re
urlRequest = "https://api.scryfall.com/cards/named&fuzzy="

name = input("What is the name of your card?: ")

urlRequest += name + "/"

hasExtra = str(input("Do you have any other parameters you'd like to search based on? (Y/N) "))


while hasExtra.lower() != "n":
    
    if hasExtra.lower() == "y":
        extraParam = str(input("What additional parameters do you want to search based on? (set, etc): "))

        if extraParam.lower() == "set":
            while True: 
                setInput = str(input("Great! Enter the three letter code for your set: ").lower())
                if re.fullmatch("\w{3}", setInput):
                    break
                else:
                    print("Oopsie Whoopsie your input does not match a valid set code!")
        else:
            print("You're stinky.")
                    
    elif hasExtra.lower() =="n":
        #do the thing
        print("poop")
    else:
        print("That's not a valid response - please use Y/N.")
        
    hasExtra = str(input("Do you have any other parameters you'd like to search based on? (Y/N) "))

print("You've reached the end of the program! Congratulations!")
