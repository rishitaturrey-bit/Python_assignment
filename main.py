start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

num = start

while num <= end:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, "is Prime")

    num += 1