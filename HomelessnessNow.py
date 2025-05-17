import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Base data for 2025
base_data = {
    'City': ['London', 'Bristol', 'Sheffield', 'Manchester', 'New York', 'Los Angeles', 'San Diego', 'Houston'],
    'Country': ['UK', 'UK', 'UK', 'UK', 'US', 'US', 'US', 'US'],
    '2025_Homeless_Youth': [20500, 5900, 3850, 4650, 24300, 21300, 10700, 7500],
    'Annual_Growth_Rate': [0.01, 0.009, 0.008, 0.011, 0.015, 0.014, 0.012, 0.013]  # Annual growth from 2025–2055
}

# Convert to DataFrame
df_base = pd.DataFrame(base_data)

# Simulate data from 2025 to 2055
years = list(range(2025, 2056))
trend_data = []

for _, row in df_base.iterrows():
    city = row['City']
    country = row['Country']
    population = row['2025_Homeless_Youth']
    growth = row['Annual_Growth_Rate']
    
    for year in years:
        projected = population * ((1 + growth) ** (year - 2025))
        trend_data.append({
            'City': city,
            'Country': country,
            'Year': year,
            'Projected_Homeless_Youth': int(projected)
        })

df_trend = pd.DataFrame(trend_data)

# Plot: Trends over time (2025–2055)
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_trend, x='Year', y='Projected_Homeless_Youth', hue='City', style='Country', markers=False)
plt.title('Projected Youth Homelessness (2025–2055) in Urban Areas Near Affluent Neighborhoods')
plt.xlabel('Year')
plt.ylabel('Projected Homeless Youth')
plt.grid(True)
plt.tight_layout()
plt.show()

# Summary: Final year projections
final_2055 = df_trend[df_trend['Year'] == 2055].sort_values(by='Projected_Homeless_Youth', ascending=False)
print("\nTop Cities by Projected Homeless Youth in 2055:\n")
print(final_2055[['City', 'Country', 'Projected_Homeless_Youth']])
