# Two common operations are indexing and assigning to an index position. 

def test1() :
    a = []
    for i in range(1000):
        a = a + [i]

def test2():
    a = []
    for i in range(1000):
        a.append(i)

def test3():
    a = [i for i in range(1000)]

def test4():
    a = list(range(1000))
    
from timeit import Timer

def time_compare() :
    t1 = Timer("test1()", "from __main__ import test1")
    print(f"concatenation: {t1.timeit(number = 1000):15.2f} milliseconds")

    t2 = Timer("test2()", "from __main__ import test2")
    print(f"appending: {t2.timeit(number = 1000):15.2f} milliseconds")

    t3 = Timer("test3()", "from __main__ import test3")
    print(f"list comprehension: {t3.timeit(number = 1000):15.2f} milliseconds")

    t4 = Timer("test4()", "from __main__ import test4")
    print(f"list range: {t4.timeit(number = 1000):15.2f} milliseconds")
time_compare()

#--------------------
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print(f"pop(0): {pop_zero.timeit(number = 1000):10.5f} milliseconds")

x = list(range(2000000))
print(f"pop(): {pop_end.timeit(number = 1000):10.5f} milliseconds")

print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")
for i in range(1_000_000, 100_000_001, 1_000_000):
    x = list(range(i))
    pop_zero_t = pop_zero.timeit(number = 1000)
    x = list(range(i))
    pop_end_t = pop_end.timeit(number = 1000)
    print(f"{i:<10d}{pop_zero_t:>15.5f}{pop_end_t:>15.5f}")
    # pop() shows steady speed O(1)
    # pop(0) : O(n)
    
    list.index()