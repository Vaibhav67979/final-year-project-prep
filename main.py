import plotly.express as px

# fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
# fig.write_html('first_figure.html', auto_open=True)
# fig.show()


# import plotly.graph_objects as go
#
# fig_widget = go.FigureWidget(fig)
# fig_widget

''' Basic graphs '''

# df = px.data.gapminder().query("country=='India'")
# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in India')
# fig.show()
# import plotly.graph_objects as go
# import pandas as pd
# import numpy as np
#
# # Assuming you have a DataFrame 'df' with time series data of the machine
# df = pd.DataFrame({
#     'Time': pd.date_range(start='1/1/2023', periods=100),
#     'Value': np.random.randn(100).cumsum()
# })
#
# fig = go.Figure()
#
# # Add traces
# fig.add_trace(go.Scatter(x=df['Time'], y=df['Value'], mode='lines+markers', name='lines+markers'))
#
# # Edit the layout
# fig.update_layout(
#     title='Run Chart of Machine',
#     xaxis_title='Time',
#     yaxis_title='Value',
#     plot_bgcolor='rgb(37, 150, 190)',
#     paper_bgcolor='#be4d25',
# )
#
#
# fig.show()

import plotly.graph_objects as go
import pandas as pd
import numpy as np

# # Assuming you have a DataFrame 'df' with time series data of the machine
# df = pd.DataFrame({
#     'Time': pd.date_range(start='1/1/2023', periods=100),
#     'Value': np.random.randn(100).cumsum()
# })
#
# fig = go.Figure()
#
# # Add traces for different sections
# # Section 1
# fig.add_trace(go.Scatter(x=df['Time'][:30], y=df['Value'][:30], mode='lines+markers', name='Section 1', line=dict(color='blue')))
#
# # Section 2
# fig.add_trace(go.Scatter(x=df['Time'][30:70], y=df['Value'][30:70], mode='lines+markers', name='Section 2', line=dict(color='red')))
#
# # Section 3
# fig.add_trace(go.Scatter(x=df['Time'][70:], y=df['Value'][70:], mode='lines+markers', name='Section 3', line=dict(color='green')))
#
# # Edit the layout
# fig.update_layout(title='Run Chart of Machine',
#                    xaxis_title='Time',
#                    yaxis_title='Value')
#
# fig.show()


# Assuming you have a DataFrame 'df' with time series data of the machine
df = pd.DataFrame({
    'Time': pd.date_range(start='1/1/2023', periods=100),
    'Value': np.random.randn(100).cumsum()
})

fig = go.Figure()

# Add trace
fig.add_trace(go.Scatter(x=df['Value'], y=df['Time'], mode='lines+markers', name='lines+markers'))

# Add shapes to the layout
shapes = []
for i in range(len(df)):
    if df['Value'].iloc[i] > 8:
        color = 'red'
    elif 6 <= df['Value'].iloc[i] <= 8:
        color = 'yellow'
    else:
        color = 'green'

    shapes.append(
        dict(
            type="rect",
            xref="paper",
            yref="y",
            x0=0,
            y0=df['Time'].iloc[i],
            x1=1,
            y1=df['Time'].iloc[i + 1] if i < len(df) - 1 else df['Time'].iloc[i],
            fillcolor=color,
            opacity=0.5,
            layer="below",
            line_width=0,
        )
    )

fig.update_layout(
    title='Run Chart of Machine',
    xaxis_title='Value',
    yaxis_title='Time',
    shapes=shapes
)

fig.show()

