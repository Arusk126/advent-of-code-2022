
def compute_priority(item):

    priority_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    priority_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    if(str.islower(item)):
        for letter in priority_lowercase:
            if(letter == item):
                priority = priority_lowercase.index(letter) + 1
                return priority
    else:
        for letter in priority_uppercase:
            if(letter == item):
                priority = priority_uppercase.index(letter) + 27
                return priority


#part 1
sum = 0
with open('input.txt', 'r') as input:
    for line in input:
        length = len(line)
        compartment1 = line[0:length//2]
        compartment2 = line[length//2:]
        
        for char in compartment1:
            found = compartment2.find(char)
            if(found != -1):
                sum += compute_priority(char)
                break
print(sum)

#part 2
sum = 0
line_number = 1
line1 = ''
line2 = ''
line3 = ''
with open('input.txt', 'r') as input:
    for line in input:
        if(line_number == 1):
            line1 = line
            line_number += 1
        elif(line_number == 2):
            line2 = line
            line_number += 1
        else:
            line3 = line
            line_number = 1

            for char in line1:
                found1 = line2.find(char)
                if(found1 != -1):
                    found2 = line3.find(char)
                    if(found2 != -1):
                        sum += compute_priority(char)
                        break
print(sum)