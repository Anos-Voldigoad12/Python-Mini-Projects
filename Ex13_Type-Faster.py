"""
    Exercise : Create a program to help the user type faster.
    Give him a word and ask him to write it five times.
    Check how many seconds it took him to type the word at each round.
    In the end, tell the user ho many mistakes were made and
        show him a chart with the typing speed evolution during the 5 rounds.
"""

import random
import time as t
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
legend = ["1","2","3","4","5"]
y = []
mistake_count = 0
words = ["pneumonia", "jaundice", "typhoid", "cholera", "malaria", "tuberculosis"]
word = random.choice(words)

print("================================================================")
print("Your word is :", word)
print("Type the word as fast as you can... You have 5 rounds...")
print("(Press Enter to continue)")
print("================================================================")
input()
for i in range(5) :
    t_before = t.time()
    user_input = input("Round %d : " % (i + 1))
    t_after = t.time()
    speed = round((1 / (t_after - t_before)), 3)
    y.append(speed)
    if user_input != word :
        mistake_count += 1
print("\nNumber of Mistakes :", mistake_count)
plt.xlabel("Rounds")
plt.ylabel("Speed (in words/sec)")
plt.title("Typing Speed Evolution")
plt.xticks(x,legend)
plt.plot(x, y)
plt.show()
