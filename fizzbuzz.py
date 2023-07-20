def zznumber(number):
    #number is divisible by m iff not number % m
    if not number % 3:
        if not number % 5:
            return "FizzBuzz"
        else:
            return "Fizz"
    elif not number % 5:
        return "Buzz"
    else:
        return number
    
def main():
    for n in range(1, 101):
        print(zznumber(n))

main()
    

