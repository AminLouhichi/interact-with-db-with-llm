import streamlit as st
import pandas as pd
from databases import *
from chromadb_vector import *
from traitement import *

# Title of the app
st.title("Ask questions about your data")

# Dropdown to select a choice
dbs=database()
choice = st.selectbox("Select a choice dtabase", dbs)

# Display the chosen choice
st.write(f"Chosen: {choice}")

# Text input to write a variable
var_input = st.text_input("Enter a variable", "")
contexte,tables=create_context(choice)
tables=list(set(tables))
co=vector(contexte,tables)


print(all_statements)
# Placeholder
print(tables)
st.text("Chat with me")

# Button to trigger an action
if st.button("Click Me"):
    result=query(co, var_input)

    all_statements = ', '.join([stmt.replace('\n', ',') for stmt_list in result for stmt in stmt_list])
    # Sample DataFrame (replace this with your own DataFrame)
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "Location": ["New York", "San Francisco", "Los Angeles"]
    }
    df = pd.DataFrame(data)
    
    # Display the DataFrame
    st.write("DataFrame:", df)
