import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {'Apple': -6.9, 'Banana': 57.9, 'Bread': 79.4, 'Bun': 15.2, 'Doughnut': 18.6, 'Egg': 17.1, 'Fried Dough Twist': 11.8, 
        'Grape': 143.8, 'Lemon': 0.61, 'Litchi': 20.3, 'Mango': 12.5, 'Mooncake': 13.3, 'Orange': 2.8, 'Pear': 20.9,
        'Peach': 4.7, 'Plum': -3.6, 'Qiwi': 4.4, 'Sachima': 20.5, 'Tomato': 1.5}

# Extract labels and values
labels = list(data.keys())
values = list(data.values())

# Plotting
fig, ax = plt.subplots()

# Plot the bars with colors based on the sign of x values, reduce bar width
bars = ax.barh(labels, values, color=np.where(np.array(values) > 0, 'tab:blue', 'tab:blue'), height=0.6)

# Add x value labels on top of each bar with adjusted position and percent sign
for bar, value in zip(bars, values):
    label_position = (min(value, 40), bar.get_y() + bar.get_height() / 2)
    ax.text(*label_position, f'{value:.1f}%', ha='left' if value > 0 else 'right',
            va='center', color='black', fontweight='bold', fontsize=8)

# Add labels and title
ax.set_xlabel('Mean Error (%)')
#ax.set_ylabel('Class Labels')
#ax.set_title('Bar Plot with Positive and Negative Values')

# Adjust x-axis limits for equal spacing on both sides
x_limit = 40

# Set x-axis ticks with the specified interval
x_interval = 10
ax.set_xticks(np.arange(-x_limit, x_limit + 1, x_interval))

# Remove y-axis ticks
ax.tick_params(axis='y', which='both', left=False)

# Remove vertical dotted lines for each x value
ax.xaxis.grid(False)

# Add vertical lines to x-axis labels
for x_tick in ax.get_xticks():
    ax.axvline(x=x_tick, color='gray', linestyle='-', linewidth=0.5)

# Show the plot
ax.set_xlim(left=-10, right=x_limit)

plt.show()