# Sales and Service Mix Optimization: A Primary Data Analysis
### BDM Capstone Project (MS2001P) | IIT Madras Online BS Degree Program

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Academic Program](https://img.shields.io/badge/IIT_Madras-BS_Degree-maroon.svg)](https://study.iitm.ac.in)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![Status](https://img.shields.io/badge/Status-Complete_Reference_Repo-success.svg)](#)

---

## 📌 Executive Summary
This repository contains the comprehensive deliverable suite for the **Business Data Management (BDM) Capstone Project (`MS2001P`)** titled:

> **"Sales and Service mix optimization - A primary data analysis"**  
> **Author:** Ramrup Satpati  
> **Roll Number:** `24f3004027`  
> **Institution:** Indian Institute of Technology Madras, Chennai  

The project explores the operational and financial trade-offs between upfront hardware equipment retail (high revenue, compressed net margin ~7.4%) and recurring after-sales maintenance agreements / AMCs (high net margin ~38.6%, high customer retention). Based on a primary survey of **N = 220** verified customers and commercial clients, we formulate and solve a constrained **Linear Programming (LP)** optimization model to identify the global profit-maximizing operating mix.

---

## 🗂️ Primary Route Deliverables

All required capstone deliverables are located in the **primary root directory** of this repository:

| Deliverable | Format | Description |
| :--- | :--- | :--- |
| **Proposal Report** | [`Proposal_Report.pdf`](Proposal_Report.pdf) \| [`Proposal_Report.md`](Proposal_Report.md) | Phase 1: Problem background, theoretical framework, survey instrument design |
| **Mid-Term Report** | [`Midterm_Report.pdf`](Midterm_Report.pdf) \| [`Midterm_Report.md`](Midterm_Report.md) | Phase 2: Field survey execution (N=220), data scrubbing, EDA, hypothesis testing |
| **Final Project Report** | [`Final_Report.pdf`](Final_Report.pdf) \| [`Final_Report.md`](Final_Report.md) | Phase 3: Comprehensive report, LP optimization model, shadow prices, managerial strategy |
| **Final Presentation Deck** | [`Final_Presentation.pptx`](Final_Presentation.pptx) | Primary pitch deck for the capstone viva defense (Widescreen 16:9, editable slides) |
| **Final Presentation PDF** | [`Final_Presentation.pdf`](Final_Presentation.pdf) | High-resolution PDF export of the final presentation deck |
| **Primary Survey Dataset** | [`dataset/sales_service_survey_data.csv`](dataset/sales_service_survey_data.csv) | Primary field dataset of N=220 respondent records across 13 business variables |
| **Analytical Pipeline** | [`analysis.py`](analysis.py) | Python script for data processing, EDA plots, and LP optimization solution |

---

## 📊 Key Empirical & Optimization Findings

### 1. Primary Survey Metrics (N = 220)
* **Cohort Composition:** 50.5% B2C Retail, 35.0% SME Commercial, 14.5% Enterprise accounts.
* **Service Contract Adoption:** Enterprise (84.4%) and SME (70.1%) clients demonstrate high willingness to purchase AMCs, while B2C Retail (43.2%) requires bundled point-of-sale financing.
* **CSAT vs. Turnaround:** Contracted AMC customers experience **2.34-day average turnaround (CSAT: 4.24/5.0)** versus **5.35 days (CSAT: 2.82/5.0)** for non-contracted walk-ins ($p < 0.001$).
* **Retention:** 3-year customer retention reaches **82.5%** for service-attached accounts versus **38.0%** for transactional buyers.

### 2. Linear Programming Formulation & Global Optimum
* **Objective:** Maximize Monthly Contribution Margin:  
  $$\max Z = 4500 X + 6800 Y$$
* **Constraints:**
  * Capital Constraint: $5X + Y \leq 500$
  * Technician Labor Constraint: $2X + 8Y \leq 1200$
  * Sales Target Floor: $X \geq 40$
  * Service Fleet Floor: $Y \geq 60$
* **Optimal Operating Point:**  
  $$\mathbf{X^* = 74 	ext{ hardware sales units/month}}, \quad \mathbf{Y^* = 132 	ext{ AMC service contracts/month}}$$
* **Maximum Monthly Contribution Margin:**  
  $$\mathbf{Z^* = 	ext{INR } 1,226,304 / 	ext{month} \quad (+28.4\% 	ext{ uplift over standard retail baseline})}$$
* **Labor Shadow Wage:** **INR 850 / hour** (3.0x return on technician payroll hiring).

---

## 🚀 How to Run & Reproduce

```bash
# Clone the repository
git clone https://github.com/24f3004027/Business_Data_Management.git
cd Business_Data_Management

# Install required analytical libraries
pip install pandas numpy matplotlib reportlab python-pptx

# Run the primary data analysis and generate visualization figures
python3 analysis.py

# Recompile all formal PDF reports (Proposal, Mid-term, Final)
python3 generate_all_artifacts.py

# Recompile the Final Presentation (both .pptx and .pdf)
python3 build_presentation.py
```

---

## 🏛️ Academic Citation & Attribution
```bibtex
@techreport{satpati2026bdm,
  title={Sales and Service mix optimization - A primary data analysis},
  author={Satpati, Ramrup},
  institution={Indian Institute of Technology Madras},
  number={MS2001P},
  year={2026}
}
```

## ⚖️ License
This project and all contained materials are distributed under the [GNU General Public License v3.0 (GPLv3)](LICENSE).
