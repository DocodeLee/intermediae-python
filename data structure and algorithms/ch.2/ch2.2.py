import time
def sum(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n +1 ):
        the_sum = the_sum +i
    
    end = time.time()
    return the_sum, end - start


def sum_of_n_3(n):
    start = time.time()
    a = (n * (n +1 )) / 2
    end = time.time()
    return a, end - start
print(sum(10000))
print(sum_of_n_3(10000))

print(sum(100000))
print(sum_of_n_3(100000))