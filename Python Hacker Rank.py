""""Hacker Rank Projects """""
import math

#-------------------------------------------------------------------------------
"""Python Print Function

number = int(input(""))
for i in range(1, number + 1):
    print(i, end="")
"""""
#-------------------------------------------------------------------------------
"""Python Filtered, list, map function

n = int(input())  # Read the number of scores
arr = list(map(int, input().split()))  # Read and store the scores as a list
max_score = max(arr)  # Find the highest score
# Create a new list excluding all occurrences of the highest score
filtered_scores = [score for score in arr if score != max_score]
runner_up = max(filtered_scores)  # Find the highest score in the filtered list
print(runner_up)  # Print the runner-up score
"""""
#-------------------------------------------------------------------------------
"""Python Check if a number is even or odd
z = int(input("insert num: "))

if z % 2 == 0:
    print("is even")
else:
    print("is odd")
"""""
#-------------------------------------------------------------------------------
"""Python Convert celsius to fahrenheit

c=float(input("Celsius: "))
f = (c* 9/5)+32
print("Fahrenheit: ", f)
"""""
#-------------------------------------------------------------------------------
"""Python Calculate the sum of two numbers entered by the user

print("Sum:", int(input("Num1: ")) + int(input("Num2: ")))
"""""
#-------------------------------------------------------------------------------
"""Python find the largest number of three numbers

print("Largest:",max(int(input("Num1: ")),int(input("Num2: ")),int(input("Num3: "))))
"""""
#-------------------------------------------------------------------------------
"""Python reverse a string

a = str(input("Enter a string: "))
"(A[START:STOP:STEP])"
print(a[::-1])
"""""
#-------------------------------------------------------------------------------
"""Python Count vowels in a string

a = str.lower(input("Enter a string: "))
vowels = "aeiou"
totalcount = 0

for v in vowels:
    totalcount += a.count(v)
print(totalcount)
"""""
#-------------------------------------------------------------------------------
"""Python Check for Anagrams

list_a = str.lower(input("Enter a string1: "))
list_b = str.lower(input("Enter a string2: "))

sorted_list_a = sorted(list_a)
sorted_list_b = sorted(list_b)

if sorted_list_a == sorted_list_b:
    print("Anagrams")
else:
    print("Not Anagrams")
"""""
#-------------------------------------------------------------------------------
"""Python Factorial calculator

import math

n = int(input("Enter a number: "))

for count in range(1, n + 1):
    fact = math.factorial(count)
    print(fact)
"""""
#-------------------------------------------------------------------------------
"""Python Generate a multiplication table

I started to use Pythonic Style and start using functions
for having a better looking code and professional

def multiplication_table(number: int) -> None:
    for multiplier in range(1, number + 1):
        print(f"{multiplier} * {number} = {multiplier * number}")

if __name__ == "__main__":
    try:
        user_input = int(input("Number: "))
        multiplication_table(user_input)
    except ValueError:
        print("Please enter a valid integer.")
"""""
#-------------------------------------------------------------------------------