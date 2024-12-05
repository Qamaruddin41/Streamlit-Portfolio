import streamlit as st
from PIL import Image

# Set up the page configuration
st.set_page_config(
    page_title="Mohammed Qamaruddin | Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS for styling
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        color: #00416a;
        text-align: center;
        font-weight: bold;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #0078D4;
        text-align: center;
    }
    .section-title {
        font-size: 2rem;
        color: #00416a;
        border-bottom: 2px solid #0078D4;
        margin-bottom: 10px;
    }
    .skill-badge {
        background-color: #0078D4;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        margin-right: 10px;
        font-size: 1rem;
    }
    .contact-link {
        color: #0078D4;
        font-size: 1.2rem;
        text-decoration: none;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Main title and subtitle
st.markdown('<h1 class="main-title">Welcome to Mohammed Qamaruddin\'s Portfolio</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Aspiring Cybersecurity Professional | Ethical Hacker | Cloud Security Enthusiast</p>', unsafe_allow_html=True)

# Add a profile image
profile_pic = "https://via.placeholder.com/200"  # Replace with actual profile picture URL
st.image(profile_pic, width=200, caption="Mohammed Qamaruddin", use_column_width=False)

# Sidebar Contact Information
st.sidebar.title("Contact Me")
st.sidebar.markdown(f"""
- 📧 **Email**: [mqamaruddin07@gmail.com](mailto:mqamaruddin07@gmail.com)
- 🔗 **LinkedIn**: [linkedin.com/in/mohammad-qamaruddin-220343230](https://www.linkedin.com/in/mohammad-qamaruddin-220343230)
- 🌐 **GitHub**: [Qamaruddin41](https://github.com/Qamaruddin41)
- 🖥️ **Portfolio**: [qamaruddin41.github.io](https://qamaruddin41.github.io/Personal-Portfolio/)
""")

# Introduction Section
st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
st.write("""
I am a cybersecurity professional with expertise in **GRC** and **technical security**, 
constantly expanding my knowledge to protect organizations in an ever-evolving digital world.
I am passionate about creating secure systems, analyzing vulnerabilities, and implementing robust solutions to mitigate risks.
""")

# Experience Section
st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Security Intern | Mastercard")
    st.write("""
    - Deployed phishing email simulations targeting 100+ users.
    - Reduced phishing risks by recommending targeted training.
    - Improved employee security awareness using simulation data.
    """)

with col2:
    st.subheader("Cloud Security Intern | Zscaler")
    st.write("""
    - Learned and implemented **Zero Trust Architecture** in cloud environments.
    - Secured over 100 user accounts through Zero Trust policies.
    - Participated in workshops to develop strategies for mitigating security risks.
    """)

st.subheader("Ethical Hacking Intern | Corizo")
st.write("""
- Conducted vulnerability assessments, identifying critical flaws.
- Collaborated with mentors to develop mitigation strategies.
- Improved system security by addressing 70% of identified vulnerabilities.
""")

# Projects Section
st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)

project1, project2 = st.columns(2)
with project1:
    st.subheader("Expense Tracker (Python)")
    st.write("""
    - Developed a **Python-based app** to track daily expenses for up to 50 users.
    - Enhanced data accuracy with persistent CSV-based storage.
    - Reduced manual errors by **90%** with automated tracking.
    [GitHub Repo](https://github.com/me50/Qamaruddin41.git)
    """)

with project2:
    st.subheader("Cybersecurity Homelab")
    st.write("""
    - Built VMs to simulate real-world penetration testing scenarios.
    - Configured firewalls and IDS to handle over **1000 attack vectors**.
    - Utilized tools like **Metasploit**, **Nmap**, and **Wireshark**.
    [GitHub Repo](https://github.com/Qamaruddin41/Cybersecurity-Home-Lab)
    """)

# Skills Section
st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

skills = [
    "HTML", "CSS", "JavaScript", "Python", "Bootstrap", "Git", "GitHub", 
    "VMware", "Linux", "AWS", "Google Cloud", "NIST Frameworks", "SIEM Tools"
]
st.write(" ".join([f'<span class="skill-badge">{skill}</span>' for skill in skills]), unsafe_allow_html=True)

# Certifications Section
st.markdown('<h2 class="section-title">Certifications</h2>', unsafe_allow_html=True)
certifications = [
    "Google Cybersecurity Professional Course (2024)",
    "CS50 Introduction to Python Programming (2023)"
]
st.write("\n".join([f"- {cert}" for cert in certifications]))

# Footer
st.markdown('<h2 class="section-title">Let\'s Connect!</h2>', unsafe_allow_html=True)
st.write("Feel free to reach out via email or connect on LinkedIn. Let’s collaborate on making the digital world a safer place!")

st.markdown("---")
st.markdown('<p style="text-align: center;">© 2024 Mohammed Qamaruddin | Built with ❤️ in Streamlit</p>', unsafe_allow_html=True)
