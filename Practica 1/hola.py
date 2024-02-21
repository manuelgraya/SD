print ("hola, mundo!")

a = float (input("Introduce un número: "))
b = float (input("Introduce un número: "))
c = float (input("Introduce un número: "))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print ("El área del triángulo es", area)

#take three numbers from user  
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):#else if 
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

def return_x (x):
    return x

a = return_x(5)
print(a)

