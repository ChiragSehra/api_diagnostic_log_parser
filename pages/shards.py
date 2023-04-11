import streamlit as st
import pandas as pd

from common_fns import aggrid_interactive_table

@st.cache_data
def load_data(path):
    data = pd.read_json(path)
    return data
st.title("Shard utilisation")

if 'ZIP_FILE' in st.session_state:
    ZIP_FILE = st.session_state['ZIP_FILE']
    df = load_data(path=f'/tmp/{ZIP_FILE.split(".")[0]}/{ZIP_FILE.split(".")[0]}/shards.json')
    
    co1, co2= st.columns(2)
    
    
    
    # Unassigned Indexes
    unassigned_indexes=df[df['state']=='UNASSIGNED']
    if unassigned_indexes.empty:
        unassigned_shards = 0

        # st.metric(label="UNASSIGNED indexes", value=unassigned_shards)
        co1.metric(label="UNASSIGNED indexes", value=unassigned_shards)
    else:
        # st.metric(label="UNASSIGNED indexes", value=unassigned_indexes.count())
        co1.metric(label="UNASSIGNED indexes", value=unassigned_indexes.count()[0])

    # Relocating Indexes
    relocating_indexes=df[df['state']=='RELOCATING']
    if relocating_indexes.empty:
        relocating_shards = 0

        # st.metric(label="RELOCATING indexes", value=relocating_shards)
        co2.metric(label="RELOCATING indexes", value=relocating_shards)
    else:
        # st.metric(label="RELOCATING indexes", value=relocating_indexes.count()[0])
        co2.metric(label="RELOCATING indexes", value=relocating_indexes.count()[0])

    body="""
        - State of index could be 
            - UNASSIGNED: The shard is not currently assigned to any node in the cluster.
            - INITIALIZING: The shard is in the process of initializing on a node in the cluster.
            - RELOCATING: The shard is being moved from one node to another in the cluster.
            - STARTED: The shard is available and actively accepting requests.
            - POST_RECOVERY: The shard has completed recovery and is in the process of post-recovery operations.
            - CLOSED: The shard has been closed and is no longer accepting requests.
    """

    st.caption(body, unsafe_allow_html=False, help=False)

    st.subheader("Shards Information")

    # Display ag-grid with filtering option
    selection = aggrid_interactive_table(df=df)

    st.subheader("Indexes with small amount of documents - WORTH DELETING")

    THRESHOLD = 150
    docs_150 = df[df['docs']<THRESHOLD].sort_values(by='docs')
    docs_150=docs_150[~docs_150['index'].str.startswith('.')]
    selection2 = aggrid_interactive_table(df=docs_150)

else:
    st.error("Please upload zip file to continue!")


