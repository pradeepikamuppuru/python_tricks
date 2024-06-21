#if input is 12345 
#it makes it 1+2+3+4+5 = 15
#since length of 15 >1
# it performs 1+5= 6
# if the one digit result is 1 it returns happy else not happy
def convert_sum(result):
    temp = [int(digit) for digit in result]
    total = sum(temp)
    if total >= 10:
        return convert_sum(str(total))
    else:
        if total == 1:
            print("Happy")
        else:
            print("Not Happy")

string = input()
print(convert_sum(string))
