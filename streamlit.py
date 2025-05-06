
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud
from collections import Counter
import string

# Load data
df = pd.read_csv("sentiment_scores.csv")
keyword_df = pd.read_csv("keyword_freq.csv")

# Streamlit Page Setup
st.set_page_config(page_title="Asia’s Economic Outlook on U.S. Tariff Policy", layout="wide")
st.title("📈 Data-Driven Business Insights into Asia’s Economic Outlook on U.S. Tariff Policy")

st.markdown("""
This dashboard analyzes how Asia-based news media frames U.S. tariff policies using sentiment scoring and keyword analysis.  
It delivers business-relevant insights that reflect **regional market sentiment** and help identify potential risks and opportunities.
""")

# Filter by Source
sources = st.sidebar.multiselect("📌 Filter by Source", df["Source"].unique(), default=df["Source"].unique())
filtered_df = df[df["Source"].isin(sources)]

# 1. Sentiment Table
st.subheader("1. Sentiment Scores")
st.dataframe(filtered_df[["Source", "URL", "Compound", "Positive", "Neutral", "Negative"]])

# 2. Sentiment Boxplot
st.subheader("2. Sentiment Distribution by Source")
fig1, ax1 = plt.subplots()
sns.boxplot(data=filtered_df, x="Source", y="Compound", palette="Set2", ax=ax1)
st.pyplot(fig1)

# Average Scores Table
st.markdown("**📊 Average Compound Score per Source**")
st.dataframe(filtered_df.groupby("Source")["Compound"].mean().reset_index())

# 3. Keyword Frequency
st.subheader("3. Top 20 Keywords")
fig2, ax2 = plt.subplots()
sns.barplot(data=keyword_df.head(20), x="Frequency", y="Keyword", palette="viridis", ax=ax2)
st.pyplot(fig2)

# 4. Word Cloud
st.subheader("4. Word Cloud")
all_text = " ".join(df["Content"].astype(str)).lower()
words = all_text.translate(str.maketrans('', '', string.punctuation)).split()
stopwords = set([
    "said", "would", "could", "also", "one", "new", "us", "u.s.", "get", "year",
    "news", "reuters", "aljazeera", "cnn", "say", "make", "like", "may", "asia", "amp"
])
filtered_words = [w for w in words if w not in stopwords and len(w) > 3]
word_freq = Counter(filtered_words)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(word_freq))
fig3, ax3 = plt.subplots(figsize=(15, 7))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

