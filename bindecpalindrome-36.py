def to_base(number,basek):
#Converts the passed number in a different base, both values should be
#   integers and the base must be between 2 and 10 inclusively.

    ret_value=""
    sign=""
    if number < 0:
        sign="-"
        number = -number
    if number == 0:
        return  "0"
    while number>0:
        digit = number % basek
        number = number / basek
        ret_value = str(digit) + ret_value
    return int(sign+ret_value)

def isPalindrome(number):    
    n = str(number)
    cp = list(n)
    li = list(n)
    li.reverse()
    return cp == li

def main():
    list36 = []
    for i in range(1,1000000):
        if isPalindrome(i) and isPalindrome(to_base(i,2)):
            list36.append(i)
    print "Total Numbers palindromic in Binary and Decimal bases (Range 1-1Million) : %d" % len(list36)
    sum = 0
    for n in list36:
        sum = sum + n
    print "Their total Sum : %d" % sum

if __name__ == "__main__":
    main()