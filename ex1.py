import plotly.graph_objects as go

# Sample data
data = {
    'number': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'value': [42.1, 40.4, 44.3, 45.5, 46.1, 37.0, 46.0, 41.9, 39.7]
}

# Create a Plotly figure
fig = go.Figure()

# Create three horizontal shapes for the different background colors
fig.add_shape(
    go.layout.Shape(
        type="rect",
        x0=0,
        x1=9,
        y0=0,
        y1=38,
        fillcolor="red",
        opacity=0.5,
        layer="below",
    )
)

fig.add_shape(
    go.layout.Shape(
        type="rect",
        x0=0,
        x1=9,
        y0=38,
        y1=40,
        fillcolor="yellow",
        opacity=0.5,
        layer="below",
    )
)

fig.add_shape(
    go.layout.Shape(
        type="rect",
        x0=0,
        x1=9,
        y0=40,
        y1=44,
        fillcolor="green",
        opacity=0.5,
        layer="below",
    )
)

fig.add_shape(
    go.layout.Shape(
        type="rect",
        x0=0,
        x1=9,
        y0=44,
        y1=46,
        fillcolor="yellow",
        opacity=0.5,
        layer="below",
    )
)

fig.add_shape(
    go.layout.Shape(
        type="rect",
        x0=0,
        x1=9,
        y0=46,
        y1=84,
        fillcolor="red",
        opacity=0.5,
        layer="below",
    )
)

# Add a line plot
fig.add_trace(go.Scatter(x=data['number'], y=data['value'], mode='lines+markers'))

# Customize layout
fig.update_layout(
    title="Run Chart",
    xaxis_title="Number",
    yaxis_title="Value",
    yaxis=dict(range=[35, 50], tickvals=list(range(0, 51, 1)),),
    showlegend=False,
)

for i in range(len(data['number'])):
    value = data['value'][i]
    if value >= 46 or value <= 38:
        fig.add_annotation(
            x=data['number'][i],
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
fig.write_html('ex1.html', auto_open=True)
