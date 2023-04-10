import streamlit as st
import pandas as pd
from common_fns import aggrid_interactive_table
import json
import datetime

st.title("Cluster Stats")

if 'ZIP_FILE' in st.session_state:
    ZIP_FILE = st.session_state['ZIP_FILE']
    with open(f'/tmp/{ZIP_FILE.split(".")[0]}/{ZIP_FILE.split(".")[0]}/cluster_health.json', 'r') as f:
        data = json.load(f)

    df = pd.json_normalize(data)

    st.subheader("Node Information")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.metric("Total Nodes", df['number_of_nodes'])
    col2.metric("Data Nodes", df['number_of_data_nodes'])
    col3.metric("Relocating Shards", df['relocating_shards'])
    col4.metric("Total Initializing Shards", df['initializing_shards'])
    col5.metric("Total Unassigned Shards", df['unassigned_shards'])
    col6.metric("Active Shard Percent", round(df['active_shards_percent_as_number'],2))
    col7.metric("Total Pending Tasks", df['number_of_pending_tasks'])




    with open(f'/tmp/{ZIP_FILE.split(".")[0]}/{ZIP_FILE.split(".")[0]}/cluster_stats.json', 'r') as f:
        stats_cluster = json.load(f)
    cluster_stats = pd.json_normalize(stats_cluster)

    st.subheader("Index Stats")
    co1, co2, co3, co4, co5, = st.columns(5)
    co1.metric("Index Count", cluster_stats['indices.count'])
    co2.metric("Total Primary Shards", cluster_stats['indices.shards.primaries'])
    co3.metric("Total Replica Shards", int(cluster_stats['indices.shards.primaries']*cluster_stats['indices.shards.replication']))
    co4.metric("Total Documents", cluster_stats['indices.docs.count'])
    co5.metric("Total Size of all Shards (GB)", round(cluster_stats['indices.store.size_in_bytes']/9.313225746154785*1e-10,2))

    st.subheader("Memory Information")
    co6, co7, co8, co9, co10  = st.columns(5)
    co6.metric("Available processors for JVM", cluster_stats['nodes.os.available_processors'])
    co7.metric("Total Physical Memory", round(cluster_stats['nodes.os.mem.total_in_bytes']/9.313225746154785*1e-10,2), help="Total amount of physical memory across all selected nodes in GB")
    co8.metric("Total Free Physical Memory (GB)", round(cluster_stats['nodes.os.mem.free_in_bytes']/9.313225746154785*1e-10,2), help="Amount of free physical memory across all selected nodes in GB")
    co9.metric("Total Used Physical Memory (GB)", round(cluster_stats['nodes.os.mem.used_in_bytes']/9.313225746154785*1e-10,2), help="Amount of physical memory in use across all selected nodes")
    co10.metric("Max open file descriptors", cluster_stats['nodes.process.open_file_descriptors.max'], help="Maximum number of concurrently open file descriptors allowed across all selected nodes")


    # JVM INFORMATION
    st.subheader("JVM Information")
    c1, c2, c3= st.columns(3)
    c1.metric("Used JVM Memory (GB)", round(cluster_stats['nodes.jvm.mem.heap_used_in_bytes']/9.313225746154785*1e-10,2),help="Memory currently in use by the heap across all selected nodes")
    c2.metric("Max JVM Memory (GB)", round(cluster_stats['nodes.jvm.mem.heap_max_in_bytes']/9.313225746154785*1e-10,2),help="Maximum amount of memory, in bytes, available for use by the heap across all selected nodes")
    c3.metric("Total Active Threads", cluster_stats['nodes.jvm.threads'],help="Number of active threads in use by JVM across all selected nodes")
        
        
        
        
        
    with open(f'/tmp/{ZIP_FILE.split(".")[0]}/{ZIP_FILE.split(".")[0]}/cluster_settings_defaults.json') as f:
        settings = json.load(f)
    cluster_settings = pd.json_normalize(settings)
    st.subheader("Cluster Setting Defaults")
    st.json(settings, expanded=False)

else:
    st.error("Please upload zip file to continue!")
    # st.experimental_refresh()
    
