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
# df = pd.DataFrame({
#     'Time': pd.date_range(start='1/1/2023', periods=100),
#     'Value': np.random.randn(100).cumsum()
# })
#
# fig = go.Figure()
#
# # Add trace
# fig.add_trace(go.Scatter(x=df['Value'], y=df['Time'], mode='lines+markers', name='lines+markers'))
#
# # Add shapes to the layout
# shapes = []
# for i in range(len(df)):
#     if df['Value'].iloc[i] > 8:
#         color = 'red'
#     elif 6 <= df['Value'].iloc[i] <= 8:
#         color = 'yellow'
#     else:
#         color = 'green'
#
#     shapes.append(
#         dict(
#             type="rect",
#             xref="paper",
#             yref="y",
#             x0=0,
#             y0=df['Time'].iloc[i],
#             x1=1,
#             y1=df['Time'].iloc[i + 1] if i < len(df) - 1 else df['Time'].iloc[i],
#             fillcolor=color,
#             opacity=0.5,
#             layer="below",
#             line_width=0,
#         )
#     )
#
# fig.update_layout(
#     title='Run Chart of Machine',
#     xaxis_title='Value',
#     yaxis_title='Time',
#     shapes=shapes
# )
#
# fig.show()


# import plotly.express as px
#
# fig = px.scatter(x=range(10), y=range(10))
# fig.write_html("file.html", auto_open=True)


# import pandas as pd
#
# df = pd.read_excel('gcs_data.xlsx')
#
# shift_avg_dict = {}
#
# for shift, group in df.groupby('Shift'):
#     gcs_values = group['GCS'].tolist()
#     avg_gcs = sum(gcs_values) / len(gcs_values)
#     shift_avg_dict[shift] = avg_gcs
#
# # Convert the dictionary to two separate lists
# shift_numbers = list(shift_avg_dict.keys())
# average_gcs_values = list(shift_avg_dict.values())
#
# print(shift_avg_dict)

import pandas as pd

df = pd.read_excel('gcs_data.xlsx')
shift_numbers = []
average_gcs_values = []

for shift, group in df.groupby('Shift'):
    gcs_values = group['GCS'].tolist()
    avg_gcs = sum(gcs_values) / len(gcs_values)
    shift_numbers.append(shift)
    average_gcs_values.append(avg_gcs)

data = {
    'shift': shift_numbers,
    'avg': average_gcs_values
}


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


