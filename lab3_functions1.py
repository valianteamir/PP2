import random
import math
from itertools import permutations

# 1. Convert grams to ounces
def grams_to_ounces(grams):
    return grams * 28.3495231

# 2. Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# 3. Solve heads and legs puzzle
def solve(numheads, numlegs):
    rabbits = (numlegs - (numheads * 2)) // 2
    chickens = numheads - rabbits
    return chickens, rabbits

# 4. Filter prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

# 5. Print all permutations of a string
def string_permutations(s):
    return list(permutations(s))

# 6. Reverse words in a sentence
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# 7. Check for consecutive 3s
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# 8. Check for 007 sequence
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# 9. Volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# 10. Unique elements in list
def unique_list(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

# 11. Palindrome check
def is_palindrome(word):
    return word == word[::-1]

# 12. Print histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

# 13. Guess the number game
def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    attempts = 0
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

#     print(grams_to_ounces(100))
#     print(fahrenheit_to_celsius(100))
#     print(solve(35, 94))
#     print(filter_prime([10, 15, 17, 21, 29, 31, 42, 43]))
#     print(string_permutations("abc"))
#     print(reverse_sentence("We are ready"))
#     print(has_33([1, 3, 3]))
#     print(spy_game([1, 2, 4, 0, 0, 7, 5]))
#     print(sphere_volume(3))
#     print(unique_list([1, 2, 2, 3, 4, 4, 5]))
#     print(is_palindrome("madam"))
#     histogram([4, 9, 7])
#     # guess_the_number()  # Uncomment to play the game
