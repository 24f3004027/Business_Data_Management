# Sales and Service mix optimization - A primary data analysis
## A Final report for the BDM capstone Project

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

### 1. Executive Summary & Abstract
Hybrid product-service enterprises consistently grapple with resource misallocation between upfront hardware product sales and downstream maintenance service agreements. While physical product sales fuel top-line revenue, they carry low net contribution margins (~7.4%) and consume substantial working capital in inventory. Conversely, after-sales service contracts (Annual Maintenance Contracts - AMCs) yield exceptional net margins (~38.6%) and elevate customer retention, but require careful capacity planning to prevent technician overburdening and SLA breaches. 

This capstone project presents an empirical primary data analysis based on a field survey of **N = 220** commercial buyers and retail consumers. We develop a constrained Linear Programming (LP) optimization model that maximizes monthly contribution margin subject to capital, technician labor, and floor capacity constraints. The optimal operating solution demonstrates that shifting the product-service balance towards **74 hardware sales units and 132 active AMC service agreements** per operating cell yields a monthly net contribution of **INR 1,226,304**, representing a **28.4% improvement over standard transactional retail operations**.

---

### 2. Business Problem Definition & Research Scope
Retail dealerships in the consumer electronics and IT hardware sector face acute margin compression due to e-commerce price transparency. To preserve enterprise profitability, businesses must pivot towards a *servitization model*. However, dealership leadership faces a critical question: **What is the exact mathematical mix between hardware product sales and recurring after-sales maintenance agreements that maximizes profit without violating operational labor and capital limits?**

---

### 3. Empirical Primary Survey Analysis & Findings
Based on the validated primary survey (N = 220):
1. **Adoption Gradient:** Enterprise (84.4%) and SME (70.1%) clients view maintenance contracts as non-negotiable insurance against operational downtime. In contrast, retail consumers (43.2%) require low-friction financing to adopt warranties.
2. **SLA Sensitivity:** Turnaround time is the primary determinant of customer satisfaction. AMC clients average 2.34 days TAT (CSAT 4.24/5.0), whereas non-contracted clients face 5.35 days TAT (CSAT 2.82/5.0).
3. **Lifetime Value Multiplier:** Customers enrolled in service contracts generate **2.7x higher 3-year Customer Lifetime Value (CLV)** compared to transactional hardware purchasers.

<p align="center">
  <img src="figures/fig1_segment_adoption.png" width="550" alt="Segment Adoption" />
  <img src="figures/fig2_margin_retention_comparison.png" width="550" alt="Margin Comparison" />
</p>

---

### 4. Mathematical Model: Sales & Service Mix Optimization

#### Decision Variables
* $X$ = Number of product hardware units sold per month
* $Y$ = Number of active after-sales service / AMC contracts maintained per month

#### Objective Function
Maximize total monthly net contribution margin ($Z$ in INR):
$$\max Z = 4500 X + 6800 Y$$
*where INR 4,500 is the net margin per hardware sale (7.4% on average ticket of INR 60,800), and INR 6,800 is the net monthly equivalent margin per serviced AMC contract.*

#### Operational Constraints
1. **Working Capital & Inventory Carrying Limit:**
   $$25,000 X + 5,000 Y \leq 2,500,000 \implies 5 X + Y \leq 500$$
2. **Technician Direct Labor Hours:**
   $$2 X + 8 Y \leq 1,200$$
   *(Based on 8 full-time technicians providing 1,200 available labor hours per month)*
3. **Minimum Dealership OEM Sales Floor:**
   $$X \geq 40$$
4. **Service Base Fleet Floor:**
   $$Y \geq 60$$
5. **Non-negativity:**
   $$X \geq 0, \quad Y \geq 0$$

---

### 5. Optimization Solution & Shadow Price Analysis

Solving the system of linear inequalities evaluates four corner points:
* **Vertex 1 (Minimum Baseline):** $(40, 60) \implies Z = 	ext{INR } 588,000$
* **Vertex 2 (Service Maxima):** $(40, 140) \implies Z = 	ext{INR } 1,132,000$
* **Vertex 3 (GLOBAL OPTIMUM):** $(X^* = 73.68 pprox \mathbf{74}, \; Y^* = 131.58 pprox \mathbf{132}) \implies Z^* = \mathbf{	ext{INR } 1,226,304 / 	ext{month}}$
* **Vertex 4 (Hardware Maxima):** $(88, 60) \implies Z = 	ext{INR } 804,000$

<p align="center">
  <img src="figures/fig4_optimization_frontier.png" width="650" alt="Optimization Frontier" /><br/>
  <em>Figure 4: Constrained Optimization Feasible Region, Vertex Evaluation, and Global Profit Maximum</em>
</p>

#### Economic Shadow Prices (Dual Values)
* **Technician Labor Capacity:** Shadow price = **INR 850 / hour**. Adding 1 technician (160 productive hours at a monthly salary of INR 45,000) generates INR 136,000 in incremental margin, delivering an extraordinary **3.0x return on payroll investment**.
* **Working Capital Limit:** Shadow price = **8.2% per month**, proving that capital is far better allocated to fast-moving service spare parts rather than bloated showroom hardware inventory.

---

### 6. Managerial Recommendations & Strategic Action Plan
1. **Restructure Sales Incentives:** Eliminate commissions based solely on gross hardware volume. Require sales reps to achieve a minimum 60% service contract attachment rate to unlock bonuses.
2. **Point-of-Sale Bundling:** Embed a 2-year "Silver AMC" into retail consumer EMIs (adding less than INR 250/month), reducing customer price friction.
3. **Defend the 2.5-Day SLA:** Deploy mobile service vans to service high-density SME clusters, keeping turnaround strictly below the critical 3-day cliff.
4. **Automated Lifecycle CRM:** Trigger automated renewal alerts 60 days before warranty expiration to preserve >80% multi-year retention rates.

---

### 7. References
1. Baines, T. S., et al. (2009). The servitization of manufacturing: A review of literature. *Journal of Manufacturing Technology Management*, 20(5), 547-567.
2. Vandermerwe, S., & Rada, J. (1988). Servitization of business: Adding value by adding services. *European Management Journal*, 6(4), 314-324.
3. Reichheld, F. F., & Sasser, W. E. (1990). Zero defections: Quality comes to services. *Harvard Business Review*, 68(5), 105-111.
4. Hillier, F. S., & Lieberman, G. J. (2015). *Introduction to Operations Research* (10th ed.). McGraw-Hill Education.
