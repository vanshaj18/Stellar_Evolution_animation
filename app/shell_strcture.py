import plotly.graph_objects as go

def shell_structure_figure(stage: str, step_frac: float = 0.0):
    import plotly.graph_objects as go

    fig = go.Figure()
    stage = stage.lower()

    # Outer envelope
    fig.add_shape(type="circle",
                  xref="x", yref="y",
                  x0=0, y0=0, x1=2, y1=2,
                  line_color="black", fillcolor="lightyellow")

    # Defaults
    annotation = "Unknown structure"

    if "main sequence" in stage:
        # Core grows slightly with step_frac
        core_r = 0.3 + 0.05 * step_frac
        fig.add_shape(type="circle", xref="x", yref="y",
                      x0=1 - core_r, y0=1 - core_r,
                      x1=1 + core_r, y1=1 + core_r,
                      fillcolor="orange", line_color="red")
        annotation = "Core: H fusion"

    elif "subgiant" in stage or "giant" in stage:
        # Inert core shrinking slightly, H-shell expanding
        core_r = 0.25 - 0.05 * step_frac
        shell_r = 0.45 + 0.15 * step_frac

        # Core
        fig.add_shape(type="circle", xref="x", yref="y",
                      x0=1 - core_r, y0=1 - core_r,
                      x1=1 + core_r, y1=1 + core_r,
                      fillcolor="gray", line_color="black")
        # H-burning shell
        fig.add_shape(type="circle", xref="x", yref="y",
                      x0=1 - shell_r, y0=1 - shell_r,
                      x1=1 + shell_r, y1=1 + shell_r,
                      fillcolor="orange", line_color="red", opacity=0.4)
        annotation = "Inert core + H-burning shell"

    elif "supernova" in stage:
        # Central glowing core
        core_r = 0.2 + 0.1 * step_frac
        fig.add_shape(type="circle", xref="x", yref="y",
                    x0=1 - core_r, y0=1 - core_r,
                    x1=1 + core_r, y1=1 + core_r,
                    fillcolor="white", line_color="orange", opacity=0.8)

        # Expanding glowing shockwave rings
        num_rings = 3
        for i in range(num_rings):
            ring_r = 0.6 + i * 0.3 + step_frac * 0.5  # expanding with step_frac
            fig.add_shape(type="circle", xref="x", yref="y",
                        x0=1 - ring_r, y0=1 - ring_r,
                        x1=1 + ring_r, y1=1 + ring_r,
                        line=dict(color="red", width=2),
                        opacity=max(0.2, 0.6 - i * 0.2))

        annotation = "💥 Supernova Explosion"

    elif "white dwarf" in stage:
        core_r = 0.1 + 0.02 * step_frac  # Slight pulsation
        fig.add_shape(type="circle", xref="x", yref="y",
                      x0=1 - core_r, y0=1 - core_r,
                      x1=1 + core_r, y1=1 + core_r,
                      fillcolor="lightgray", line_color="black")
        annotation = "Compact degenerate core"

    elif "neutron star" in stage:
        core_r = 0.05 + 0.01 * step_frac
        fig.add_shape(type="circle", xref="x", yref="y",
                      x0=1 - core_r, y0=1 - core_r,
                      x1=1 + core_r, y1=1 + core_r,
                      fillcolor="purple", line_color="black")
        annotation = "Neutron star core"

    elif "black hole" in stage:
        # Central dark core
        fig.add_shape(type="circle", xref="x", yref="y",
                    x0=0.9, y0=0.9, x1=1.1, y1=1.1,
                    fillcolor="black", line_color="white")

        # Event horizon glow (ring)
        ring_r = 0.3 + 0.05 * (step_frac * 10 % 1)  # mild pulsating glow
        fig.add_shape(type="circle", xref="x", yref="y",
                    x0=1 - ring_r, y0=1 - ring_r,
                    x1=1 + ring_r, y1=1 + ring_r,
                    line=dict(color="purple", width=3),
                    opacity=0.6)

        annotation = "🕳 Black Hole Core"


    # Annotation
    fig.add_annotation(x=1, y=2.2, text=annotation, showarrow=False,
                       font=dict(size=14), xanchor="center")

    # Layout
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False, range=[-0.5, 2.5])
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False, range=[-0.5, 2.5])
    fig.update_layout(height=400, width=400, margin=dict(t=50, b=10, l=10, r=10))

    return fig
