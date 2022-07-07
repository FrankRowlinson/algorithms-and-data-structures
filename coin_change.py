# greed algorithm - give change with the minimum amount of coins
# problem of this algorithm being greed: if coins are not multiples of each other, then it can be
# unoptimal to use it, e.g.: coins in denominations of 1, 7 and 16. If you try to give change of 22, 
# then it won't be optimal to greedly give coin '16' first. 

def main() -> None:
    coins = [1, 5, 10, 25]
    n = int(input())
    result = list()
    while n:
        if n >= coins[-1]:
            n -= coins[-1]
            result.append(coins[-1])
        else:
            coins.pop()
    print(result)


if __name__ == '__main__':
    main()
