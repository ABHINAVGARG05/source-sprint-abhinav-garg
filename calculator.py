
x = int(input("Enter the first number: "))
print("the list of operators is: + - * / %")
a=input("Please select your operator : ")
y = int(input("Enter the second number: "))
if a == "+" :
    print(x+y)
if a == "-"  :
    print(x-y)
if a == "*" :
    print(x*y)
if a == "/" :
    print(x/y)
if a == "%":
    print(x%y)
if a!="+" and a!="-" and a!="*" and a!="/" :
    print("YOUR ARE AN IDIOT")
    print()
