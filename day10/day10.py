def getJoltDiffs(adapter_list):
    diffs = []
    for a,b in zip(adapter_list[1:], adapter_list):
        diffs.append(a-b)
    return diffs

#so i noted down the numbers in the diffs but turns out you don't actually need to
def num_arrangements(adapter_list):
    arrangements = {0:1}
    for adapter in adapter_list:
        arrangements[adapter] = (arrangements.get(adapter - 3,0) + arrangements.get(adapter - 2,0) + arrangements.get(adapter - 1,0))
    return arrangements
    # return math.prod(
    #     (2 ** (len(m) - 1)) - (len(m) == 4)
    #     for k, g in groupby(diffs)
    #     if k == 1 and len((m := list(g))) > 1
    # )

f = open("day10.txt","r")
adapters = f.readlines()
adapters = [int(i) for i in adapters]
#add in 0, add in max + 3
adapters.append(0)
adapters.append(max(adapters) + 3)
#sort so the list is in order when you want to go through the adapters.
adapters.sort()
print(adapters)
diffs = getJoltDiffs(adapters) 
print(diffs.count(1) * diffs.count(3))
#3 different sets
adapters.remove(0)
print(num_arrangements(adapters))