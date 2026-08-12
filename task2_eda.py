import pandas as pd

df = pd.read_csv("Paper_leaks_India(3).csv", encoding="cp1252")
df.columns = df.columns.str.strip()

# Clean fields
df["Date"] = pd.to_datetime(
    df["Date of Exam/Incident"], dayfirst=True, errors="coerce"
)
df["Year"] = df["Date"].dt.year
df["Action taken"] = df["Action taken"].fillna("Not specified")

print("===== PAPER LEAKS INDIA — EDA =====")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nIncidents by Year:")
print(df["Year"].value_counts().sort_index())

print("\nTop Incident Areas:")
print(df["Area(s) of Incident"].value_counts().head(10))

print("\nLeak Confirmation Status:")
print(df["Leak Confirmation Status"].value_counts())

print("\nConducting Body Type:")
print(df["Conducting Body Type"].value_counts())

print("\nActions Taken:")
print(df["Action taken"].value_counts().head(10))

# Save analysis tables
df.to_csv("Paper_leaks_India_cleaned.csv", index=False)

df["Year"].value_counts().sort_index().rename_axis("Year").reset_index(
    name="Incidents"
).to_csv("eda_year_summary.csv", index=False)

df["Area(s) of Incident"].value_counts().rename_axis(
    "Area"
).reset_index(name="Incidents").to_csv("eda_area_summary.csv", index=False)

df["Leak Confirmation Status"].value_counts().rename_axis(
    "Status"
).reset_index(name="Incidents").to_csv("eda_status_summary.csv", index=False)

print("\nEDA files saved successfully.")
