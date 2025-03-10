import streamlit as st
import openai
from github import Github, GithubException
from streamlit_pyspark_optimizer import PySparkOptimizerLLMApp
import os



GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")                                                  

st.markdown("<h1 style='font-size: 2em;'>🔍 GitHub PySpark & SQL Code Optimizer</h1>", unsafe_allow_html=True)

file_type = st.radio("Select the type of file to optimize:", ("Python", "SQL"))

repo_url = st.text_input("Enter GitHub Repository URL (e.g., https://github.com/user/repo)")
if repo_url and file_type:
    repo_name = "/".join(repo_url.split("/")[-2:]).replace(".git", "")

    g = Github(GITHUB_TOKEN)
    
    try:
        repo = g.get_repo(repo_name)

        @st.cache_data
        def get_files(file_ext, path=""):
            files = {}
            contents = repo.get_contents(path)
            while contents:
                file_content = contents.pop(0)
                if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path))
                elif file_content.path.endswith(file_ext):
                    files[file_content.path] = file_content
            return files

        file_extension = ".py" if file_type == "Python" else ".sql"
        files = get_files(file_extension)

        if not files:
            st.warning(f"No {file_type} files were found in the repository.")
        else:
            file_list = list(files.keys())
            
            search_query = st.text_input(f"Search for a {file_type} file")
            st.text("or")
            filtered_files = [f for f in file_list if search_query.lower() in f.lower()] if search_query.strip()!="" else file_list
            selected_file = st.selectbox(f"Select a {file_type} file", filtered_files)

            if st.button("Submit") and selected_file:
                file_content = files[selected_file].decoded_content.decode("utf-8")

                st.write(f"📂 **Analyzing:** `{selected_file}`")

                with st.spinner("Processing..."):
                    suggestions = PySparkOptimizerLLMApp(file_content,file_type).run()

                st.markdown(f"{suggestions}")

                report_md = f"# Code Optimization Report\n\n**File:** `{selected_file}`\n\n{suggestions}"
                st.download_button("📥 Download Report", report_md, selected_file.replace(".", "_report.") + ".txt", "text/markdown")
    except GithubException:
        st.warning("Please provide a valid GitHub repository URL.")

if st.button("Clear"):
    st.session_state.clear()