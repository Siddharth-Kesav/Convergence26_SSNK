import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive, FloatSlider

# Number of panels / balconies to simulate
num_panels = 200

def simulate_spiral(angle_deg):
    """Calculates coordinates and renders the 2D top-down spiral simulation."""
    indices = np.arange(num_panels)
    theta = indices * np.radians(angle_deg)
    radius = np.sqrt(indices) # Scaling factor for natural spacing

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Set up the figure
    fig, ax = plt.subplots(figsize=(7, 7))
    colors = np.linspace(0, 1, num_panels)

    scatter = ax.scatter(x, y, c=colors, cmap='viridis', s=80, alpha=0.8, edgecolor='k')

    ax.set_title(f"Phyllotaxis Spiral Simulation\nAngle: {angle_deg}°", fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

# Create an interactive slider widget for Google Colab
angle_slider = FloatSlider(
    value=137.5,
    min=1.0,
    max=180.0,
    step=0.5,
    description='Angle (°):',
    continuous_update=True
)

# Display the interactive widget connected to the simulation function
interactive_plot = interactive(simulate_spiral, angle_deg=angle_slider)
display(interactive_plot)
