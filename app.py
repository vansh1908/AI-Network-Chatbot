import streamlit as st
import pandas as pd
from chatbot import process_query

st.set_page_config(
    page_title="Net Minds",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Net Minds")
st.subheader("AI-Powered Network Intelligence System")

with st.sidebar:
    st.markdown("### Example Queries")
    st.markdown("""
    - Count Cisco devices  
    - Show all POPs in Delhi  
    - List Juniper equipment  
    - How many routers are active?
    """)

query = st.text_input(
    "Ask your question",
    placeholder="e.g. Count all D-Link devices in Mumbai"
)

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a query")
    else:
        with st.spinner("Analyzing..."):
            try:
                result = process_query(query)

                if isinstance(result, str):
                    st.info(result)
                else:
                    df = pd.DataFrame(result)
                    st.success("Result")
                    st.dataframe(df, use_container_width=True)

            except Exception as e:
                st.error(str(e))