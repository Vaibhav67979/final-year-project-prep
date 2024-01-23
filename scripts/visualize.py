import plotly.graph_objects as go

def visualize(df, from_date, to_date, WL1, LCL, UCL, SC1, SC2):
    # Filter data for the specified date
    filtered_data = df[(df['Date'] >= from_date) & (df['Date'] <= to_date)]

    fig = go.Figure()

    fig.add_shape(
        go.layout.Shape(
            type="rect",
            x0=filtered_data['DateTime'].iloc[0],
            x1=filtered_data['DateTime'].iloc[-1],
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
            x0=filtered_data['DateTime'].iloc[0],
            x1=filtered_data['DateTime'].iloc[-1],
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
            x0=filtered_data['DateTime'].iloc[0],
            x1=filtered_data['DateTime'].iloc[-1],
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
            x0=filtered_data['DateTime'].iloc[0],
            x1=filtered_data['DateTime'].iloc[-1],
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
            x0=filtered_data['DateTime'].iloc[0],
            x1=filtered_data['DateTime'].iloc[-1],
            y0=SC1,
            y1=SC2,
            fillcolor="red",
            opacity=0.5,
            layer="below",
        )
    )

    # Add a scatter plot
    fig.add_trace(go.Scatter(x=filtered_data['DateTime'], y=filtered_data['GCS'], mode='lines+markers'))

    # Customize layout
    fig.update_layout(
        title=f"Run Chart - {from_date} to {to_date}",
        xaxis_title="Time",
        yaxis_title="G.C Strength",
        yaxis=dict(range=[1000, 1500]),
        showlegend=False,
    )

    for i in range(len(filtered_data)):
        value = filtered_data['GCS'].iloc[i]
        if value >= 46 or value <= 38:
            fig.add_annotation(
                x=filtered_data['DateTime'].iloc[i],
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
    fig.write_html(f'VIZ_{from_date}-{to_date}.html', auto_open=True)
