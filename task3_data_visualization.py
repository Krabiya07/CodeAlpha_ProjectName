import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

df = pd.read_csv("Paper_leaks_India_cleaned.csv", encoding="cp1252")
df.columns = df.columns.str.strip()

output = Path("visualizations")
output.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Incidents by year
year_counts = df["Year"].value_counts().sort_index()
plt.figure(figsize=(10, 5))
year_counts.plot(kind="bar")
plt.title("Paper Leak Incidents by Year")
plt.xlabel("Year")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output / "01_incidents_by_year.png", dpi=180)
plt.close()

# 2. Top 10 areas
area_counts = df["Area(s) of Incident"].value_counts().head(10).sort_values()
plt.figure(figsize=(10, 6))
area_counts.plot(kind="barh")
plt.title("Top 10 Areas by Paper Leak Incidents")
plt.xlabel("Number of Incidents")
plt.ylabel("Area")
plt.tight_layout()
plt.savefig(output / "02_top_areas.png", dpi=180)
plt.close()

# 3. Confirmation status
status_counts = df["Leak Confirmation Status"].value_counts()
plt.figure(figsize=(7, 5))
status_counts.plot(kind="bar")
plt.title("Leak Confirmation Status")
plt.xlabel("Status")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output / "03_confirmation_status.png", dpi=180)
plt.close()

# 4. Conducting body type vs status
ct = pd.crosstab(df["Conducting Body Type"], df["Leak Confirmation Status"])
ct.plot(kind="bar", figsize=(9, 5))
plt.title("Leak Status by Conducting Body Type")
plt.xlabel("Conducting Body Type")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output / "04_body_type_vs_status.png", dpi=180)
plt.close()

# 5. Actions taken
actions = df["Action taken"].value_counts().head(10).sort_values()
plt.figure(figsize=(10, 6))
actions.plot(kind="barh")
plt.title("Most Common Actions Taken")
plt.xlabel("Number of Incidents")
plt.ylabel("Action")
plt.tight_layout()
plt.savefig(output / "05_actions_taken.png", dpi=180)
plt.close()

# 6. Combined dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

year_counts.plot(kind="bar", ax=axes[0, 0])
axes[0, 0].set_title("Incidents by Year")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Cases")

area_counts.plot(kind="barh", ax=axes[0, 1])
axes[0, 1].set_title("Top 10 Areas")
axes[0, 1].set_xlabel("Cases")
axes[0, 1].set_ylabel("Area")

status_counts.plot(kind="bar", ax=axes[1, 0])
axes[1, 0].set_title("Confirmation Status")
axes[1, 0].set_xlabel("Status")
axes[1, 0].set_ylabel("Cases")
axes[1, 0].tick_params(axis="x", rotation=0)

ct.plot(kind="bar", ax=axes[1, 1])
axes[1, 1].set_title("Status by Conducting Body Type")
axes[1, 1].set_xlabel("Body Type")
axes[1, 1].set_ylabel("Cases")
axes[1, 1].tick_params(axis="x", rotation=0)

fig.suptitle("Paper Leaks in India — Data Analytics Dashboard", fontsize=18)
plt.tight_layout()
plt.savefig(output / "06_dashboard.png", dpi=180, bbox_inches="tight")
plt.close()

print("All visualizations saved in the visualizations folder.")
