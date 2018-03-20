import math

def compute():
	p, x =  -1, 600851475143
	while p < math.sqrt(x) + 1:
		for p in range(2, int(math.sqrt(x)) + 1):
			if(x % p == 0):
				x =  x//p
				break
	return x


if __name__ == "__main__":
	print(compute())