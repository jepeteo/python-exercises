import numpy as np
import pandas as pd

def monte_carlo_dice_simulation(dice_sides, num_simulations):
    # Generate random rolls for each die
    rolls = [np.random.randint(1, side + 1, num_simulations) for side in dice_sides]
    
    # Sum the rolls across each simulation
    results = np.sum(rolls, axis=0)
    
    # Calculate frequency of each result
    unique, counts = np.unique(results, return_counts=True)
    
    # Create a result table
    result_table = pd.DataFrame({'Sum': unique, 'Frequency': counts})
    result_table['Probability'] = (result_table['Frequency'] / num_simulations) * 100
    result_table['Probability'] = result_table['Probability'].round(2)
        
    return result_table

# Input list of dice sides
dice_sides = [20, 20]

# Number of simulations
num_simulations = 10000000

# Run the simulation
result_table = monte_carlo_dice_simulation(dice_sides, num_simulations)

# Print the result table
print(result_table)
