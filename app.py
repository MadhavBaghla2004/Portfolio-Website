import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from pathlib import Path
from PIL import Image
import base64


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Madhav Baghla"
PAGE_ICON = ":m:"
NAME = "Madhav Baghla"
DESCRIPTION = """
Computer Engineering Student @ UC San Diego
"""

PROJECTS = {
    "1. Data Cleaning & Transformation": "https://www.youtube.com/watch?v=wObV_hwu2QM",
    "2. Data Analysis": "https://example.com/project2",
    "3. Data Visualization": "https://example.com/project3",
    "4. Data Engineering/ Data Science": "https://example.com/project4",
}




st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.write("""
<div style="position: fixed; top: 0; right: 0; background-color: black; color: white; padding: 10px;">
    View on computer for best experience
</div>
""", unsafe_allow_html=True)



# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)


with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

    st.markdown(
    f"""
    <style>
        .stDownloadButton>button {{
            background-color: black;
            color: white;
            border: 2px solid white;
            border-radius: 5px;
            padding: 8px 16px;
            cursor: pointer;
        }}
        .stDownloadButton>button:hover {{
            background-color: #222;
        }}
    </style>
    """
    , unsafe_allow_html=True
)


# --- LOAD CSS, PDF & PROFILE PIC ---
dark_mode = st.sidebar.checkbox('Dark mode', False)
css_file = current_dir / "styles" / ("dark.css" if dark_mode else "main.css")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


def add_bg_from_local(light_image_file, dark_image_file, dark_mode=False):
    if dark_mode:
        image_file = dark_image_file
    else:
        image_file = light_image_file

    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
            backdrop-filter: blur(10px);
        }}
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            backdrop-filter: blur(2px); /* Adjust the blur radius as needed */
            z-index: -1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('bg.png', 'dark_bg.png', dark_mode)

with st.sidebar:
    
    
   choose = option_menu(
                        "", 
                        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Blog", "Resume", "Contact"],
                         icons=['person fill','clock history', 'tools', 'book half', 'clipboard', 'image', 'paperclip', 'envelope'],
                         default_index=0,
                         styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    
   st.markdown("""

    <h2> <img src="https://cdn.dribbble.com/users/891352/screenshots/7105199/media/5238cf20f0301e51fea9cad8912b9ea3.gif" width="50px" /> &nbsp;Socials:</h2>


  <a href="https://www.linkedin.com/in/madhavbaghla">
    <img src="https://i.pinimg.com/originals/de/b4/6f/deb46f02a59e3b3a2aa58fac16290d63.gif" alt="LinkedIn" height="35" width="35">
  </a>


  <a href="https://twitter.com/OnlyMB04">
    <img src="https://vectorseek.com/wp-content/uploads/2023/07/Twitter-X-Logo-Vector-01-2.jpg" alt="Twitter" height="35" width="35">
  </a>

   <a href="https://discord.com/users/735389282184986744">
    <img src="https://cdn.dribbble.com/users/5242374/screenshots/16641455/media/0a74ea6b1d505b316ced8be139175fc3.gif" alt="Discord" height="35" width="35">
  </a>

  <a href="mailto:madhavbaghla4@gmail.com">
    <img src="https://cdn.dribbble.com/users/4874/screenshots/3074660/gmaildribbble.gif" alt="Gmail" height="35" width="35">
  </a>

  <a href="https://github.com/MadhavBaghla2004">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6H3k5o1hr4luxqjzGWsJEKODInCZKG2Q_Fg&usqp=CAU" alt="Github" height="35" width="35">
  </a>
  

""",True)
# --- ABOUT ME ---
if choose == "About Me":
  st.write('\n')
  st.subheader("About Me")
  st.markdown(
    """
    <blockquote style="background-color: black; color: white; padding: 10px;">
🤔 Interested in Data Science and Machine Learning <br>
🎓 Studying Computer Engineering @ UC San Diego <br>
💼 Open to Internships <br>
🌱 Learning more about Cloud Architecture, Systems Design and AI <br>
🌍 I can speak English, Hindi and French <br>

</blockquote>
""",unsafe_allow_html=True
)

elif choose == "Experience":
# --- WORK HISTORY ---
 st.write('\n')
 st.subheader("Work History")
 st.markdown("""### GitHub Statistics

| <a href="https://github.com/MadhavBaghla2004/github-readme-stats"><img align="center" src="https://github-readme-stats.vercel.app/api?username=MadhavBaghla2004&include_all_commits=true&count_private=true&show_icons=true&theme=radical" alt="Madhav's github stats" /></a> | <a href="https://github.com/MadhavBaghla2004/github-readme-stats"><img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MadhavBaghla2004&layout=compact&text_color=daf7dc&bg_color=151515" /></a> |
| ------------- | ------------- |
 """,True) 

elif choose == "Projects":
 st.write('\n')
 st.header("Projects :")
 for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

elif choose == "Technical Skills":
   st.write('\n')
   st.header("Tech Stack")
   st.markdown(
    """


- <img src="https://img.shields.io/badge/Programming%20Languages :-adff2f?style=flat&logoColor=white">&nbsp;
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/-Python-007ACC?style=flat&logo=python&logoColor=FFFFFF"></a>
  <a href="https://www.java.com/en/"><img src="http://img.shields.io/badge/-Java-F89820?style=flat&logo=openjdk&logoColor=white"></a>
  <a href="https://www.r-project.org/"> <img src="https://img.shields.io/badge/-R-00008b?style=flat&logo=R&logoColor=white"></a>
  
  
- <img src="https://img.shields.io/badge/Database%20:-adff2f?style=flat&logoColor=white"> &nbsp;
  <a href="https://www.mongodb.com"><img src="https://img.shields.io/badge/-MongoDB-4DB33D?style=flat&logo=mongodb&logoColor=FFFFFF"></a>
  <a href="https://www.mysql.com"><img src="https://img.shields.io/badge/-MySQL-66cdaa?style=flat&logo=mysql&logoColor=blue"></a>
  
- <img src="https://img.shields.io/badge/Tools And%20Technologies :-adff2f?style=flat&logoColor=white">  &nbsp; &nbsp;
  <a href="https://git-scm.com"><img src="http://img.shields.io/badge/-Git-F1502F?style=flat&logo=git&logoColor=FFFFFF"></a>
  <a href="https://github.com"><img src="http://img.shields.io/badge/-Github-000000?style=flat&logo=github&logoColor=FFFFFF"></a>
  <a href="https://www.markdownguide.org"><img src="http://img.shields.io/badge/-Markdown-ff0000?style=flat&logo=markdown&logoColor=FFFFFF"></a>

  
- <img src="https://img.shields.io/badge/IDEs %20:-adff2f?style=flat&logoColor=white">  &nbsp;
   <a href="https://code.visualstudio.com"><img src="http://img.shields.io/badge/-Visual%20Studio%20Code-1e90ff?style=flat&logo=visual-studio-code&logoColor=FFFFFF"></a>
   <a href="https://posit.co/products/open-source/rstudio/"><img src="http://img.shields.io/badge/-RStudio-4169e1?style=flat&logo=rstudio&logoColor=FFFFFF"></a>
   <a href="https://www.jetbrains.com/pycharm/"><img src="http://img.shields.io/badge/-PyCharm-ff1493?style=flat&logo=PyCharm&logoColor=FFFFFF"></a>
   <a href="https://www.jetbrains.com/idea/"><img src="http://img.shields.io/badge/-IntelliJ -ff69b4?style=flat&logo=intellij-idea&logoColor=FFFFFF"></a>

- <img src="https://img.shields.io/badge/Data Analysis %20 And Visualisation Tools :-adff2f?style=flat&logoColor=white">  &nbsp;
  <a href="https://powerbi.microsoft.com/en-in/"><img src="https://img.shields.io/badge/Power_BI-9932cc?style=flat&logo=powerbi&logoColor=white"></a>
  <a href="https://www.microsoft.com/en-in/microsoft-365/excel"><img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=flat&logo=microsoft-excel&logoColor=white"></a>

  
<h3> </h3>
""", True
)





   



