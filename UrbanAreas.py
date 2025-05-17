import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated data for UK and US cities
data = {
    'City': [
        'London', 'Bristol', 'Sheffield', 'Manchester', 'New York', 'Los Angeles', 'San Diego', 'Houston'
    ],
    'Country': [
        'UK', 'UK', 'UK', 'UK', 'US', 'US', 'US', 'US'
    ],
    'Homeless_Youth_2023': [
        20200, 5800, 3800, 4600, 24000, 21000, 10600, 7400
    ],
    'Affluent_Area_Proximity_Score': [ # 1 (Low) to 10 (High)
        9, 6, 7, 8, 10, 9, 8, 7
    ],
    'Temporary_Housing_Units': [
        11000, 2500, 1300, 2100, 12000, 8000, 8100, 4200
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add a calculated column: Homeless Youth per Housing Unit
df['Youth_per_Unit'] = df['Homeless_Youth_2023'] / df['Temporary_Housing_Units']

# Display summary
print("Youth Homelessness Overview:\n", df)

# Plot 1: Bar chart - Homeless Youth by City
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='City', y='Homeless_Youth_2023', hue='Country')
plt.title('Youth Homelessness by City (UK vs US)')
plt.ylabel('Number of Homeless Youth (2023)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Scatter Plot - Affluent Area Proximity vs Youth Homelessness
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Affluent_Area_Proximity_Score', y='Homeless_Youth_2023', hue='Country', style='Country', s=100)
plt.title('Youth Homelessness vs Proximity to Affluent Areas')
plt.xlabel('Affluent Area Proximity Score')
plt.ylabel('Homeless Youth Count')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 3: Ratio Analysis
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='City', y='Youth_per_Unit', hue='Country')
plt.title('Homeless Youth per Temporary Housing Unit')
plt.ylabel('Ratio (Youth / Unit)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
