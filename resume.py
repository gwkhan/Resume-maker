# resume maker


from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", size=20)
pdf.cell(200, 10, txt="Resume", ln=1, align="C")
pdf.ln(5)

name = input("Enter your name: ").capitalize()
age = input("Enter your age: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt=f"Name: {name}", ln=1)
pdf.cell(200, 10, txt=f"Age: {age}", ln=1)
pdf.cell(200, 10, txt=f"Phone: {phone}", ln=1)
pdf.cell(200, 10, txt=f"Email: {email}", ln=1)
pdf.ln(5)

education = input("Enter your Education: ").capitalize()
if education.strip():
    pdf.set_font("Arial", "B", size=18)
    pdf.cell(200, 10, txt="Education", ln=1)
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=education, ln=1)
    pdf.ln(5)

Skills = input("Enter your skills separated by commas(,): ")
if Skills.strip():
    skill = Skills.split(",")
    pdf.set_font("Arial", "B", size=18)
    pdf.cell(200, 10, txt="Skills", ln=1)
    pdf.set_font("Arial", size=16)
    for a in skill:
        pdf.cell(200, 10, txt=f"• {a.strip().capitalize()}", ln=1)
    pdf.ln(5)

experience = input("Enter your experience: ")
if experience.strip():
    pdf.set_font("Arial", "B", size=18)
    pdf.cell(200, 10, txt="Experience", ln=1)
    pdf.set_font("Arial", size=16)
    pdf.multi_cell(0, 10, experience.strip())
    pdf.ln(5)

pdf.output("resume.pdf")
print("✅ Resume saved as 'resume.pdf'")