import colorama
from colorama import Fore
print (Fore.GREEN+ 'welcome to zork please input your age')
print(Fore.WHITE)
age = int(input())
while not(age>0 and age<100): # input validation + comparison operator + logical operator
	print (Fore.RED+'your age is not between 1 and 99')
	print(Fore.WHITE)
	age=int(input())
print(Fore.GREEN+'please input your first name (must be less than 12 characters')
name1 =str(input())      # string variable
while not len(name) <12:   # input validation + LEN function
	print (Fore.RED+'your first name is not less than 12 characters long')
	print(Fore.WHITE)
	name1=str(input())   # string variable
print(Fore.GREEN+'please input your last name (must be less than 12 characters')
name2 = str(input())      # string variable
while not len(name) <12:   # input validation + LEN function
	print (Fore.RED+'your last name is not less than 12 characters long')
	print(Fore.WHITE)
	name2=str(input())    #string variable
name = name1+' '+name2   # concatenation
inventory=[' ',' ',' ',' ',' ',' ']   # 1D arrays
money = 100    # running total
keepgoing=True   #boolean variable
while keepgoing==True and money>0:    # input validation + comparison operator
	print(Fore.CYAN+'you are at the mall and have 100 pounds')
	print (Fore.MAGENTA+'do you want to go to the food court(F), walmart(W) or home(H)')
	choice = input()
	while not choice  == 'W' or 'F'or 'H':    # input validation + comparison operator + logical operator
		print (Fore.RED+'that wasnt a choice')
		print (Fore.WHITE)
		choice = input()
	if choice =='H':              # conditional statement
		keepgoing = False
	elif choise == 'F':              # conditional statement
		print (Fore.CYAN+'the food court is not open')
		print (Fore.MAGENTA+'do you want to go home(H) or to walmart(W)')
		while not choice == 'W' or 'H':                     # input validation + comparison operator + logical operator
			print (Fore.RED+'that wasnt a choice')
			print (Fore.WHITE)
			choice = input()
		if choice == 'H':              # conditional statement
			keepgoing = False
	print (Fore.CYAN+'you are in wallmart')
	print (Fore.MAGENTA+'do you want to go to the food section(F), game section(G) or home(H)')
	while not choice == 'W' or 'F'or 'H':              # input validation + comparison operator + logical operator
		print (Fore.RED+'that wasnt a choice')
		print (Fore.WHITE)
		choice = input()
	if choice =='H':              # conditional statement
		keepgoing = False
	elif choise == 'F':              # conditional statement
		print (Fore.CYAN+'you see candy and fruit')
		print (Fore.MAGENTA+'do you want to go to the fruit(F) or the candy(C)')
		while not choice == 'F' or 'C':                      # input validation + comparison operator + logical operator
			print (Fore.RED+'that wasnt a choice')
			print (Fore.WHITE)
			choice = input()
		if choice == 'F':              # conditional statement
			print (Fore.CYAN+'for some reason there is only bananas')
			print (Fore.MAGENTA+'would you like to buy some for 1 pound each(Y or N)')
			while not choice == 'N' or 'Y':                 # input validation + comparison operator + logical operator
				print (Fore.RED+'that wasnt a choice')
				print (Fore.WHITE)
				choice = input()
			if choice == 'Y':              # conditional statement
				print ('how many')
				num = int(input())
				while num > money:                   # input validation + comparison operator
					print (Fore.RED+'you dont have enough money')
					print (Fore.WHITE)
					num = input()
				for x in range (num):        # fixed loop
					money=money-1          # running total
				inventory[0]=str(num)+paydays
			print ('now you go home')
			keepgoing=False
		else:
			print (Fore.CYAN+'for some reason there is only paydays')
			print (Fore.MAGENTA+'would you like to buy some for 1 pound each(Y or N)')
			while not choice == 'N' or 'Y':           # input validation + comparison operator + logical operator
				print (Fore.RED+'that wasnt a choice')
				print (Fore.WHITE)
				choice = input()
			if choice == 'Y':              # conditional statement
				print ('how many')
				num = int(input())
				while num > money:         # input validation + comparison operator
					print (Fore.RED+'you dont have enough money')
					print (Fore.WHITE)
					num = input()
				for x in range (num):      #fixed loop
					money=money-1     # running total
				inventory[0]=str(num)+paydays   # concatenation
			print ('now you go home')
			keepgoing=False
print('you now have'+money+'pounds and'+inventory[0])  # 1D array
