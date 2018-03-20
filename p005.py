import math, timeit

start = timeit.default_timer()

def compute():
	return eval('*'.join(str(x) for x in [i**int(math.log(20,i)) for i in range(2,20) if all([i%j for j in range(2,int(math.sqrt(i))+1)])]))

if __name__ == "__main__":
	print(compute())

	stop = timeit.default_timer()
	print("Runtime:", stop - start) 