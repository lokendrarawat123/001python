print("helo github")
'''
Write a simple calculator program that takes two numbers 
and an operator (+, -, *, /) as input from the user. 
Perform the corresponding operation and print the result.
'''
first_number = int(input("Enter the first number :"))
second_number = int(input("Enter the second number:"))
operator = int(input("""Enter a operator \nfor adding   =[1]
for subtract =[2]\nfor multiply =[3]
for division =[4] \n """))
if (operator == (1)):
    print(f"the sum of {first_number} and {second_number} is :", first_number + second_number)
elif (operator == (2)):
    print(f"the subtraction of {first_number} and {second_number} is :", first_number - second_number)
elif (operator == (3)):
    print(f"the multiplication of {first_number} and {second_number} is :", first_number * second_number)
elif (operator == (4)):
    if (second_number == 0):
        print("the answer is infinite because your input is zero.")
    else:
        print(f"the division of {first_number} and {second_number} is :", first_number / second_number)
else:
    print("you entered wrong operator.")

