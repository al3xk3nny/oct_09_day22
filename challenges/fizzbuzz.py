# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# i = 0
# 
# for i in range(100):
#     i += 1
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#       print("Fizz")
#     elif i % 5 == 0:
#       print("Buzz")
#     else:
#         print(i)
#
# print("Done")


# Second option

# i = 0
#
# while i < 100:
#     print(i)
#     i += 1
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
# 
# print("Done")


# Richard's solutions

# Solution 1 - using elif statements

# nums = range(1, 101)

# for num in nums:
#     if num % 3 == 0 and num % 5 == 0: # This statement has to be first as it is the most restictive.
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:    
#         print(num)

# Solution 2 - using if statements and continue

# nums = range(1, 101)

# for num in nums:
    
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#         continue
    
#     if num % 3 == 0:
#         print("Fizz")
#         continue
        
#     if num % 5 == 0:
#         print("Buzz")
#         continue
    
#     print(num)

# Solution 3 - no special case for "FizzBuzz"

nums = range(1, 101)

for num in nums:
    
    value = "" # i.e. empty string
    
    if num % 3 == 0:
        value += "Fizz" # appends "Fizz" to the end of empty string
        
    if num % 5 == 0:
        value += "Buzz" # appends "Buzz" to the end of empty string
    
    if value == "": # if value is empty string
        value = str(num) # print value as a string (not as an int)

    print(value)