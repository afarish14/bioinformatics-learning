print("hello, world")  #first code - side effect: display hello, world

name = input("what is your name?")  #prompts the user for a response and assigns value to variable name

name = name.strip()  #.strip is a string method that removes unwanted spaces and whitespace characters from the beginning and end of a string

name = name.capitalize()  #.capitalize changes the first character of a string to uppercase only

name = name.title()  #.title makes the first letter of every word uppercase

print(name)  #displays value of the variable name

print("Hello,",name)  #comma seperates arguments and automatically provides space

print("Hello, ", end="")  #end is an argument inside print that controls what gets put at the end of the printed output,print() automatically puts a newline /n at the end. putting end="" makes it so a new line isnt inputted
print(name)

print("Hello,", name, sep="")  #sep=separator - controls what goes between multiple things you are printing

print(f"Hello, {name}")  #putting an f before quotation marks and using {} allows you to put variables or calculations directly inside your text

def hello(to):
    print("hello", to)

name = input("what's your name? ")
hello(name)