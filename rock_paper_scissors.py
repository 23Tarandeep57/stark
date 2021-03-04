import random
choice = ['rock','paper','scissor']
def win_lose(comp_move,our_move):#wrting all the permutations and printing the results
	if our_move == 'rock' and comp_move=='paper':
		print('results : you lost')
	if our_move == 'rock' and comp_move=='rock':
		print('results : tie'.title())
	if our_move == 'rock' and comp_move=='scissor':
		print('results : you won')
	if our_move == 'paper' and comp_move=='scissor':
		print('results : you lost'.title())
	if our_move == 'paper' and comp_move=='paper':
		print('results : tie'.title())
	if our_move == 'paper' and comp_move=='rock':
		print('results : you won'.title())
	if our_move == 'scissor' and comp_move=='rock':
		print('results : you lost'.title())
	if our_move == 'scissor' and comp_move=='scissor':
		print('results : tie'.title())
	if our_move == 'rescissor' and comp_move=='paper':
		print('results : you won'.title())

def main():
	run = True
	while run:
		choice_num = random.randint(0,2)
		comp_move = choice[choice_num]
		our_move  = input('enter your move: ')
		if our_move in choice:
			print("computer's move: "+ comp_move)
			
		else:
			print('please enter a VALID move')
			print()
			our_move  = input('enter your move: ')
		
		win_lose(comp_move,our_move)
		print()
main()
