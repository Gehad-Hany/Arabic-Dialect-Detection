# Arabic Dialect Detection App

This is a Streamlit-based web application that detects the dialect of Arabic text using a pre-trained BERT model from CAMeL-Lab.

## Features

- Detects Arabic dialects: Egyptian, Gulf, Levantine, and English.
- Allows users to input multiple lines of text for batch analysis.
- Displays the predicted dialect and confidence score for each input text.
- Provides example phrases for quick testing.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/arabic-dialect-detection.git
    cd arabic-dialect-detection
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run project5_cv.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter Arabic text in the provided text area and click "Detect Dialect" to see the results.

## Example

You can try the following example phrases to see how the model performs:

- "إزيك عامل إيه؟" (Egyptian)
- "شلونك يا الطيب؟" (Gulf)
- "كيفك اليوم؟" (Levantine)
- "Hello, how are you?" (English)

## Files

- [project5_cv.py](http://_vscodecontentref_/0): The main application file containing the Streamlit UI and dialect detection logic.

## License

This project is licensed under the MIT License. See the LICENSE file for details.