# Set seed for reproducibility
np.random.seed(4848)

# Lists to store bootstrap results
mean_values = []
std_values = []
percentile_98_values = []

# Generate 500 bootstrap samples, each of size 150
for _ in range(500):
    bootstrap_sample = df.sample(n=150, replace=True)
    bp_values = bootstrap_sample['BloodPressure']
    
    mean_values.append(bp_values.mean())
    std_values.append(bp_values.std())
    percentile_98_values.append(np.percentile(bp_values, 98))

# Calculate statistics for the full population
pop_mean = df['BloodPressure'].mean()
pop_std = df['BloodPressure'].std()
pop_98th_percentile = np.percentile(df['BloodPressure'], 98)

# Calculate average values from the bootstrap results
avg_bootstrap_mean = np.mean(mean_values)
avg_bootstrap_std = np.mean(std_values)
avg_bootstrap_98th = np.mean(percentile_98_values)

# Create a summary table for comparison
bp_summary = pd.DataFrame({
    'Statistic': ['Mean', 'Standard Deviation', '98th Percentile'],
    'Population Value': [pop_mean, pop_std, pop_98th_percentile],
    'Bootstrap Estimate': [avg_bootstrap_mean, avg_bootstrap_std, avg_bootstrap_98th]
})

print(bp_summary)
# Rename columns for display
bp_summary_renamed = bp_summary.rename(columns={
    'Population Value': 'Population',
    'Bootstrap Estimate': 'Bootstrap Avg'
})

# Melt the DataFrame for seaborn plotting
bp_melted = bp_summary_renamed.melt(id_vars='Statistic', var_name='Group', value_name='Value')

# Define custom colors: blue for Population, pink for Bootstrap Avg
custom_palette = {'Population': '#4A90E2', 'Bootstrap Avg': '#FF69B4'}

# Create bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=bp_melted, x='Statistic', y='Value', hue='Group', palette=custom_palette)

# Add labels and title
plt.title('Blood Pressure Comparison: Population vs Bootstrap Average\n(500 Samples, Size = 150)', fontsize=14)
plt.ylabel('Statistic Value')
plt.xlabel('Blood Pressure Statistic')

# Final layout and save
plt.tight_layout()
plt.savefig("bloodpressure_population_vs_bootstrap_blue_pink.png")
plt.show()

