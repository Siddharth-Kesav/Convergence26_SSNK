import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phyllotaxis Spiral Simulation", layout="centered")

st.title("Phyllotaxis Spiral Simulation")
st.caption("A top-down simulation of panels/balconies arranged in a spiral pattern.")

NUM_PANELS = 200

# Interactive angle control (Streamlit's slider replaces the ipywidgets slider)
angle_deg = st.slider(
    "Angle (°)",
    min_value=1.0,
    max_value=180.0,
    value=137.5,
    step=0.5,
)

def simulate_spiral(angle_deg: float, num_panels: int = NUM_PANELS):
    """Calculates coordinates for the 2D top-down spiral simulation."""
    indices = np.arange(num_panels)
    theta = indices * np.radians(angle_deg)
    radius = np.sqrt(indices)  # Scaling factor for natural spacing

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Index doubles as "altitude": panel 0 = lowest, last panel = highest
    altitude = indices

    return x, y, altitude

x, y, altitude = simulate_spiral(angle_deg)

fig, ax = plt.subplots(figsize=(7, 7))

# viridis_r reversed so LOW altitude -> light color, HIGH altitude -> dark color
scatter = ax.scatter(
    x, y, c=altitude, cmap="viridis_r", s=80, alpha=0.8, edgecolor="k"
)

ax.set_title(f"Phyllotaxis Spiral Simulation\nAngle: {angle_deg}°", fontsize=14, fontweight="bold")
ax.set_aspect("equal")
ax.axis("off")

cbar = fig.colorbar(scatter, ax=ax, shrink=0.7, pad=0.03)
cbar.set_label("Altitude", fontsize=11, fontweight="bold")
cbar.set_ticks([altitude.min(), altitude.max()])
cbar.set_ticklabels(["Lower\n(lighter)", "Higher\n(darker)"])

st.pyplot(fig)

st.markdown(
    "**Legend:** the lighter a panel's color, the *lower* its altitude; "
    "darker panels sit *higher* in the spiral."
)
