#starting with the black jack game 
from random import shuffle
#object classes
class PLAYERS():
	
	def __init__(self,no):
		self.name=input('Enter player {} Name: '.format(no)) 
		print('Welcome {}'.format(self.name))
		self.balance=0
		self.cards=[]
		self.bet=0
		self.card_val=0
		self.with_amt=0
	def hit(self,gdeck):
		self.cards.append(gdeck.deck.pop(0))
		self.card_val=card_value(self.cards)
		
	def stand(self):
		print('Player stands')

	def betm(self):
		while True:
			try:
				self.bet=int(input('Place ur bet: '))
			except:
				print('Enter a valid numerical amount!!')
			else:
				print('Thank you')
				break
		print('The bet is placed')
	def player_balance(self):
		print('Player balance is {}'.format(self.balance))

class DEALER():
	def __init__(self):
		print('Hiii this computer will be dealer')
		self.cards=[]
		self.card_val=0
	def dist_cards(self,gdeck,player):
		print('Dealer is shuffling the cards')
		shuffle(gdeck.deck)
		print ('dealer will now distribute the cards')
		for x in [1,2]:
			self.cards.append(gdeck.deck.pop(0))
			player.cards.append(gdeck.deck.pop(0))
		print('Cards are now distributed')
	def hit(self,gdeck):
		self.cards.append(gdeck.deck.pop(0))
		self.card_val=card_value(self.cards)
	def stand():
		pass
	
class BANK():
	def __init__(self):
		self.amount=10000000
	def withdraw(self,player,amt):
		player.balance+=amt
		player.with_amt+=amt
		self.amount-=amt
	def show_balance(self):
		print('Total balance is {}'.format(self.amount))
	
class CARDS():
	def __init__(self):
		self.deck=[]
		for x in 'A 2 3 4 5 6 7 8 9 10 J Q K'.split():
			for y in 'SDCH':
				self.deck.append(x+y)


#important functions required
def bust_chk(person):
	return person.card_val>21


def win_chk(player,dealer):
	return  player.card_val>=dealer.card_val


def blackjack_chk(player):
	return player.cards==21

def card_value(lst):
	val=0
	for x in lst:
		if x[0] in '2 3 4 5 6 7 8 9 10'.split():
			val+=int(x[0])
		elif x[0] in 'J Q K'.split():
			val+=10
		else:
			if 21-val >=11:
				val+=11
			else:
				val+=1
	return val
def show_cards(person):
	for x in person.cards:
		print(x+'\t')
def game_end():
	answer=input('want another round?enter Y for yes and N for no. ').lower()
	while True:
		if answer=='y' or answer=='n':
			break
		else:
			answer=input('enter valid input-Y or N').lower()
	if answer=='y':
		print('A new round begins!!')
		return False
	else:
		print('The game ends here')
		return True

def play_game(play,n,dealer,bank,card_deck):
	
	print('Player {} will now ask for money from bank'.format(play1.name))
	while True:
		try:
			amt=int(input('Enter amount u want from bank '))
		except:
			print ('Enter a valid numerical amount')
		else:
			print('Thank you')
			break
	bank.withdraw(play1,amt)
	print('player {}  balance is now {} and bank balance is now {}'.format(play1.name,play1.balance,bank.amount))
	print ('{} is requested to place the bet'.format(play1.name))
	play1.betm()
	dealer.dist_cards(card_deck,play1)
	print('The Dealer cards are:\n')
	for x in dealer.cards:
		if dealer.cards.index(x)==0:
			print('X')
			continue
		print(x+'\t')
	print('Player {} cards are: \n'.format(play1.name))
	show_cards(play1)
	card_value(play1.cards)
	card_value(dealer.cards)
	if blackjack_chk(play1):
		print('The player has won with natural blackjack!')
		play1.balance+=play1.bet*1.5
		bank.amount-=play1.bet*1.5
		print('player wins {}'.format(play1.bet*2.5))
		bank.show_balance()
		play1.player_balance()
		return None
	else:
		while True:
			action=input('do want to hit or stand.enter H for hit and S for stand ').lower()
			while True:
		 		if action=='h' or action=='s':
		 			break
		 		else:
		 			action=input('wrong input. enter again: ').lower()
			if action=='h':
				play1.hit(card_deck)
				show_cards(play1)
				if bust_chk(play1):
					print ('You have busted')
					bank.amount+=play1.bet
					play1.balance-=play1.bet
					bank.show_balance()
					play1.player_balance()
					return None
				elif blackjack_chk(play1):
					print('you have won')
					print('you win {}'.format(play1.bet*2))
					play1.balance+=play1.bet
					bank.amount-=play1.bet
					bank.show_balance()
					play1.player_balance()
					return None
			elif action=='s':
				play1.stand()
				break
		print('The dealer will show his cards')
		show_cards(dealer)
		if blackjack_chk(dealer):
			print ('The dealer wins with a natural blackjack')
			bank.amount+=play1.bet
			play1.balance-=play1.bet
			bank.show_balance()
			play1.player_balance()
			return None
		while True:
			if dealer.card_val<=play1.card_val:
				print('The dealer will hit the card')
				dealer.hit(card_deck)
				show_cards(dealer)
				if bust_chk(dealer):
					print('Dealer has busted.player wins')
					print('you win {} '.format(play1.bet*2))
					play1.balance+=play1.bet
					bank.amount-=play1.bet
					bank.show_balance()
					play1.player_balance()
					return None
				elif blackjack_chk(dealer):
					print ('The dealer wins with a  blackjack')
					bank.amount+=play1.bet
					play1.balance-=play1.bet
					bank.show_balance()
					play1.player_balance()
					return None
			else:
				break
		if win_chk(play1,dealer):
			print('Player wins.')
			print('you win {}'.format(play1.bet*2))
			play1.balance+=play1.bet
			bank.amount-=play1.bet
			bank.show_balance()
			play1.player_balance()
			return None
		else:
			print ('The dealer wins.')
			bank.amount+=play1.bet
			play1.balance-=play1.bet
			bank.show_balance()
			play1.player_balance()
			return None

print('Welcome to BLACKJACK!')
no_players=input('Enter no. of players.Max player allowed are 6')
while True:
	if no_players in '123456':
		break
	else:
		no_players=input('Enter valid input')
n=int(no_players)
play=[]
for x in range(n):
	play.append(PLAYERS(x+1))
dealer=DEALER()
bank=BANK()
while True:
	card_deck=CARDS() 
	play_game(play,n,dealer,bank,card_deck)
	del card_deck
	dealer.cards=[]
	play1.cards=[]
	if game_end():
		print('After returning withdrawn money to bank current standings are:')
		pb=play1.balance-play1.with_amt
		bb=bank.amount+play1.with_amt
		print('Bank: {}'.format(bb))
		print('Player {} : {}'.format(play1.name,pb))
		del play1
		del dealer
		del bank
		break










	










