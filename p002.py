def compute():
	ans, x , y , z = 0, 1, 1, 2
	while z < 4000000:
		ans += z
		x = y + z
		y = z + x
		z = x + y
	return ans

if __name__ == "__main__":
	print(compute())