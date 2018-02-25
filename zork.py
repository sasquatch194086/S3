import colorama
from colorama import Fore
print (Fore.GREEN+ 'welcome to zork please input your age')
print(Fore.WHITE)
age = int(input())
while not(age>0 and age<100):
	print (Fore.RED+'your age is not between 1 and 99')
	print(Fore.WHITE)
	age=int(input())
print(Fore.GREEN+'please input your first name (must be less than 12 characters')
name1 =str(input())
while not len(name) <12:
	print (Fore.RED+'your first name is not less than 12 characters long')
	print(Fore.WHITE)
	name1=str(input())
print(Fore.GREEN+'please input your last name (must be less than 12 characters')
name2 = str(input())
while not len(name) <12:
	print (Fore.RED+'your last name is not less than 12 characters long')
	print(Fore.WHITE)
	name2=str(input())
name = name1+' '+name2
inventory=[' ',' ',' ',' ',' ',' ']
money = 100
keepgoing=True
while keepgoing==True and money>0:
	print(Fore.CYAN+'you are at the mall and have 100 pounde')
	print (Fore.MAGENTA+'do you want to go to the food court(F), walmart(W) or home(H)')
	choice = input()
	while not choice  == 'W' or 'F'or 'H':
		print (Fore.RED+'that wasnt a choice')
		print (Fore.WHITE)
		choice = input()
	if choice =='H':
		keepgoing = False
	elif choise == 'F':
		print (Fore.CYAN+'the food court is not open')
		print (Fore.MAGENTA+'do you want to go home(H) or to walmart(W)')
		while not choice == 'W' or 'H':
			print (Fore.RED+'that wasnt a choice')
			print (Fore.WHITE)
			choice = input()
		if choice == 'H':
			keepgoing = False
	print (Fore.CYAN+'you are in wallmart')
	print (Fore.MAGENTA+'do you want to go to the food section(F), game section(G) or home(H)')
	while not choice == 'W' or 'F'or 'H':
		print (Fore.RED+'that wasnt a choice')
		print (Fore.WHITE)
		choice = input()
	if choice =='H':
		keepgoing = False
	elif choise == 'F':
		print (Fore.CYAN+'you see candy and fruit')
		print (Fore.MAGENTA+'do you want to go to the fruit(F) or the candy(C)')
		while not choice == 'F' or 'C':
			print (Fore.RED+'that wasnt a choice')
			print (Fore.WHITE)
			choice = input()
		if choice == 'F':
			print (Fore.CYAN+'for some reason there is only bananas')
			print (Fore.MAGENTA+'would you like to buy some for 1 pound each(Y or N)')
			while not choice == 'N' or 'Y':
				print (Fore.RED+'that wasnt a choice')
				print (Fore.WHITE)
				choice = input()
			if choice == 'Y':
				print ('how many')
				num = int(input())
				while num > money:
					print (Fore.RED+'you dont have enough money')
					print (Fore.WHITE)
					num = input()
				for x in range (num):
					money=money-1
				inventory[0]=str(num)+paydays
			print ('now you go home')
			keepgoing=False
		else:
			print (Fore.CYAN+'for some reason there is only paydays')
			print (Fore.MAGENTA+'would you like to buy some for 1 pound each(Y or N)')
			while not choice == 'N' or 'Y':
				print (Fore.RED+'that wasnt a choice')
				print (Fore.WHITE)
				choice = input()
			if choice == 'Y':
				print ('how many')
				num = int(input())
				while num > money:
					print (Fore.RED+'you dont have enough money')
					print (Fore.WHITE)
					num = input()
				for x in range (num):
					money=money-1
				inventory[0]=str(num)+paydays
			print ('now you go home')
			keepgoing=False
print('you now have'+money+'pounds and'+inventory[0])
