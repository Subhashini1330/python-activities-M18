num = int(input("Enter a number: "))

num_str = str(num)
num_digits = len(num_str)
sum = 0

for digit in num_str:
    sum += int(digit) ** num_digits

if sum == num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")
