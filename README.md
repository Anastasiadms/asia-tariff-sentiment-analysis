> Web scraping and NLP dashboard for analyzing Asia-based news sentiment on U.S. tariffs.

# Data-Driven Business Insights into Asia’s Economic Outlook on U.S. Tariff Policy Using Web Scraping, NLP & Streamlit Visualization

## Project Overview
This project is a real-world data-driven project that uses **web scraping, Natural Languange Processing (NLP), and streamlit based dashboard** to analyze how Asia-based media (CNN and Al-Jazeera) frames current U.S. tariff policies.

**Streamlit-Dashboard:** [https://asia-tariff-sentiment-analysis.streamlit.app/](https://asia-tariff-sentiment-analysis.streamlit.app/)

## Project Objectives
- Scrape 50-100 articles from CNN and Al Jazeera using pagination.
- Filter by keywords that related to trade and economy.
- Apply VADER sentiment analysis on article contents.
- Visualize the result using boxplots, tables, and word clouds.
- Build and Deploy dashboard using Streamlit Cloud.

## Summary of Project's Workflow
1. News Sources
   - Al Jazeera : `/news/asia-pacific`, `/economy`, `/tag/us-china-trade-war`
   - CNN Asia : `/world/asia` 
2. Web Scraping Setup
   - Pagination handling
   - Used User-Agent Rotation headers
3. Filtering
   - Have minimum 100 words per article
   - Must contain certain keywords such as `tariff`, `trade`, `export`,           `china`, `economy`
4. Sentiment Analysis
   - Used VADER
   - Scoring based on Compound, Positive, Neutral, Negative
5. Export Data
    - `sentiment_scores.csv` and `keyword_freq.csv`

## Streamlit Dashboard Features
- Sentiment table with URLs and scores
- Boxplot of compound sentiment by source
- Keyword frequency bar chart  
- Word cloud from article content
- Sidebar filtering by source

## Project's Key Insight
- CNN news coverage on U.S. tariffs in Asia is highly polarized, ranging from strongly negative to strongly positive sentiment.
- Al Jazeera has a generally positive tone with more variation after expanding to multiple sections.
- Top keywords include *“trade,” “China,” “exports,” “tariffs,” and “economy.”*
- The dashboard helps stakeholders monitor how media sentiment may influence regional economic expectations.

