# Sales and Service mix optimization - A primary data analysis
## A Proposal report for the BDM capstone Project

**Submitted by:**  
**Name:** Ramrup Satpati  
**Roll number:** 24f3004027  

<p align="center">
  <img src="iitm_logo.png" width="220" alt="IIT Madras Logo" />
</p>

**IITM Online BS Degree Program,**  
**Indian Institute of Technology, Madras, Chennai**  
**Tamil Nadu, India, 600036**  

---

### 1. Executive Summary & Business Problem Context
Modern consumer electronics, commercial IT hardware, and office automation retail enterprises face severe margin compression in core equipment sales. Traditional retail business models focus almost exclusively on hardware unit throughput. However, rising customer acquisition costs, fierce e-commerce price competition, and inventory carrying costs have compressed pure product sales net margins down to **7.4%**. 

In contrast, post-warranty after-sales services—including Annual Maintenance Contracts (AMC), preventative checkups, and priority breakdown repairs—command net contribution margins exceeding **38.6%** and provide predictable, non-cyclical cash flow.

Despite the superior unit economics of after-sales services, dealerships frequently struggle to establish the optimal operating mix:
* Over-indexing on hardware sales drains working capital and crowds out technician bandwidth.
* Over-indexing on maintenance services without an adequate hardware installed base leads to technician underutilization and customer attrition.

This capstone project presents an empirical, primary data-driven research framework to determine the optimal allocation of capital, sales effort, and technical labor between hardware sales and after-sales service agreements.

---

### 2. Research Objectives & Primary Research Questions
This project investigates three central empirical questions:
1. **Primary Research Question 1:** What are the key consumer and organizational drivers that dictate customer willingness to enroll in structured after-sales maintenance agreements (AMC / extended warranty) at the point of sale?
2. **Primary Research Question 2:** How do unit contribution margins, customer retention rates, and Customer Lifetime Value (CLV) vary between pure transactional buyers versus service-contracted accounts?
3. **Primary Research Question 3:** Under finite technician labor hours, retail floor capital, and customer turnaround time constraints, what is the mathematically optimal sales-to-service ratio that maximizes net enterprise contribution margin?

---

### 3. Theoretical Framework & Literature Grounding
* **Servitization Theory (Vandermerwe & Rada, 1988; Baines et al., 2009):** Manufacturing and retail firms achieve sustainable competitive advantages by transitioning from transactional goods sellers to integrated product-service providers.
* **Retention Economics (Reichheld & Sasser, 1990):** Retaining existing accounts via recurring service agreements yields 25% to 95% higher enterprise profitability compared to continuous reliance on new customer acquisition.
* **Constrained Resource Allocation (Hillier & Lieberman, 2015):** Operations research principles applied to dual-channel capacity planning under capital and labor bottlenecks.

---

### 4. Primary Data Collection Strategy & Survey Instrument
Primary data will be collected via a structured field survey administered across **N = 220** verified retail consumers and commercial business buyers in Tier-1 and Tier-2 urban equipment centers.

| Target Cohort | Sampling Frame | Sample Size | Data Capture Focus |
| :--- | :--- | :--- | :--- |
| **B2C Retail Consumers** | Walk-in shoppers & appliance buyers | 110 (50.0%) | Price sensitivity, warranty perception, DIY tendencies |
| **SME Commercial Clients** | Small offices, clinics, legal/accounting firms | 75 (35.0%) | Downtime tolerance, AMC adoption, turnaround speed |
| **Enterprise Accounts** | Corporate branch offices & institutions | 35 (15.0%) | Multi-year SLAs, fleet size, mission-critical response |

---

### 5. Proposed Analytical Pipeline
1. **Data Scrubbing & Validation:** Verification of zero missing attributes, outlier screening, and normality testing using Python (Pandas/NumPy).
2. **Exploratory Data Analysis (EDA):** Bivariate cross-tabulations analyzing turnaround times (TAT), customer satisfaction (CSAT), and AMC contract opt-in rates.
3. **Econometric Modeling:** Binary logistic regression identifying the key determinants of service adoption propensity.
4. **Constrained Mathematical Optimization:** Linear Programming (LP) model solved via the Simplex method to identify the profit-maximizing product-service bundle mix.

---

### 6. Project Timeline & Capstone Milestones
| Milestone Phase | Scheduled Weeks | Key Deliverables | Status |
| :--- | :--- | :--- | :--- |
| **Phase 1: Proposal** | Weeks 1 – 3 | Problem formulation, literature grounding, survey tool | **Completed** |
| **Phase 2: Mid-Term** | Weeks 4 – 7 | Primary field survey (N=220), data scrubbing, EDA | Scheduled |
| **Phase 3: Final Report** | Weeks 8 – 11 | Econometric models, LP optimization, strategic insights | Scheduled |
| **Phase 4: Final Viva** | Week 12 | Pitch deck presentation & defense | Scheduled |
