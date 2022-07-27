# this is 0/1 knapsack problem and it's solution using dynamic programming


def knapsack_bu(items: list, W: int) -> int:
    items.sort(key=lambda x: x[0])
    cost_matrix = [[0 for _ in range(W + 1)] for _ in range(len(items) + 1)]
    n = len(items)
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            cost_matrix[i][w] = cost_matrix[i - 1][w]
            # weight and cost of i-th item
            w_i = items[i - 1][0]
            c_i = items[i - 1][1]
            if w_i <= w:
                cost_matrix[i][w] = max(cost_matrix[i][w], \
                    cost_matrix[i - 1][w - w_i] + c_i)
    for row in cost_matrix:
        print(*row)
    return cost_matrix[n][W]
            

def main():
    items1, w1 = [(5, 7), (1, 1), (3, 4), (4, 5)], 7
    items2, w2 = [(6, 30), (3, 14), (4, 16), (2, 9)], 10
    print(knapsack_bu(items1, w1))
    print(knapsack_bu(items2, w2))


if __name__ == "__main__":
    main()