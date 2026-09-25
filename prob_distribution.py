import numpy as np
import matplotlib.pyplot as plt

# Define function to compute the probability distribution
def compute_photon_distribution(m_max, gT=0.45):
    P_current = np.zeros(m_max + 1) # IC : m=0 atoms -> 0 photons with probability equal to 1.0
    P_current[0] = 1.0 # At most m photons after m atoms have passed through the cavity

    # Create dictionary where to save the requested results 
    target_m = [2, 5, 30, 100, 1000]
    saved_distributions = {} 

    # Iterative calculation
    for m in range(1, m_max + 1):
        P_next = np.zeros(m_max + 1)
        for n in range(m + 1):
            cos_term = np.cos(gT * np.sqrt(n + 1))**2 * P_current[n]
            sin_term = np.sin(gT * np.sqrt(n))**2 * P_current[n - 1] if n > 0 else 0.0 # No negative indices

            P_next[n] = cos_term + sin_term

        P_current = P_next

        if m in target_m:
            saved_distributions[m] = P_current.copy() # Save requested results (deep copy of data)

    return saved_distributions

# Parameters
gT = float(input("Insert coupling gT: ")) # Ask for coupling value
ms = [2, 5, 30, 100, 1000] # List of requested m values
distributions = compute_photon_distribution(1000, gT)

# To draw plots
for m in ms:
    P_n = distributions[m]
    # Check the probability conservation 
    prob_sum = np.sum(P_n)
    n_peak = np.argmax(P_n)
    peak_value = P_n[n_peak]
    print(f"Per m = {m:4d} -> Sum P(n): {prob_sum:.6f} | Peak for n = {n_peak} (Value: {peak_value:.4f})")

    max_n_to_show = max(int(np.max(np.where(P_n > 1e-4))) + 5, 10) # Display only the significant portion of the plot (prob > 1e-4)
    n_axis = np.arange(max_n_to_show) 

    plt.plot(n_axis, P_n[:max_n_to_show], label=f'm={m}', marker='o', markersize=3)

plt.xlabel('Number of photons $n$')
plt.ylabel('Probability $P_m(n)$')
plt.title(f'Probability of having $n$ photons in the cavity after $m$ interactions for gT={gT}')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
