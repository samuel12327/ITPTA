# # PRINT OUTPUT
# print("Hello World")
# print("Hello", "World")
# print("H" + "E" + "L" + "L" + "O")
# print('H', 'E', 'L', 'L', 'O')
# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(6 ** 2)

# # USER INPUT
# x = 2
# y = 4
# print(x + y)

# # STRING CONCATENATION
# x = input("Input X: ")
# y = input("Input Y: ")
# print(x + y)

# # INTEGER OPERATION
# a = int(input("Input A: "))
# b = int(input("Input B: "))
# print(a + b)

# # FLOAT OPERATION
# c = float(input("Input C: "))
# d = float(input("Input D: "))
# print(c + d)

# # CONDITIONALS
# num = 6
# guess = int(input("Guess the Number: "))
# if guess < num:
#     print("Too Low!")
# elif guess == num:
#     print("You are Right!")
# else:
#     print("Too High!")

# # LOOPS
# for i in range(0, 10):
#     print(i)

# num = 10
# i = 0
# while i < num:
#     print(i)
#     i = i + 1

# # CONDITIONALS & LOOPS
# num = 6
# while True:
#     guess = int(input("Guess the Number: "))
#     if guess < num:
#         print("Too Low!")
#     elif guess == num:
#         print("You are Right!")
#         break
#     else:
#         print("Too High!")

# LISTS
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums[-1])

# for i in nums:
#     print(i)

# nums.append(10)
# print(nums)

# print(len(nums))
res = 1
for i in range(5):
    res = res * (i+1)
    print(res)
print(res)
