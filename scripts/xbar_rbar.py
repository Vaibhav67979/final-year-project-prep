import plotly.graph_objects as go
import numpy as np

def spc_analysis(df, from_date, to_date, UCL, LCL):
    # Filter data for the specified date
    filtered_data = df[(df['Date'] >= from_date) & (df['Date'] <= to_date)]

    # Calculate X-bar (mean) and R (range)
    filtered_data['XBar'] = filtered_data['GCS'].mean()
    filtered_data['R'] = filtered_data['GCS'].max() - filtered_data['GCS'].min()

    # Create X-bar chart
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=filtered_data['DateTime'], y=filtered_data['GCS'], mode='lines+markers'))
    fig1.add_trace(go.Scatter(x=filtered_data['DateTime'], y=filtered_data['XBar'], mode='lines', name='X-bar'))
    fig1.add_trace(go.Scatter(x=filtered_data['DateTime'], y=[UCL]*len(filtered_data), mode='lines', name='UCL'))
    fig1.add_trace(go.Scatter(x=filtered_data['DateTime'], y=[LCL]*len(filtered_data), mode='lines', name='LCL'))
    fig1.update_layout(
        title=f"X-bar Chart - {from_date} to {to_date}",
        xaxis_title="Time",
        yaxis_title="X-bar Value",
        showlegend=True,
    )
    fig1.show()
    # fig1.write_html(f'XBar_{from_date}-{to_date}.html', auto_open=True)

    # Create R-bar chart
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=filtered_data['DateTime'], y=filtered_data['GCS'], mode='lines+markers'))
    fig2.add_trace(go.Scatter(x=filtered_data['DateTime'], y=filtered_data['R'], mode='lines', name='R-bar'))
    fig2.add_trace(go.Scatter(x=filtered_data['DateTime'], y=[UCL]*len(filtered_data), mode='lines', name='UCL'))
    fig2.add_trace(go.Scatter(x=filtered_data['DateTime'], y=[LCL]*len(filtered_data), mode='lines', name='LCL'))
    fig2.update_layout(
        title=f"R-bar Chart - {from_date} to {to_date}",
        xaxis_title="Time",
        yaxis_title="R Value",
        showlegend=True,
    )
    fig2.show()
    # fig2.write_html(f'RBar_{from_date}-{to_date}.html', auto_open=True)
    