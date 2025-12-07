# Author: 22f3003001@ds.study.iitm.ac.in
# Customer Engagement Metrics Correlation Analysis
# Created for Kessler Kuhlman and Sporer - Executive Presentation

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic customer engagement data
n_customers = 500

# Create correlated customer engagement metrics
website_visits = np.random.normal(25, 8, n_customers)
email_opens = 0.6 * website_visits + np.random.normal(15, 5, n_customers)
social_engagement = 0.4 * website_visits + 0.3 * email_opens + np.random.normal(10, 4, n_customers)
purchase_frequency = 0.5 * website_visits + 0.4 * email_opens + np.random.normal(5, 2, n_customers)
customer_satisfaction = 0.3 * purchase_frequency + 0.2 * social_engagement + np.random.normal(7, 1.5, n_customers)
loyalty_score = 0.4 * customer_satisfaction + 0.3 * purchase_frequency + np.random.normal(6, 1.8, n_customers)

# Create DataFrame
data = pd.DataFrame({
    'Website Visits': website_visits,
    'Email Opens': email_opens,
    'Social Engagement': social_engagement,
    'Purchase Frequency': purchase_frequency,
    'Customer Satisfaction': customer_satisfaction,
    'Loyalty Score': loyalty_score
})

# Calculate correlation matrix
correlation_matrix = data.corr()

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")  # Larger text for presentations

# Create figure with exact size for 512x512 output
plt.figure(figsize=(8, 8))

# Create heatmap with professional styling
sns.heatmap(
    correlation_matrix,
    annot=True,  # Show correlation values
    fmt='.2f',  # Format to 2 decimal places
    cmap='RdYlGn',  # Red-Yellow-Green color palette (professional)
    center=0,  # Center colormap at zero
    square=True,  # Make cells square
    linewidths=1,  # Add gridlines
    cbar_kws={
        'label': 'Correlation Coefficient',
        'shrink': 0.8
    },
    vmin=-1,  # Correlation range
    vmax=1
)

# Add title and labels
plt.title('Customer Engagement Metrics\nCorrelation Analysis', 
          fontsize=16, 
          fontweight='bold', 
          pad=20)
plt.xlabel('Engagement Metrics', fontsize=12, fontweight='bold')
plt.ylabel('Engagement Metrics', fontsize=12, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the chart as PNG with exactly 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
print("Chart saved successfully as 'chart.png' (512x512 pixels)")
print(f"\nCorrelation Matrix Summary:")
print(f"Strongest positive correlation: {correlation_matrix.max().max():.3f}")
print(f"Strongest negative correlation: {correlation_matrix.min().min():.3f}")

# Display the chart
plt.show()
