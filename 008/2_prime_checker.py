# You need to write a function that checks whether if the number passed into it is a prime number or not.

#Write your code below this line 👇

import time

def prime_checker(number):
    
    start = time.time() # time to execute function
    
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False

    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

    end = time.time()
    total_time = int(end - start)

    print(f"Execution time: {total_time} seconds")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=1)
