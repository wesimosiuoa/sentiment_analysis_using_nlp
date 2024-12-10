import pandas as pd
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
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