from fpdf import FPDF
import os


class PDF(FPDF):
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Set font
        self.set_font('Aptos', '', 10)
        # Page number
        self.cell(0, 10, f'{self.page_no()}', 0, 0, 'C')      

# Define reusable styles
def set_style(font="Aptos", style='', size=12, color=(0, 0, 0)):
    pdf.set_font(font, style, size)
    pdf.set_text_color(*color)

prev_pros = [
    {
        "title": "Developed legal office document and task management system for Ethiopian Airlines",
        "description": [
                    "Developed a document management system to automate legal and administrative workflows.",
                    "Built with .NET and MS SQL Server for robust APIs and secure, high-performance data storage.",
                    "Used Next.js 15 (App Router) and Tailwind CSS for responsive, server-rendered frontend.",
                    "Have real-time analytics, contract management (e-signing, version control), case tracking, task automation, and scheduling.",
                    "Reduced manual processing by 60%, improved collaboration with role-based access, and streamlined operations by unifying tools.",
        ]       
        
    },
    {
        "title": "Built secure authentication system with role-based access",
        "description": 
        [
            "Implemented JWT-based authentication for secure user login in the Bankify financial app.",
            "Added claim-based authorization to control access—customers saw only their data, admins had elevated privileges.",
            "Built with .NET Core and Identity Framework for seamless role management and improved security without compromising user experience.",        
        ]       
       
    },
    {
        "title": "Integrated Stripe subscriptions with feature gating",
        "description": [
                "Designed a subscription-based pricing model with tiered plans (Basic, Pro, Enterprise) and dynamic feature access.",
                "Implemented feature flags for seamless upgrades/downgrades based on user subscription level.",
                "Built with React (frontend) and Node.js (backend), integrating Stripe for payments to boost monetization and scalability.",       
                ]        
        
    }
]

services = [
"Full-stack Web Application Development",
"Admin Dashboards & Internal Tools",
"API Development & Integration",
"Authentication and Role-based Access",
"Stripe/Payment Integration",
"Performance Optimization & Mobile Responsiveness",
"MVPs for SaaS or EdTech platforms",
]

clients = [
"Early-stage startups needing an MVP",
"SaaS platforms that need dashboards and subscriptions",
"Non-tech founders looking for technical execution",
"Educational platforms needing course, payment, and user systems",
]

experience = [
    {
    "company":"Ethiopian Airlines Group(ETAG)", 
     "title":"Software Developer",
     "description":[
                    "Built end-to-end web apps with .NET, React, and MS SQL, improving data processing efficiency by 40%.",
                    "Partnered with senior engineers to deliver scalable software, reducing deployment time by 30%.",
                    "Enhanced SAP modules via RFC integration and report programming, cutting manual tasks by 50%.",
                    "Boosted ERP system performance while developing enterprise apps, ensuring 99% uptime."
                ],        
     "duration":"Apr 2024 - Present"
     },
    {
    "company":"Addis International Bank(ADIB)", 
     "title":"Trainee Software Developer",
     "description":[
                "Boosted customer satisfaction by 15% for both account holders and external users.",
                "Improved accessibility and UX to double the customer base."
            ] ,
     "duration":"Dec 2023 - Apr 2024"
     },
    {
    "company":"Freelance", 
     "title":"Full-stack Developer",
     "description": [
        "Built a desktop app for AAU that automated nationwide seismic data management.",
        "Delivered a data-driven solution improving earthquake tracking/analysis by 60%.",
   ],
     "duration":"Jun 2023 - Present"
     },
    {
    "company":"Amhara Bank", 
     "title":"Intern Software Developer",
     "description":[
        "Revamped bank's currency display app with brand-aligned design, boosting readability and UX by 25%.",
        "Mastered Git, Postman, and DevOps through collaboration with senior engineers"   ],
     "duration":"Jan 2023 - Feb 2023"
     },
]

education=[
    {
        "institution":"Addis Ababa University",
        "location":"Addis Ababa, Ethiopia",        
        "major":"Computer Science (Bachelor's | Undergraduate Degree)",
        "score":"Great Distiniction",
        "duration":"Oct 2019 - Jul 2023"
    }
]

tech_stack = [
"Languages:\u00A0 \u00A0C#, JavaScript(TypeScript), Python, C++.",
"Frameworks:\u00A0 \u00A0ASP.NET Core, Node.js, Express.js, React.js, Next.js, Tailwind CSS.",
"Database:\u00A0 \u00A0PostgreSQL,MS SQL Server, MongoDB. ",
"Cloud:\u00A0 \u00A0Azure, Supabase, Firebase.",
"Tools:\u00A0 \u00A0Git, Azure DevOps, Postman, VS Code, Visual Studio, Docker (basic).",
]


# Create PDF with updated contact info
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_font('Aptos', '', "fonts/aptos-regular.ttf", uni=True)
pdf.add_font('Aptos-italic','I',"fonts/aptos-italic.ttf",uni=True)
pdf.add_font('Aptos-bold', 'B', "fonts/aptos-bold.ttf", uni=True)

# Name and headline with improved horizontal line
# Fill a cell with color
pdf.set_fill_color(241, 245, 249)   
pdf.set_font("Aptos-bold", 'B', 16)
pdf.cell(0, 7, "Sewlesew Biazen", ln=True,align='C',fill=True)
pdf.set_font("Aptos", '', 12)
current_y = pdf.get_y()  # Get current Y position after name
pdf.multi_cell(0, 8, "Full-Stack Web Developer | React(Next.js), ASP.NET Core, Node.js(Express.js), MongoDB, SQL, ABAP",fill=True)
set_style("Aptos-italic", 'I',11,(50, 50, 50))
pdf.multi_cell(0, 6, "sewlesewbiazen@gmail.com \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 "
"+251961718044 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 https://linkedin.com/in/sewlesew-biazen-sfd " 
" https://sewlesewbi.netlify.app \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 "
"https://github.com/SEWLESEWBIAZEN \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 \u00A0 Addis Ababa, Ethiopia",align='C')  # ln=False prevents line break
pdf.set_text_color(0, 0, 0)
pdf.ln(3)

# Introduction section
pdf.set_font("Aptos-bold", 'B', 14)
pdf.cell(0, 8, "Professional Profile", ln=True)

# Calculate position for horizontal line (after multi_cell)
line_y = pdf.get_y()-1   # Add small spacing
pdf.line(10, line_y, pdf.w - 10, line_y)  # Full width line with margins

# Optional: Styled horizontal line (thinner/lighter)
pdf.set_line_width(0.1)
pdf.set_draw_color(200, 200, 200)  # Light gray
pdf.line(10, line_y, pdf.w - 10, line_y)
pdf.set_draw_color(0)  # Reset to black
pdf.set_line_width(0.2)  # Reset default width
pdf.ln(2)  # Add spacing after line
pdf.set_font("Aptos", '', 12)
pdf.multi_cell(0, 6, "I help startups and businesses build powerful, fast, and scalable web applications using modern technologies. " \
"Whether it's building a full product from scratch or improving an existing one, I deliver clean, responsive, and secure solutions.")
pdf.ln(3)

# Experience Section
pdf.set_font("Aptos-bold", 'B', 14)
pdf.cell(0, 10, "Experience:", ln=True)
# Calculate position for horizontal line (after multi_cell)
line_y = pdf.get_y()-1   # Add small spacing
pdf.line(10, line_y, pdf.w - 10, line_y)  # Full width line with margins
# Optional: Styled horizontal line (thinner/lighter)
pdf.set_line_width(0.1)
pdf.set_draw_color(200, 200, 200)  # Light gray
pdf.line(10, line_y, pdf.w - 10, line_y)
pdf.set_draw_color(0)  # Reset to black
pdf.set_line_width(0.2)  # Reset default width
pdf.ln(2)  # Add spacing after line

# Main experience loop
for exp in experience:
    # Company and duration (same line)
    set_style("Aptos-bold", 'B', 12, (0, 0, 0))
    pdf.cell(0, 6, f"{exp['company']}", ln=False)    
    set_style("Aptos-italic", 'I', 12, (75, 75, 75))
    pdf.cell(0, 6, exp['duration'], ln=True, align='R')
    
    # Title (indented)
    pdf.set_x(13)
    set_style("Aptos-italic", 'I', 12, (0, 0, 0))
    pdf.cell(0, 6, exp['title'], ln=True)
    
    # Description (indented, italic)    
    set_style("Aptos","",12,(25,25,25))
    for ex in exp['description']:
        pdf.set_x(15)
        pdf.multi_cell(0, 7, f"• {ex}")
    pdf.ln(3) 

# Education Section
pdf.set_font("Aptos-bold", 'B', 14)
pdf.cell(0, 10, "Education:", ln=True)
# Calculate position for horizontal line (after multi_cell)
line_y = pdf.get_y()-1   # Add small spacing
pdf.line(10, line_y, pdf.w - 10, line_y)  # Full width line with margins
# Optional: Styled horizontal line (thinner/lighter)
pdf.set_line_width(0.1)
pdf.set_draw_color(200, 200, 200)  # Light gray
pdf.line(10, line_y, pdf.w - 10, line_y)
pdf.set_draw_color(0)  # Reset to black
pdf.set_line_width(0.2)  # Reset default width
pdf.ln(2)  # Add spacing after line  

# main education section
for edu in education:
    # Institution and Duration (same line)
    set_style("Aptos-bold", 'B', 12, (0, 0, 0))
    pdf.cell(0, 6, edu['institution'], ln=False)    
    set_style("Aptos-italic", 'I', 12, (75, 75, 75))
    pdf.cell(0, 6, edu['duration'], ln=True, align='R') 
    set_style("Aptos", '', 12, (50, 50, 50))  

    # Major and Score (same line, indented)
    pdf.set_x(15)  
    pdf.cell(0, 6, f"• {edu['major']}", ln=True)    
    pdf.set_x(15) 
    set_style("Aptos-italic", 'I', 12, (175, 175, 175))   
    pdf.cell(0, 6, f"****{edu['score']}****", ln=True)
    pdf.set_x(15)
    set_style("Aptos", '', 12, (50, 50, 50))  
    pdf.cell(0, 5, f"• {edu['location']}", ln=True)    
    pdf.ln(3)  # Space between entries

pdf.add_page()
# Recent Projects section
set_style("Aptos-bold", 'B', 14,(0,0,0))
pdf.cell(0, 10, "Recent Projects:", ln=True)

# Calculate position for horizontal line (after multi_cell)
line_y = pdf.get_y() -1  # Add small spacing
pdf.line(10, line_y, pdf.w - 10, line_y)  # Full width line with margins
# Optional: Styled horizontal line (thinner/lighter)
pdf.set_line_width(0.1)
pdf.set_draw_color(200, 200, 200)  # Light gray
pdf.line(10, line_y, pdf.w - 10, line_y)
pdf.set_draw_color(0)  # Reset to black
pdf.set_line_width(0.2)  # Reset default width
pdf.ln(2)  # Add spacing after line

for pro in prev_pros:  
    set_style("Aptos-bold","B",12,(0,0,0))   
    pdf.cell(0, 6, f"{pro['title']}", ln=True)  
    set_style("Aptos","",12,(25,25,25))
    for desc in pro['description']:
         pdf.set_x(15)
         pdf.multi_cell(0, 7, f"• {desc}")         
    pdf.ln(3)

# Tech Stack section
pdf.set_font("Aptos-bold", 'B', 14)
pdf.cell(0, 10, "Technical Skills:", ln=True)
# Calculate position for horizontal line (after multi_cell)
line_y = pdf.get_y()-1   # Add small spacing
pdf.line(10, line_y, pdf.w - 10, line_y)  # Full width line with margins
# Optional: Styled horizontal line (thinner/lighter)
pdf.set_line_width(0.1)
pdf.set_draw_color(200, 200, 200)  # Light gray
pdf.line(10, line_y, pdf.w - 10, line_y)
pdf.set_draw_color(0)  # Reset to black
pdf.set_line_width(0.2)  # Reset default width
pdf.ln(2)  # Add spacing after line
pdf.set_font("Aptos", '', 12)
for skill in tech_stack:
    pdf.set_x(15)
    pdf.cell(0, 6, f"• {skill}", ln=True)
pdf.ln(5)

pdf.add_page() # start in new page
pdf.set_font("Aptos", '', 12)

# Services section
pdf.set_font("Aptos-bold", 'B', 14)
pdf.cell(0, 10, "What I Can Help You With:", ln=True)

# Calculate position for horizontal line (after multi_cell)
line_y = pdf.get_y()-1   # Add small spacing
pdf.line(10, line_y, pdf.w - 10, line_y)  # Full width line with margins
# Optional: Styled horizontal line (thinner/lighter)
pdf.set_line_width(0.1)
pdf.set_draw_color(200, 200, 200)  # Light gray
pdf.line(10, line_y, pdf.w - 10, line_y)
pdf.set_draw_color(0)  # Reset to black
pdf.set_line_width(0.2)  # Reset default width
pdf.ln(2)  # Add spacing after line
set_style('Aptos', '', 12,(0,0,0))
for service in services:
    pdf.set_x(15)
    pdf.cell(0, 6, f"• {service}", ln=True)
pdf.ln(5)

# Clients section
pdf.set_font("Aptos-bold", 'B', 14)
pdf.cell(0, 10, "Who I Work With:", ln=True)

# Calculate position for horizontal line (after multi_cell)
line_y = pdf.get_y() -1  # Add small spacing
pdf.line(10, line_y, pdf.w - 10, line_y)  # Full width line with margins

# Optional: Styled horizontal line (thinner/lighter)
pdf.set_line_width(0.1)
pdf.set_draw_color(200, 200, 200)  # Light gray
pdf.line(10, line_y, pdf.w - 10, line_y)
pdf.set_draw_color(0)  # Reset to black
pdf.set_line_width(0.2)  # Reset default width
pdf.ln(2)  # Add spacing after line
pdf.set_font("Aptos", '', 12)
for client in clients:
    pdf.set_x(15)
    pdf.cell(0, 6, f"• {client}", ln=True)
pdf.ln(5)
pdf.set_font("Aptos", '', 12)   

# Closing section
pdf.set_font("Aptos-italic", 'I', 12)
pdf.multi_cell(0, 6, "I look forward to the opportunity to discuss how I can contribute to your projects and startups. Please feel free to contact me for any inquiries or project discussions.")

# Calculate position for horizontal line (after multi_cell)
line_y = pdf.get_y() +10  # Add small spacing
pdf.line(10, line_y, pdf.w - 10, line_y)  # Full width line with margins
# Optional: Styled horizontal line (thinner/lighter)
pdf.set_line_width(0.1)
pdf.set_draw_color(200, 200, 200)  # Light gray
pdf.line(10, line_y, pdf.w - 10, line_y)
pdf.set_draw_color(0)  # Reset to black
pdf.set_line_width(0.2)  # Reset default width
pdf.ln(2)  # Add spacing after line

# Save the PDF
pdf.output("exports/Sewlesew_Biazen_Resume_Updated.pdf")