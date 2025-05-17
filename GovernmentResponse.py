import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Years to simulate
years = np.arange(2025, 2056)

# Initialize factors influencing government response (0 = no impact, 1 = max impact)
# We'll simulate how these factors might evolve or persist over time.

# 1. Political priorities (0 = low priority, 1 = high priority)
political_priority = np.linspace(0.3, 0.7, len(years))  # slow rise due to awareness

# 2. NIMBYism strength (0 = no opposition, 1 = max opposition)
nimbyism = np.linspace(0.8, 0.6, len(years))  # slight decline but still high opposition

# 3. Funding availability (0 = none, 1 = abundant)
funding = np.concatenate([np.linspace(0.3, 0.6, 10), np.linspace(0.6, 0.4, len(years) - 10)]) 
# initial rise then decline due to economic cycles

# 4. Systemic coordination (0 = poor, 1 = excellent)
systemic_coordination = np.linspace(0.2, 0.5, len(years))  # slight improvement

# 5. Social stigma (0 = none, 1 = high stigma)
social_stigma = np.linspace(0.7, 0.4, len(years))  # reducing stigma over time

# 6. Political will (0 = none, 1 = strong)
political_will = np.linspace(0.25, 0.55, len(years))  # slowly growing political will

# Calculate government response as weighted sum of factors
# Assign weights (importance) to each factor
weights = {
    'political_priority': 0.25,
    'nimbyism': -0.20,  # negative impact
    'funding': 0.25,
    'systemic_coordination': 0.15,
    'social_stigma': -0.10,  # negative impact
    'political_will': 0.15
}

gov_response = (
    political_priority * weights['political_priority'] +
    nimbyism * weights['nimbyism'] +
    funding * weights['funding'] +
    systemic_coordination * weights['systemic_coordination'] +
    social_stigma * weights['social_stigma'] +
    political_will * weights['political_will']
)

# Normalize response to 0-1 range
gov_response = (gov_response - gov_response.min()) / (gov_response.max() - gov_response.min())

# Build DataFrame
df = pd.DataFrame({
    'Year': years,
    'Political Priority': political_priority,
    'NIMBYism': nimbyism,
    'Funding': funding,
    'Systemic Coordination': systemic_coordination,
    'Social Stigma': social_stigma,
    'Political Will': political_will,
    'Government Response': gov_response
})

# Plot Government Response over time
plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['Government Response'], label='Government Response to Youth Homelessness', linewidth=3, color='blue')
plt.title('Simulated Government Response to Youth Homelessness Near Affluent Areas (2025–2055)')
plt.xlabel('Year')
plt.ylabel('Response Level (0=Ignore, 1=Strong Intervention)')
plt.grid(True)
plt.ylim(0, 1.1)
plt.legend()
plt.show()

# Display data table for final 5 years
print(df.tail(5))
