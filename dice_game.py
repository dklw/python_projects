# import random

# target = 16
# tries = 0
# sum = 0
# while target != sum:
#     random_dice1 = random.randint(1,6)
#     random_dice2 = random.randint(1,6)
    
#     sum =  random_dice1 + random_dice2
#     tries += 1
    
# print("It took", tries, "tries to get a total of", target,"with two dice.")
import random

target_sum = int(input("Enter the target sum: "))
rolls_count = 0
current_sum = 0

while current_sum != target_sum:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    current_sum = dice1 + dice2
    rolls_count += 1
    print(f"Roll {rolls_count}: {dice1} + {dice2} = {current_sum}")

print(f"It took {rolls_count} rolls to achieve the target sum of {target_sum}.")
