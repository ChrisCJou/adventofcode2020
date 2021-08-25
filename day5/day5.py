import math
def main():
    f = open("day5.txt","r")
    seats = f.read().split("\n")
    f.close()
    seat_ids = [get_seat_id(seat) for seat in seats]
    seat_ids.sort()
    #part1
    print(max(seat_ids))
    #part2
    #since the range is 13 to 978, the most straight forward with list comprehensions
    answer = [id for id in range(13,978) if id not in seat_ids]
    print(answer)
def get_seat_row(seat_code):
    row_code = seat_code[:7]
    lower_bound = 0
    upper_bound = 127
    for char in row_code:
        if(char =='F'):
            upper_bound = math.floor((upper_bound + lower_bound) / 2)
        else:
            lower_bound = math.ceil((upper_bound + lower_bound) / 2)
    return upper_bound
def get_seat_col(seat_code):
    col_code = seat_code[7:]
    lower_bound = 0
    upper_bound = 7
    for char in col_code:
        if(char =='L'):
            upper_bound = math.floor((upper_bound + lower_bound) / 2)
        else:
            lower_bound = math.ceil((upper_bound + lower_bound) / 2)
    return upper_bound

def get_seat_id(seat_code):
    return get_seat_row(seat_code) * 8 + get_seat_col(seat_code)
if __name__ == "__main__":
    main()