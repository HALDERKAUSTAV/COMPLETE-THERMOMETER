while True:
    print("Options:")
    print("Enter '1' to convert celcius to fahrenhite")
    print("Enter '2' to convert fahrenhite to celsius")
    print("Enter '5' to exit")
    user_input = input(": ")
    if user_input=="1":
        c=eval(input("Enter tempareture in celcius:"))
        print("required temp in farenhite",(9*c/5)+32)
    elif user_input=="2":
        f=eval(input("Enter temparature in fahrenhite"))
        print("Required temp in celcius ",5*(f-32)/9)
    elif user_input=="5":
        break
    else:
        print("Wrong choice")