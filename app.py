import streamlit as st
st.title('Bitcoin')
col1, col2 = st.columns(2)

with col1:
    st.image('bitcoin.jpeg')

with col2:
    st.write("""
    Bitcoin (abbreviation: BTC[a] or XBT;[b] sign: ₿) is the first decentralized cryptocurrency. Nodes in the peer-to-peer bitcoin network verify transactions through cryptography and record them in a public distributed ledger, called a blockchain, without central oversight. Consensus between nodes is achieved using a computationally intensive system based on proof-of-work called mining. Bitcoin mining requires increasing quantities of electricity[5] and was responsible for 0.2% of world greenhouse gas emissions as of 2022.[6]""")

st.header('Larger Market cap')
st.subheader("ADA")
st.subheader("Matic")
st.subheader("Solana")
st.subheader("DOT")

st.header('Web3.0')
st.subheader('ICP')
st.subheader('File')
st.subheader('Theta')