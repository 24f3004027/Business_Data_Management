import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig_dir = '/Users/ramrupsatpati/Downloads/Business_Data_Management/figures'
os.makedirs(fig_dir, exist_ok=True)

df = pd.read_csv('/Users/ramrupsatpati/Downloads/Business_Data_Management/dataset/sales_service_survey_data.csv')

print("=== BDM CAPSTONE PRIMARY DATA ANALYSIS SUMMARY ===")
print("Total Respondents:", len(df))
print("\nSegment Breakdown:")
print(df['Customer_Segment'].value_counts(normalize=True)*100)

print("\nService Attachment Rate by Segment:")
attach_rates = df.groupby('Customer_Segment')['Service_Contract_OptIn'].apply(lambda x: (x == 'Yes').mean() * 100)
print(attach_rates)

print("\nMean CSAT by Service Contract OptIn:")
print(df.groupby('Service_Contract_OptIn')['CSAT_Rating'].mean())

print("\nMean Turnaround Time (Days) by OptIn:")
print(df.groupby('Service_Contract_OptIn')['Avg_Turnaround_Days'].mean())

# Figure 1: Service Opt-in by Customer Segment
fig, ax = plt.subplots(figsize=(7, 4.5))
segments = df['Customer_Segment'].unique()
x = np.arange(len(segments))
opt_yes = [((df['Customer_Segment'] == s) & (df['Service_Contract_OptIn'] == 'Yes')).sum() for s in segments]
opt_no = [((df['Customer_Segment'] == s) & (df['Service_Contract_OptIn'] == 'No')).sum() for s in segments]

ax.bar(x - 0.18, opt_yes, width=0.36, label='Service Attached (AMC/Warranty)', color='#1B365D')
ax.bar(x + 0.18, opt_no, width=0.36, label='Transactional Only (No AMC)', color='#D9822B')
ax.set_xticks(x)
ax.set_xticklabels(segments, fontweight='bold', fontsize=10)
ax.set_ylabel('Number of Respondents', fontweight='bold', fontsize=10)
ax.set_title('Primary Survey: Service Contract Adoption by Customer Segment (N=220)', fontsize=12, fontweight='bold', pad=12)
ax.legend(frameon=True)
for i in range(len(segments)):
    ax.text(x[i] - 0.18, opt_yes[i] + 1.5, f'{opt_yes[i]}', ha='center', fontsize=9, fontweight='bold')
    ax.text(x[i] + 0.18, opt_no[i] + 1.5, f'{opt_no[i]}', ha='center', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{fig_dir}/fig1_segment_adoption.png', dpi=300)
plt.close()

# Figure 2: Margin & CLV Comparison (Hardware vs Service)
fig, ax = plt.subplots(figsize=(7, 4.5))
metrics = ['Gross Margin (%)', 'Net Margin (%)', '3-Yr Retention Rate (%)']
hardware_vals = [12.8, 7.4, 38.0]
service_vals = [54.2, 38.6, 82.5]
x = np.arange(len(metrics))
ax.bar(x - 0.18, hardware_vals, width=0.36, label='Hardware Product Sales', color='#4A6572')
ax.bar(x + 0.18, service_vals, width=0.36, label='After-Sales Services & AMC', color='#800000')
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontweight='bold', fontsize=10)
ax.set_ylabel('Percentage (%)', fontweight='bold', fontsize=10)
ax.set_title('Financial Contribution Margin & Retention Comparison', fontsize=12, fontweight='bold', pad=12)
ax.legend(frameon=True)
for i in range(len(metrics)):
    ax.text(x[i] - 0.18, hardware_vals[i] + 1.5, f'{hardware_vals[i]}%', ha='center', fontsize=9, fontweight='bold')
    ax.text(x[i] + 0.18, service_vals[i] + 1.5, f'{service_vals[i]}%', ha='center', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{fig_dir}/fig2_margin_retention_comparison.png', dpi=300)
plt.close()

# Figure 3: CSAT vs Turnaround Time
fig, ax = plt.subplots(figsize=(7, 4.5))
scatter = ax.scatter(df['Avg_Turnaround_Days'], df['CSAT_Rating'], c=df['Service_Contract_OptIn'].map({'Yes': '#800000', 'No': '#1B365D'}), alpha=0.7, s=60, edgecolors='none')
ax.set_xlabel('Average Turnaround Time (Days)', fontweight='bold', fontsize=10)
ax.set_ylabel('Customer Satisfaction (CSAT Rating 1-5)', fontweight='bold', fontsize=10)
ax.set_title('Impact of Service Turnaround Speed on Customer Satisfaction', fontsize=12, fontweight='bold', pad=12)
# Custom legend
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Contracted AMC (Fast TAT / High CSAT)', markerfacecolor='#800000', markersize=9),
                   Line2D([0], [0], marker='o', color='w', label='Transactional Only (Delayed TAT / Lower CSAT)', markerfacecolor='#1B365D', markersize=9)]
ax.legend(handles=legend_elements, loc='upper right', frameon=True)
plt.tight_layout()
plt.savefig(f'{fig_dir}/fig3_csat_turnaround.png', dpi=300)
plt.close()

# Figure 4: Optimization Model Feasible Region and Optimal Mix
# Maximize Z = 4500 * X_sales + 6800 * Y_service
# Constraints:
# 1) Sales Working Capital: 25000*X + 5000*Y <= 2,500,000  => 5X + Y <= 500
# 2) Tech Labor Hours: 2*X + 8*Y <= 1,200
# 3) Minimum Sales requirement: X >= 40
# 4) Service capacity floor: Y >= 60
fig, ax = plt.subplots(figsize=(7, 5))
x_vals = np.linspace(0, 120, 400)
# Constraint 1: Y <= 500 - 5X
y1 = 500 - 5 * x_vals
# Constraint 2: Y <= (1200 - 2X) / 8 = 150 - 0.25X
y2 = 150 - 0.25 * x_vals

ax.plot(x_vals, y1, label=r'Capital Constraint ($5X + Y \leq 500$)', color='#C0392B', lw=2)
ax.plot(x_vals, y2, label=r'Tech Labor Capacity ($2X + 8Y \leq 1200$)', color='#2980B9', lw=2)
ax.axvline(40, color='#27AE60', linestyle='--', label=r'Min Sales Volume ($X \geq 40$)', lw=1.8)
ax.axhline(60, color='#8E44AD', linestyle='--', label=r'Min Service Base ($Y \geq 60$)', lw=1.8)

# Feasible polygon vertices:
# V1: X=40, Y=60
# V2: X=40, Y=(1200 - 80)/8 = 140
# V3: Intersection of 5X + Y = 500 and 2X + 8Y = 1200
# 5X + Y = 500 => Y = 500 - 5X => 2X + 8(500 - 5X) = 1200 => 2X + 4000 - 40X = 1200 => -38X = -2800 => X = 73.68, Y = 131.58
# V4: Intersection of 5X + Y = 500 and Y = 60 => 5X = 440 => X = 88, Y = 60
poly_x = [40, 40, 73.68, 88]
poly_y = [60, 140, 131.58, 60]
ax.fill(poly_x, poly_y, color='#2ECC71', alpha=0.25, label='Feasible Mix Region')

# Profit contours: Z = 4500X + 6800Y
# At (40, 140): Z = 4500*40 + 6800*140 = 180000 + 952000 = 1,132,000
# At (73.68, 131.58): Z = 4500*73.68 + 6800*131.58 = 331,560 + 894,744 = 1,226,304 (OPTIMAL!)
# At (88, 60): Z = 4500*88 + 6800*60 = 396000 + 408000 = 804,000
ax.plot(73.68, 131.58, marker='*', markersize=16, color='#D4AC0D', markeredgecolor='black', label='Optimal Mix (X*=74, Y*=132)\nMax Margin: INR 1,226,304/mo')

ax.set_xlim(0, 110)
ax.set_ylim(0, 180)
ax.set_xlabel('Product Hardware Sales Units (X / month)', fontweight='bold', fontsize=10)
ax.set_ylabel('Service AMC Contracts Delivered (Y / month)', fontweight='bold', fontsize=10)
ax.set_title('Linear Programming Optimization: Sales & Service Allocation Frontier', fontsize=12, fontweight='bold', pad=12)
ax.legend(loc='lower left', fontsize=8.5, frameon=True)
plt.tight_layout()
plt.savefig(f'{fig_dir}/fig4_optimization_frontier.png', dpi=300)
plt.close()

print("\nFigures successfully saved to figures/ directory!")
