def two_sum_2(numbers, target):
    left = 0
    right = len(numbers) - 1

    while right > left:
        current_sum = numbers[right] + numbers[left]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1


numbers = [2, 7, 11, 15]
numbers2 = [2,3,4]
print(two_sum_2(numbers2, 6))
