import streamlit as st
import os

st.set_page_config(

page_title="Chloe Julia S. Geonzon | Portfolio",

page_icon="👋",

layout="wide",

)
st.sidebar.image(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "assets",
    "Geonzon_pic.jpg"  
    ))
st.sidebar.markdown("Name: Chloe Julia S. Geonzon")
st.sidebar.markdown("Section: F2")
st.sidebar.markdown("Program & Year: Bachelor of Science in Computer Science - 3")


col1, col2 = st.columns(2)
with col1:
    st.title("Chloe Julia S. Geonzon")
    st.write("3rd Year BS Computer Science, Section F2")
    st.write(">*Remember there is always grass to touch, not only your computer screen*")
    st.divider()
    st.subheader("Biography")
    st.write("Currently a 3rd year Computer Science in Cebu Institute of Technology-University who is exploring the different advancements and progressions of technology and AI. I aspire to be someone who will dig deeper into the world of Data Analysis and Science, Artificial Intelligence (AI), Game Development, and Web Development.")
    st.divider()

with col2:
    st.image(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "assets",
    "Geonzon_pic.jpg"  
    ))
tab_Overview, tab_Hobbies, tab_skills, tab_repositories = st.tabs(["Overview", "Hobbies", "Skills", "Repositories"])

with tab_Overview:
    st.subheader("Background & Education Journey")
    st.write("I am a Waraynon, but grew up with speaking English, who was born and raised in Tacloban City, Leyte. Throughout my whole childhood, I loved playing video games, dancing, and making art. But my early experiences are very far from how I got into the field I am today. I got into my field after discovering how to gain a deeper knowledge of everything that happens behind the screens of a computer. With that, I am now standing here today, as someone who has learned a lot, but is still continuously learning the neverending advancements of tehcnology.💻☝🏼")
    st.write("")
    st.write("I studied in St. Therese Educational Foundation of Tacloban Inc., (STEFTI)🙏 throughout my whole elementary journey—I was just a child who was just enjoying her childhood being a performer while learning the basics the school fed me with.📚🧑‍🩰 I started high school in Eastern Visayas State University(EVSU) with the vow to step out of my bubble and be something greater.💪 I've been an honor student from the start until the end of my highschool journey and graduated with high honors.🥈 And now, I am a college student at Cebu Institute of Technology, and the main highlights of the journey I have been through so far in this school is discovering every framework and fundamentals of development for everything we see today in our screens.😝☝🏼💻")
    st.divider()
    st.subheader("🎬Key Milestones:")
    st.write("● **2025**- Developed a POS app using Java")
    st.write("● **2026**- Developed a 2D game using JavaFX and JavaFXML")
    st.write('<p style="margin-left: 24px;">- Created a mobile application using Kotlin</p>', 
        unsafe_allow_html=True)
    st.write('<p style="margin-left: 24px;">- Developed a 2D pixelated game called "Pinoy Party" and became one of the top 10 finalists in the DOST:NEXT LEVEL competition and given the opportunity to showcase our game in IMAGINATION CONVENTION 2026</p>', 
            unsafe_allow_html=True)
    

    st.write('<p style="margin-left: 24px;">- Developed a 3D game called "PARA PO: Mangga Dyip Simulator</p>', 
            unsafe_allow_html=True)
    st.write('<p style="margin-left: 24px;">- Developed an app using Python-Django</p>', 
                unsafe_allow_html=True)
    st.write('<p style="margin-left: 24px;">- Developed a Streamlit app</p>', 
                    unsafe_allow_html=True)


with tab_Hobbies:
    st.subheader("Non-Technical Hobbies")
    col1, col2, col3 = st.columns(3, border = True)
    with col1:
        st.markdown("**Drawing**", text_alignment="center")
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "Drawings.jpg"  
            ))
        st.markdown("*Follow me @moonjulya._*", text_alignment="center")

    with col2:
        st.markdown("**Reading**", text_alignment="center")
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "Books.jpg"  
            ))
        st.markdown("*I own a lot of books but I also have a lot of pending*", text_alignment="center")

    with col3:
        st.markdown("**Writing**", text_alignment="center")
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "substack1.png"  
            ))
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "substack2.png"  
            ))
    
    col4, col5= st.columns(2, border=True)
    with col4:
        st.markdown("**Dancing**", text_alignment="center")
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "dancing.jpeg"  
            ),width=400)
    with col5:
        st.markdown("**Playing video games**", text_alignment="center")
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "gaming.jpg"  
            ))
        st.markdown("*A minecraft nerd*", text_alignment="center")
    st.divider()

    st.subheader("Technical Hobbies")
    st.markdown("● **Code and Programming**")
    st.image(os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "assets",
                "programming.jpg"  
                ), width=400)

with tab_skills:
    st.subheader("🎨 Digital Art & Asset Creation:")
    
    _, col1, col2, _, _ = st.columns([0.05, 0.28, 0.28, 0.5, 0.5], gap="small")

    base_dir = os.path.dirname(os.path.abspath(__file__))

    with col1:
        st.image(os.path.join(base_dir, "assets", "ibis.png"), width=100)
        st.markdown("Ibis Paint")

    with col2:
        st.image(os.path.join(base_dir, "assets", "adobe.png"), width=100)
        st.markdown("Adobe Fresco")
            
    st.subheader("💻 Technical")
    st.code("""Core Technologies:
    print('Python, C#, C, Django, Java, MySQL/SQLite, PostgreSQL, GDScript')""", language="python")

    st.code("""Web-Based Technologies:
    print('HTML, CSS, JavaScript, Tailwind')""", language="python")

    st.subheader("🫟 UI/UX & Prototyping")
    _, col3, col4, _, _ = st.columns([0.05, 0.28, 0.3, 0.5, 0.5], gap="small")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    with col3:
            st.image(os.path.join(base_dir, "assets", "figma.avif"), width=100)
            st.markdown("Figma")
    
    with col4:
            st.image(os.path.join(base_dir, "assets", "canva.png"), width=100)
            st.markdown("Canva")


with tab_repositories:
     st.subheader("Capstone Projects")
