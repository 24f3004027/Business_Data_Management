import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

REPO_DIR = '/Users/ramrupsatpati/Downloads/Business_Data_Management'
pdf_path = os.path.join(REPO_DIR, 'Ramrup_Satpati_Resume.pdf')

# Letter size: 8.5 x 11 inches = 612 x 792 pt
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=32,
    rightMargin=32,
    topMargin=26,
    bottomMargin=24
)

PRIMARY = colors.HexColor("#1B365D")   # IITM Navy
ACCENT = colors.HexColor("#800000")    # IITM Maroon
DARK = colors.HexColor("#222222")
GRAY = colors.HexColor("#555555")

s_name = ParagraphStyle('RName', fontName='Helvetica-Bold', fontSize=18, leading=21, alignment=1, textColor=PRIMARY)
s_role = ParagraphStyle('RRole', fontName='Helvetica-Bold', fontSize=10, leading=13, alignment=1, textColor=ACCENT)
s_contact = ParagraphStyle('RContact', fontName='Helvetica', fontSize=8, leading=11, alignment=1, textColor=DARK)
s_links = ParagraphStyle('RLinks', fontName='Helvetica-Bold', fontSize=8, leading=11, alignment=1, textColor=PRIMARY)

s_sec = ParagraphStyle('RSec', fontName='Helvetica-Bold', fontSize=9.5, leading=12, textColor=PRIMARY, spaceBefore=4, spaceAfter=2)
s_item_title = ParagraphStyle('RTitle', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=DARK)
s_item_sub = ParagraphStyle('RSub', fontName='Helvetica-Oblique', fontSize=8, leading=10, textColor=ACCENT)
s_item_date = ParagraphStyle('RDate', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=GRAY, alignment=2)
s_body = ParagraphStyle('RBody', fontName='Helvetica', fontSize=8, leading=10.5, textColor=DARK, spaceAfter=2)
s_bullet = ParagraphStyle('RBullet', fontName='Helvetica', fontSize=8, leading=10.5, textColor=DARK, leftIndent=10, firstLineIndent=-7, spaceAfter=1.5)

story = []

# 1. Header
story.append(Paragraph("RAMRUP SATPATI", s_name))
story.append(Paragraph("Data Science & Machine Learning Engineer | ENFJ-A Protagonist", s_role))
story.append(Spacer(1, 2))
story.append(Paragraph("+91 8709601508 &bull; 24f3004027@ds.study.iitm.ac.in &bull; Jamshedpur, Jharkhand, India - 831004", s_contact))
story.append(Paragraph("GitHub: github.com/RSNPIIT &bull; LinkedIn: linkedin.com/in/ramrup-satpati-683970341 &bull; Portfolio: app-portfolio-dczpzvutdgvevdv8sedtls.streamlit.app", s_links))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=3, spaceAfter=4))

# 2. Professional Summary
story.append(Paragraph("PROFESSIONAL SUMMARY", s_sec))
story.append(Paragraph(
    "Degree-level BS student in Data Science & Applications at <b>IIT Madras</b> (Roll: 24f3004027 | <b>TOPPER - Top Course Grade - Diploma</b>). "
    "Technically grounded in Machine Learning, Deep Learning, Generative AI, and Linear Programming optimization. "
    "As an <b>ENFJ-A (Protagonist)</b>, blends mathematical and algorithmic rigor with empathetic collaboration, systems thinking, "
    "and clear communication to build scalable, human-centered computational applications.", s_body
))
story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#D8D8D8"), spaceBefore=3, spaceAfter=3))

# 3. Education
story.append(Paragraph("EDUCATION", s_sec))
edu_table = [
    [Paragraph("<b>Indian Institute of Technology Madras (IIT Madras)</b>", s_item_title), Paragraph("<b>2024 – Present</b>", s_item_date)],
    [Paragraph("<i>Bachelor of Science (BS) in Data Science and Applications (Degree Level)</i>", s_item_sub), Paragraph("Chennai, India", s_item_date)],
]
t_edu = Table(edu_table, colWidths=[5.6*inch, 2.0*inch])
t_edu.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5), ('TOPPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t_edu)
story.append(Paragraph("• <b>Academic Distinction:</b> Awarded <b>'TOPPER - Top Course Grade - Diploma'</b> badge; completed Foundational & dual Diploma coursework.", s_bullet))
story.append(Paragraph("• <b>Key Coursework:</b> Machine Learning Foundations & Practice (MLP), Deep Learning & GenAI, Business Data Management (BDM), Modern App Dev I & II (MAD 1/2), Tools in Data Science (TDS).", s_bullet))
story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#D8D8D8"), spaceBefore=3, spaceAfter=3))

# 4. Technical Skills
story.append(Paragraph("TECHNICAL & LEADERSHIP SKILLS", s_sec))
story.append(Paragraph("• <b>Languages & Databases:</b> Python (Advanced), SQL (PostgreSQL, SQLite), JavaScript, Bash Scripting, HTML5/CSS3.", s_bullet))
story.append(Paragraph("• <b>AI, ML & Modeling:</b> PyTorch, TensorFlow, Scikit-Learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn, GenAI & LLM architectures.", s_bullet))
story.append(Paragraph("• <b>Optimization & Analytics:</b> Constrained Linear Programming (SciPy, Simplex), Customer Lifetime Value (CLV), Econometrics, EDA.", s_bullet))
story.append(Paragraph("• <b>Frameworks & Tools:</b> Flask, Vue.js, Streamlit, RESTful APIs, Git, Docker, Linux/macOS, Jupyter.", s_bullet))
story.append(Paragraph("• <b>Leadership Dynamics (ENFJ-A):</b> Empathetic leadership, psychological safety, milestone tracking, systems thinking.", s_bullet))
story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#D8D8D8"), spaceBefore=3, spaceAfter=3))

# 5. Key Projects
story.append(Paragraph("FEATURED PROJECTS", s_sec))

# Project 1: BDM
p1_table = [
    [Paragraph("<b>Sales and Service Mix Optimization – Primary Data Analysis</b>", s_item_title), Paragraph("<b>Oct 2026</b>", s_item_date)],
    [Paragraph("<i>Operations Research & Business Analytics | GitHub: 24f3004027/Business_Data_Management</i>", s_item_sub), Paragraph("", s_item_date)]
]
t_p1 = Table(p1_table, colWidths=[5.6*inch, 2.0*inch])
t_p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0.5), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t_p1)
story.append(Paragraph("• Executed primary field survey ($N = 220$) evaluating after-sales service (AMC) attachment economics across retail and enterprise buyers.", s_bullet))
story.append(Paragraph("• Formulated and solved a constrained Simplex LP model balancing working capital and technician labor to optimize contribution margin.", s_bullet))
story.append(Paragraph("• Identified optimal mix ($X^* = 74$ sales, $Y^* = 132$ AMCs), yielding <b>+28.4% profit uplift</b> (INR 1.226M/mo) and a 3.0x return on technician payroll.", s_bullet))

# Project 2: Deep Learning & GenAI
p2_table = [
    [Paragraph("<b>Deep Learning & Generative AI Systems</b>", s_item_title), Paragraph("<b>2026</b>", s_item_date)],
    [Paragraph("<i>Neural Architectures & Generative Modeling | GitHub: 24f3004027/Deep_Learning_Project</i>", s_item_sub), Paragraph("", s_item_date)]
]
t_p2 = Table(p2_table, colWidths=[5.6*inch, 2.0*inch])
t_p2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0.5), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t_p2)
story.append(Paragraph("• Implemented deep learning pipelines utilizing CNNs, recurrent sequence models, and transformer architectures in PyTorch/TensorFlow.", s_bullet))
story.append(Paragraph("• Applied transfer learning, latent space representations, and attention mechanisms to optimize inference latency and accuracy.", s_bullet))

# Project 3: MAD 2 Placement Portal
p3_table = [
    [Paragraph("<b>Placement Portal Application V2 (MAD 2 Capstone)</b>", s_item_title), Paragraph("<b>2025 – 2026</b>", s_item_date)],
    [Paragraph("<i>Full-Stack Enterprise App | GitHub: 24f3004027/Placement_Portal_Application_V2</i>", s_item_sub), Paragraph("", s_item_date)]
]
t_p3 = Table(p3_table, colWidths=[5.6*inch, 2.0*inch])
t_p3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0.5), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t_p3)
story.append(Paragraph("• Engineered an enterprise university placement platform with RBAC authentication for Admins, Corporate Recruiters, and Candidates.", s_bullet))
story.append(Paragraph("• Integrated RESTful APIs with Flask, automated background job queues (Celery/Redis), and designed a reactive Vue.js interface.", s_bullet))

# Project 4: MLP / Python Projects
p4_table = [
    [Paragraph("<b>Predictive Modeling & Statistical Machine Learning (MLP)</b>", s_item_title), Paragraph("<b>2025</b>", s_item_date)],
    [Paragraph("<i>Supervised Learning & EDA | GitHub: 24f3004027/Machine_Learning_Practice_Project</i>", s_item_sub), Paragraph("", s_item_date)]
]
t_p4 = Table(p4_table, colWidths=[5.6*inch, 2.0*inch])
t_p4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0.5), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t_p4)
story.append(Paragraph("• Developed end-to-end predictive classification pipelines in Scikit-Learn/XGBoost with grid-search hyperparameter tuning.", s_bullet))
story.append(Paragraph("• Maintained monorepo utilities across multi-brand parking algorithms and hospital management systems (HMS).", s_bullet))

story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#D8D8D8"), spaceBefore=3, spaceAfter=3))

# 6. Experience & Leadership
story.append(Paragraph("EXPERIENCE & LEADERSHIP INITIATIVES", s_sec))
exp_table = [
    [Paragraph("<b>Open Source Contributor & Technical Project Lead</b>", s_item_title), Paragraph("<b>2024 – Present</b>", s_item_date)],
    [Paragraph("<i>Independent Data Science & Software Developer | GitHub: RSNPIIT</i>", s_item_sub), Paragraph("Remote", s_item_date)]
]
t_exp = Table(exp_table, colWidths=[5.6*inch, 2.0*inch])
t_exp.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0.5), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t_exp)
story.append(Paragraph("• Architected reproducible data science and optimization repositories; authored clear documentation and analytical codebooks.", s_bullet))
story.append(Paragraph("• Applied ENFJ-A strengths to foster psychological safety, active team consensus, and structured milestone tracking in technical projects.", s_bullet))

doc.build(story)
print("Updated Ramrup_Satpati_Resume.pdf generated.")
