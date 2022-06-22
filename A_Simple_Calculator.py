# A simple calculater

# signs for different operations
print("Enter an operator : "
      "\nfor addition press : + "
      "\nfor subtraction press : - "
      "\nfor multiplication press : * "
      "\nfor division press : / "
      "\nfor exponential press : ** "
      "\nfor floor division press : // "
      "\nfor remainder press : % ")

# Takes input from the user for different operations
choice = input("Enter your choice : ")

if choice in ("+","-","*","/","**","//","%"):

      # Takes input from the user
      num1 = int(input("Enter 1st number : "))
      num2 = int(input("Enter 2nd number : "))

      # For Addition operation
      if choice == "+":
          print(num1+num2)

     # For Subtraction operation
      elif choice == "-":
          print(num1-num2)

      # For Multiplication operation
      elif choice =="*":
          print(num1*num2)

      # For Division operation
      elif choice =="/":
          print(num1/num2)

      # For Exponential operation
      elif choice == "**":
          print(num1**num2)

      # For Floor Division operation
      elif choice == "//":
          print(num1//num2)

      # For Remainder
      elif choice == "%":
          print(num1%num2)

else:
    print("invalid input")
