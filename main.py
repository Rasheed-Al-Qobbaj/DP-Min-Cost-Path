import numpy as np
import matplotlib.pyplot as plt

# Example data for petrol cost and hotel cost
petrol_costs = np.array([[0, 10, 20, 30],  # City 1
                         [10, 0, 25, 35],  # City 2
                         [20, 25, 0, 15],  # City 3
                         [30, 35, 15, 0]])  # City 4

hotel_costs = np.array([50, 60, 70, 80])  # Hotel costs for each city


def min_cost_traversal(N, petrol_costs, hotel_costs):
    M = len(petrol_costs)  # Number of cities
    dp = np.zeros((N + 1, M))  # Initialize dynamic programming table

    # Fill in base cases
    dp[0] = 0

    # Iterate over stages
    for stage in range(1, N + 1):
        for city in range(M):
            # Compute minimum cost for current stage and city
            dp[stage][city] = min(
                dp[stage - 1][prev_city] + petrol_costs[prev_city][city] + hotel_costs[city] for prev_city in range(M))

    return dp


# Example usage
N = 3  # Number of stopovers
dp_table = min_cost_traversal(N, petrol_costs, hotel_costs)

# Visualize the dynamic programming table as a heatmap
plt.figure(figsize=(8, 6))
plt.imshow(dp_table, cmap='viridis', origin='lower', aspect='auto')
plt.colorbar(label='Minimum Cost')
plt.xlabel('City')
plt.ylabel('Stage')
plt.title('Dynamic Programming Table')
plt.xticks(np.arange(len(hotel_costs)), np.arange(1, len(hotel_costs) + 1))
plt.yticks(np.arange(N + 1), np.arange(N + 1))
plt.grid(visible=False)
plt.show()
