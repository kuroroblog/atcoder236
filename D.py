# <方針>
# Nの最大値が小さいので、前通りの組み合わせを試して答えを求めると良い。
# 2人を選ぶときに、1, 2 = 2, 1の選び方は等しいことを意味する。
# 1, 1の組み合わせなどは存在しない。

# 標準入力を受け付ける。
N = int(input())
A = [list(map(int, input().split())) for _ in range(2 * N - 1)]

ans = 0

def dfs(dancer, score):

    if len(dancer) == 0:
        global ans
        ans = max(ans, score)
        return

    first_dancer = dancer[0]

    for i in range(1, len(dancer)):
        second_dancer = dancer[i]

        dfs(dancer[1:i] + dancer[i+1:], score ^ A[first_dancer - 1][second_dancer - first_dancer - 1])

dfs([i + 1 for i in range(2 * N)], 0)
print(ans)
