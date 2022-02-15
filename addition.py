def addition(a,b):
    c = a + b
    d = a- b
    return c,d
   
    #print("Function:" , c) return is the last statement in function

sum,diff = addition(5,4)
print(sum)
print(diff)
#sum1 = addition('hi','python)#print(sum1)
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
great = greatest(a,b,c)
print("greatest number is:", great)


print("Positional Arguments")

def shop(item,price):
    print("The price of",item,"is",price)
shop("pen",10)

print("Keyword Arguments")
shop(item ="pen",price="")



    

