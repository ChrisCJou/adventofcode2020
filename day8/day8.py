def getAccValue(boot_code):
    looped = False
    visited_instructions = set()
    accumulator = 0
    i = 0
    while i < len(boot_code):
        if "acc" in boot_code[i]:
            #print(boot_code[i])
            accumulator += int(boot_code[i].split(" ")[1])
            i = i+1
        elif "jmp" in boot_code[i]:
            i += int(boot_code[i].split(" ")[1])
        elif "nop" in boot_code[i]:
            i += 1
        if i not in visited_instructions:
            visited_instructions.add(i)
        else:
            looped = True
            break
    #print(visited_instructions)
    return str(accumulator) + ":" + str(looped)

f = open("day8.txt","r")
code = f.readlines()
#part1
print(getAccValue(code))

#part2
#change jmp to no-op and no-op to jmp
for index, line in enumerate(code):
    new_boot_code = code.copy()
    #print(str(index) + " " + str(line))
    if "nop" in line:
        new_boot_code[index] = new_boot_code[index].replace("nop","jmp")
        if("False" in getAccValue(new_boot_code)):
            #print(str(line) + ":" + str(index))
            print(getAccValue(new_boot_code))
    elif "jmp" in line:
        new_boot_code[index] = new_boot_code[index].replace("jmp","nop")
        if("False" in getAccValue(new_boot_code)):
            #print(str(line) + ":" + str(index))
            print(getAccValue(new_boot_code))