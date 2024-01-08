#A function that adds two to a given number

def add_two(num):
    # Check if the user's input is a number
    try:
        int(num)

         #Add two to the given number
        add_result = num

        #return the resault
        return add_result

    # Return an error in case input is not valid
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    
    


def sub_two(num):
    # Check if the user's input is a number
    try:
        int(num)

        #Add two to the given number
        sub_result = num - 2

        #return the resault
        return sub_result

    # Return an error in case input is not valid
    except ValueError:
        print("Invalid input. Please enter a number.")
        return