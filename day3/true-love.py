# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
name1 = "Angela Yu"
name2 = "Jack Bauer"
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
counter_1 = 0
counter_2 = 0
word = "true love"
for i in word.split()[0]:
    for x in (name1 + name2).lower():
        if i == x:
            counter_1 += 1
for i in word.split()[1]:
    for x in (name1 + name2).lower():
        if i == x:
            counter_2 += 1
final_score = counter_1 * 10 + counter_2
if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")