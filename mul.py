a=int(input("a \n"))
b=int(input("b \n "))
print ("x", end="")
x=1
while x<=a:
    print(x,end="")
    x+=1
y=1
while y<=b:
      print(" ")
      print(y,end="")   
      z=1    
      while z<=a:
            print(y*z,end="")
            z+=1
      y+=1
print()    

