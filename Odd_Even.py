num = input("What's the number your want to check? ")
div = int(num) % 2
if div == 0:
    if int(num)%4 == 0:
        print("It's an even number and multiple of 4!")
    else:
        print("The number is an even number!")
else:
    print("The number is an odd number!")

n_num = input("Set a new number to be checked: ")
n_div = input("What's it going to be divided by? ")
check = int(n_num) % int(n_div)
if check == 0:
    print(n_num + " is evenly divided by " + n_div)
else:
    print(n_num + " is NOT evenly divided by " + n_div)