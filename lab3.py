# коментар до лабораторної
def kth_largest(numbers, k):
    if k < 1 or k > len(numbers):
        return -1

    top = []

    for number in numbers:
        position = len(top)

        for i in range(len(top)):
            if number > top[i]:
                position = i
                break

        top.insert(position, number)
        if len(top) > k:
            top.pop()

    return top[k - 1]


print("Програма знаходить k-те за величиною число у списку")

text = input("Введіть числа через пробіл: ")
numbers = []
for part in text.split():
    numbers.append(int(part))
k = int(input("Яке за величиною число знайти? "))
print(kth_largest(numbers, k))
