import pandas as pd
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from collections import Counter
# from nltk.tokenize import word_tokenize

from nltk.tokenize import word_tokenize

# # Example usage of word_tokenize
# text = "This is an example sentence."
# words = word_tokenize(text)
# print(words)

def read_and_convert():
    try:
        # Attempt to read the file
        data = pd.read_excel('sentimentdataset.xlsx', engine='openpyxl')
        # print(f"Social Media Data\n{data.head()}")

        # Convert to CSV
        data.to_csv('sentimentdataset.csv', index=False)
        print("File converted to CSV.")
        df =  pd.read_csv('sentimentdataset.csv')

        return df
    except Exception as e:
        print(f"An error occurred: {e}")

print (f" CSV FILE \n ", read_and_convert())

analyzer = SentimentIntensityAnalyzer()
data = read_and_convert()
df = pd.DataFrame(data)

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

def get_sentiment(text): 
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound > 0.05: 
        return "Positive"
    
    elif compound < -0.05: 
        return "Negative"
    else : 
        return "Neutral"
    

df['Processed_Text'] = df['Text'].apply(preprocess_text)
print (f" Processed Text \n {df.head}")
df["Sentiment"] = df["Text"].apply(get_sentiment)
print(df) 
print ("  Processed \n ", df['Processed_Text'])
print ("  Sentiment \n ", df['Sentiment'])


sentiments = [get_sentiment(text) for text in df["Text"]]

# Count occurrences of each sentiment
sentiment_counts = Counter(sentiments)

# Create a bar plot for sentiment distribution
labels = sentiment_counts.keys()
values = sentiment_counts.values()

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['green', 'red', 'gray'])

# Adding title and labels
plt.title("Sentiment Distribution Bar Chart  - Reviews from different platforms. ")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()


labels = list(sentiment_counts.keys())  
sizes = list(sentiment_counts.values())  
colors = ['green', 'red', 'gray'] 
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=(0.1, 0, 0))
plt.title("Sentiment Distribution Pie Chart - Reviews from different platforms.  ")
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.show()




