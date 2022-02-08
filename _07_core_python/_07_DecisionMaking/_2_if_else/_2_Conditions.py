
'''
REQ: Check whether given number is - positive or 
                                   - negative
                                   - neither positive nor negative
1 condition  : if 
2 conditions : if else
3 conditions : if elif else
4 conditions : if elif elif else
5 conditions : if elif elif elif else

-2,-1,0,1,2

'''
print("-----------Positive or Negative-----------")
#num = 10
num = int(input("Enter any number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:     # elif num == 0
    print("Neither pos. nor Neg.")



'''
Find Student result for input marks with class category. 
                    First class  >= 60
                    Second class >= 50 and < 60
                    Third class  >= 35 and < 50
                    Fail         <  35
Add validation logic for wrong input data 
'''
print("-----------Result with class-----------")
# STATE
marks = int(input("Enter marks :"))

# BEHAVIOR
 # 1. Validation
if marks < 0 or marks > 100:
    print("Please enter valid marks between 0 to 100")
else:
    if marks >= 60:
        print("Result : FIRST CLASS")
        if marks == 100:
            print("-----SUPER..Congratulations-----")
        elif marks >= 90:
            print("----GOOD..Congratulations-------")
    elif marks >= 50 and marks < 60:
        print("Result: SECOND CLASS")
    elif marks >= 35 and marks < 50:
        print("Result: THIRD CLASS")
    else:
        print("Result: FAIL")
        if marks == 0:
            print("--------DOUBLE SUPER----------")