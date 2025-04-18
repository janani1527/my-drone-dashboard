import plotly.graph_objects as go

def create_gauge(title, value, min_val, max_val, unit, color="royalblue"):
    fig = go.Figure(go.Indicator(
        mode="gauge+number", 
        value=value, 
        title={'text': f"{title} ({unit})"},
        gauge={
            'axis': {'range': [min_val, max_val]},  # Set range of the gauge
            'bar': {'color': color},               # Color of the gauge bar
            'bgcolor': "white",
        }
    ))
    fig.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=0))
    return fig
