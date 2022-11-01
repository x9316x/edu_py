print('Введите число N:')
N = int(input())

sub = [0] * N
sub[0] = 1

for i in range(N):
		if i > 0:
			sub[i] = (i + 1) * sub[i-1]
			
print(sub)
