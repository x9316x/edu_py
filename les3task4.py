Dec = int(input())
Bin = ''

while Dec != 1:
	if Dec % 2 == 0:
		Bin = '0' + Bin
	else:
		Bin = '1' + Bin
	Dec = Dec // 2
	
Bin = '1' + Bin

print(Bin)
