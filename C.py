# 標準入力を受け付ける。
N, M = map(int, input().split())

S = list(map(str, input().split()))
T = list(map(str, input().split()))

# 普通列車で止まることのできる、全ての駅をdict型で保存する。
stations = {}
for i in range(len(T)):
    stations[T[i]] = True

for i in range(len(S)):
    # 急行列車で止まる駅が、上で宣言したdict型の駅に該当するかどうか確かめる。
    # ある場合`Yes`, ない場合`No`と返す。
    if stations.get(S[i]) is not None:
        print('Yes')
    else:
        print('No')
