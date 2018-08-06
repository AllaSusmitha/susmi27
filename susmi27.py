N,K=map(int,raw_input().split())
if N <= 100000 and K <= 100000:
	for i in range(N+1,K+1):
		if (i%2 != 0):
			print i,
