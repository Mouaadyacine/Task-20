a=int( input("svp entrer le 1er entier") )
b=int( input("svp entrer le 2eme entier") )
op=input("svp entrer une operation")
match op:
    case"+":print("a+b=",a+b)
    case"-":print("a-b=",a-b)
    case"*":print("a*b=",a*b)
    case"/":print("a/b=",a/b)
