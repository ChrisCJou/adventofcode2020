def read_file_into_array(file_name):
    f = open(file_name,"r")
    num_array = f.read().split('\n')
    list_of_integers = [int(i) for i in num_array]
    return list_of_integers
def check_sum_2020_p1(a, b):
    return (a+b == 2020)
def check_sum_2020_p2(a,b,c):
    return (a+b+c == 2020)
def get_2020_product(part):
    numbers = read_file_into_array("day1.txt")
    if part == "p1": 
        for x in numbers:
            for y in numbers:
                if (check_sum_2020_p1(x,y)):
                    print(x*y)
    else:
        for x in numbers:
            for y in numbers:
                for z in numbers:
                    if (check_sum_2020_p2(x,y,z)):
                        print(x*y*z)
def main():
   get_2020_product("p1")
if __name__ == "__main__":
    main()