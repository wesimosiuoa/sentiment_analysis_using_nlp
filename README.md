# Sentiment Analysis using NLP

This project uses Natural Language Processing (NLP) and Sentiment Analysis to analyze textual data and visualize the sentiment distribution. It uses the `NLTK` library's SentimentIntensityAnalyzer for sentiment classification and generates visualizations such as bar charts and pie charts.
## Visualizations
The project generates two main types of visualizations:

**1. Bar Chart**: Shows the count of positive, negative, and neutral sentiments.
**2. Pie Chart**: Displays the percentage distribution of each sentiment type.

## Contributing
If you'd like to contribute to the project, feel free to fork the repository and submit a pull request.

## License
You can use this markdown content for your README file to give an overview of your project, its features, installation instructions, and code usage.



## Features

- **Sentiment Analysis**: Classifies text as Positive, Negative, or Neutral.
- **Data Preprocessing**: Cleans and preprocesses text by removing stopwords.
- **Visualizations**: Displays a bar chart and pie chart to show sentiment distribution.
- **File Conversion**: Converts Excel files to CSV for analysis.

## Technologies Used

- **Python**: The main programming language used.
- **NLTK**: Library for sentiment analysis and text processing.
- **Matplotlib**: Library for generating visualizations (bar chart and pie chart).
- **Pandas**: For handling data in CSV format.
- **Jupyter**: Optional for running the code in a notebook environment.

## Installation

1. Clone the repository or download the project files.
2. Install the required libraries using pip:
    ```bash
    pip install pandas nltk matplotlib openpyxl
    ```

3. Download the necessary NLTK datasets by running the following code:
    ```python
    import nltk
    nltk.download('vader_lexicon')
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

4. Place your dataset (`sentimentdataset.xlsx`) in the project directory.
## Usage

1. Place your Excel dataset (e.g., `sentimentdataset.xlsx`) in the project folder.
2. Run the Python script to preprocess the data and generate sentiment visualizations.
    ```bash
    python sentiment_analysis.py
    ```

3. The script will convert the Excel file to CSV, preprocess the text data, perform sentiment analysis, and display a bar chart and pie chart showing the sentiment distribution.

### Code Example

Here is an example of how the sentiment analysis and visualizations are done:

```python
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Preprocess and analyze sentiment
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound > 0.05:
        return "Positive"
    elif compound < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Read the dataset
data = pd.read_excel('sentimentdataset.xlsx', engine='openpyxl')
data['Sentiment'] = data['Text'].apply(get_sentiment)

# Generate bar chart
sentiment_counts = Counter(data['Sentiment'])
plt.bar(sentiment_counts.keys(), sentiment_counts.values())
plt.title('Sentiment Distribution (Bar Chart)')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Generate pie chart
sizes = list(sentiment_counts.values())
labels = list(sentiment_counts.keys())
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode=(0.1, 0, 0))
plt.title('Sentiment Distribution (Pie Chart)')
plt.axis('equal')
plt.show()


