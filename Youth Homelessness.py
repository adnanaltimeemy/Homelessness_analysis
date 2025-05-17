import matplotlib.pyplot as plt

# Sample data: Youth homelessness estimates (in thousands) by year
years = [2018, 2019, 2020, 2021, 2022]

# Hypothetical data – replace with real data from sources like Crisis UK, HUD (USA)
uk_homeless_youth = [103, 110, 120, 115, 125]  # in thousands
us_homeless_youth = [500, 530, 600, 580, 610]  # in thousands

plt.figure(figsize=(10, 6))
plt.plot(years, uk_homeless_youth, marker='o', label='UK Youth Homelessness')
plt.plot(years, us_homeless_youth, marker='s', label='US Youth Homelessness')
plt.title('Youth Homelessness Trends: UK vs US (2018–2022)')
plt.xlabel('Year')
plt.ylabel('Number of Homeless Youth (in thousands)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
# This code visualizes the trends in youth homelessness in the UK and US over a period of years.
# The data is hypothetical and should be replaced with actual statistics from reliable sources.
# The plot shows the number of homeless youth in thousands for both countries, allowing for a comparison of trends.
# The x-axis represents the years, while the y-axis shows the number of homeless youth.             