#Question 1
import random

six_count = 0
one_count = 0
two_sixes = 0
previous = 0

for i in range(20):
    dice = random.randint(1, 6)

    print("Roll:", dice)

    if dice == 6:
        six_count += 1

    if dice == 1:
        one_count += 1

    if dice == 6 and previous == 6:
        two_sixes += 1

    previous = dice

print("Number of 6s:", six_count)
print("Number of 1s:", one_count)
print("Two 6s in a row:", two_sixes)


#Question 2
total = 0
for i in range(10):
    total = total + 10
    print("You completed", total, "jumping jacks.")
    if total == 100:
        print("Congratulations! You completed the workout.")
        break
    tired = input("Are you tired? (yes/no): ")
    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ")
        if skip == "yes" or skip == "y":
            print("You completed a total of", total, "jumping jacks.")
            break
    else:
        remaining = 100 - total
        print(remaining, "jumping jacks are remaining.")