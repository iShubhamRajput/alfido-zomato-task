# Zomato Dataset Analysis Report

**Internship Task:** Zomato Dataset Analysis  
**Dataset:** `bhanupratapbiswas/zomato` from Kaggle  
**Objective:** Analyze restaurant and review data to find insights about ratings, cuisines, location preferences, price, and factors affecting ratings.

## 1. Dataset Overview

The dataset contains **56,252 rows** and **13 columns**. Important columns include restaurant name, location, cuisine, online ordering, table booking, rating, votes, liked dishes, restaurant type, and approximate cost for two people.

## 2. Data Cleaning Summary

The raw dataset had mixed text and numeric fields, so the following cleaning steps were required:

- Converted `rate` values such as `4.1/5` into numeric ratings.
- Treated `NEW`, `-`, and blank ratings as missing values.
- Converted `approx_cost(for two people)` from text to numeric by removing commas.
- Converted `votes` to numeric values.
- Removed invalid shifted rows where `online_order` or `book_table` was not `Yes` or `No`.
- Split comma-separated cuisines into individual cuisine names for cuisine-level analysis.
- Used `dish_liked` text for popular dish and word-cloud analysis.

Important missing-value observations:

| Column | Missing or Invalid Values |
|---|---:|
| rate | 10,116 |
| dish_liked | 28,225 |
| phone | 1,296 |
| approx_cost(for two people) | 521 |
| rest_type | 338 |
| cuisines | 203 |
| location | 126 |

After rating and category cleaning, **41,665 valid rows** were used for most analysis. The average clean rating was **3.70**.

## 3. Exploratory Data Analysis

### 3.1 Location Hotspots

Top restaurant-heavy locations:

| Location | Restaurant Count | Average Rating |
|---|---:|---:|
| BTM | 3,930 | 3.57 |
| Koramangala 5th Block | 2,319 | 4.01 |
| HSR | 2,019 | 3.67 |
| Indiranagar | 1,847 | 3.83 |
| JP Nagar | 1,717 | 3.68 |
| Jayanagar | 1,643 | 3.78 |
| Whitefield | 1,582 | 3.62 |
| Marathahalli | 1,443 | 3.54 |

Best-rated locations with at least 100 restaurants:

| Location | Count | Average Rating |
|---|---:|---:|
| Lavelle Road | 487 | 4.14 |
| Koramangala 3rd Block | 191 | 4.02 |
| St. Marks Road | 343 | 4.02 |
| Koramangala 5th Block | 2,319 | 4.01 |
| Church Street | 546 | 3.99 |
| Koramangala 4th Block | 841 | 3.92 |
| Cunningham Road | 475 | 3.90 |
| Residency Road | 605 | 3.86 |

**Insight:** BTM has the highest restaurant density, but premium and central food hubs such as Lavelle Road, St. Marks Road, Church Street, and Koramangala blocks achieve better average ratings.

### 3.2 Cuisine vs Rating

Most common cuisines:

| Cuisine | Count | Average Rating |
|---|---:|---:|
| North Indian | 17,406 | 3.64 |
| Chinese | 13,005 | 3.61 |
| South Indian | 6,394 | 3.61 |
| Fast Food | 6,360 | 3.61 |
| Continental | 5,245 | 3.96 |
| Biryani | 5,071 | 3.55 |
| Cafe | 4,828 | 3.90 |
| Desserts | 4,537 | 3.86 |
| Beverages | 3,873 | 3.81 |
| Italian | 3,213 | 3.95 |

Highest-rated cuisines with at least 100 entries:

| Cuisine | Count | Average Rating |
|---|---:|---:|
| Modern Indian | 145 | 4.31 |
| Malaysian | 109 | 4.31 |
| Japanese | 340 | 4.26 |
| Mediterranean | 546 | 4.21 |
| European | 687 | 4.17 |
| Korean | 141 | 4.15 |
| Asian | 1,204 | 4.14 |
| Steak | 558 | 4.09 |
| American | 1,336 | 4.07 |
| Salad | 1,062 | 4.07 |

**Insight:** Common cuisines like North Indian and Chinese dominate supply, but niche and premium cuisines such as Modern Indian, Japanese, Mediterranean, European, and Asian receive stronger ratings.

### 3.3 Price vs Rating

| Price Segment | Count | Average Rating |
|---|---:|---:|
| Budget <= 300 | 12,587 | 3.57 |
| Value 301-600 | 15,906 | 3.62 |
| Mid 601-1000 | 7,790 | 3.80 |
| Premium 1001-2000 | 4,518 | 4.13 |
| Luxury > 2000 | 617 | 4.12 |

The correlation between price and rating is approximately **0.385**, which means price and rating have a moderate positive relationship.

**Insight:** More expensive restaurants tend to receive higher ratings, probably because they offer better ambience, service, and dining experience. However, price alone does not guarantee high ratings.

### 3.4 Online Order and Table Booking

| Feature | Category | Count | Average Rating |
|---|---|---:|---:|
| Online Order | Yes | 27,206 | 3.72 |
| Online Order | No | 14,459 | 3.66 |
| Book Table | Yes | 6,304 | 4.14 |
| Book Table | No | 35,361 | 3.62 |

**Insight:** Online ordering gives only a small rating advantage. Table booking has a much stronger relationship with ratings, suggesting that dine-in experience and service quality are important rating drivers.

### 3.5 Popular Dishes

Most frequent liked dishes:

| Dish | Count |
|---|---:|
| Pasta | 3,387 |
| Burgers | 3,017 |
| Cocktails | 2,796 |
| Pizza | 2,702 |
| Biryani | 2,073 |
| Coffee | 1,988 |
| Mocktails | 1,868 |
| Sandwiches | 1,676 |
| Paratha | 1,563 |
| Noodles | 1,410 |

**Insight:** Pasta, burgers, cocktails, pizza, biryani, and coffee are highly visible in customer likes. Restaurants can use these dishes for menu highlighting and promotional campaigns.

## 4. Visualizations Included in Notebook

The notebook contains code for the following visualizations:

- Missing values heatmap.
- Rating distribution chart.
- Top locations bar chart.
- Top cuisines bar chart.
- Price segment vs rating chart.
- Online order and table booking comparison.
- Correlation heatmap for rating, cost, and votes.
- Word cloud for popular dishes.

## 5. Recommendations for Alfido Tech

1. **Focus restaurant discovery on high-performing localities.** Promote premium food hubs like Lavelle Road, St. Marks Road, Church Street, and Koramangala because they show consistently strong ratings.

2. **Use table booking as a quality signal.** Restaurants with table booking average **4.14**, much higher than restaurants without table booking. A recommendation system should give this feature meaningful weight.

3. **Segment restaurants by price instead of treating all restaurants equally.** Premium restaurants have higher average ratings, but budget restaurants have higher volume. Separate rankings for budget, mid-range, and premium restaurants will give fairer results.

4. **Promote niche high-rated cuisines.** Modern Indian, Japanese, Mediterranean, European, Korean, and Asian cuisines receive strong ratings and can be highlighted for users looking for quality dining experiences.

5. **Use popular dishes for search and marketing.** Dishes such as pasta, burgers, cocktails, pizza, biryani, and coffee appear frequently in liked dishes. These can be used in tags, filters, personalized recommendations, and campaign keywords.

## 6. Conclusion

The Zomato dataset shows that location, cuisine, price, table booking, and customer engagement all influence ratings. Table booking and premium dining segments are especially strong indicators of better ratings. High-density areas like BTM have many restaurants, but premium localities and Koramangala blocks perform better in average rating. A restaurant recommendation system should combine rating, cuisine, locality, cost segment, table booking, and popular dish tags to produce better user recommendations.

