from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer

def cpu_function(a):
    for i in range(10_000_000):
        a[i] += a1

@jit(target_backend='cuda')
def gpu_function(a):
    for i in range(10_000_000):
        a[i] += 1


if __name__ == '__main__':
    n = 10_000_000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    cpu_function(a)
    print(f"funkcja wykonana na CPU: {timer()-start} s")

    start = timer()
    gpu_function(a)
    print(f"funkcja wykonana na GPU: {timer() - start} s")
