import streamlit as st
import pandas as pd

st.title("🛠 Maintenance & Operation Tracker")

uploaded_file = st.file_uploader("📤 Upload Daily Log (Excel)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("📋 Uploaded Data")
    st.dataframe(df)

    # Calculate daily working hours
    df["Daily Hr"] = df["Closing Hr"] - df["Opening Hr"]

    # Show summary
    summary = df.groupby("Machine")[["Daily Hr", "Fuel L"]].sum()
    st.subheader("📊 Summary by Machine")
    st.dataframe(summary)

    # Optional: line chart
    if "Date" in df.columns:
        st.subheader("📈 Daily Work Hours Chart")
        st.line_chart(df.set_index("Date")["Daily Hr"])
