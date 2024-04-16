# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker
# starts his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​
# and i + 1 for all (0 <= i < n). Return the highest altitude of a point.


def largestAltitude(self, gain):
    max_alt, curr_alt = 0, 0
    for i in gain:
        curr_alt += i
        max_alt = max(max_alt, curr_alt)
    return max_alt
