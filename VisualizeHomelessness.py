import pandas as pd
import matplotlib.pyplot as plt

# Sample data (you can replace this with real data from CSV or APIs)
data = {
    'Country': ['UK', 'UK', 'UK', 'US', 'US', 'US'],
    'Type': ['Rough Sleeping', 'Temporary Accommodation', 'Other',
             'Chronic Homelessness', 'Sheltered', 'Unsheltered'],
    'People': [4000, 96000, 10000, 127000, 354000, 226000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Split data for visualization
uk_df = df[df['Country'] == 'UK']
us_df = df[df['Country'] == 'US']

# Plotting side-by-side bar charts
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# UK plot
axes[0].bar(uk_df['Type'], uk_df['People'], color='royalblue')
axes[0].set_title('Homelessness in the UK')
axes[0].set_ylabel('Number of People')
axes[0].tick_params(axis='x', rotation=45)

# US plot
axes[1].bar(us_df['Type'], us_df['People'], color='darkred')
axes[1].set_title('Homelessness in the US')
axes[1].tick_params(axis='x', rotation=45)

# Layout
plt.tight_layout()
plt.show()
