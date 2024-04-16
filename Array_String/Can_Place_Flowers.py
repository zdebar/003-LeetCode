def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if sum(flowerbed[max(0, i-1):i + 2]) == 0:
            flowerbed[i] = 1
            count += 1
        if n <= count:
            return True
    return False


flowerbed = [1, 0, 0, 0, 1]
n = 1
print(canPlaceFlowers(flowerbed, n))