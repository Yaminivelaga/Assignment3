#Calculate 98th percentile of BMI
bmi_98_population = np.percentile(df['BMI'], 98)
print(f"98th percentile of BMI of population: {bmi_98_population}")
bmi_98_sample = np.percentile(sample_25['BMI'], 98)
print(f"98th percentile of BMI of sample 25: {bmi_98_sample}")

# Create a summary table
bmi_98_df = pd.DataFrame({
    'Diabetes Dataset': ['Population', 'Sample (n=25)'],
    '98th Percentile BMI': [bmi_98_population, bmi_98_sample]
})

print(bmi_98_df)
#Bar chart of 98th Percentile BMI
plt.figure(figsize=(6, 5))
sns.barplot(data=bmi_98_df, x='Diabetes Dataset', y='98th Percentile BMI')
plt.title('98th Percentile of BMI Comparison')
plt.ylabel('BMI')
plt.tight_layout()
plt.savefig("bmi_98th_percentile_comparison.png")
plt.show()
