import streamlit as st

# Set page configuration
st.set_page_config(page_title="Mohammed Qamaruddin's Portfolio", page_icon="🛡️", layout="wide")

# Header Section
st.title("Welcome to Mohammed Qamaruddin's Portfolio! 🛡️")
st.write("Aspiring Cybersecurity Professional | Cloud Security Enthusiast | Ethical Hacker")

# About Section
st.header("About Me")
st.write("""
I am an aspiring cybersecurity professional actively seeking roles to apply my skills in the GRC and technical areas of cybersecurity.  
With a strong foundation in cybersecurity principles, cloud security, and ethical hacking, I aim to make the digital world safer.
""")

# Contact Section
st.sidebar.header("Contact Me")
st.sidebar.write("📧 [mqamaruddin07@gmail.com](mailto:mqamaruddin07@gmail.com)")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/mohammad-qamaruddin-220343230)")
st.sidebar.write("🌐 [GitHub](https://github.com/Qamaruddin41)")
st.sidebar.write("🌍 [Portfolio](https://qamaruddin41.github.io/Personal-Portfolio/)")

# Experience Section
st.header("Experience")
st.subheader("Security Intern | Mastercard")
st.write("""
- Designed and deployed a phishing email simulation targeting over 100 simulated users.
- Analyzed simulation results, reducing risks through targeted training.
- Provided actionable recommendations to enhance employee security awareness.
""")

st.subheader("Cloud Security Intern | Zscaler")
st.write("""
- Learned and applied Zero Trust Architecture principles in cloud environments.
- Secured over 100 user accounts through Zero Trust policies.
- Participated in workshops and discussions to develop strategies for mitigating security risks.
""")

st.subheader("Ethical Hacking Intern | Corizo")
st.write("""
- Conducted vulnerability assessments on multiple systems, identifying critical flaws.
- Collaborated with mentors to implement key security measures and improve system security.
- Documented findings and delivered actionable recommendations.
""")

# Projects Section
st.header("Projects")
st.subheader("Expense Tracker using Python")
st.write("""
- Developed a Python-based application to track and categorize expenses.
- Managed up to 100 transactions per day with persistent data storage.
- Reduced manual errors by 90%.
[View Project](https://github.com/me50/Qamaruddin41.git)
""")

st.subheader("Cybersecurity Homelab")
st.write("""
- Configured virtual machines for penetration testing and vulnerability analysis.
- Conducted ethical hacking exercises with tools like Metasploit, Nmap, and Wireshark.
- Set up intrusion detection systems to handle over 1000 potential attack vectors.
[View Project](https://github.com/Qamaruddin41/Cybersecurity-Home-Lab)
""")

# Education Section
st.header("Education")
st.subheader("Bachelor of Technology")
st.write("""
- Guru Nanak Institutions Technical Campus, Telangana
- CGPA: 8.1 | Graduation Year: 2025
""")

# Certifications Section
st.header("Certifications")
certifications = [
    "Google Cybersecurity Professional Course (2024)",
    "Introduction to Python Programming by CS50 (2023)"
]
st.write("\n".join([f"- {cert}" for cert in certifications]))

# Skills Section
st.header("Skills")
st.write("""
- **Programming**: HTML, CSS, Bootstrap, JavaScript, Git, GitHub, VS Code  
- **Cybersecurity**: VMware, Linux, MySQL, NIST Frameworks, Documentation  
- **Cloud**: Google Cloud, AWS
""")

# Footer
st.write("---")
st.write("© 2024 Mohammed Qamaruddin | Powered by Streamlit")

