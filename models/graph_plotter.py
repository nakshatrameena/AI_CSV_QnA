import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
import base64

def plot_graph(df, column1, column2, graph_type="scatter"):
    """Generate graphs based on user input."""
    plt.figure(figsize=(6, 4))
    
    if graph_type == "scatter":
        sns.scatterplot(x=df[column1], y=df[column2])
    elif graph_type == "bar":
        sns.barplot(x=df[column1], y=df[column2])
    else:
        return "Invalid graph type"

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode("utf-8")
    
    return f'<img src="data:image/png;base64,{img_str}" />'
