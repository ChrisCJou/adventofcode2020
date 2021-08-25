def read_file_into_array(file_name):
    f = open(file_name,"r")
    lines = f.read().split("\n\n")
    f.close()
    return lines
def check_fields_valid(field, line):
    if(field == "byr:"):
        return int(line) in range(1920, 2003)
    elif(field == "iyr:"):
        return int(line) in range(2010, 2021)
    elif(field == "eyr:"):
        return int(line) in range(2020, 2031)
    elif(field == "hgt:"):
        if(line[-2:] == "cm" ):
            return int(line[:-2]) in range(150,194)
        if(line[-2:] == "in" ):
            return int(line[:-2]) in range(59,77)
    elif(field=="hcl:"):
        return (line[0] =="#" and len(line) == 7)
    elif (field =="ecl:"):
        return line in "ambblubrngrygrnhzloth"
    elif(field == "pid:"):
        return len(line) == 9
def main():
    passports = read_file_into_array("day4.txt")
    passports = [i.split() for i in passports]
    filtered_list = []
    part1 = 0
    part2 = 0
    exists = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
    for passport in passports:
        fields_existed = 0
        for field_name in exists:
            if field_name in str(passport):
                fields_existed +=1
        if fields_existed == 7:
            part1+=1
            filtered_list.append(passport)
    for passport in filtered_list:
        fields_validated = 0
        for item in passport:
            if(check_fields_valid(item[:4], item[4:])):
                fields_validated +=1
        if fields_validated == 7:
            part2 +=1
    print(part1)
    print(part2)
if __name__ == "__main__":
    main()