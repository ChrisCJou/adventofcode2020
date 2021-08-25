def containsBag(name, insideBags):
    for child in insideBags:
        if name == child:
            return True
        if containsBag(name,data[child]):
            return True
    return False
def countInsideBags(insideBags):
    if insideBags == {}:
        return 0
    total = 0
    for insideBagName in insideBags:
        total += ((countInsideBags(data[insideBagName]) + 1) * insideBags[insideBagName])
    return total

f = open("day7.txt","r")
bag_list = f.readlines()
data = {}
for line in bag_list:
    words = line.split()
    key = words[0] + ' ' + words[1]
    data[key] = {}
    for i, word in enumerate(words):
        if words[i].isnumeric():
            subKey = words[i + 1] + ' ' + words[i + 2]
            data[key][subKey] = int(word)
print(data)

answer = []
searchName = "shiny gold"

for bag in data:
    if containsBag(searchName, data[bag]):
        answer.append(bag)
#part1
print(len(answer))
#part2
print(countInsideBags(data[searchName]))
