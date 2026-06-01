"""
Zomato Dataset Analysis
Alfido Tech Internship Task 1

This Python script is a GitHub-readable backup of the Jupyter notebook.
Use the notebook for charts, and use this file if GitHub notebook preview fails.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud


sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)


def load_data():
    possible_paths = [
        Path("data/zomato.csv"),
        Path("zomato.csv"),
        Path("zomato_task1/data/zomato.csv"),
    ]
    for path in possible_paths:
        if path.exists():
            return pd.read_csv(path, on_bad_lines="skip")
    raise FileNotFoundError("Could not find zomato.csv. Put it in data/zomato.csv.")


def clean_data(df):
    clean = df.copy()

    for col in clean.select_dtypes(include="object").columns:
        clean[col] = clean[col].astype(str).str.strip()
        clean[col] = clean[col].replace({"nan": None, "None": None, "": None})

    clean["rating"] = (
        clean["rate"].astype(str).str.extract(r"(\d+(?:\.\d+)?)")[0].astype(float)
    )
    clean.loc[(clean["rating"] < 0) | (clean["rating"] > 5), "rating"] = np.nan

    cost_col = "approx_cost(for two people)"
    clean["cost_for_two"] = (
        clean[cost_col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.extract(r"(\d+(?:\.\d+)?)")[0]
        .astype(float)
    )

    clean["votes"] = pd.to_numeric(clean["votes"], errors="coerce")
    valid = clean[clean["rating"].notna()].copy()
    return clean, valid


def save_chart(path):
    Path("charts").mkdir(exist_ok=True)
    plt.tight_layout()
    plt.savefig(Path("charts") / path, dpi=160, bbox_inches="tight")
    plt.close()


def main():
    df = load_data()
    clean, valid = clean_data(df)

    print("Original rows:", len(df))
    print("Clean valid rows:", len(valid))
    print("Average rating:", round(valid["rating"].mean(), 2))
    print("Average cost for two:", round(valid["cost_for_two"].mean(), 0))

    top_locations = valid["location"].value_counts().head(12)
    sns.barplot(x=top_locations.values, y=top_locations.index, palette="viridis")
    plt.title("Top Restaurant Location Hotspots")
    plt.xlabel("Restaurant Count")
    plt.ylabel("Location")
    save_chart("top_locations.png")

    location_rating = (
        valid.groupby("location")
        .agg(count=("name", "count"), avg_rating=("rating", "mean"))
        .query("count >= 100")
        .sort_values("avg_rating", ascending=False)
        .head(12)
    )
    print("\nBest rated locations:")
    print(location_rating)

    cuisine_df = valid[["cuisines", "rating"]].dropna().copy()
    cuisine_df["cuisine"] = cuisine_df["cuisines"].str.split(",")
    cuisine_df = cuisine_df.explode("cuisine")
    cuisine_df["cuisine"] = cuisine_df["cuisine"].str.strip()

    cuisine_summary = (
        cuisine_df.groupby("cuisine")
        .agg(count=("rating", "size"), avg_rating=("rating", "mean"))
        .query("count >= 100")
    )
    print("\nMost common cuisines:")
    print(cuisine_summary.sort_values("count", ascending=False).head(10))
    print("\nHighest rated cuisines:")
    print(cuisine_summary.sort_values("avg_rating", ascending=False).head(10))

    valid["price_segment"] = pd.cut(
        valid["cost_for_two"],
        bins=[0, 300, 600, 1000, 2000, np.inf],
        labels=[
            "Budget <=300",
            "Value 301-600",
            "Mid 601-1000",
            "Premium 1001-2000",
            "Luxury >2000",
        ],
    )
    price_rating = (
        valid.groupby("price_segment", observed=False)
        .agg(count=("name", "count"), avg_rating=("rating", "mean"))
        .reset_index()
    )
    print("\nPrice segment analysis:")
    print(price_rating)

    sns.barplot(data=price_rating, x="price_segment", y="avg_rating", palette="magma")
    plt.title("Price Segment vs Average Rating")
    plt.xticks(rotation=25, ha="right")
    plt.ylim(3.3, 4.3)
    save_chart("price_vs_rating.png")

    valid_order = valid[
        valid["online_order"].isin(["Yes", "No"])
        & valid["book_table"].isin(["Yes", "No"])
    ].copy()
    print("\nOnline order rating:")
    print(valid_order.groupby("online_order")["rating"].agg(["count", "mean"]))
    print("\nTable booking rating:")
    print(valid_order.groupby("book_table")["rating"].agg(["count", "mean"]))

    corr = valid[["rating", "cost_for_two", "votes"]].corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation Heatmap")
    save_chart("correlation_heatmap.png")

    dish_text = " ".join(
        valid["dish_liked"].dropna().astype(str).str.replace(",", " ", regex=False)
    )
    if not dish_text.strip():
        dish_text = " ".join(
            valid["cuisines"].dropna().astype(str).str.replace(",", " ", regex=False)
        )
    if dish_text.strip():
        wordcloud = WordCloud(
            width=1100, height=500, background_color="white", colormap="tab10"
        ).generate(dish_text)
        plt.figure(figsize=(13, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud of Popular Dishes / Cuisines")
        save_chart("wordcloud.png")

    print("\nRecommendations:")
    print("1. Promote high-rated localities such as Lavelle Road and Koramangala.")
    print("2. Use table booking as a strong quality signal.")
    print("3. Create separate ranking lists by price segment.")
    print("4. Highlight niche high-rated cuisines.")
    print("5. Use popular dish names as search and marketing tags.")


if __name__ == "__main__":
    main()

