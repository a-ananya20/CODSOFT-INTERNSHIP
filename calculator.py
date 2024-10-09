def calculator():
    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2st Number: "))
    while(True):
        if(num1 ==0 and num2==0):
            break
        else:
            oper=input("Enter Operator to perform operation: ")
            if(oper=='+'):
                print(num1 + num2)
            elif(oper=='-'):
                print(num1 - num2)
            elif(oper=='*'):
                print(num1 * num2)
            elif(oper=='/'):
               print(num1 / num2)
            elif(oper=='%'):
                print( num1 % num2)
            else:
                print("invalid operator")
                break
calculator()