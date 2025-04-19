"""def counter(limit):
    for i in range(1,limit+1):

        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)


limit = input("Select the range of the limit:")

if limit.isnumeric() == False:
    print("Wrong type")

else:
    limit = int(limit)
    print("start")
    counter(limit)

print("end")"""

def fizzbuzz(limit):

    for i in range(limit):
        if i%3 == 0:
            print("fizzbuzz")
        elif i%3==1:
            print("fizz")
        elif i%3==2:
            print("buzz")



limit = input("What is the end number of the limit (starting from 0)")


if limit.isnumeric() == False:
    print("Wrong input type")

elif limit.isnumeric() == True:
    limit = int(limit)
    fizzbuzz(limit)


