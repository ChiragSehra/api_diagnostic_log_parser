import streamlit as st
import pandas as pd
from common_fns import aggrid_interactive_table
import json
import datetime

def load_data(path):
    data = pd.read_json(path)
    return data

st.title("Node Allocation")
if 'ZIP_FILE' in st.session_state:
    ZIP_FILE = st.session_state['ZIP_FILE']
    st.subheader("Node Allocation")
    
    
    with open(f'/tmp/{ZIP_FILE.split(".")[0]}/{ZIP_FILE.split(".")[0]}/allocation.json','r') as f:
        allocate = json.load(f)
    allocation = pd.json_normalize(allocate)
    
    df = allocation[['node','disk.percent', 'shards', 'disk.used', 'disk.avail','disk.total']]
    selection2 = aggrid_interactive_table(df=df)
    
else:
    st.error("Please upload zip file to continue!")