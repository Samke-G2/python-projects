# Program that finds the prime numbers between 1 and a given number

def find_primes(n):
    primes = [2]
    count_1 = 3
    
    while count_1 <= n:
        count_2 = 2

        while count_2 < count_1:
            # check = 2
            for i in range(2, count_1):
                if count_1 % i == 0:
                    continue
                elif count_1 % i != 0:
                    count_2 +=1 
                    continue
            else:
                if count_2 == count_1:
                    primes.append(count_1) 
            count_2 += 1
            
        count_1 += 1
            
    return primes


primes_to = int(input("Find primes up to: "))

print(find_primes(primes_to))
                    