import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.pdfgen import canvas

REPO_DIR = '/Users/ramrupsatpati/Downloads/Business_Data_Management'
PHOTO_PATH = os.path.join(REPO_DIR, 'ramrup_formal_photo.png')
pdf_path = os.path.join(REPO_DIR, 'Ramrup_Satpati_Resume.pdf')

class ResumeCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        page_num = self._pageNumber
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#666666"))

        if page_num > 1:
            # Header on page 2+
            self.drawString(36, letter[1] - 24, "Ramrup Satpati | Resume & Technical Portfolio (IIT Madras Roll: 24f3004027)")
            self.drawRightString(letter[0] - 36, letter[1] - 24, "Degree Level - Data Science")
            self.setStrokeColor(colors.HexColor("#E0E0E0"))
            self.setLineWidth(0.5)
            self.line(36, letter[1] - 28, letter[0] - 36, letter[1] - 28)

        # Footer on all pages
        self.setStrokeColor(colors.HexColor("#E0E0E0"))
        self.setLineWidth(0.5)
        self.line(36, 26, letter[0] - 36, 26)
        self.drawString(36, 16, "Ramrup Satpati &bull; +91 8709601508 &bull; 24f3004027@ds.study.iitm.ac.in")
        page_str = f"Page {page_num} of {total_pages}"
        self.drawRightString(letter[0] - 36, 16, page_str)
        self.restoreState()

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=32,
    bottomMargin=32
)

NAVY = colors.HexColor("#1B365D")
MAROON = colors.HexColor("#800000")
DARK = colors.HexColor("#222222")
GRAY = colors.HexColor("#555555")
BLUE_LINK = colors.HexColor("#0B5394")

styles = getSampleStyleSheet()

s_name = ParagraphStyle('RName', fontName='Helvetica-Bold', fontSize=20, leading=23, textColor=NAVY)
s_role = ParagraphStyle('RRole', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=MAROON)
s_contact = ParagraphStyle('RContact', fontName='Helvetica', fontSize=8, leading=11, textColor=DARK)
s_link_hdr = ParagraphStyle('RLinkHdr', fontName='Helvetica', fontSize=8, leading=11, textColor=BLUE_LINK)

s_sec = ParagraphStyle('RSec', fontName='Helvetica-Bold', fontSize=9.5, leading=12, textColor=NAVY, spaceBefore=6, spaceAfter=2)
s_title = ParagraphStyle('RTitle', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=DARK)
s_sub = ParagraphStyle('RSub', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=MAROON)
s_date = ParagraphStyle('RDate', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=GRAY, alignment=2)
s_body = ParagraphStyle('RBody', fontName='Helvetica', fontSize=8, leading=11, textColor=DARK, spaceAfter=2)
s_bullet = ParagraphStyle('RBullet', fontName='Helvetica', fontSize=8, leading=10.5, textColor=DARK, leftIndent=11, firstLineIndent=-7, spaceAfter=2)
s_proj_url = ParagraphStyle('RProjUrl', fontName='Helvetica-Oblique', fontSize=7.5, leading=9.5, textColor=BLUE_LINK)

story = []

# ==========================================
# 1. HEADER WITH EMBEDDED FORMAL PHOTO
# ==========================================
left_hdr = [
    Paragraph("<b>RAMRUP SATPATI</b>", s_name),
    Spacer(1, 2),
    Paragraph("<b>Data Science & Machine Learning Engineer | ENFJ-A Protagonist</b>", s_role),
    Spacer(1, 2),
    Paragraph("<b>Roll No:</b> 24f3004027 &bull; <b>Email:</b> 24f3004027@ds.study.iitm.ac.in &bull; <b>Phone:</b> +91 8709601508", s_contact),
    Paragraph("<b>Address:</b> T4 Jhelum Block, Alok Vihar, Ghorabandha, Jamshedpur, Jharkhand, India - 831004", s_contact),
    Spacer(1, 2),
    Paragraph("<b>LinkedIn:</b> <link href='https://www.linkedin.com/in/ramrup-satpati-683970341'><u>linkedin.com/in/ramrup-satpati-683970341</u></link>", s_link_hdr),
    Paragraph("<b>GitHub:</b> <link href='https://github.com/RSNPIIT'><u>github.com/RSNPIIT</u></link> &bull; <link href='https://github.com/24f3004027'><u>github.com/24f3004027</u></link>", s_link_hdr),
    Paragraph("<b>Portfolio:</b> <link href='https://app-portfolio-dczpzvutdgvevdv8sedtls.streamlit.app'><u>app-portfolio-dczpzvutdgvevdv8sedtls.streamlit.app</u></link>", s_link_hdr),
]

if os.path.exists(PHOTO_PATH):
    photo_img = Image(PHOTO_PATH, width=1.1*inch, height=1.4*inch)
    right_hdr = [photo_img]
else:
    right_hdr = [Spacer(1, 1.4*inch)]

hdr_table_data = [[left_hdr, right_hdr]]
t_hdr = Table(hdr_table_data, colWidths=[6.2*inch, 1.4*inch])
t_hdr.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (1,0), (1,0), 'RIGHT'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))
story.append(t_hdr)
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceBefore=4, spaceAfter=4))

# ==========================================
# 2. PROFESSIONAL PROFILE & PERSONALITY
# ==========================================
story.append(Paragraph("PROFESSIONAL SUMMARY", s_sec))
story.append(Paragraph(
    "Degree-level BS student in Data Science & Applications at <b>IIT Madras</b> (Roll: 24f3004027 | <b>TOPPER - Top Course Grade - Diploma</b>). "
    "Technically grounded in Machine Learning, Deep Learning, Generative AI systems, and Operations Research mathematical optimization models. "
    "As an <b>ENFJ-A (Protagonist)</b>, blends analytical rigor with empathetic collaboration, systems thinking, and structured cross-functional communication "
    "to lead high-impact technical initiatives bridging algorithmic intelligence with human-centered applications.", s_body
))
story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#D0D0D0"), spaceBefore=3, spaceAfter=3))

# ==========================================
# 3. EDUCATION & GPA
# ==========================================
story.append(Paragraph("EDUCATION", s_sec))
edu_data = [
    [Paragraph("<b>Indian Institute of Technology Madras (IIT Madras)</b>", s_title), Paragraph("<b>2024 – Present</b>", s_date)],
    [Paragraph("<i>Bachelor of Science (BS) in Data Science and Applications (Degree Level)</i>", s_sub), Paragraph("Chennai, India", s_date)],
]
t_edu = Table(edu_data, colWidths=[5.6*inch, 2.0*inch])
t_edu.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))
story.append(t_edu)
story.append(Paragraph("• <b>Academic Standing & GPA:</b> <b>CGPA: 8.8 / 10.0</b> (Degree Level) &bull; Awarded <b>'TOPPER - Top Course Grade - Diploma'</b> Honor Badge.", s_bullet))
story.append(Paragraph("• <b>Foundational & Diploma Certifications:</b> Completed all theoretical components for dual Diplomas in Programming and Data Science.", s_bullet))
story.append(Paragraph("• <b>Core Coursework:</b> Machine Learning Foundations & Practice (MLF/MLP), Deep Learning & GenAI (Viva: 45/50, 90%), Business Data Management (BDM), Modern App Dev I & II (MAD 1/2), Tools in Data Science (TDS), Systems & Usable Security (Elite Distinction 81%).", s_bullet))
story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#D0D0D0"), spaceBefore=3, spaceAfter=3))

# ==========================================
# 4. TECHNICAL & LEADERSHIP SKILLS
# ==========================================
story.append(Paragraph("TECHNICAL & LEADERSHIP SKILLS", s_sec))
story.append(Paragraph("• <b>Languages & Databases:</b> Python (Expert), SQL (PostgreSQL, SQLite), JavaScript, Bash/Shell, HTML5/CSS3.", s_bullet))
story.append(Paragraph("• <b>Machine Learning & AI:</b> PyTorch, TensorFlow, Scikit-Learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn, GenAI & Transformer Models.", s_bullet))
story.append(Paragraph("• <b>Optimization & Methods:</b> Constrained Linear Programming (Simplex / SciPy), Customer Lifetime Value (CLV), Econometrics, EDA.", s_bullet))
story.append(Paragraph("• <b>Web & Tools:</b> Flask, Vue.js, Streamlit, RESTful APIs, Git/GitHub, Docker, Linux/macOS, Jupyter Notebooks.", s_bullet))
story.append(Paragraph("• <b>Leadership & Personal Dynamics (ENFJ-A):</b> Empathetic leadership, proactive psychological safety, systems thinking, milestone tracking.", s_bullet))
story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#D0D0D0"), spaceBefore=3, spaceAfter=3))

# ==========================================
# 5. FEATURED TECHNICAL PROJECTS (WITH ALL EXPLICIT LINKS)
# ==========================================
story.append(Paragraph("FEATURED PROJECTS & REPOSITORIES", s_sec))

def add_project(name, period, github_url, bullets):
    p_hdr = [
        [Paragraph(f"<b>{name}</b>", s_title), Paragraph(f"<b>{period}</b>", s_date)],
        [Paragraph(f"<link href='{github_url}'><u>{github_url}</u></link>", s_proj_url), Paragraph("", s_date)]
    ]
    t = Table(p_hdr, colWidths=[5.6*inch, 2.0*inch])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t)
    for b in bullets:
        story.append(Paragraph(f"• {b}", s_bullet))
    story.append(Spacer(1, 2))

# 1. BDM Project
add_project(
    "Sales and Service Mix Optimization – Primary Data Analysis (BDM Capstone)",
    "Oct 2026",
    "https://github.com/24f3004027/Business_Data_Management",
    [
        "Administered a primary field survey across 220 retail/commercial clients evaluating after-sales service (AMC) attachment economics.",
        "Formulated and solved a constrained Simplex Linear Programming (LP) model balancing technician labor and working capital limits.",
        "Discovered optimal mix (74 sales units, 132 AMC contracts/mo), securing a <b>+28.4% profit increase</b> (INR 1.226M/mo) and a 3.0x return on technician payroll."
    ]
)

# 2. DL & GenAI
add_project(
    "Deep Learning & Generative AI Systems",
    "2026",
    "https://github.com/24f3004027/Deep_Learning_Project",
    [
        "Implemented end-to-end deep learning pipelines utilizing CNNs, recurrent sequence models, and transformer representations in PyTorch/TensorFlow.",
        "Applied transfer learning and latent space representations; scored <b>45 / 50 (90%) in oral viva defense</b> and 10/10 on the technical report."
    ]
)

# 3. MAD 2 Placement Portal
add_project(
    "Placement Portal Application V2 (MAD 2 Capstone)",
    "2025 – 2026",
    "https://github.com/24f3004027/Placement_Portal_Application_V2",
    [
        "Architected an enterprise placement management platform supporting Role-Based Access Control (RBAC) for Admins, Corporate Recruiters, and Candidates.",
        "Built RESTful APIs with Flask, automated background job queues (Celery/Redis), and designed a reactive Vue.js interface."
    ]
)

# 4. MAD 1 Vehicle Parking
add_project(
    "Vehicle Parking Management System (MAD 1 Capstone)",
    "2025",
    "https://github.com/24f3004027/vehicle-parking-appv1",
    [
        "Engineered an automated multi-slot vehicle parking application with automated ticket timestamps, dynamic rate billing, and SQLite database storage.",
        "Implemented server-side validation and session security in Python/Flask with clean responsive UI."
    ]
)

# 5. MAD 1 Hospital Management System (HMS)
add_project(
    "Hospital Management System – HMS (MAD 1 Improvement Project)",
    "2025",
    "https://github.com/24f3004027/HMS-MAD-Projectv1",
    [
        "Constructed a comprehensive clinical records and appointment scheduling system connecting doctors, patients, and administrators.",
        "Designed relational database schemas, automated appointment slot booking, and generated diagnostic summaries."
    ]
)

# 6. MLP Project
add_project(
    "Predictive Machine Learning & Classification Pipeline (MLP)",
    "2025",
    "https://github.com/24f3004027/Machine_Learning_Practice_Project",
    [
        "Developed end-to-end supervised machine learning models utilizing Scikit-learn and XGBoost for classification and regression tasks.",
        "Executed feature transformation, cross-validated grid search hyperparameter tuning, and model explainability metrics."
    ]
)

# 7. Python Projects Monorepo
add_project(
    "Python Projects Monorepo",
    "2024 – 2026",
    "https://github.com/RSNPIIT/Python-Projects",
    [
        "Consolidated repository of modular algorithmic tools, data structures, automation utilities, and numerical scripts in Python."
    ]
)

story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#D0D0D0"), spaceBefore=3, spaceAfter=3))

# ==========================================
# 6. EXPERIENCE & LEADERSHIP INITIATIVES
# ==========================================
story.append(Paragraph("EXPERIENCE & LEADERSHIP INITIATIVES", s_sec))
exp_data = [
    [Paragraph("<b>Open Source Contributor & Technical Project Lead</b>", s_title), Paragraph("<b>2024 – Present</b>", s_date)],
    [Paragraph("<i>Independent Data Science & Software Developer | GitHub: RSNPIIT</i>", s_sub), Paragraph("Remote", s_date)]
]
t_exp = Table(exp_data, colWidths=[5.6*inch, 2.0*inch])
t_exp.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))
story.append(t_exp)
story.append(Paragraph("• Architected reproducible data science and optimization repositories; authored clear documentation and analytical codebooks.", s_bullet))
story.append(Paragraph("• Applied ENFJ-A strengths to foster psychological safety, active team consensus, and structured milestone tracking in technical projects.", s_bullet))

# ==========================================
# 7. CERTIFICATIONS & LANGUAGES
# ==========================================
story.append(Spacer(1, 2))
story.append(Paragraph("CERTIFICATIONS & LANGUAGES", s_sec))
story.append(Paragraph("• <b>Certifications:</b> Top Course Grade - Diploma Honor (IIT Madras), Systems and Usable Security (Elite Distinction 81%), Completed Foundational & Dual Diploma coursework.", s_bullet))
story.append(Paragraph("• <b>Languages:</b> English (Professional Working Proficiency), Hindi (Native), Bengali.", s_bullet))

doc.build(story, canvasmaker=ResumeCanvas)
print("Updated photo resume with running headers/footers built successfully!")
