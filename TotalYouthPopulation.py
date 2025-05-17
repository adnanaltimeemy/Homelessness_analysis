# Total youth population (ages 16–24) in millions, hypothetical
uk_youth_population = 6.5  # million
us_youth_population = 38.0  # million

# Convert raw homeless counts to % of total youth population
uk_percent = [(h / (uk_youth_population * 1000)) * 100 for h in uk_homeless_youth]
us_percent = [(h / (us_youth_population * 1000)) * 100 for h in us_homeless_youth]

plt.figure(figsize=(10, 6))
plt.plot(years, uk_percent, marker='o', label='UK Homeless Youth (%)')
plt.plot(years, us_percent, marker='s', label='US Homeless Youth (%)')
plt.title('Percentage of Homeless Youth: UK vs US (2018–2022)')
plt.xlabel('Year')
plt.ylabel('Homeless Youth (% of total youth population)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
