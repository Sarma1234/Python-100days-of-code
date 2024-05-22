print(round(27/3, 2))
print(round(2.66666, 2))
print(type(8 // 3)) # // gives you integer output
print(type(4 / 2))  # / gives floating point number
result = 4/2
result /= 2
print(result)

score = 0
score += 1
print(score)
print("your score is" + str(score))

#f-string
score = 0
height = 1.8
isWinning = True
# different data types can be combined inside a string using f
print(f"Your score is {score}, your height is {height}, your wining is {isWinning}")