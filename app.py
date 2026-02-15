import streamlit as st
import json

st.title("CommunityConnect AI")

# Load FAQ
with open("faqs.json", "r") as f:
    faqs = json.load(f)

# Profile selection
profile = st.selectbox(
    "Select your profile",
    ["Student", "Farmer", "Job Seeker"]
)

# User input
query = st.text_input("Ask your question")

# Simple FAQ search
if query:
    found = False

    for item in faqs:
        if profile.lower() in item["profile"].lower():
            if query.lower() in item["question"].lower():
                st.success(item["answer"])
                found = True
                break

    if not found:
        st.warning("No answer found in offline database.")
