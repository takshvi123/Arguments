def cube(num):
    return num * num * num

def div_by_3(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False

num = int(input("Enter the number: "))
result = div_by_3(num)

if result:
    print(f"The cube of {num} is {result}.")
else:
    print(f"{num} is not divisible by 3.")
