'''
- The lower of the two walls on either side of each index determines how much water can be trapped.
- Need to adjust the left_max and right_max variables as we iterate through the array
'''
def trap(height):
    total = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        if left_max < right_max:
            if height[left] < left_max:
                total += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if height[right] < right_max:
                total += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1
    
    return total