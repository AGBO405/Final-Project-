
import pandas as pd
import matplotlib.pyplot as plt

crime = pd.read_csv("CrimeSheet.csv", low_memory=False)

print(crime.columns)
print("\n")

print(crime.head())
print("\n")

crime = crime.dropna(subset=["Neighborhood"])

crime_table = crime["Neighborhood"].value_counts().reset_index()
crime_table.columns = ["Neighborhood", "Crime Count"]

best_neighborhoods = crime_table.sort_values("Crime Count")

print("Top 10 neighborhoods with the fewest crimes:")
print(best_neighborhoods.head(10))
print("\n")

top10 = best_neighborhoods.head(10)

plt.figure(figsize=(10, 5))
plt.bar(top10["Neighborhood"], top10["Crime Count"])
plt.xticks(rotation=45)
plt.title("Top 10 Safest Neighborhoods (Fewest Crimes)")
plt.xlabel("Neighborhood")
plt.ylabel("Crime Count")
plt.tight_layout()
plt.show()