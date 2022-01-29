# 標準入力を受け付ける。
# Sの文字列を1文字単位で配列に格納する。
S = list(input())

a, b = map(int, input().split())

# a文字目とb文字目を入れ替える。
# a - 1, b - 1しているのは、配列indexを考慮するため。
S[b - 1], S[a - 1] = S[a - 1], S[b - 1]

print(''.join(S))
