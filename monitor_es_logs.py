import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import os
import zipfile
import time
import shutil

# embed streamlit docs in a streamlit app

st.set_page_config(
    page_title="Monitoring Elasticsearch performance logs",
    page_icon="--",
    layout='wide'
)
st.title("Monitoring ES Logs")
st.sidebar.success("Select a page above.")

# Uploading the api_diagnostics zip file
zip_file = st.file_uploader("Choose a ZIP file", type="zip")

# If a ZIP file was uploaded, extract its contents into a new directory
if zip_file is not None:
    # Create a new directory to store the extracted files
    zip_file_name = zip_file.name
    zip_file_dir = os.path.join("/tmp", os.path.splitext(zip_file_name)[0])
    os.makedirs(zip_file_dir, exist_ok=True)

    with zipfile.ZipFile(zip_file) as zip_ref:
        zip_ref.extractall(zip_file_dir)

    # List the files in the extracted directory
    files = os.listdir(zip_file_dir)
    st.success("Files extracted successfully. You can continue to use the application!")
    # Schedule folder deletion after 2 days
    # expiry_time = time.time() + 2 * 24 * 60 * 60 # 2 days in seconds
    expiry_time = time.time() + 2 * 60 * 60 # 2 hours in seconds

    st.write(f"This folder will be deleted on {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expiry_time))}.")

# Delete the extracted folder if it has expired
expiry_time = st.experimental_get_query_params().get("expiry")
if expiry_time is not None and time.time() > float(expiry_time[0]):
    shutil.rmtree(zip_file_dir, ignore_errors=True)
    st.write(f"Deleted folder {zip_file_dir}.")


st.subheader("Important URLs to study:")
st.markdown('<a href="https://www.elastic.co/blog/managing-and-troubleshooting-elasticsearch-memory" target="_self">Managing and Troubleshooting ES Memory</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/blog/a-heap-of-trouble" target="_self">A heap of trouble</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#heap-sizing" target="_self">Heap Sizing and swapping</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/size-your-shards.html" target="_self">Sizing your shards</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/cluster-stats.html" target="_self">Cluster Stats</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/cluster-nodes-stats.html" target="_self">Cluster Node Stats</a>', unsafe_allow_html=True)

