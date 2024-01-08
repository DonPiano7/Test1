from tools.numbers.simp import *
from tools.numbers.comp import *
from tools.col import *

func1_called = False
func2_called = False

def main():

    global func1_called, func2_called

    while True:
        print("Choose a module: 1:add_two, 2:sub_two, 3:sumofdigits, 4:ispal, 0:exit")
        func_number = input("Enter Function number: ")

        if func_number == "0":
            break

        num = int(input("Enter a number: "))

        try:
            if func_number == "1":
                result = add_two(num)
                func1_called = True
            elif func_number == "2":
                result = sub_two(num)
                func2_called = True
            elif func_number == "3":
                if not (func1_called and func2_called):
                    raise Exception("Functions 1 and 2 must be called before function 3.")
                result = sumofdigits(num)
            elif func_number == "4":
                if not (func1_called and func2_called):
                    raise Exception("Functions 1 and 2 must be called before function 4.")
                result = ispal(num)
            else:
                result = "Invalid module."
        except Exception as e:
            result = f"Error: {str(e)}"

        print("Result:", result)

if __name__ == '__main__':
    main()