
def calculate(a, operator, b):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        if b==0:
            return None
        return a/b
    else:
        return None
def main():
    while True:
        first=input("first number (or q): ")
        if first=="q":
            break
        try:
            a=float(first)
            operator=input("operator (+ - * /): ")
            b=float(input("second number: "))
            result=calculate(a, operator, b)
            if result is None:
                print("cannot calculate that")
            else:
                print("result:", result)
        except ValueError:
            print("cannot calculate")
if __name__ == "__main__":
    main()