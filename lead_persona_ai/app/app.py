import streamlit as st
import pandas as pd


#Title
st.set_page_config(page_title="Enriched Leads Viewer", layout='wide')
st.title("Enriched Leads Dashboard")
st.caption("View, search, and download enriched persona data for your LinkedIn leads.")

@st.cache_data
def load_data():
    return pd.read_csv("data/enriched_leads.csv")
        
df = load_data()

#Seach/Filter
with st.sidebar:
    st.header("Filter Leads")
    search_text = st.text_input("Search by Name, Company, Title, Industry")
    industry_filter = st.selectbox("Filter by Industry", options=["ALL"] + sorted(df["Industry"].dropna().unique().tolist()))
    st.markdown("---")
    st.caption("Use filters above and navigate leads below")

filtered_df = df.copy()

#Pagination State
if "lead_index" not in st.session_state:
    st.session_state.lead_index=0
elif st.session_state.lead_index >= len(filtered_df):
    st.session_state.lead_index = 0

if industry_filter != "ALL":
    filtered_df = filtered_df[filtered_df["Industry"] == industry_filter]

if search_text:
    search_text_lower = search_text.lower()
    filtered_df = filtered_df[filtered_df.apply(lambda row: search_text_lower in row.to_string().lower(), axis=1)]

#Show Table
st.subheader(f"Showing {len(filtered_df)} Enriched Leads")
st.dataframe(filtered_df, use_container_width = True)

#Navigation
def prev_lead():
    st.session_state.lead_index = max(st.session_state.lead_index - 1, 0)

def next_lead():
    st.session_state.lead_index = min(st.session_state.lead_index + 1, len(filtered_df) - 1)

#Header
st.markdown(f"**Total Leads (filtered):** {len(filtered_df)}")

#Detailed View
if len(filtered_df) > 0:
    lead = filtered_df.iloc[st.session_state.lead_index]

    st.markdown("Lead Details")
    st.markdown(f"{lead['Name']}** - *{lead['Job Title']} at {lead['Company']}*")
    st.markdown("[LinkedIn Profile]({lead['LinkedIn']})")
    st.markdown(f"Industry: {lead['Industry']}")

    tab1, tab2, tab3 = st.tabs(["Persona", "Pitch Angle", "Icebreaker"])
    with tab1:
        st.write(lead["Persona"])
    with tab2:
        st.write(lead["Pitch Angle"])
    with tab3:
        st.write(lead["Icebreaker"])

    #Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.button("Previous", on_click=prev_lead, disabled=st.session_state.lead_index == 0)
    with col3:
        st.button("Next", on_click=next_lead, disabled=st.session_state.lead_index >= len(filtered_df) -1)

    st.markdown(f"Viewing lead **{st.session_state.lead_index + 1} of {len(filtered_df)}**")
else:
    st.warning("No leads match you search/filter criteria.")

#Download
st.download_button(
    label="Download Filtered Leads CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_enriched_leads.csv",
    mime="text/csv"
)
















