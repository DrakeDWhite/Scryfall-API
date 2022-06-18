## Import the regular expression module.
import re
## Import requests, so we can work with APIs - I guess vscode needs pip._vendor
import pip._vendor.requests as requests

## this is test is being done with the ScryFall REST APIs at https://scryfall.com/docs/api/cards/named

##TO-DO
##  add the request logic via the requests module
##  figure out how to print out the image
##  loop back to the original input if it's an invalid card search
##  clean up a lot of the code
##  account for invalid set codes
##  make it prettier

## define our base request string so we can append to it later
urlRequest = "https://api.scryfall.com/cards/named&fuzzy="

## First input - Since this only needs to be asked once, it's outside of the loop
name = input("What is the name of your card?: ")
# replace all spaces with + because the scryfall api gods demand it
name = name.replace(" ", "+")

## Add the name var to the original request URL 
urlRequest += name + "/"

## ask the user if they have additional parameters - the first time we don't need to loop, but the next time this is 
## asked you'll  notice it's in the loop
hasExtra = str(input("Do you have any other parameters you'd like to search based on? (Y/N) "))

## we loop until the hasExtra value is "n", case-insensitive.
while hasExtra.lower() != "n" or hasExtra.lower() == "no":
    ## if they do want extra parameters, they give em!
    if hasExtra.lower() == "y" or hasExtra.lower() == "yes":
        extraParam = str(input("What additional parameters do you want to search based on? (set, etc): "))
        ## only supporting "set" rn, but will expand later
        if extraParam.lower() == "set":
            while True: 
                # make them enter the set code
                setInput = str(input("Great! Enter the three letter code for your set: ").lower())
                # make sure the set code is three alphanumeric chars (this is not yet accounting for fake set codes)
                if re.fullmatch("\w{3}", setInput):
                    # if they are, stop the loop!
                    break
                else:
                    # print if it's not three alphanum characters
                    print("Oopsie Whoopsie your input does not match a valid set code!")
        else:
            #account for anything other than "set" as extraParam
            print("You're stinky.")
                    
    elif hasExtra.lower() =="n" or hasExtra.lower() == "no":
        #do the thing
        break
    else:
        print("That's not a valid response - please use Y/N.")
        
    hasExtra = str(input("Do you have any other parameters you'd like to search based on? (Y/N) "))

print(urlRequest)
