import streamlit as st
from transformers import pipeline
import pandas as pd

# Load the dialect detection model
dialect_pipeline = pipeline("text-classification", model="CAMeL-Lab/bert-base-arabic-camelbert-da")

# Mapping model labels to dialect names
dialect_labels = {
    "LABEL_0": "مصري",
    "LABEL_1": "خليجي",
    "LABEL_2": "شامي",
    "LABEL_3": "إنجليزي"
}

# Streamlit UI
st.title("🌍 Arabic Dialect Detection App")
st.write("Enter Arabic text, and the model will identify its dialect.")

# Example phrases for quick testing
example_phrases = [
    "إزيك عامل إيه؟",  # Egyptian
    "شلونك يا الطيب؟",  # Gulf
    "كيفك اليوم؟",  # Levantine
    "Hello, how are you?"  # English
]

def analyze_dialect(texts):
    """Function to analyze multiple texts and return results in a structured format."""
    results = dialect_pipeline(texts)
    df_results = pd.DataFrame({
        "Text": texts,
        "Predicted Dialect": [dialect_labels.get(res['label'], "غير معروف") for res in results],
        "Confidence Score": [round(res['score'], 4) for res in results]
    })
    return df_results

# User input with support for multiple lines
user_input = st.text_area("Enter text(s) here (one per line):")

# Button to analyze dialect
if st.button("Detect Dialect"):
    if user_input.strip():
        texts = user_input.split("\n")
        with st.spinner("Analyzing dialects..."):
            results_df = analyze_dialect(texts)
        st.write("### Results:")
        st.dataframe(results_df)
    else:
        st.warning("Please enter at least one text for analysis.")

# Button to insert example text
if st.button("Try an Example"):
    st.text_area("Enter text(s) here (one per line):", value="\n".join(example_phrases))