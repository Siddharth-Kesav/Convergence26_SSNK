import streamlit as st
import numpy as np
import plotly.graph_objects as go

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

    # Index doubles as "altitude", flipped so the outer edge is lowest
    # and the center is highest (e.g. a tower spiraling upward toward the core)
    altitude = (num_panels - 1) - indices

    return x, y, altitude

x, y, altitude = simulate_spiral(angle_deg)

# viridis_r reversed so LOW altitude -> light color, HIGH altitude -> dark color
fig = go.Figure(
    data=go.Scatter(
        x=x,
        y=y,
        mode="markers",
        marker=dict(
            size=14,
            color=altitude,
            colorscale="Viridis",
            reversescale=True,  # low altitude -> light, high altitude -> dark
            line=dict(width=1, color="black"),
            opacity=0.85,
            colorbar=dict(
                title=dict(text="Altitude", side="top"),
                tickvals=[altitude.min(), altitude.max()],
                ticktext=["Lower (lighter)", "Higher (darker)"],
            ),
        ),
    )
)

fig.update_layout(
    title=f"Phyllotaxis Spiral Simulation — Angle: {angle_deg}°",
    xaxis=dict(visible=False, scaleanchor="y", scaleratio=1),
    yaxis=dict(visible=False),
    width=650,
    height=650,
    margin=dict(l=20, r=20, t=60, b=20),
    transition=dict(duration=300, easing="cubic-in-out"),  # smooth redraw
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    "**Legend:** the lighter a panel's color, the *lower* its altitude; "
    "darker panels sit *higher* in the spiral."
)
