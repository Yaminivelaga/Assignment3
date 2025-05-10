# Set seed for reproducibility
np.random.seed(4848)

# Taking a random sample of 25 from total population
sample_25 = df.sample(n=25, random_state=4848)

# Calculate mean and max glucose values for the whole population
population_mean = df['Glucose'].mean()
population_max = df['Glucose'].max()

# Calculate mean and max glucose values for the sample of 25
sample_mean = sample_25['Glucose'].mean()
sample_max = sample_25['Glucose'].max()

# Print the results
print("Mean Glucose in Population:", population_mean)
print("Max Glucose in Population:", population_max)
print("Mean Glucose in Sample (25):", sample_mean)
print("Max Glucose in Sample (25):", sample_max)

summary = {
    'Dataset': ['Population', 'Sample (25)'],
    'Mean Glucose': [population_mean, sample_mean],
    'Max Glucose': [population_max, sample_max]
}
glucose_df = pd.DataFrame(summary)
glucose_df.set_index('Dataset', inplace=True)
print(glucose_df)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample summary (replace with your actual values if different)
glucose_df = pd.DataFrame({
    'Dataset': ['Population', 'Sample (n=25)'],
    'Mean Glucose': [df['Glucose'].mean(), sample_25['Glucose'].mean()],
    'Max Glucose': [df['Glucose'].max(), sample_25['Glucose'].max()]
})

plt.figure(figsize=(12, 5))

# Bar chart for Mean Glucose
plt.subplot(1, 2, 1)
sns.barplot(data=glucose_df, x='Dataset', y='Mean Glucose')
plt.title('Mean Glucose Comparison')
plt.ylabel('Mean Glucose Level')
plt.xlabel('Diabetes Dataset')
plt.savefig("Mean_glucose_comparison.png")

# Bar chart for Max Glucose
plt.subplot(1, 2, 2)
sns.barplot(data=glucose_df, x='Dataset', y='Max Glucose',)
plt.title('Max Glucose Comparison')
plt.ylabel('Max Glucose Level')
plt.xlabel('Diabetes Dataset')
plt.savefig("Max_glucose_comparison.png")
