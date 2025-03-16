import streamlit as st

# st.markdown("""
# <h1 style='text-align: center; font-size: 2.3em; font-family: "Georgia", "Times New Roman", serif; color: #ECF0F1; letter-spacing: 2px; font-weight: bold; text-transform: uppercase; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.6);'>
#      Welcome to <span style='color:#F39C12; font-style: italic;'>CodeOptiAI</span>
# </h1>
# """, unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes typing {
    from { width: 0 }
    to { width: 20ch } /* Adjust ch based on your text length */
}

@keyframes blink {
    50% { border-color: transparent }
}

.scroll-title {
    width: 23ch;
    overflow: hidden;
    white-space: nowrap;
    border-right: .15em solid #F39C12;
    animation: typing 4s steps(25, end), blink .75s step-end infinite;
    color: #ECF0F1;
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 2.5em;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.6);
}

.scroll-title span {
    color: #F39C12;
    font-style: italic;
}
</style>

<div class="scroll-title">
    Welcome to <span>CodeOptiAI</span>
</div>
""", unsafe_allow_html=True)




st.markdown("""
### Your AI-powered Multi-Language Code Optimization Platform

**CodeOptiAI** helps developers to:
- Seamlessly optimize source code (Python, SQL, Scala, Java, R, Go, Bash, Rust) from GitHub repositories.
- Upload local code files across multiple languages for instant optimization.
- Paste raw code into a text area for fast AI-powered improvement suggestions.

---
""")

st.write("Click below to navigate")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Go to GitHub Repo Optimizer"):
        st.switch_page("pages/GitRepoOptimizer.py")
with col2:
    if st.button("⚙️ Go to Manual Code Optimizer"):
        st.switch_page("pages/ManualCodeOptimizer.py")
