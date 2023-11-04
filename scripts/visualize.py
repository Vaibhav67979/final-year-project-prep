import plotly.graph_objects as go

def visualize(data, WL1, LCL, UCL, SC1, SC2):
    fig = go.Figure()

    fig.add_shape(
        go.layout.Shape(
            type="rect",
            # x0=0,
            # x1=9,
            y0=0,
            y1=WL1,
            fillcolor="red",
            opacity=0.5,
            layer="below",
        )
    )

    fig.add_shape(
        go.layout.Shape(
            type="rect",
            # x0=0,
            # x1=9,
            y0=WL1,
            y1=LCL,
            fillcolor="yellow",
            opacity=0.5,
            layer="below",
        )
    )

    fig.add_shape(
        go.layout.Shape(
            type="rect",
            # x0=0,
            # x1=9,
            y0=LCL,
            y1=UCL,
            fillcolor="green",
            opacity=0.5,
            layer="below",
        )
    )

    fig.add_shape(
        go.layout.Shape(
            type="rect",
            # x0=0,
            # x1=9,
            y0=UCL,
            y1=SC1,
            fillcolor="yellow",
            opacity=0.5,
            layer="below",
        )
    )

    fig.add_shape(
        go.layout.Shape(
            type="rect",
            # x0=0,
            # x1=9,
            y0=SC1,
            y1=SC2,
            fillcolor="red",
            opacity=0.5,
            layer="below",
        )
    )

    # Add a line plot
    fig.add_trace(go.Scatter(x=data['shift'], y=data['avg'], mode='lines+markers'))

    # Customize layout
    fig.update_layout(
        title="Run Chart",
        xaxis_title="G.C Strength",
        yaxis_title="Batch",
        yaxis=dict(range=[1000, 1500], tickvals=list(range(0, 1600, 50)), ),
        showlegend=False,
    )

    for i in range(len(data['shift'])):
        value = data['avg'][i]
        if value >= 46 or value <= 38:
            fig.add_annotation(
                x=data['shift'][i],
                y=value,
                text=f'Value: {value:.1f}',
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor='black',
                opacity=0.7,
                bgcolor='lightgray',
                bordercolor='black',
                borderwidth=2,
            )

    fig.show()
    fig.write_html('VIZ.html', auto_open=True)