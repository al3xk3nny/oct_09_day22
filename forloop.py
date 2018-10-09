# For loops

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in nums:
#     print(num % 2 == 0)
# This prints False, True, False, True etc. as the expression in print is a boolean.

# Nested For loops

nums = [1, 2, 3, 4]

for x in nums:
    for y in nums:
        print(x + y)
# A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop".
