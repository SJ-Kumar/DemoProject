from math import sqrt

def is_prime(number):
    if isinstance(number, float):
        raise TypeError(f"Only integers are accepted: {number}")
    if number < 2:
        raise ValueError(f"Only integers above 1 are accepted: {number}")
    for candidate in range(2, int(sqrt(number))+1):
        if number % candidate == 0:
            return False
    return True

print("Is the given number prime?:") 
print(is_prime (5))