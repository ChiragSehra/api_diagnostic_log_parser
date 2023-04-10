import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import os
import zipfile

# embed streamlit docs in a streamlit app
# ZIP_FILE = "api-diagnostics-20230404-101458.zip"
st.set_page_config(
    page_title="Monitoring Elasticsearch performance logs",
    page_icon="--",
    layout='wide'
)
st.title("Monitoring ES Logs")
st.sidebar.success("Select a page above.")

# Uploading the api_diagnostics zip file
zip_file = st.file_uploader("Choose a ZIP file", type="zip")

if zip_file is not None:
    # Create a new directory to store the extracted files

    zip_file_name = zip_file.name
    ZIP_FILE = zip_file_name
    zip_file_dir = os.path.join("/tmp", os.path.splitext(zip_file_name)[0])
    os.makedirs(zip_file_dir, exist_ok=True)

    with zipfile.ZipFile(zip_file) as zip_ref:
        zip_ref.extractall(zip_file_dir)

    # List the files in the extracted directory
    files = os.listdir(zip_file_dir)
    st.success("Files extracted successfully. You can continue to use the application!")
    st.session_state['ZIP_FILE'] = ZIP_FILE




st.subheader("Important URLs to study:")
st.markdown('<a href="https://www.elastic.co/blog/managing-and-troubleshooting-elasticsearch-memory" target="_self">Managing and Troubleshooting ES Memory</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/blog/a-heap-of-trouble" target="_self">A heap of trouble</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#heap-sizing" target="_self">Heap Sizing and swapping</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/size-your-shards.html" target="_self">Sizing your shards</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/cluster-stats.html" target="_self">Cluster Stats</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/cluster-nodes-stats.html" target="_self">Cluster Node Stats</a>', unsafe_allow_html=True)

