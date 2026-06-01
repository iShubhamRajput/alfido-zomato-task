# Executive Summary: Zomato Dataset Analysis

**Task:** Zomato Dataset Analysis  
**Dataset:** Kaggle `bhanupratapbiswas/zomato`  
**Prepared for:** Alfido Tech Internship Submission

## Objective

The objective of this task was to analyze restaurant and review data to identify useful insights about ratings, cuisines, locations, price ranges, and factors that affect restaurant performance.

## Data and Cleaning

The dataset contains **56,252 rows** and **13 columns**. Key fields include restaurant name, location, cuisines, online ordering, table booking, rating, votes, liked dishes, restaurant type, and approximate cost for two people.

Cleaning work included:

- Converted rating text such as `4.1/5` into numeric ratings.
- Treated `NEW`, `-`, blanks, and invalid rating values as missing.
- Converted cost values into numeric rupee amounts.
- Converted votes into numeric values.
- Split multiple cuisines into separate cuisine labels.
- Used liked-dish text for popular dish and word-cloud analysis.

After cleaning, **41,665 valid rated rows** were used for the main analysis. The average clean restaurant rating was **3.70**.

## Main Findings

- **Location matters:** BTM has the highest restaurant count, but premium/central locations such as **Lavelle Road**, **St. Marks Road**, **Church Street**, and **Koramangala blocks** have stronger average ratings.
- **Cuisine pattern:** North Indian and Chinese are the most common cuisines, but niche cuisines such as **Modern Indian**, **Japanese**, **Mediterranean**, **European**, and **Korean** receive higher average ratings.
- **Price affects rating:** Higher price segments have better average ratings. Budget restaurants average around **3.57**, while premium restaurants average around **4.13**.
- **Table booking is a strong signal:** Restaurants with table booking average **4.14**, compared with **3.62** for restaurants without table booking.
- **Popular dish tags:** Pasta, burgers, cocktails, pizza, biryani, and coffee are frequent in liked dishes and can improve search and promotions.

## Business Recommendations

1. Promote high-rated food hubs such as Lavelle Road, St. Marks Road, Church Street, and Koramangala.
2. Use table booking as a strong quality signal in ranking and recommendation systems.
3. Create separate rankings for budget, mid-range, premium, and luxury restaurants.
4. Highlight niche high-rated cuisines for discovery and curated collections.
5. Use popular dish terms as searchable tags and marketing campaign keywords.

## Deliverables

- Notebook: `zomato_analysis.ipynb`
- Report: `zomato_report.md` and `zomato_report.pdf`
- Charts: files inside `charts/`
- Dataset: `data/zomato.csv`

