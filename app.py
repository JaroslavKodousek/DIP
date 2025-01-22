import streamlit as st
import DIP_scripts

st.set_page_config(layout="wide")
st.title("DIP kalkulátor")

if 'final1' not in st.session_state:
    st.session_state['final1'] = None

if 'final2' not in st.session_state:
    st.session_state['final2'] = None

col1, col2 = st.columns(2)

with col1:
    st.title("Portu")
    input_monthly = st.number_input("Měsíční vklad", value=4000, key="input_monthly1")
    interest_yearly_percent = st.number_input("Roční úrok (poplatek) v procentech", value=0.5, key="interest_yearly_percent1")
    buying_fee = st.number_input("Poplatek za nákup", value=0, key="buying_fee1")
    earnings_yearly_percent = st.number_input("Roční výnos v procentech", value=6, key="earnings_yearly_percent1")
    buying_frequency_yearly = st.number_input("Frekvence nákupu za rok", value=12, key="buying_frequency_yearly1")
    years_investing = st.number_input("Počet let investování", value=34, key="years_investing1")

    if st.button("Vypočítej", key="calculate1"):
        final1 = DIP_scripts.dip_calculation(
            input_monthly,
            interest_yearly_percent,
            buying_fee,
            earnings_yearly_percent,
            buying_frequency_yearly,
            years_investing,
        )
        st.session_state['final1'] = final1

    if st.session_state['final1'] is not None:
        st.subheader(f"Výsledek {st.session_state['final1']:,.0f} Kč")

with col2:
    st.title("Patria")
    input_monthly2 = st.number_input("Měsíční vklad", value=4000, key="input_monthly2")
    interest_yearly_percent2 = st.number_input("Roční úrok (poplatek) v procentech", value=0.12, key="interest_yearly_percent2")
    buying_fee2 = st.number_input("Poplatek za nákup", value=150, key="buying_fee2")
    earnings_yearly_percent2 = st.number_input("Roční výnos v procentech", value=6, key="earnings_yearly_percent2")
    buying_frequency_yearly2 = st.number_input("Frekvence nákupu za rok", value=12, key="buying_frequency_yearly2")
    years_investing2 = st.number_input("Počet let investování", value=34, key="years_investing2")

    if st.button("Vypočítej", key="calculate2"):
        final2 = DIP_scripts.dip_calculation(
            input_monthly2,
            interest_yearly_percent2,
            buying_fee2,
            earnings_yearly_percent2,
            buying_frequency_yearly2,
            years_investing2,
        )
        st.session_state['final2'] = final2

    if st.session_state['final2'] is not None:
        st.subheader(f"Výsledek {st.session_state['final2']:,.0f} Kč")