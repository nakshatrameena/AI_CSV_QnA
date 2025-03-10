# AI CSV QnA - Gradio-Based CSV Question Answering & Visualization

## Project Overview
This project is a **Gradio-based web application** that allows users to:  
 Upload a CSV file 
 Ask **questions** about the dataset using an **LLM (Large Language Model)** 
 Generate **graphs and visualizations** based on the data 

The application integrates **Ollama (Local LLM Execution), Pydantic AI, and Gradio** to process CSV files and provide interactive insights.

---

##  Features
✔ **CSV File Handling** - Upload and validate CSV files  
✔ **AI-Powered Q&A** - Ask text & numerical questions, answered by an **LLM**  
✔ **Data Visualization** - Generate and view graphs within Gradio  
✔ **Local LLM Execution** - Uses **Mistral/Llama2 (via Ollama)** for fast processing  
✔ **Error Handling** - Handles missing data, invalid inputs, and LLM failures  

---

##  Tech Stack
- **Python**  (Backend Logic)
- **Gradio** (Frontend UI)
- **Pandas** (CSV Processing)
- **Matplotlib & Seaborn** (Graph Plotting)
- **Ollama** (LLM Execution)
- **Pydantic AI** (Query Structuring)
- **GitHub** (Version Control)

---

##  Project Structure
```
AI_CSV_QnA/
│── app.py                   # Main application file
│── requirements.txt          # Required dependencies
│── models/
│   ├── query_processor.py    # LLM-based query processing
│   ├── graph_plotter.py      # Graph visualization functions
│   ├── file_handler.py       # CSV file handling & validation
│── static/
│   ├── sample.csv            # Sample dataset for testing
│── README.md                 # Project documentation
```

---

## 🛠️ Installation & Setup

### **1️ Clone the Repository**
```bash
git clone https://github.com/nakshatrameena/AI_CSV_QnA.git
cd AI_CSV_QnA
```

### **2️ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️ Install & Run Ollama**
- Download & install **Ollama** from: [https://ollama.com/download](https://ollama.com/download)
- Pull the LLM model (choose a smaller model for low-memory systems):
```bash
ollama pull mistral  # OR
ollama pull llama2:7b
```

### **4️ Run the Application**
```bash
python app.py
```
Open your browser and go to **[http://127.0.0.1:7860](http://127.0.0.1:7860)**  

---

## 📊 How the Project Works

### **1️ Upload a CSV File**
- The user uploads a CSV file using **Gradio's file upload**.
- The file is processed using **Pandas** to check for validity.

### **2️ Ask Questions About the Data**
- The user enters a question related to the dataset.
- The **query is sent to an LLM (Mistral/Llama2)** via **Ollama**.
- The model processes the question and generates a response.

### **3 Generate Graphs**
- The user selects two columns for visualization.
- The app supports **scatter plots & bar charts**.
- Graphs are plotted using **Matplotlib & Seaborn**.

---

## Example Queries
- "What is the average price?"
- "Which city has the most expensive house?"
- "Show a scatter plot of Price vs Area."

---

## Troubleshooting

### **Ollama Memory Error**
If you see **"model requires more system memory"**, switch to a smaller LLM:
```bash
ollama pull mistral
```
Then update `query_processor.py` to use `"mistral"` instead of `"llama3"`.

---

## Submission Details
- **GitHub Repo:** [https://github.com/nakshatrameena/AI_CSV_QnA](https://github.com/nakshatrameena/AI_CSV_QnA)  
- **Developed by:** Nakshatra Meena  
- **Submission Date:** March 13, 2024  

---

## License
This project is for educational purposes only. Feel free to modify and improve!

---

**Developed by [Nakshatra Meena](https://github.com/nakshatrameena)**

