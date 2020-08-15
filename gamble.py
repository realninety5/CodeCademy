import random
win = 50
lose = 50
money = 100

#Write your game of chance functions here
# Call the result of a coin flip
def coin_flip(bet, money):
  if money < 1:
    return "You, gritting!"
  if not(bet == "Head" or bet=="Tails"):
    return "Son of a , follow the rules please"
  if(random.randint(1,2) == 1):
    b = 'Heads'
  else:
    b = 'Tails'
  if bet == b:
    return b, "You won " + str(win + money)
  else:
    return b, "You lost " + str(money - lose)

# even or odd game
def cho_han(bet, money):
  rn = random.randint(1, 6) + random.randint(1, 6)
  if rn % 2 == 0:
    b = 'Even'
  else:
    b = 'Odd'
  if bet == b:
    return b, "You won " + str(money + win)
  else:
    return b, "You lose " + str(money - lose)

# card picking game
def card(money):
  lst = [0]
  lst[0] = random.randint(1, 52)
  rn = random.randint(1, 52)
  if rn not in lst:
    lst.append(rn)
  else:
    lst.append(random.randint(1, 52))
  p1 = lst[0]
  p2 = lst[1]
  if p1 > p2:
    return 'You won. you have ' + str(lst[0]) + ', and cpt has ' + str(lst[1]) + ". New money is " + str(money + win)
  else:
    return 'You lose. you have ' + str(lst[0]) + ', and cpt has ' + str(lst[1]) + ". New money is " + str(money - lose) 


# roulette game
def roulette(bet, money):
  r = random.randint(-1, 36)
  #return r
  if r == bet:
    return r, ". You won "+ str(money * 36)
  elif(r%2 == 0):
    if(bet == "Even"):
      return r, ". You won "+str(money * 2)
  elif(r%2==1):
    if(bet == "Odd"):
      return r, ". You won "+str(money*2)
  if r==0 or r==-1:
    return r, "You lose "+ str(-money)
  else:
    return r,"You lose "+str(-money)

#Call your game of chance functions here
#money+= coin_flip('Tails', 20)
#for i in range(36):
print(coin_flip("Heads!", -money))
