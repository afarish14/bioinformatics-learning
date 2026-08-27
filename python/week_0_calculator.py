x = input("what's x? ")  #assigns value of whatever user inputs to variable x
y = input("what's y? ")  #assigns value of whatever user inputs to variable y

z = int(x) + int(y)  #int turns text into integers so it doesnt get treated as strings and concatonate the two

print(z)  #prints the variable z which is the value of x + y

x = int(input("what's x? "))  #automatically stores the users input for x as an integer
y = int(input("what's y? "))  #automatically stores the users inout for y as a integer

print(x + y )

x = float(input("what's x? "))  #automatically stores the users input for x as a float which allows user to input numerical values that contain decimal points
y = float(input("what's y? "))  #automatically stores the users inout for y as a float which allows user to input numerical values that contain decimal points

print(x + y )

x = float(input("what's x? "))  #automatically stores the users input for x as a float which allows user to input numerical values that contain decimal points
y = float(input("what's y? "))  #automatically stores the users inout for y as a float which allows user to input numerical values that contain decimal points

z = x + y

print(f"{z:,}")  #adding the f string, colon, and comma allows for large numbers to be formatted correctly e.g. 1000000 - 1,000,000

x = float(input("what's x? "))  #automatically stores the users input for x as a float which allows user to input numerical values that contain decimal points
y = float(input("what's y? "))  #automatically stores the users inout for y as a float which allows user to input numerical values that contain decimal points

z = round(x / y, 2)  #placing a comma and then the number 2 allows it to round to two decimal places

print (z)

x = float(input("what's x? "))  #automatically stores the users input for x as a float which allows user to input numerical values that contain decimal points
y = float(input("what's y? "))  #automatically stores the users inout for y as a float which allows user to input numerical values that contain decimal points

z = x/y

print(f"{z:.2f}")  #placing an f string a colon and .2f allows the value to be rounded to two decimal places