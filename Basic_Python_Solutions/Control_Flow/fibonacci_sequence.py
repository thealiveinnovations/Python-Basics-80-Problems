#Write a program to print the first 10 numbers in the fibonacci sequence.
n = 8
num_1 = 0
num_2 = 1
next_num = num_2
count = 1
print(num_1,num_2, end=" ")
while count <= 8:
    print(next_num, end=' ')
    count += 1
    num_1,num_2 = num_2,next_num
    next_num = num_1 + num_2
