import numpy as np

arr1 = np.random.randint(0, 100, size = (3,3))
arr2 = np.random.randint(0, 100, size = (3,3))

add = arr1 + arr2
sub = arr1 - arr2
mul = arr1 * arr2

print(f'Массив 1:\n{arr1} \nМасссив 2:\n{arr2} \nҚосындысы:\n{add} \nАйырмасы:\n{sub} \nКөбейтіндісі:\n{mul}')