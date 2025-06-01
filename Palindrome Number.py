num = int(input("Enter a number: "))
num_str = str(num)

reversed_num = num_str[::-1]

if num_str == reversed_num:
    print(num,"is a Palindrome number.")
else:
    print(num,"is not a Palindrome number.")
