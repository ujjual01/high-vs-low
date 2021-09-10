import random
from art import logo,vs
from gamedata import data



def format_data(acc):
  acc_name=acc['name']
  acc_desc=acc['description']
  acc_coun=acc['country']
  return f'{acc_name},a{acc_desc},of {acc_coun}'

def check_ans(guess,a_follower,b_follower):
  if a_follower > b_follower:
    return guess=='a'
  else:
    return guess=='b'

def play():
  score=0
  game_over=False
  while not game_over:
    random1=random.choice(data)
    random2=random.choice(data)
    if random1==random2:
      random2=random.choice(data)
    print(f'It\'s a match between')
    a=random1['name']
    b=random2['name']
    print(f'a. {a}')
    print(format_data(random1))
    print(vs)
    print(f'b. {b}')
    print(format_data(random2))
    guess=input("Who have higher folower count a or b :")
    is_correct=check_ans(guess,random1['follower_count'],random2['follower_count'])

    if is_correct:
      score+=1
      print("yow won ")
 

    else:
      print("Youe are wrong")
    cont=input("You want to continue y/n :")
    if cont=='n':
      print(f'your total score is {score}')
      game_over=True

print(logo)
play()


  