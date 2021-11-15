from itertools import permutations
import numpy as np
from numpy import random

random_array =  np.random.choice(10,3, replace=True)

permute =  list(permutations(random_array, 3))
final = []
for per in permute:
    answer =""
    for p in per:
        answer+=str(p)
    ans = max(final.append(answer))