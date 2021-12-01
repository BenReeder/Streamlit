import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price Viewer
### **By Ben Reeder**

Shown are the Closing Prices and Volumes of Google, Tesla, SalesForce, and Bitcoin
# *Google*

""")


tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1m', start='2015-5-31', end='2020-5-31')

st.write(""" ### Close """)
st.line_chart(tickerDf.Close)
st.write(""" ### Volume """)
st.line_chart(tickerDf.Volume)

st.write("""
# *TSLA*
""")

tickerSymbol = 'TSLA'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1m', start='2015-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write(""" ### Close """)
st.line_chart(tickerDf.Close)
st.write(""" ### Volume """)
st.line_chart(tickerDf.Volume)


st.write("""
# *SalesForce*
""")

tickerSymbol = 'CRM'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1m', start='2015-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write(""" ### Close """)
st.line_chart(tickerDf.Close)
st.write(""" ### Volume """)
st.line_chart(tickerDf.Volume)


st.write("""
# *BITCOIN*
""")

tickerSymbol = 'BTC-USD'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1m', start='2015-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write(""" ### Close """)
st.line_chart(tickerDf.Close)
st.write(""" ### Volume """)
st.line_chart(tickerDf.Volume)
