import streamlit as st
import pandas as pd
from common_fns import aggrid_interactive_table
import json
import datetime
import os
import zipfile

def load_data(path):
    data = pd.read_json(path)
    return data

st.title("Compare API Diagnostic logs")

col1, col2 = st.columns(2)
zip_file_1 = col1.file_uploader("Choose a ZIP file 1", type="zip")
zip_file_2 = col2.file_uploader("Choose a ZIP file 2", type="zip")


if zip_file_1 is not None and zip_file_2 is not None:

    zip_file_name_1 = zip_file_1.name
    zip_file_name_2 = zip_file_2.name
    ZIP_FILE_1 = zip_file_name_1
    ZIP_FILE_2 = zip_file_name_2
    
    zip_file_1_dir = os.path.join("/tmp", os.path.splitext(zip_file_name_1)[0])
    zip_file_2_dir = os.path.join("/tmp", os.path.splitext(zip_file_name_2)[0])
    os.makedirs(zip_file_1_dir, exist_ok=True)
    os.makedirs(zip_file_2_dir, exist_ok=True)

    with zipfile.ZipFile(zip_file_1) as zip_ref_1:
        zip_ref_1.extractall(zip_file_1_dir)
        
    with zipfile.ZipFile(zip_file_2) as zip_ref_2:
        zip_ref_2.extractall(zip_file_2_dir)
        
    
    # List the files in the extracted directory
    files_1 = os.listdir(zip_file_1_dir)
    files_2 = os.listdir(zip_file_2_dir)
    
    st.success("Files extracted successfully. You can continue to use the application!")
    st.session_state['ZIP_FILE_1'] = ZIP_FILE_1
    st.session_state['ZIP_FILE_2'] = ZIP_FILE_2
    
    # Cluster Stats
    if 'ZIP_FILE_1' in st.session_state:
        ZIP_FILE_1 = st.session_state['ZIP_FILE_1']
        with open(f'/tmp/{ZIP_FILE_1.split(".")[0]}/{ZIP_FILE_1.split(".")[0]}/cluster_health.json', 'r') as f:
            data = json.load(f)

        df_1 = pd.json_normalize(data)
    
    if 'ZIP_FILE_2' in st.session_state:
        ZIP_FILE_2 = st.session_state['ZIP_FILE_2']    
        with open(f'/tmp/{ZIP_FILE_2.split(".")[0]}/{ZIP_FILE_2.split(".")[0]}/cluster_health.json', 'r') as f:
            data = json.load(f)

        df_2 = pd.json_normalize(data)
        
    # selection1 = aggrid_interactive_table(df=df_1)
    # selection2 = aggrid_interactive_table(df=df_2)
    st.subheader("Node Information")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.metric("Total Nodes", df_2['number_of_nodes'], delta=float(df_2['number_of_nodes'])-float(df_1['number_of_nodes']))
    col2.metric("Data Nodes", df_2['number_of_data_nodes'], delta=float(df_2['number_of_data_nodes'])-float(df_1['number_of_data_nodes']))
    col3.metric("Relocating Shards", df_2['relocating_shards'], delta=float(df_2['relocating_shards'])-float(df_1['relocating_shards']))
    col4.metric("Total Initializing Shards", df_2['initializing_shards'], delta=float(df_2['initializing_shards'])-float(df_1['initializing_shards']))
    col5.metric("Total Unassigned Shards", df_2['unassigned_shards'], delta=float(df_2['unassigned_shards'])-float(df_1['unassigned_shards']))
    col6.metric("Active Shard Percent", round(df_2['active_shards_percent_as_number'],2), delta=round(float(df_2['active_shards_percent_as_number'])-float(df_1['active_shards_percent_as_number']),2))
    col7.metric("Total Pending Tasks", df_2['number_of_pending_tasks'], delta=float(df_2['number_of_pending_tasks'])-float(df_1['number_of_pending_tasks']))
        
    with open(f'/tmp/{ZIP_FILE_1.split(".")[0]}/{ZIP_FILE_1.split(".")[0]}/cluster_stats.json', 'r') as f:
        stats_cluster_1 = json.load(f)
    cluster_stats_1 = pd.json_normalize(stats_cluster_1)
    
    with open(f'/tmp/{ZIP_FILE_2.split(".")[0]}/{ZIP_FILE_2.split(".")[0]}/cluster_stats.json', 'r') as f:
        stats_cluster_2 = json.load(f)
    cluster_stats_2 = pd.json_normalize(stats_cluster_1)
    
    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    
    
    st.subheader("Index Stats")
    co1, co2, co3, co4, co5, = st.columns(5)
    co1.metric("Index Count", cluster_stats_2['indices.count'], delta=float(cluster_stats_2['indices.count']) - float(cluster_stats_1['indices.count']))
    co2.metric("Total Primary Shards", cluster_stats_2['indices.shards.primaries'], delta=float(cluster_stats_2['indices.shards.primaries']) - float(cluster_stats_1['indices.shards.primaries']))
    co3.metric("Total Replica Shards", int(cluster_stats_2['indices.shards.primaries']*cluster_stats_2['indices.shards.replication']),delta=float(int(cluster_stats_2['indices.shards.primaries']*cluster_stats_2['indices.shards.replication']))-float(int(cluster_stats_1['indices.shards.primaries']*cluster_stats_1['indices.shards.replication'])))
    co4.metric("Total Documents", cluster_stats_2['indices.docs.count'], delta=float(cluster_stats_2['indices.docs.count']) - float(cluster_stats_1['indices.docs.count']))
    co5.metric("Total Size of all Shards (GB)", round(cluster_stats_2['indices.store.size_in_bytes']/9.313225746154785*1e-10,2), delta=float(round(cluster_stats_2['indices.store.size_in_bytes']/9.313225746154785*1e-10,2)) - float(round(cluster_stats_1['indices.store.size_in_bytes']/9.313225746154785*1e-10,2)))


    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    
    
    st.subheader("Memory Information")
    co6, co7, co8, co9, co10  = st.columns(5)
    co6.metric("Available processors for JVM", cluster_stats_2['nodes.os.available_processors'], delta=float(cluster_stats_2['nodes.os.available_processors']) - float(cluster_stats_1['nodes.os.available_processors']))
    co7.metric("Total Physical Memory", round(cluster_stats_2['nodes.os.mem.total_in_bytes']/9.313225746154785*1e-10,2), delta=float(cluster_stats_2['nodes.os.mem.total_in_bytes']/9.313225746154785*1e-10) - float(cluster_stats_1['nodes.os.mem.total_in_bytes']/9.313225746154785*1e-10), help="Total amount of physical memory across all selected nodes in GB")
    co8.metric("Total Free Physical Memory (GB)", round(cluster_stats_2['nodes.os.mem.free_in_bytes']/9.313225746154785*1e-10,2), delta=float(cluster_stats_2['nodes.os.mem.free_in_bytes']/9.313225746154785*1e-10) - float(cluster_stats_1['nodes.os.mem.free_in_bytes']/9.313225746154785*1e-10), help="Amount of free physical memory across all selected nodes in GB")
    co9.metric("Total Used Physical Memory (GB)", round(cluster_stats_2['nodes.os.mem.used_in_bytes']/9.313225746154785*1e-10,2), delta=float(cluster_stats_2['nodes.os.mem.used_in_bytes']/9.313225746154785*1e-10) - float(cluster_stats_1['nodes.os.mem.used_in_bytes']/9.313225746154785*1e-10), help="Amount of physical memory in use across all selected nodes")
    co10.metric("Max open file descriptors", cluster_stats_2['nodes.process.open_file_descriptors.max'], delta=float(cluster_stats_2['nodes.process.open_file_descriptors.max']) - float(cluster_stats_1['nodes.process.open_file_descriptors.max']), help="Maximum number of concurrently open file descriptors allowed across all selected nodes")
        
    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
        
    st.subheader("JVM Information")
    c1, c2, c3= st.columns(3)
    c1.metric("Used JVM Memory (GB)", round(cluster_stats_2['nodes.jvm.mem.heap_used_in_bytes']/9.313225746154785*1e-10,2), delta=float(cluster_stats_2['nodes.jvm.mem.heap_used_in_bytes']/9.313225746154785*1e-10) - float(cluster_stats_1['nodes.jvm.mem.heap_used_in_bytes']/9.313225746154785*1e-10),help="Memory currently in use by the heap across all selected nodes")
    c2.metric("Max JVM Memory (GB)", round(cluster_stats_2['nodes.jvm.mem.heap_max_in_bytes']/9.313225746154785*1e-10,2), delta=float(cluster_stats_2['nodes.jvm.mem.heap_max_in_bytes']) - float(cluster_stats_1['nodes.jvm.mem.heap_max_in_bytes']),help="Maximum amount of memory, in bytes, available for use by the heap across all selected nodes")
    c3.metric("Total Active Threads", cluster_stats_2['nodes.jvm.threads'], delta=float(cluster_stats_2['nodes.jvm.threads']/9.313225746154785*1e-10) - float(cluster_stats_1['nodes.jvm.threads']/9.313225746154785*1e-10),help="Number of active threads in use by JVM across all selected nodes")
        
        
    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
# else:
