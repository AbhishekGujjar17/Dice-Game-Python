import random , sys

print("This is a Game of  Dice and  each dice has six numbers from 1 to 6\n")

print("The rules of this games are as follows\n")

print("*Maximum bet is $1000 and Minimum bet is $5\n\n*Three dice are used per game session\n") #rules of the game

print("*If one matched dice is found then prize is 2x,if two are found then prize is 4x and if three matched dice have been found then the prize is 10x\n")

print("*If no matched dice have been found then you will loose the bet for this game session\n")

print("$$$$ Lets play $$$$\n")

balance = int(input("Enter the total amount of money you bring in the casino for gambling: \n")) #getting the initial amount 

amountwon = 0

while balance>5:  #to check if the user have enough funds
    print("Select an option")

    print("1.Play\n2.Quit")

    choice = int(input("Enter your option: \n"))

    if choice == 1:
        print("$$$$ Lets play $$$$")
        bet = int(input("Enter the amount of money you want to bet: \n")) #taking the amount to be bet as input
        if 5<=bet<=1000:
            condition = True
            

            while condition:
                num = int(input("Select the dice number from 1-6 on which you want to bet: \n")) #asking the user to select one number to bet
                if num>=1 or num<=6:
                    condition = False

            dicelist = []  #empty list
            for i in range(3): #applying for loop to store the random values from 1 to 6 in dicelist
                c = random.randint(1,6)
                a = dicelist.append(c)
            

            count = 0  
            print("The number on dice 1 is\n",dicelist[0])
            print("The number on dice 2 is\n",dicelist[1])
            print("The number on dice 3 is\n",dicelist[2])
            
            for i in dicelist: #to check if the value guess by the user is equal to the value on any of the dice
                if i==num:
                    count+=1


            
                    
            
            prize = 0 #storing initial amount won as 0
            if count == 1: #if one dice matches the balance is double
                prize = 2*balance
                

            elif count == 2: #if two dice matches the balance is 4x
                prize = 4*balance
                

            elif count == 3: #if all three dice matches the balance is 4x
                prize = 10*balance
                

            elif count == 0:  #if no dice matches the bet is lost
                
                balance = balance - bet
                print("You lost! $\n",bet)
                print("The balance left with you is\n",balance)

            balance+=prize  #total balance

            amountwon+=prize #amount won
            if count!=0:
                print("Congo you won $\n",prize)  #printing the amount won
                print("Your new balance is\n",balance) #printing the total balance left with the user


    if choice == 2:
        print("Alright,You have won the total amount of $\n",amountwon) #printing the totalamount won and exit
        sys.exit()


else:
    print("Insufficient money\nthankyou!") #printing insufficient funds

    


            


    
        
    
    
        


