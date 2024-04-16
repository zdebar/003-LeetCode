def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])

    # Initialize variables
    end = intervals[0][1]
    count = 0

    # Iterate through the sorted intervals
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # Overlapping interval found, need to remove it
            count += 1
        else:
            # Non-overlapping interval found, update end time
            end = intervals[i][1]

    return count


# Example usage:
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverlapIntervals(intervals))  # Output should be