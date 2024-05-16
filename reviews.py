import pandas as pd

# Read the CSV file
data = pd.read_csv("data/winemag-data-130k-v2.csv")

# Group by country and calculate count and average points
summary = data.groupby('country').agg({'country': 'count', 'points': 'mean'}).rename(columns={'country': 'count'}).reset_index()

# Round the average points to 1 decimal point
summary['points'] = summary['points'].round(1)

# Sort the summary data by count in descending order
summary = summary.sort_values('count', ascending=False)

# Write the summary data to a new CSV file without index
summary.to_csv("data/reviews-per-country.csv", index=False)

print(summary)