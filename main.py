### JHL Development Robot Coffee Barista
### Learning In Python Part 3

business = "Jacks Coffee House"  ## Name Of The Buisness

price = 5  ## Price Of Each Coffee (All Coffees Are The Same Price Currently)

menu = "Black Coffee, Espresso, Light and Sweet,\n" + "Ice Coffee, and Cappucino"  ## Items Listed On Menu

print("Hello Welcome To " + business + "!!!")

print("Thank you so much for coming in today!!!")

name = input("What is your name?\n")  ## Persons Name

if name == "Ben": ## Ben was banned from my coffee shop 
  print("You are banned from " + business + " we will not serve you. " + 
        "Please leave!!!") ## This is the message they will recieve if they try to enter (Ben)
  exit()
else:
  print("Nice to meet you " + name + "!!!" +
        " Thank you for coming in today!!!")

order = input("What Would You Like To Order?\n" +
              "This Is What We Have On Our Menu For Today:\n" + menu + "\n")

quantity = input("How much " + order + " Would you like?\n")

total = price * int(quantity)

print("Sounds great " + name + " Your total is going to be " + "$" +
      str(total) + "\n" + "we will get your " + quantity + " " + order +
      " right up for you!!!" +
      " We will call you to the register when your \n" + quantity + " " +
      order + " is ready!!!")

print("Hey " + name + " Your " + quantity + " " + order +
      " is ready at the counter!!!\n" + "Thank you for choosing " + business +
      "!!!\n" + "Have a good day, and we hope to see you soon!!!")
