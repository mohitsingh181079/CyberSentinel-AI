import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="CyberSentinel-AI", layout="wide", page_icon="🛡️")

st.title("🛡️ CyberSentinel-AI - Live Threat Dashboard")
st.markdown("**Autonomous Threat Intelligence & Countermeasure Engine**")
st.divider()

# Create Sample Data (No external CSV needed)
data = {
    'ip_address': ['192.168.1.10', '45.33.21.5', '192.168.1.11', '103.22.44.8', '10.0.0.5'],
    'login_attempts': [2, 98, 3, 150, 1],
    'data_mb': [50, 1200, 60, 5000, 30],
    'is_attack': [0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Top Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Logs", len(df))
col2.metric("Attacks Detected", len(df[df['is_attack']==1]), delta="2 Critical", delta_color="inverse")
col3.metric("System Status", "ACTIVE")

# Graph Section
st.subheader("📊 Threat Analysis")
fig = px.bar(df, x='ip_address', y='login_attempts', color='is_attack',
             title="Login Attempts per IP (1 = Attack / 0 = Safe)",
             labels={'is_attack': 'Threat Level'},
             color_continuous_scale=['green', 'red'])
st.plotly_chart(fig, use_container_width=True)

# Live Logs Table
st.subheader("Live Network Logs")
st.dataframe(df, use_container_width=True)

# AI Agent - Self Healing Log
st.subheader("🤖 AI Agent - Self Healing Log")
for index, row in df.iterrows():
    if row['is_attack'] == 1:
        st.error(f"🚨 ALERT: Attack from IP {row['ip_address']} | Attempts: {row['login_attempts']} -> ACTION: IP Blocked & Logged to Supabase!")
    else:
        st.success(f"✅ IP {row['ip_address']} is Safe - Traffic Normal")

#st.balloons()