def my_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst

nums = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    num = int(input("Введите число: "))
    nums.append(num)

sorted_nums = my_sort(nums)
print(sorted_nums)
