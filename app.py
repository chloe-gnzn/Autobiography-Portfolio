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
    "Geonzon_sidebarPic.jpg"  
    ))
st.sidebar.markdown("**Name:** Chloe Julia S. Geonzon")
st.sidebar.markdown("**Section:** F2")
st.sidebar.markdown("**Program & Year:** Bachelor of Science in Computer Science - 3")
st.sidebar.divider()
st.sidebar.markdown("**CONTACT:**")
st.sidebar.link_button(
    "👩‍💻 LinkedIn",
    "https://www.linkedin.com/in/chloe-julia-geonzon-9b4266425/",
    use_container_width=True
)
st.sidebar.link_button(
    "✉️ Email",
    "mailto:your_email@gmail.com",
    use_container_width=True
)
st.sidebar.link_button(
    "👾 GitHub",
    "https://github.com/chloe-gnzn",
    use_container_width=True
)
st.sidebar.link_button(
    "👥 Facebook",
    "https://www.facebook.com/chleymi/",
    use_container_width=True
)


col1, col2 = st.columns(2)
with col1:
    st.title("Chloe Julia S. Geonzon")
    st.write("3rd Year BS Computer Science, Section F2")
    st.write(">*Remember there is always grass to touch, not only your computer screen — an aspiring Computer Science Explorer, specializing in Data Analysis, Web Development, Game Engineering, and Digital Assets*")
    st.divider()
    st.subheader("Biography")
    st.write("Currently a 3rd year Computer Science student in Cebu Institute of Technology-University who is exploring the different advancements and progressions of technology and AI. I aspire to be someone who will dig deeper into the world of Data Analysis and Science, Artificial Intelligence (AI), Game Development, and Web Development.")
    st.divider()

with col2:
    st.image(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "assets",
    "Geonzon_profile.png"  
    ))
tab_Overview, tab_Hobbies, tab_skills, tab_repositories = st.tabs(["🫧Overview", "🧃Hobbies", "🪄Skills", "💾Repositories"])

with tab_Overview:
    st.subheader("📓Background & Education Journey")
    st.write("Throughout my whole childhood, I loved playing video games, dancing, and making art. But my early experiences are very far from how I got into the field I am today. I got into my field after discovering how to gain a deeper knowledge of everything that happens behind the screens of a computer. With that, I am now standing here today, as someone who has learned a lot, but is still continuously learning the neverending advancements of tehcnology.💻☝🏼")
    st.write("")
    st.write("I studied in St. Therese Educational Foundation of Tacloban Inc., (STEFTI)🙏 throughout my whole elementary journey—I was just a child who was just enjoying her childhood being a performer while learning the basics the school fed me with.📚🧑‍🩰 I started high school in Eastern Visayas State University(EVSU) with the vow to step out of my bubble and be something greater.💪 I've been an honor student from the start until the end of my highschool journey and graduated with high honors.🥈 And now, I am a college student at Cebu Institute of Technology, and the main highlights of the journey I have been through so far in this school is discovering every framework and fundamentals of development for everything we see today in our screens.😝☝🏼💻")
    st.divider()
    st.subheader("🎬Key Milestones:")
    st.code("2025 - Developed a POS app using Java")
    st.code("""2026 - Developed a 2D game using JavaFX and JavaFXML
     - Created a mobile application using Kotlin
     - Developed a 2D pixelated game and became one of the top 10 finalists in the DOST:NEXT LEVEL competition and 
       given the opportunity to showcase our game in IMAGINATION CONVENTION 2026
     - Developed a 3D game 
     - Developed an app using Python-Django
     - Developed a Streamlit app""")



with tab_Hobbies:
    st.subheader("🌈Non-Technical Hobbies")
    col1, col2= st.columns(2, border = True)
    with col1:
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "drawingRow1.png"  
            ))
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "drawingRow2.png"  
            ))
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "drawingRow3.png"  
            ))
       
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("**DRAWING**", text_alignment="center")
        st.markdown("Drawing has been my creative sanctuary long before I ever typed my first line of code. From sketching childhood ideas to crafting digital illustrations using Adobe Fresco and IbisPaint, art allows me to visualize worlds and breathe life into original concepts.", text_alignment="right")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(">*Follow me @moonjulya._*", text_alignment="right")
         
    col3, col4 = st.columns(2, border=True)
    with col4:
        st.image(os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "assets",
                "reading.PNG"  
                ))

    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")   
        st.markdown("**READING**", text_alignment="center")
        st.markdown("Reading is one of my favorite escapes from the glow of computer monitors—though my ambition often outpaces my free time! I have a growing mountain of books on my shelves, accompanied by an ever-expanding 'To-Be-Read' backlog that I swear I'm going to finish one day. Whether diving into gripping fiction, worldbuilding lore, or fresh perspectives, collecting and reading books remains my quiet way to recharge and stay curious.", text_alignment="left")

    col5, col6 = st.columns(2, border=True)
    with col5:
        st.image(os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "assets",
                "dancing.jpg"  
                ))
    with col6:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("""**DANCING**""", text_alignment="center")
        st.markdown("Before debugging syntax, there was choreography. Dancing is the physical counterweight to my hours behind a monitor—a high-energy outlet rooted in musicality, discipline, and creative expression that keeps me grounded and active.", text_alignment="right")

    col7, col8 = st.columns(2, border=True)
    with col8:
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "gaming.jpg"  
            ))
    with col7:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")        
        st.write("")
        st.write("")
        st.markdown("**PLAYING VIDEO GAMES**", text_alignment="center")
        st.markdown("If there’s one constant in my life, it’s my love for gaming. I play for the pure thrill of it—the late-night sessions where 'just one more level' turns into hours, the satisfaction of unlocking tough achievements, and the magic of experiencing stories you can actually control. Gaming isn't just downtime for me; it’s an adventure I always look forward to returning to.", text_alignment="left")
        st.write(">*Minecraft is life tho*")

    st.divider()
    st.subheader("🌩️Technical Hobbies")
    col9, col10 = st.columns(2, border=True)
    with col9:
         st.image(os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "assets",
                "programming.jpg"  
                ))
    with col10:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("**CODE AND PROGRAMMING**", text_alignment="center")
        st.markdown("To me, programming is modern-day craftsmanship. It’s the thrill of untangling challenging logic, tracking down that elusive bug, and transforming raw code into seamless, functional applications. From full-stack web platforms to game systems, I love the process of turning clean logic into real-world software solutions.", text_alignment="right")

with tab_skills:
    st.subheader("🎨 Digital Art & Asset Creation")
    
    col1, col2, col3, col4, col5 = st.columns([0.28, 0.28, 0.3, 0.3, 0.3], gap="small", border=True)
         
    base_dir = os.path.dirname(os.path.abspath(__file__))

    with col1:
        st.image(os.path.join(base_dir, "assets", "ibis.png"), use_container_width=True)
        st.write("")
        st.markdown("Ibis Paint")
    with col2:
        st.image(os.path.join(base_dir, "assets", "adobe.png"),  use_container_width=True)
        st.write("")
        st.markdown("Adobe Fresco")

    with col3:
        st.image(os.path.join(base_dir, "assets", "blender.png"), use_container_width=True)
        st.write("")
        st.write("")
        st.markdown("Blender") 

    with col4:
        st.image(os.path.join(base_dir, "assets", "aseprite.png"), use_container_width=True)
        st.markdown("Aseprite") 
    with col5:
        st.image(os.path.join(base_dir, "assets", "resprite.png"), use_container_width=True)
        st.markdown("Resprite") 
        

    st.divider()
    st.subheader("💻 Technical")
    st.code("""Core Technologies:
    print('Python, C#, C, Django, Java, MySQL/SQLite, PostgreSQL, GDScript')""", language="python")

    st.code("""Web-Based Technologies:
    print('HTML, CSS, JavaScript, Tailwind')""", language="python")

    st.divider()
    st.subheader("🫟 UI/UX & Prototyping")
    col3, col4, _, _, _= st.columns([0.3, 0.3, 0.3, 0.3, 0.3], gap="small")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    with col3:
            with st.container(border=True):
                st.image(os.path.join(base_dir, "assets", "figma.avif"), use_container_width=True)
                st.markdown("Figma")
    
    with col4:
            with st.container(border=True):
                st.image(os.path.join(base_dir, "assets", "canva.png"), use_container_width=True)
                st.markdown("Canva")

    st.divider()
    st.subheader("🏫 Leadership Skills")
    with st.container(border=True):
        st.markdown("""🔴🔵**Google Developer Groups on Campus — CITU**🟢🟡""")
        st.write("- **Member Evaluator** *(2025-2026)*: Assessed and reviewed candidate applications, portfolios, and technical interests to identify engaged student builders for the community.")
        st.write("- **Chief of Finance** *(2026-2027)*: Directed the organization’s financial strategy, budget allocation, and fund management across large-scale technical events, workshops, and hackathons. Spearheaded transparent financial reporting, monitored operational expenditures, and optimized resource distribution to maximize event impact. Collaborated closely with executive leads, external partners, and sponsors to secure funding pipelines, ensure fiscal compliance, and maintain sustainable organizational growth.")

    with st.container(border=True):
            st.markdown("""🖤💛**Computer Students' Society (CSS)**""")
            st.write("- **Committee on Public Relations Asst. Head** *(2026-2027)*: Co-directed PR campaigns and digital outreach strategies, growing audience engagement and event participation across campus and regional communities.")
           
    
with tab_repositories:
    st.subheader("Personal Projects", text_alignment="center")
    st.markdown("*Turning passion into pixels, and logic into playable realities.*", text_alignment="center")

    col1, col2 = st.columns(2, border=True)
    with col1:
         st.markdown("**Pinoy Party**", text_alignment="center")
         st.image(os.path.join(
                         os.path.dirname(os.path.abspath(__file__)),
                         "assets",
                         "pinoy_party.png"  
                         ))
         st.markdown("**Role:** `Frontend Developer`")
         st.markdown("**Tools/Technologies Used:** `C#, GDScript, Godot Gaming Engine`")
         st.markdown("**Description:** Pinoy Party is a multiplayer `Godot 4` party game inspired by classic Filipino street games! Gather your friends, roll the dice on the virtual board, and compete in fast-paced minigames to see who will be crowned the ultimate champion.")
         st.page_link(
            "https://github.com/Zephyrdoestech/Pinoy-Party",
            label="View on GitHub",
            icon="🔗"
            ) 

    with col2:
        st.markdown("**PARA PO! : Mangga Dyip SImulator**", text_alignment="center")
        st.image(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "mangga_dyip.jpg"  
            ))
        st.markdown("**Role:** `3D-Asset Developer`")
        st.markdown("**Tools/Technologies Used:** `Godot Gaming Engine, Blender`")
        st.markdown("**Description:** `Mangga Jeep Corp.` is looking for a night shift conductor for the streets of SeaVu City! Work the late-night route, collect fares, meet passengers, and keep the ride moving until the last stop. What could go wrong?")
        st.write("")
        st.page_link(
            "https://b1nggb0ngg.itch.io/mangga-dyip-simulator",
            label="View on itch.io",
            icon="🔗"
            ) 
    
    st.divider()
    st.subheader("Capstone Projects", text_alignment="center")
    st.markdown("*Bridging theory and execution to build technology that matters.*", text_alignment="center")
    col3, col4 = st.columns(2, border=True)
    with col3:
             st.markdown("**Sari-Sari Smart**", text_alignment="center")
             st.image(os.path.join(
                             os.path.dirname(os.path.abspath(__file__)),
                             "assets",
                             "SSS-Login.png"  
                             ))
             st.image(os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "assets",
                            "SSS-POS.png"  
                            ))
             st.markdown("**Role:** `UI Designer and Lead Frontend Developer`")
             st.markdown("**Tools/Technologies Used:** `Java, Swing`")
             st.markdown("**Description:** The SariSariSmart streamlines daily operations by `automating` sales tracking, inventory management, customer loyalty programs, and financial analytics.")
             st.page_link(
                "https://github.com/irenguinita/SariSariSmart",
                label="View on GitHub",
                icon="🔗"
                ) 
    
    with col4:
            st.markdown("**Sir-Serato-Simulator**", text_alignment="center")
            st.image(os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "assets",
                "sir-serato--simulator.png"  
                ))
            st.markdown("**Role:** `Lead UI/Asset Developer, Sub Gameplay Programmer`")
            st.markdown("**Tools/Technologies Used:** `JavaFX, JavaFXML`")
            st.markdown("**Description:** `Sir Serator Simulator` is a high-stake arcade classroom management simulator game where you act as the iconic teacher, `Sir Jay Vince Serato`, proctoring a set of students that are taking your quizzes. Of course, being a teacher comes with its own set of problems. You must be vigilant in ensuring that your students do not attempt to cheat or else you will lose your patience and your sanity.")
            st.write("")
            st.page_link(
                "https://github.com/binggbongg/CSIT228-Capstone-Sir-Jay-Simulator",
                label="View on GitHub",
                icon="🔗"
                ) 
    
    st.divider()
    st.subheader("Other Projects", text_alignment="center")
    st.markdown('`print("Side quests, sandbox builds, and quick prototypes.")`', text_alignment="center")
    col5, col6 = st.columns(2, border=True)
    with col5:
            st.markdown("**MedFind**", text_alignment="center")
            st.image(os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "assets",
                            "MedFind.png"  
                            ))
            st.markdown("**Role:** `Full-Stack Developer`")
            st.markdown("**Tools/Technologies Used:** `HTML, CSS, JavaScript, Python, Django`")
            st.page_link(
                    "https://github.com/chloe-gnzn/MedFind",
                    label="View on GitHub",
                    icon="🔗"
                    ) 
    with col6:
            st.markdown("**Univents**", text_alignment="center")
            st.image(os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "assets",
                            "univents1.png"  
                            ))
            st.image(os.path.join(
                        os.path.dirname(os.path.abspath(__file__)),
                        "assets",
                        "univents2.png"  
                        ))
            st.markdown("**Role:** `Full-Stack Developer`")
            st.markdown("**Tools/Technologies Used:** ` HTML, CSS, JavaScript, PHP, MySQL`")
            st.markdown("**Description:** Univents is a Web-based centralized app for school organizations. This helps 'students' be able to stay-updated to the current events happening around the campus or events being held by school chapters and organizations. This allows them to RSVP, and stay updated on the events they have joined. For the 'organizers', this helps them promote their event more efficiently, and be able to track the number of students who have attended, were present, and were absent in the event.")
            st.page_link(
                    "https://github.com/irenguinita/univents",
                    label="View on GitHub",
                    icon="🔗"
                    ) 

    col7, col8 = st.columns(2, border=True)
    with col7:
   
            st.markdown("**G-Split**", text_alignment="center")
            st.image(os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "assets",
                "G-split.png"  
                ), use_container_width=True)
            st.markdown("**Description:** An `automated split-save QR wallet` for karenderia owners that instantly partitions incoming cash-ins and digital payments into designated expense jars, safeguarding operating capital from impulse spending.")
            st.write("")
            st.write("")
            st.write("")
        
    with col8:

                st.markdown("**SnappidySnap!**", text_alignment="center")
                st.image(os.path.join(
                                os.path.dirname(os.path.abspath(__file__)),
                                "assets",
                                "SnappidySnap.png"  
                                ))
                st.markdown("**Description:** Snappidy Snap is a `retro-inspired, browser-based digital photo booth.` It lets users select a custom frame, take a timed series of three webcam snapshots, decorate their strip with draggable and resizable emoji stickers, and watch their personalized strip come to life through an animated mechanical printer before downloading the finished keepsake.")