# Python code to train Pokemon
powers = [3, 4, 5, 6, 2, 5, 8, 1, 0]

mini, maxi = 0,0

for power in powers:
    if mini == 0 and maxi == 0:
        mini, maxi = powers[0], powers[0]
        print(mini, maxi)
    else:
        mini = min(mini, power)
        maxi = max(maxi, power)
        print(mini, maxi)