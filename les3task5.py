n = int(input())

f = [0] * (n + 1)
neg = [0] * n

f[0] = 0
f[1] = 1

neg[0] = 1
neg[0] = 1

for i in range(2, (n + 1)):
	f[i] = f[i - 2] + f[i - 1]

for i in range(1, n):
	neg[i] = neg[i - 2] - neg[i - 1]

neg_rev = neg[::-1]

res = neg_rev + f

print(res)
