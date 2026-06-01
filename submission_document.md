# Zomato Dataset Analysis Submission Document

**Candidate:** Shubham Rajput  
**Internship:** Alfido Tech  
**Task:** 1 - Zomato Dataset Analysis  
**Dataset:** `bhanupratapbiswas/zomato` from Kaggle  
**GitHub Repository Link:** GitHub repository link - https://github.com/iShubhamRajput/alfido-zomato-task/blob/main/zomato_analysis.ipynb 
**Notebook Link:** GitHub notebook link - https://colab.research.google.com/drive/1v5hYBUsJCzOxq1VYDo8bYBjkt2G8Ua8o?usp=sharing 

## 1. Executive Summary

This project analyzes the Zomato restaurant dataset to understand factors affecting restaurant ratings. The analysis covers data cleaning, missing value handling, cuisine-level performance, location hotspots, price-rating relationship, table booking impact, online ordering impact, and popular dish terms.

The dataset has **56,252 rows** and **13 columns**. After cleaning invalid and missing ratings, **41,665 valid rated rows** were used for analysis. The average clean rating is **3.70**. Key findings show that premium localities, niche cuisines, higher price segments, and table booking availability are associated with stronger restaurant ratings.

## 2. Notebook and Code

Notebook file:

- `zomato_analysis.ipynb`

Main notebook sections:

- Library setup and dataset loading
- Data inspection
- Data cleaning
- Missing value analysis
- Location analysis
- Cuisine analysis
- Price vs rating analysis
- Online ordering and table booking analysis
- Correlation heatmap
- Word cloud
- Recommendations and conclusion

## 3. Dataset

Dataset used:

- Kaggle dataset: `bhanupratapbiswas/zomato`
- Local file: `data/zomato.csv`

Main columns:

- `name`
- `location`
- `cuisines`
- `rate`
- `votes`
- `online_order`
- `book_table`
- `dish_liked`
- `approx_cost(for two people)`
- `listed_in(type)`

## 4. Data Cleaning

Cleaning steps completed:

- Parsed ratings from text format such as `4.1/5`.
- Treated invalid values such as `NEW`, `-`, blank values, and out-of-range values as missing.
- Converted cost text into numeric rupee values.
- Converted votes into numeric values.
- Split comma-separated cuisines for cuisine-level analysis.
- Used liked-dish text for word cloud and popular dish insights.

## 5. Charts and Visualizations

### 5.1 Location Hotspots

![Top Restaurant Location Hotspots](charts/location_hotspots.svg)

BTM has the highest number of restaurants, followed by Koramangala 5th Block, HSR, Indiranagar, JP Nagar, Jayanagar, Whitefield, and Marathahalli.

### 5.2 Cuisine Analysis

![Cuisine Popularity and Ratings](charts/top_cuisines.svg)

North Indian and Chinese are the most common cuisines, but niche cuisines such as Modern Indian, Malaysian, Japanese, Mediterranean, European, and Korean have stronger average ratings.

### 5.3 Price vs Rating

![Price Segment vs Average Rating](charts/price_vs_rating.svg)

Premium restaurants show higher average ratings than budget restaurants. The price-rating correlation is approximately **0.385**, showing a moderate positive relationship.

### 5.4 Table Booking and Online Ordering

![Table Booking and Online Ordering Impact](charts/table_booking_impact.svg)

Table booking has a strong positive relationship with restaurant rating. Restaurants with table booking average **4.14**, while restaurants without table booking average **3.62**.

## 6. Key Findings

- Average rating after cleaning: **3.70**
- Clean valid rated rows: **41,665**
- Top restaurant-density location: **BTM**
- Strong rated location among large locations: **Lavelle Road**
- Most common cuisine: **North Indian**
- Strong high-rated cuisines: **Modern Indian**, **Malaysian**, **Japanese**, **Mediterranean**, **European**
- Table booking is a stronger quality indicator than online ordering.
- Premium and luxury restaurants generally receive better ratings than budget restaurants.

## 7. Recommendations for Alfido Tech

1. **Promote high-rated localities:** Highlight restaurants from Lavelle Road, Church Street, St. Marks Road, and Koramangala for premium discovery.
2. **Use table booking in ranking:** Since table booking is strongly linked with higher ratings, it should be used as a recommendation signal.
3. **Create price-based ranking:** Budget, mid-range, and premium restaurants should be ranked separately for fairer user recommendations.
4. **Highlight niche cuisines:** Modern Indian, Japanese, Mediterranean, European, Korean, and Asian cuisines can be used for curated collections.
5. **Use dish tags:** Pasta, burgers, pizza, biryani, coffee, and cocktails should be used as search tags and campaign keywords.

## 8. Conclusion

The Zomato analysis shows that restaurant ratings are influenced by location, cuisine, price segment, table booking availability, and customer engagement. A strong recommendation system should combine rating, locality, cuisine, cost segment, table booking, votes, and popular dish tags.

