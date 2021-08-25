def read_file_into_array(file_name):
    f = open(file_name,"r")
    pw_array = f.readlines()
    f.close()
    return pw_array

def check_password(line):
    #lines consist of 3 things, number of characters, character, password
    number, character, password = line.split(' ')
    minNum, maxNum = number.split('-')
    character = character[0]
    #print(minNum + " " + maxNum)
    return (password.count(character) <= int(maxNum) and password.count(character) >= int(minNum))

def check_password_2(line):
    #lines consist of 3 things, number of characters, character, password
    number, character, password = line.split(' ')
    posOne, posTwo = number.split('-')
    character = character[0]
    #print(minNum + " " + maxNum)
    #I learned about bitwise xor at some point so I'm using it --> ^
    return ((password[int(posOne)-1] == character) ^ (password[int(posTwo)-1] == character))


def main():
    passwords = read_file_into_array('day2.txt')
    validPasswords = 0
    for line in passwords:
        if check_password_2(line):
            validPasswords+=1
    print(validPasswords)
if __name__ == "__main__":
    main()