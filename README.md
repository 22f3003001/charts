# Customer Engagement Metrics - Correlation Heatmap

**Author Email:** 22f3003001@ds.study.iitm.ac.in

## Project Overview

Professional-grade Seaborn heatmap visualization for Kessler Kuhlman and Sporer, analyzing customer engagement metric correlations for executive presentation.

## Business Context

This visualization supports the client's quarterly business review, providing data-driven insights into customer engagement patterns across six key metrics:

- **Website Visits**: Monthly average visits per customer
- **Email Opens**: Email campaign engagement rate
- **Social Engagement**: Social media interaction score
- **Purchase Frequency**: Number of purchases per quarter
- **Customer Satisfaction**: Satisfaction rating (1-10 scale)
- **Loyalty Score**: Customer loyalty index

## Visualization Details

- **Chart Type:** Correlation Heatmap
- **Library:** Seaborn (Python)
- **Dimensions:** 512x512 pixels
- **Color Scheme:** Red-Yellow-Green (RdYlGn)
- **Format:** PNG

## Key Insights

The correlation heatmap reveals:
1. Strong positive correlations between website visits and other engagement metrics
2. Significant relationship between customer satisfaction and loyalty
3. Purchase frequency as a key driver of overall engagement

## Files

- `chart.py` - Python script generating the visualization
- `chart.png` - Generated heatmap (512x512px)
- `README.md` - This documentation

## Usage

```bash
python chart.py
```

This will generate `chart.png` with the correlation heatmap.

## Requirements

```
seaborn>=0.12.0
matplotlib>=3.5.0
pandas>=1.4.0
numpy>=1.21.0
```

## Contact

For questions or customizations: 22f3003001@ds.study.iitm.ac.in
