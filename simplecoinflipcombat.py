# Working mini combat system

import random

gold = 10
health = 3
healthEnemy = 3
coin = ["Heads", "Tails"]
print("You have", gold, "Gold")
print("Flip the coin!! (type anything to flip)")
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
        print(coinflip)
        health -= 1
        print("You got hit for 1 damage", health)
        
    count += 1
    print("Turn", count)
    print("Flip the coin!! (type anything to flip)")
    flip = str(input())
    if flip == "y" or "yes" :
     flip = True
    
    if health == 1 :
        gold -= 10
        print(coinflip)
        print("You died!!")
        print("You lost 10 Gold!!", gold)
        print("You now have", gold, "Gold")
        break
    elif healthEnemy == 1 :
        gold += 10
        print(coinflip)
        print("You killed it!!")
        print("You earned 10 Gold!!")
        print("You now have", gold, "Gold")
        break

    
