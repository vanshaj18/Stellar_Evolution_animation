import plotly.graph_objects as go

def shell_structure_figure(stage: str):
    fig = go.Figure()
    stage = stage.lower()

    # Base star circle (outer envelope)
    fig.add_shape(type="circle",
                  xref="x", yref="y",
                  x0=0, y0=0, x1=2, y1=2,
                  line_color="black", fillcolor="lightyellow")
    
    # Core and shell layers depend on stage:
    if "main sequence" in stage:
        # Core burning hydrogen
        fig.add_shape(type="circle", xref="x", yref="y", x0=0.7, y0=0.7, x1=1.3, y1=1.3,
                      fillcolor="orange", line_color="red", name="Core H-burning")
        annotation = "Core: H fusion"
    elif "subgiant" in stage or "giant" in stage:
        # Inert core + hydrogen shell
        fig.add_shape(type="circle", xref="x", yref="y", x0=0.8, y0=0.8, x1=1.2, y1=1.2,
                      fillcolor="gray", line_color="black", name="Inert Core")
        fig.add_shape(type="circle", xref="x", yref="y", x0=0.6, y0=0.6, x1=1.4, y1=1.4,
                      fillcolor="orange", line_color="red", opacity=0.4, name="H Shell")
        annotation = "Inert core + H-burning shell"
    elif "supernova" in stage:
        # Core collapse - marked differently
        fig.add_shape(type="rect", x0=0, y0=0, x1=2, y1=2,
                      fillcolor="darkred", opacity=0.6, line_color="red")
        annotation = "Core Collapse!"
    elif "white dwarf" in stage:
        # Compact hot core only
        fig.add_shape(type="circle", xref="x", yref="y", x0=0.9, y0=0.9, x1=1.1, y1=1.1,
                      fillcolor="lightgray", line_color="black", name="White Dwarf")
        annotation = "Compact degenerate core"
    elif "neutron star" in stage:
        # Very compact core
        fig.add_shape(type="circle", xref="x", yref="y", x0=0.95, y0=0.95, x1=1.05, y1=1.05,
                      fillcolor="purple", line_color="black", name="Neutron Star")
        annotation = "Neutron star core"
    else:
        annotation = "Unknown structure"

    # Add annotation
    fig.add_annotation(x=1, y=2.2, text=annotation, showarrow=False,
                       font=dict(size=14))

    # Layout cleanup
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False, range=[-0.5, 2.5])
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False, range=[-0.5, 2.5])
    fig.update_layout(height=400, width=400, margin=dict(t=50, b=10, l=10, r=10))

    return fig
