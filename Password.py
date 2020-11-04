#password

import random

answer = random.randint(1,100)
left = 1
right = 100
while True:
    print("enter a number between ",left, " and ",right)

    number = input()
    while number.isdigit()== False:
        number = input("invalid input!!\n")
    number = int(number)

    if left<number and number<right:
        if(number == answer):
            print("corret answer!")
            break
        else:
            if(number>answer):
                right = number
            else:
                left = number
            print("password is between " ,left, "~", right)
    else:
        print("number must be between ", left, "and" , right, "!!")
