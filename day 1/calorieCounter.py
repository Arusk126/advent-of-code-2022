#The jungle must be too overgrown and difficult to navigate in vehicles or
#access from the air; the Elves' expedition traditionally goes on foot. As
#your boats approach land, the Elves begin taking inventory of their
#supplies. One important consideration is food - in particular, the number
#of Calories each Elf is carrying (your puzzle input).

#The Elves take turns writing down the number of Calories contained by the
#various meals, snacks, rations, etc. that they've brought with them, one
#item per line. Each Elf separates their own inventory from the previous
#Elf's inventory (if any) by a blank line.

#Example List Start
#1000
#2000
#3000
#
#4000
#
#5000
#6000
#
#7000
#8000
#9000
#
#10000
#Example List End

#In case the Elves get hungry and need extra snacks, they need to know which
#Elf to ask: they'd like to know how many Calories are being carried by the
#Elf carrying the most Calories. In the example above, this is 24000
#(carried by the fourth Elf).

#part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
calories = 0
with open('output.txt', 'w') as output:
    with open('calorie_list.txt', 'r') as input: 
        for line in input:
            try:
                num = float(line)
                calories += num
            except ValueError:
                output.write(str(calories) + '\n')
                calories = 0
    output.write(str(calories) + '\n')


highest = 0
with open('output.txt', 'r') as input:
    for line in input:
        num = float(line)
        if(num > highest):
            highest = num
    
print("highest:", highest)


#part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
first = 0
second = 0
third = 0
with open('output.txt', 'r') as input:
    for line in input:
        num = float(line)
        if(num > first):
            third = second
            second = first
            first = num
        elif(num > second):
            third = second
            second = num
        elif(num > third):
            third = num

print("first:", first)
print("second", second)
print("third", third)

sum = first + second + third
print("sum:", sum)
