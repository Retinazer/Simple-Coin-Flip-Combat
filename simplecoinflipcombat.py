# Working mini combat system

import random

health = 3
healthEnemy = 3
coin = ["Heads", "Tails"]
print("Flip the coin!! (Type anything to flip)")
flip = str(input())
if flip == "y" or "yes" :
    flip = True
count = 0
while flip == True:
    coinflip = random.choice(coin)

    
    if (coinflip == "Heads") :
        healthEnemy -= 1
        print(coinflip)
        print("You hit for 1 damage", healthEnemy)
    else :
        health -= 1
        print(coinflip)
        print("You got hit for 1 damage", health)
        
    count += 1
    print("Turn", count)
    print("Flip the coin!! (Type anything to flip)")
    flip = str(input())
    if flip == "y" or "yes" :
     flip = True
    
    if health == 1 :
        print(coinflip)
        print("You died!!")
        break
    elif healthEnemy == 1 :
        print(coinflip)
        print("You killed it!!")
        break

    



