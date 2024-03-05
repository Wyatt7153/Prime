def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_or_composite(num):
    if is_prime(num):
        return 'prime'
    else:
        return 'composite'
    
def main():
    cut_loops = ''
    numList = []
    amount_of_numbers = int(input("How many numbers do you need to check? "))
    for number in range(1, amount_of_numbers + 1):
        try:
            num = abs(int(input('Enter a number greater than 1: ')))
            if num < 2:
                raise ValueError
            numList.append(num)
        except ValueError:
            print("Please enter a valid positive integer greater than 1.")
    

    for number in numList:
        print(f'{number} is {prime_or_composite(number)}')

if __name__ == "__main__":
    main()