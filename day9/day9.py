import itertools
def getFirstWeakness(preambleLength, numbers):
    possible_sums = [int(i) for i in numbers[preambleLength:]]
    #append
    #pop(0)
    preamble = [int(i) for i in numbers[:preambleLength]]
    combinations = itertools.combinations(preamble, 2)
    for possible_sum in possible_sums:
        test = False
    # first get the current preamble
    # second get the list of sums
    # check if possible sum contained in it
        for combination in combinations:
            if sum(combination) == int(possible_sum):
                test = True
        if not test:
            return possible_sum
        preamble.pop(0)
        preamble.append(possible_sum)
        combinations = itertools.combinations(preamble, 2)         
def contiguous_set(invalid_number, numbers):
    cont_set = set()
    match = 0
    index = 0
    while index < len(numbers):
        #print(cont_set)
        match = match + int(numbers[index])
        if match < invalid_number:
            cont_set.add(int(numbers[index]))
            index += 1
        elif match > invalid_number:
            index = index - len(cont_set) + 1
            cont_set.clear()
            match = 0
        elif match == invalid_number:
            cont_set.add(int(numbers[index]))
            return cont_set
f = open("day9.txt","r")
XMAS = f.readlines()
#print(getFirstWeakness(7, XMAS))
print(getFirstWeakness(25, XMAS))
#preamble is first 25
#test preamble is first 5
#part2
#number is 23278925
#print(contiguous_set(127, XMAS))
print(max(contiguous_set(23278925, XMAS)) + min(contiguous_set(23278925, XMAS)))