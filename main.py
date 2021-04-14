n = 5
a = [None] * n
for i in range(n): a[i] = [None] * n
c = 1
start = 0

while(start < n // 2):
	n = n - start * 2 - 1
	for x in range(n):
		a[start][start + x] = c
		c += 1
	for y in range(n):
		a[start + y][n - 1 - start] = c
		c += 1
	for x in range(n):
		a[n - 1 - start][n - 1 - start - x] = c
		c += 1
	for y in range(n):
		a[n - 1 - start - y][start] = c
		c += 1

	start += 1

if (n % 2): a[start][start] = c

for y in range(n): print(a[y])