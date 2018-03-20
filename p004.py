def compute():
	return max([x*y for x in range(1000) for y in range(1000) if str(x*y) == str(x*y)[::-1]])

if __name__ == "__main__":
	print(compute())