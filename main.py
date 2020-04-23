import requests
import matplotlib.pyplot as plt
import threading
import numpy as np
import time

id = 'true-random-integer-generator-result'
resp = 'https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new'

y = np.arange(0,100,1)
x = np.arange(0,100,1)

plt.ion()

for i in range(10):
    #plt.clf()

    # for i in range(11):
    #     time.sleep(0.1)
    #     # y[i] = int(requests.get(resp).text[:-1])
    for _ in range(10):
        y[np.random.randint(0,100)] = np.random.randint(0,100)


    plt.plot(x,y)
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.2)

    #print(i)
plt.ioff()
plt.show()