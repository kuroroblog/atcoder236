import collections

# 標準入力を受け付ける。
N = int(input())
A = list(map(int, input().split()))

# 標準入力として与えられる、A1, A2, ...のカードに書かれた数字が、それぞれ何枚ずつあるのか数える。
# 参考 : https://note.nkmk.me/python-collections-counter/
c = collections.Counter(A)

# most_common() : A1, A2, ...のカードに書かれた数字を、持っている枚数の多い順に並べ替える。
# 持っている枚数が一番少ない、Axの値を出力する。
print(c.most_common()[len(c) - 1][0])
