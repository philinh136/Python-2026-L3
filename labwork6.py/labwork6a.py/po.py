import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,13) #x = [i/10 for i in range(-50,51)]
y = 2*x + 3 + np.sin(x)**2
plt.plot(x,y, marker = ".")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("hello, po!", fontsize=14)
plt.grid(True)
plt.savefig("po.pdf")
plt.show()