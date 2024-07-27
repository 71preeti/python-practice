'''fruit=input("enter fruit name")
color= input("enter color")
if fruit=="banana":
    if color=="green":
        print ("unripe")
    elif color=="yellow":
        print("ripe")
    else :
        print("overripe")
else:
    print("fruit is not banana")


'''
             #  WEATHER ACTIVITY SESSION 

'''weather=["sunny","rainy","snowy"]
print(weather) 
choose = input("choose weather : ") 
if choose in weather:

    if choose=="sunny":
        print(" go for a walk")
    elif choose=="rainy":
        print("read a book")
    elif choose=="snowy":
        print("build a snowman")
else:
    print("choose weather is not in list")'''


                      #Transportation mode section
                    
'''distance=int(input("enter the distance:"))
if distance<3:
    print("walk")
elif distance<16:
    print("bike")
else:
    print("car")
'''


                           # coffee custimization

'''order_size=('small','medium','large')
print(order_size)
choose_size=input("please select size:")

if choose_size in order_size:
    extra_shot="yes or no"
    choose_extrashot=input("please choose extrashot: yes or no :")
    
    if choose_extrashot=="yes":
        print(choose_size +" "+ "coffee with an extrashot")
    else:
        print(choose_size +" "+ "coffee without extrashot") 
else:
    print(" size not available")'''


              # Password checker

'''char=(input("Please enter your password : "))

# chars=len(char)
if len(char)< 6:
    print("weak password")
elif len(char) < 11:
    print("medium password")
else:
    print("strong password")'''

                                
                                #Leap year checker

'''year=int(input("please enter year : "))


if  (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):     # is case m () use krna important h 
    
        print( year ,"is a leap year.")
else:
        print(year,"is not a leap year !")'''

                            # Pet food reccomendation

'''pet_species=["dog","cat"]  
choose_species=input(" please select pet_species") 

if choose_species in pet_species:
        if choose_species=="dog":
                age=int(input("please enter age :"))
                if age<2:
                        print("puppy food")
                else:
         
                       print("adult food")
    
        if choose_species=="cat":
                age_cat=int(input("please enter cat age : "))
                if age_cat>5:
                        print("senior cat food")
                else:
                        print("child cat food ")
else:
        print(" pet species not in list ! ")'''

                               # Movie ticket pricing

'''age=int(input('please enter age'))
day=input("please enter day")
price=0
if age>=18 :
    price=price+12
    
    if day == "wednesday":
        price= price-2
        discounted_price=price
        print("final price is ",discounted_price)
    else:
        print("your price is 12 $")
else:
    price=price+8
    
    if day == "wednesday":
        price=price-2 
        discounted_price=price
        print("final price is ",discounted_price)
    else:
        print("your price is 8 $")
'''


# another method 
age=int(input("enter your age"))
day = input(" enter day")
price = 12 if age >=18 else 8
if day == "wednesday":
    price=price-2
    print("your final price is :",price)
else:
    price=price
    print("your final price is ",price)
