import numpy as np

arr = np.random.randint(0, 100, size=10)
avg = np.average(arr)
min = np.min(arr)
max = np.max(arr)

print(f'Массив: {arr} \nОрта мәні:{avg} \nМинимум:{min} \nМаксимум:{max}')

