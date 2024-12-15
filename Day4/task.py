import random
import my_module

# random_integer = random.randint(1, 100)
# print(random_integer)
# print(my_module.my_number)

random_heads_or_tails = random.randint(0,1)
print(random_heads_or_tails)
if(random_heads_or_tails == 1):
    print("正面")
else:
    print("反面")

#包含1和10
# random_float = random.uniform(1,10)
# print(random_float)