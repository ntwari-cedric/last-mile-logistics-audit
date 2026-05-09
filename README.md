# Last Mile Logistics Auditor

## Executive Summary

This project analyzes delivery performance using the Olist E-Commerce dataset.  
The analysis found that late deliveries are strongly connected to lower customer review scores. Some states showed significantly higher delay percentages than others, suggesting regional logistics challenges. The project also identified states with the highest average delivery delays to help prioritize operational improvements.

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
- Created delay_days and delivery_status columns

### Candidate's Choice
I added an additional analysis showing the states with the highest average delay days. This helps the business identify which regions consistently underperform and require logistics improvements.

---

## Tools Used
- Python
- Pandas
- Matplotlib
- Google Colab
- GitHub
