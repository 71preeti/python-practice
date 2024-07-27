         # counting positive number

'''numbers =[1,-2,3,-4,5,6,-7,-8,9,10]
positive_num_count=0
for i in numbers:
    if i >0 :
        positive_num_count+=1
print("final count of positive number is: ",positive_num_count)'''


                # sum of even number


'''n=int(input("please enter a no."))
sum_even=0
for i in range(1,n+1):
    if i %2 ==0:
        sum_even+=i
print (f"sum of even number upto {n} is  {sum_even}")'''

                     # multiplication table printer


'''table_number=int(input("enter the number "))

for i in range(1,11):
    if i ==5:
        continue
    print(table_number, 'x',i,'=', table_number*i)'''

    
                    # reverse a string using loop

'''string=input("please enter a string")
reversed_string=''

for char in string:
    reversed_string=char+reversed_string
print(reversed_string)'''
            
              #find first non-repeated character

'''string="teeter"
for char in string:
    if string.count(char)==1:
        print(char)
        break'''

                 #  factorial number 

'''number = 5
factorial=1
while number>0:
    factorial=factorial*number
    number-=1
print(factorial)'''


                     # take user input number b/w 1 to 10 using while loop


'''while True:
    num=int(input("enter number"))
    if 1 <= num <=10 :
        print("thanks")
        break
    else:
        print(" please input no. between 1 to 10")'''

                   
                   # prime number checker


'''number=int(input("please enter a number"))
is_prime=True
if number>1:
    for i in range(2,number):
        if (number % i) == 0:
            is_prime=False
            break
print(is_prime)
'''

                # list uniqness checker

items=["apple", "banana", "orange" , "apple" , "mango"]
unique_item=set()
for i in items:
    if i  in items:
        print("duplicate:",i)
        break
    unique_item.add(i)

                        
                        # exponential backoff

import time

                       

