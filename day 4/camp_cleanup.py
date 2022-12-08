
# part 1: check for full overlap
fully_contained = 0
with open('input.txt', 'r') as input:
    for line in input:
        formatted = line.replace("\n", "")
        assignments =formatted.split(',')

        elf0 = assignments[0].split('-')
        elf1 = assignments[1].split('-')

        # check if elf0 assignments entirely inside elf1
        if( int(elf1[0]) <= int(elf0[0])  and  int(elf0[1]) <= int(elf1[1]) ):
            fully_contained += 1

        # check if elf1 assignments entirely inside elf0
        elif( int(elf0[0]) <= int(elf1[0])  and  int(elf1[1]) <= int(elf0[1]) ):
            fully_contained += 1

print(fully_contained)

"""oringinal part 2 code -- overcounted by 3
overlap = 0
with open('input.txt', 'r') as input:
    for line in input:
        formatted = line.replace("\n", "")
        assignments =formatted.split(',')

        elf0 = assignments[0].split('-')
        elf1 = assignments[1].split('-')

        #check if elf0 lower overlaps
        if int(elf1[0]) <= int(elf0[0]) and int(elf0[0]) <= int(elf1[1]):
            overlap += 1

        #check if elf0 upper overlaps
        elif int(elf1[0]) <= int(elf0[1]) and int(elf0[1]) <= int(elf1[1]):
            overlap += 1

        #check if elf1 lower overlaps
        elif int(elf0[0]) <= int(elf1[0]) and int(elf1[0]) <= int(elf0[1]):
            overlap += 1

        #check if elf1 upper overlaps
        elif int(elf0[0]) <= int(elf1[1]) and int(elf1[1]) <= int(elf0[1]):
            overlap += 1
"""

# part 2: check for any overlap
overlap = 0
with open('input.txt', 'r') as input:
    for line in input:
        formatted = line.replace("\n", "")
        assignments =formatted.split(',')

        elf0 = assignments[0].split('-')
        elf1 = assignments[1].split('-')

        # creates a range using the limits, then turns the range into a set
        # uses bitwise "and" to check for overlap
        # credit hyper-neutrino
        if set(range(int(elf0[0]), int(elf0[1])+1)) & set(range(int(elf1[0]), int(elf1[1])+1)):
            overlap += 1

print(overlap)

# demo of what happens in part 2
print(set(range(0, 11)))
print(set(range(10, 30)))
if set(range(0, 11)) & set(range(10, 30)):
    print("overlap")
else:
    print("no overlap")