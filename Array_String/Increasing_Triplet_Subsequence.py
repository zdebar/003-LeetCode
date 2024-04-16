# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and
# nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


def increasingTriplet(self, nums):
    min_value = float('inf')  # Initialize min_value to positive infinity
    second_min_value = float('inf')  # Initialize second_min_value to positive infinity

    for num in nums:
        if num <= min_value:  # Update min_value if num is smaller or equal
            min_value = num
        elif num <= second_min_value:  # Update second_min_value if num is smaller or equal
            second_min_value = num
        else:
            return True  # If num is greater than both min_value and second_min_value, we've found the triplet
    return False  # No triplet found