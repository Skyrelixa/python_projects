from timeit import default_timer as timer

start = timer()
a = 1 + 2 + 3 + 4 + 5
stop = timer()

print(stop - start)