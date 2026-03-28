#Comparison with and without (3, 1) Repetition Code
import matplotlib.pyplot as plt
import numpy as np

#Physical probability of error on a single transmitted bit
p = np.linspace(0, 1, 100)

#No error correction
pr_of_incorrect_inference = p

#(3, 1) Repetition code logic
#Error happens if 2 or 3 bits are flipped
pr_of_incorrect_inference_repetition = 3 * (p**2) * (1 - p) + p**3

#Plotting
fig, ax = plt.subplots(figsize=(6, 6), layout='constrained')


ax.plot(p, pr_of_incorrect_inference, label='No Error Correction', linestyle='--')
ax.plot(p, pr_of_incorrect_inference_repetition, label='With (3, 1) Repetition Code', linewidth=2)

ax.set_title('Inference Error: Raw vs. Repetition Code')
ax.set_xlabel('Physical bit-flip probability (p)')
ax.set_ylabel('Probability of Bob inferring the wrong bit')
ax.grid(True, alpha=0.3)
ax.legend()

plt.show()
