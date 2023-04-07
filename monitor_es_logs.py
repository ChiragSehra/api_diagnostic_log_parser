import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app

st.set_page_config(
    page_title="Monitoring Elasticsearch performance logs",
    page_icon="--",
    layout='wide'
)
st.title("Monitoring ES Logs")
st.sidebar.success("Select a page above.")
st.subheader("Important URLs to study:")
st.markdown('<a href="https://www.elastic.co/blog/managing-and-troubleshooting-elasticsearch-memory" target="_self">Managing and Troubleshooting ES Memory</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/blog/a-heap-of-trouble" target="_self">A heap of trouble</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#heap-sizing" target="_self">Heap Sizing and swapping</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/size-your-shards.html" target="_self">Sizing your shards</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/cluster-stats.html" target="_self">Cluster Stats</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/cluster-nodes-stats.html" target="_self">Cluster Node Stats</a>', unsafe_allow_html=True)

