fib_range = int(input("Enter how many numbers of fibbonacci sequence you want to print begining from 0"))
num_one = 0
num_two = 1
print(num_one)
print(num_two)
for x in range(fib_range - 2):
    next_num = num_one + num_two
    print(next_num)
    num_one = num_two
    num_two = next_num
