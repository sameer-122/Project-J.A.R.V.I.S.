def try_():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print("Result:", result)
    except ValueError:
        print("1 Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("2 Cannot divide by zero.")
    except:
        print("3 An error occurred.")



if __name__ == '__main__':


    try:
        prit()
    except Exception as e1:
        try:
            print(1/0)
        except Exception as e2:
            print(e1)
            print(e2)