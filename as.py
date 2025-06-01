import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth, square

f = 2  
t_cont = np.linspace(-1, 5, 1000)  
t_disc = np.arange(-1, 5, 0.1)  


x1_cont = np.sin(2 * np.pi * f * t_cont)
x2_cont = np.where(t_cont >= 0, np.exp(-2 * t_cont), 0)
x3_cont = sawtooth(2 * np.pi * f * t_cont, width=0.5)
x4_cont = square(2 * np.pi * f * t_cont)


x1_disc = np.sin(2 * np.pi * f * t_disc)
x2_disc = np.where(t_disc >= 0, np.exp(-2 * t_disc), 0)
x3_disc = sawtooth(2 * np.pi * f * t_disc, width=0.5)
x4_disc = square(2 * np.pi * f * t_disc)


plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(t_cont, x1_cont, label="x1 contínua")
plt.stem(t_disc, x1_disc, linefmt='r-', markerfmt='ro', basefmt='r-', label="x1 discreta")
plt.title('Señal Sinusoidal x₁(t) = sin(2π·f·t)')
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t_cont, x2_cont, label="x2 contínua")
plt.stem(t_disc, x2_disc, linefmt='r-', markerfmt='ro', basefmt='r-', label="x2 discreta")
plt.title('Señal Exponencial x₂(t) = e^(–2t)·u(t)')
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t_cont, x3_cont, label="x3 contínua")
plt.stem(t_disc, x3_disc, linefmt='r-', markerfmt='ro', basefmt='r-', label="x3 discreta")
plt.title('Señal Triangular x₃(t) = tri(t, f)')
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(t_cont, x4_cont, label="x4 contínua")
plt.stem(t_disc, x4_disc, linefmt='r-', markerfmt='ro', basefmt='r-', label="x4 discreta")
plt.title('Señal Cuadrada x₄(t) = sq(t, f)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
