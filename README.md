# Last Mile Logistics Auditor

## A. Executive Summary

This project analyzes delivery performance using the Olist Brazilian E-Commerce dataset. The goal was to identify whether delayed deliveries are affecting customer satisfaction and whether certain regions experience worse delivery performance than others.

The analysis showed that late deliveries significantly reduce customer review scores. Some states also experience a much higher percentage of delayed orders, suggesting regional logistics challenges. An additional analysis revealed which states have the highest average delivery delays, helping identify operational risk areas.

This project combines data engineering, data cleaning, visualization, and business insight generation to support logistics decision-making.

---

## B. Project Links

- GitHub Repository: [Add Your GitHub Link Here]
- Notebook: [Add Notebook Link Here]
- Dashboard: [Add Dashboard Link Here]
- Presentation: [Add Presentation Link Here]

---

## C. Technical Explanation

### Data Cleaning
- Loaded and merged orders, customers, and review datasets using pandas.
- Removed rows with missing delivery dates or review scores.
- Converted delivery date columns into datetime format.
- Created a new `delay_days` column to calculate delivery performance.
- Classified deliveries into:
  - On Time
  - Late
  - Super Late

### Candidate’s Choice Feature
An additional analysis was added to calculate the average delivery delay by state. This helps identify the regions with the most severe logistics performance issues and provides more actionable business insights for operational planning.

---

## Key Insights

- Late deliveries strongly reduce customer satisfaction.
- Some states experience significantly higher late delivery rates.
- Remote regions appear to face larger delivery delays.
- Delivery estimation accuracy is an important factor in customer experience.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- GitHub
- VS Code
