print("Enter a number: ")
number = int(input())
new_number = number
result = 0
sum = 0

while(number > 0):
    result = number%10
    print("Result: ",result)
    sum = sum * 10 + result
    print("sum: ",sum)
    number = number//10
    print("number: ",number)

print("Reversed number: ",sum)