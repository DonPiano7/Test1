import string


def sumofdigits(num):
    # Check if the user's input is a number
    try:
        int(num)
        #Check if the number's length is larger than 1, if so turn it to string and append it to a list, than sum those numbers
        if(len(str(num))>1):
            charlist = list(str(num))
            sum = 0
            for i in charlist:
                sum = sum + int(i)
            return sum
        else:
            return num

    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
def ispal(num):
    # Check if the user's input is a number
    try:
        int(num)
        ispalcheck = False
        strnum = str(num)
        #Check if the number's last charecter is similar to the last in an array of strings after turning the input number into one.
        if strnum == strnum[::-1]:
            ispalcheck = True
            print(ispalcheck)
            return ispalcheck
        else:
            print(ispalcheck)
            return ispalcheck

    except ValueError:
        print("Invalid input. Please enter a number.")
        return