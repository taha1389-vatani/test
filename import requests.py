import pytse_client as tse
import streamlit as st
tse.download(symbols="نوری", write_to_csv=True)  # optional
ticker = tse.Ticker("نوری")
st.write(ticker.eps)  # EPS
st.write(ticker.p_e_ratio)  # P/E
st.write(ticker.group_p_e_ratio)  # group P/E
st.write(ticker.nav)  # NAV خالص ارزش دارایی‌ها ویژه صندوق‌ها می‌باشد
st.write(ticker.nav_date)  # last date of NAV تاریخ بروزرسانی خالص ارزش دارایی‌ها ویژه صندوق‌ها می‌باشد
st.write(ticker.psr)  # PSR این نسبت ویژه شرکت‌های تولیدی است
st.write(ticker.p_s_ratio)  # P/Sاطلاعات لحظه‌ای مانند قیمت و پیشنهادات خرید و فروش