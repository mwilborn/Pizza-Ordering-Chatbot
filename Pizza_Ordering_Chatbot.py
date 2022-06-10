print("Hello, my name is Alex your virtual assistant.  I will help you order a pizza!")
print("I am going to ask you a few questions.  After typing an answer, press enter.")
userName = input("\nEnter your name:  ")

while (len(userName) == 0):
    userName = input("Please enter your name:  ")


if userName.lower() == "marvin wilborn":
    print("\nMy creator, " + userName + ".  Pleasure to serve you!")
else:
    print("\nHello, " + userName +".  Nice to meet you!")

keepGoing = "y"
while keepGoing.lower() == "y":
    size = input("\nWhat size do you want?  Enter small, medium, or large:  ")
    while size.lower() != "small" and size.lower() != "large":
        size = input("Invalid, Invalid.  Please enter small, medium, or large:  ")

    while (len(size) == 0):
        size = input("Please enter small, medium, or large:  ")


    flavor = input("\nEnter the flavor of pizza:  ")

    while (len(flavor) == 0):
        flavor = input("Please enter a flavor:  ")

    crustType = input("\nWhat type of crust do you want?:  ")

    while (len(crustType) == 0):
        crustType = input("Please enter a crust type:  ")

    quantity = input("\nHow many of these do you want to order?  Enter a numeric value:  ")

    while not quantity.isdigit():
        quantity = input("\nValue not recognized.  Please enter a numeric value:  ")

    while (len(quantity) == 0):
        quantity = input("Please enter a numeric value:  ")

    quantity = int(quantity)

    method = input("\nIs this carry out or delivery?:  ")

    while method.lower() != "delivery" and method.lower() != "carry out" and method.lower() != "carryout":
        method = input("\nInvalid value.  Please enter delivery or carry out:  ")

    while (len(method) == 0):
        method = input("Please enter carry out or delivery:  ")

    salesTax = 1.1  

    if size.lower() == "small":
        pizzaCost = 8.99
    elif size.lower() == "medium":
        pizzaCost = 14.99
    elif size.lower() == "large":
        pizzaCost = 17.99

    if method.lower() == "delivery":
        deliveryFee = 5
    else:
        deliveryFee = 0

    total = (pizzaCost * quantity) * salesTax + deliveryFee

    print("\n------------------")
    print("Thank you, " + userName + ", for your order.")
    print("Your ", quantity, size, flavor, "pizzas with", crustType, "crust costs", "${:,.2f}".format(total) + ".")
    if total >= 50:
        print("\nCongratulations, you've been awarded a $10 Off coupon for your next order!")     
    else:
        print("\n Orders over $50 will receive a free $10 Off coupon!")
    print("\n------------------")

    print("Order has been received.  ETA 3 mins!")

    for min in range(3, 1, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end = " \r")
            import time
            time.sleep(1)

    print("Order is ready!")

    keepGoing = input("Do you want to place another order?  Enter y or n:  ")