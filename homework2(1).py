import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n",'--name', type=str,
                    help= "Enter your name! (Ex. 'Yarko','Andriy)")

parser.add_argument("-s", '--surname', type=str,
                    help= "Enter your age! (Ex. '20')")


args = parser.parse_args()

name = args.name
surname = args.surname

def Level1():
	print('Level 1')
	counter = 0
	print('First Question')
	answer = str(input())
	if answer == "first answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	print('Second Question')
	answer = str(input())
	if answer == "second answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	print('Third Question')
	answer = str(input())
	if answer == "third answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	if counter == 3:
		print('do you want to play next level?(yes or no)')
		check = str(input())
		if check == 'no':
			exit()
	else:
		print('You lose, your Score: %s'%(counter))
		print('Do you want to play again?')
		check = str(input())
		if check == 'yes':
			Level1()
		else:
			exit()
Level1()
def Level2():
	print('Level 2')
	counter = 3
	print('Fourth Question')
	answer = str(input())
	if answer == "fourth answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	print('Fifth Question')
	answer = str(input())
	if answer == "fifth answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	print('Six Question')
	answer = str(input())
	if answer == "six answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	if counter == 6:
		print('do you want to play next level?(yes or no)')
		check = str(input())
		if check == 'no':
			exit()
	else:
		print('You lose, your Score: %s'%(counter))
		print('Do you want to play again?')
		check = str(input())
		if check == 'yes':
			Level2()
		else:
			exit()
Level2()
def Level3():
	print('Level 3')
	counter = 6
	print('Seventh Question')
	answer = str(input())
	if answer == "seventh answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	print('Eight Question')
	answer = str(input())
	if answer == "eight answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	print('Ninth Question')
	answer = str(input())
	if answer == "ninth answer":
		counter +=1
		print ('Success')
		print ('Your score: %s'%(counter))
	else:
		print ('Wrong answer')
		print ('Your Score: %s'%(counter))
	if counter == 9:
		print('You are a WINNER!!!CONGRATULATIONS!!!Your Score is %s'%(counter))
	else:
		print('%s %s,You lose,your score is: %s,do you want to play again?'%(name,surname,counter))
		check = str(input())
		if check == 'yes':
			Level3()
		else:
			exit()
Level3()