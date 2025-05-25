# plot.py
import plotly.graph_objs as go
import numpy as np

def create_hr_diagram(temps, lums, temp_interp, lum_interp, stage):
    fig = go.Figure()

    # Colored zones
    fig.add_shape(type="rect",
        x0=np.log10(30000), x1=np.log10(3000),
        y0=np.log10(1e-2), y1=np.log10(1e2),
        fillcolor="lightblue", opacity=0.2, layer="below", line_width=0)

    fig.add_shape(type="rect",
        x0=np.log10(5000), x1=np.log10(3000),
        y0=np.log10(1e2), y1=np.log10(1e5),
        fillcolor="lightcoral", opacity=0.2, layer="below", line_width=0)

    fig.add_shape(type="rect",
        x0=np.log10(20000), x1=np.log10(8000),
        y0=np.log10(1e-4), y1=np.log10(1e-1),
        fillcolor="lightgray", opacity=0.2, layer="below", line_width=0)

    spectral_types = ["O", "B", "A", "F", "G", "K", "M"]
    temps_ref = [30000, 20000, 10000, 7500, 6000, 4000, 3000]
    lums_ref = [1e5, 1e3, 10, 1, 0.1, 0.01, 1e-4]

    fig.add_trace(go.Scatter(
        x=np.log10(temps_ref),
        y=np.log10(lums_ref),
        mode='markers+text',
        text=spectral_types,
        marker=dict(size=10, color='lightgray'),
        name="Spectral Types"
    ))

    fig.add_trace(go.Scatter(
        x=np.log10(temps),
        y=np.log10(lums),
        mode='lines+markers',
        line=dict(color='orange'),
        marker=dict(size=6),
        name="Evolution Track"
    ))

    fig.add_trace(go.Scatter(
        x=[np.log10(temp_interp)],
        y=[np.log10(lum_interp)],
        mode='markers+text',
        marker=dict(size=16, color='crimson'),
        text=[stage],
        textposition='bottom center',
        name="Star Position"
    ))

    fig.update_layout(
        title="Animated HR Diagram",
        xaxis_title="log(Temperature [K]) →",
        yaxis_title="log(Luminosity / L☉)",
        xaxis=dict(autorange='reversed'),
        yaxis=dict(range=[-2, 6]),
        height=600
    )

    return fig
