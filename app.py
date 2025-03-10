import gradio as gr
import pandas as pd
from models.file_handler import load_csv
from models.query_processor import process_query
from models.graph_plotter import plot_graph

df = None  # Global variable for dataset

def upload_csv(file):
    global df
    df = load_csv(file.name)
    return f"File {file.name} uploaded successfully!"

def ask_question(question):
    if df is None:
        return "Please upload a CSV file first."
    return process_query(question, df)

def generate_graph(column1, column2, graph_type):
    if df is None:
        return "Please upload a CSV file first."
    return plot_graph(df, column1, column2, graph_type)

# Define separate interfaces
upload_interface = gr.Interface(fn=upload_csv, inputs=gr.File(label="Upload CSV"), outputs=gr.Textbox(label="Upload Status"))

query_interface = gr.Interface(fn=ask_question, inputs=gr.Textbox(label="Ask a Question"), outputs=gr.Textbox(label="Query Result"))

graph_interface = gr.Interface(
    fn=generate_graph,
    inputs=[
        gr.Textbox(label="Column 1 for Graph"),
        gr.Textbox(label="Column 2 for Graph"),
        gr.Dropdown(["scatter", "bar"], label="Graph Type"),
    ],
    outputs=gr.HTML(label="Graph Output")
)

# Combine all interfaces
iface = gr.TabbedInterface([upload_interface, query_interface, graph_interface], ["Upload CSV", "Ask Question", "Generate Graph"])

if __name__ == "__main__":
    iface.launch()
