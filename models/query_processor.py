import ollama
from pydantic import BaseModel

class QueryRequest(BaseModel):
    """Defines structure for LLM input."""
    question: str
    dataframe: str  # CSV converted to string

def process_query(question, df):
    """Query the LLM with CSV data."""
    try:
        # Ensure df is not empty
        if df is None or df.empty:
            return "Error: CSV data is missing."

        # Convert dataframe to a string format for LLM processing
        input_data = QueryRequest(question=question, dataframe=df.to_csv()).dict()
        
        # Send query to LLM
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": str(input_data)}])

        # Return the model's response
        return response["message"]["content"]
    
    except Exception as e:
        return f"Error: {str(e)}"