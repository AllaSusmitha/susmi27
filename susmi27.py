N,Q=map(int,raw_input().split())
if N <= 100000 and Q <= 100000:
	for i in range(N+1,Q+1):
		if (i%2 != 0):
			print i,
