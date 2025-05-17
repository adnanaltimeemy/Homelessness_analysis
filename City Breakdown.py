import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset: Youth homelessness near wealthy areas in UK and US cities
data = {
    'City': ['London', 'Manchester', 'Los Angeles', 'New York City', 'San Francisco'],
    'Country': ['UK', 'UK', 'US', 'US', 'US'],
    'Homeless_Youth_Est': [8500, 2300, 12000, 10500, 7200],  # Estimated number of homeless youth
    'Nearby_Wealth_Area': ['Kensington & Chelsea', 'Didsbury', 'Beverly Hills', 'Upper East Side', 'Pacific Heights'],
    'Avg_House_Price_£$M': [2.4, 0.5, 3.1, 2.9, 2.8],  # Average price in millions (local currency)
    'Population_Under25': [1_100_000, 500_000, 2_400_000, 2_700_000, 950_000]
}

df = pd.DataFrame(data)

# Calculate % of youth population homeless in each city
df['Homeless_Percent'] = (df['Homeless_Youth_Est'] / df['Population_Under25']) * 100

# Plotting
plt.figure(figsize=(12, 6))
bars = plt.bar(df['City'], df['Homeless_Percent'], color=['blue', 'blue', 'red', 'red', 'red'])

# Annotate each bar with wealth area and home price
for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f"{df['Nearby_Wealth_Area'][i]}\n£${df['Avg_House_Price_£$M'][i]}M",
             ha='center', va='bottom', fontsize=9, color='black')

plt.title('Youth Homelessness (% under 25) in Cities Near Rich Urban Areas')
plt.ylabel('% of Youth Homeless')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
# This code creates a bar chart showing the percentage of youth homeless in various cities
# near wealthy urban areas, with annotations for the nearby wealthy area and average house price.
# The data is fictional and for illustrative purposes only.
# The chart provides a visual representation of the issue of youth homelessness in relation to wealth disparity.                    
# The chart can be used to raise awareness about the issue and encourage discussions on potential solutions.
# The data can be expanded with real statistics and more cities for a comprehensive analysis.
# The chart can be used in presentations, reports, or social media to highlight the issue of youth homelessness.
# The code can be modified to include more cities, different metrics, or additional visualizations as needed.
# The chart can be saved as an image file for future reference or sharing.