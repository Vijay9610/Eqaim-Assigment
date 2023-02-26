# Python script to print additional steps of two numbers

# Take numbers as input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Function to split digits of numbers and store them in lists
def getDigits(num):
    digits = []

    while num > 0:
        digits.append(num % 10)
        num = num // 10
    
    return digits

digits1 = getDigits(num1)
digits2 = getDigits(num2)

# print("Digits1: ", digits1)
# print("Digits2: ", digits2)

# Now perform addition on using digits1 and digits2 and store carry and sum at each step
def addition(digits1, digits2):
    carrySteps = []
    sumSteps = []

    # Add two numbers
    mlen = min(len(digits1), len(digits2))
    i = 0
    carry = 0
    while i < mlen:
        temp = digits1[i] + digits2[i] + carry

        carrySteps.append(str(temp // 10))
        sumSteps.append(str(temp % 10))

        carry = temp // 10

        i += 1
    

    # One of the two loops will execute now for which number of digits are more than other number
    while i < len(digits1):
        temp = digits1[i] + carry

        carrySteps.append(str(temp // 10))
        sumSteps.append(str(temp % 10))

        carry = temp // 10

        i += 1
    
    while i < len(digits2):
        temp = digits2[i] + carry

        carrySteps.append(str(temp // 10))
        sumSteps.append(str(temp % 10))

        carry = temp // 10

        i += 1
    
    if carry >= 1:
        carrySteps.append(str(carry))
        sumSteps.append(str(carry))
    
    return carrySteps, sumSteps


carrySteps, sumSteps = addition(digits1, digits2)
# print("carrySteps: ", carrySteps)
# print("sumSteps: ", sumSteps)


# Generating output as JSON object
carry = ""
sum = ""

steps = {}
for i in range(0, len(carrySteps)):
    step = "step" + str(i+1)
    carry = carrySteps[i] + carry
    sum = sumSteps[i] + sum
    steps[step] = {"carryString": str(int(carry)), "sumString": sum}

print("steps: ", steps)

