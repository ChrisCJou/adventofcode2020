def get_number_answers(answers):
    answer_set = set()
    test_set = answers.replace("\n","")
    for char in test_set:
        answer_set.add(char)
    return len(answer_set)
#part 2
def get_number_answer_everyone(answer_set):
    test_set = answer_set.split("\n")
    #print(test_set)
    intersect = set()
    intersect2 = set()
    for char in test_set[0]:
        intersect.add(char)
    #don't know if this actually matters
    if(len(test_set) != 1):
        for i in range(1, len(test_set)):
            for char in test_set[i]:
                intersect2.add(char)
            intersect.intersection_update(intersect2)
            intersect2.clear()
    return len(intersect)
#take the first person and add their things into the set
#get the intersection of subsequent sets, then set the base one to that intersection
def main():
    f = open("day6.txt","r")
    answers = f.read().split("\n\n")
    part1 = 0
    part2 = 0
    for answer_set in answers:
        part1 += get_number_answers(answer_set)
        part2 += get_number_answer_everyone(answer_set)
    print(part1)
    print(part2)
if __name__ == "__main__":
    main()