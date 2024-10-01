 # Aiden Hurd
 # 9/25/24
 # P1HW1
 # Make a program that allows someone to input intergers for exponents and another for adding and subtracting


print("Calculating Exponents")
base=int(input("Enter and integer as the base value: "))
exponent=int(input("Enter and integer as the exponent: "))

result=int(pow(base,exponent))
message=f"{base} raised to the power of {exponent} is {result} !!"
print(message)


print("Adding and Subtraction")
num1=int(input("Enter a starting interger: "))
num2=int(input("Enter an interger to add: "))
num3=int(input("Enter an interger to subtract: "))
result=int((num1 + num2))
result2=int((result - num3))

message2=f"{num1} + {num2} - {num3} is equal to {result2}"
print(message2)
