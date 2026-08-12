import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("Paper_leaks_India(3).csv", encoding="cp1252")
df.columns = df.columns.str.strip()

# 2. Clean and prepare data
df["Date"] = pd.to_datetime(df["Date of Exam/Incident"], dayfirst=True, errors="coerce")
df["Year"] = df["Date"].dt.year
df["Action taken"] = df["Action taken"].fillna("Not specified")
df["Area(s) of Incident"] = df["Area(s) of Incident"].replace({
    "Maharasthra": "Maharashtra",
    "Gujrat": "Gujarat"
})

# 3. Basic EDA
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isna().sum())
print("\nConfirmation status:")
print(df["Leak Confirmation Status"].value_counts())
print("\nIncidents by year:")
print(df["Year"].value_counts().sort_index())
print("\nTop incident areas:")
print(df["Area(s) of Incident"].value_counts().head(10))
print("\nActions taken:")
print(df["Action taken"].value_counts())

# 4. Visualizations
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10,5))
df["Year"].value_counts().sort_index().plot(kind="bar")
plt.title("Paper Leak Incidents by Year")
plt.xlabel("Year"); plt.ylabel("Number of Incidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
df["Area(s) of Incident"].value_counts().head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Areas by Reported Paper Leak Incidents")
plt.xlabel("Number of Incidents"); plt.ylabel("Area")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,5))
df["Leak Confirmation Status"].value_counts().plot(kind="bar")
plt.title("Leak Confirmation Status")
plt.xlabel("Status"); plt.ylabel("Number of Incidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

pd.crosstab(
    df["Conducting Body Type"],
    df["Leak Confirmation Status"]
).plot(kind="bar", figsize=(9,5))

plt.title("Leak Status by Conducting Body Type")
plt.xlabel("Conducting Body Type")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
