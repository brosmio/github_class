# num = input("What's the number you want to check for divisors? ")
# for i in range(1,int(num)):
#      div = int(num) % i
#      if div == 0:
#          print(i)

__author__ = 'jeffreyhunt'

num = int(input("Please choose a number to divide: "))

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)