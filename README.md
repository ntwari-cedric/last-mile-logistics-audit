# Last Mile Logistics Auditor

---

## Executive Summary

This project analyzes delivery performance using the Olist E-Commerce dataset. The analysis investigates whether inaccurate delivery estimates are affecting customer satisfaction and identifies regional differences in logistics performance.

The results show that late deliveries are strongly associated with lower customer review scores. Additionally, certain states experience significantly higher delivery delays, indicating regional inefficiencies in logistics operations. These insights can help optimize delivery planning and improve customer satisfaction.

---

## Problem Statement

Veridi Logistics suspected that inaccurate delivery estimates were negatively impacting customer satisfaction. This project aims to determine whether delivery delays influence customer review scores and whether specific regions are more affected than others.

---

## Key Insights

- Late deliveries result in significantly lower customer review scores
- Some states consistently experience higher delivery delays
- Delivery performance varies significantly across regions
- Logistics delays have a direct impact on customer satisfaction

---

## Project Links

- Notebook: https://colab.research.google.com/drive/18kol_OPx_hyfISGPI9Rmc7PTZP76z7vW?usp=sharing  
- Dashboard: https://datastudio.google.com/reporting/238fd4c6-f4f1-4945-b838-b759989fd655  
- Presentation: https://docs.google.com/presentation/d/1seaTCOR6Biwzb_XWRTCSBZtj-M4xOmlCTXR4DXOPeF0/edit?usp=sharing  

---

## Technical Explanation

### Data Cleaning
- Merged orders, customers, and reviews datasets
- Removed missing delivery dates and review scores
- Converted date columns into datetime format
- Created `delay_days` and `delivery_status` columns

### Candidate’s Choice
An additional analysis was added to identify states with the highest average delivery delays. This provides business value by highlighting regions that require operational improvements and logistics optimization.

---

## Project Structure

- analysis.py → Data cleaning and preprocessing
- day3_analysis.py → Data visualization and analysis
- cleaned_master_data.csv → Final processed dataset
- README.md → Project documentation

---

## Tools Used

- Python
- Pandas
- Matplotlib
- Google Colab
- Google Looker Studio
- GitHub

---

## Conclusion

This analysis demonstrates how logistics performance directly impacts customer satisfaction. By identifying delayed regions and their effect on reviews, the business can make data-driven decisions to improve delivery efficiency and customer experience.

---

## Note

This project was completed as part of a data engineering internship challenge focused on real-world logistics and customer sentiment analysis.
