
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
tbi_age_df = pd.read_csv('tbi_age.csv')
tbi_military_df = pd.read_csv('tbi_military.csv')
tbi_year_df = pd.read_csv('tbi_year.csv')

# Visualize TBI cases by injury mechanism over the years (Figure 1)
plt.figure(figsize=(10, 6))
sns.lineplot(data=tbi_year_df, x='year', y='number_est', hue='injury_mechanism', marker='o')
plt.title("Number of TBI Cases by Injury Mechanism Over the Years")
plt.xlabel("Year")
plt.ylabel("Estimated Number of Cases")
plt.legend(title="Injury Mechanism", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.savefig('figure1_tbi_injury_mechanism.png')
plt.show()

# Visualize TBI severity trends in military personnel (Figure 2)
plt.figure(figsize=(10, 6))
sns.lineplot(data=tbi_military_df, x='year', y='diagnosed', hue='severity', marker='o')
plt.title("TBI Severity Trends in Military Personnel")
plt.xlabel("Year")
plt.ylabel("Number of Diagnosed Cases")
plt.legend(title="Severity", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.savefig('figure2_tbi_military_severity.png')
plt.show()
