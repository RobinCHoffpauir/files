# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %% imports
# imports
import yfinance as yf
import mplfinance as mpf

# %% select a ticker
# choose a Ticker Symbol we want to research
TICKER = "MSFT"
# build dataframe with start and end date of yf.download func. (much faster than yf.history)
df = yf.download(TICKER, start="2020-07-01",
                 end="2020-12-31", auto_adjust=True)
# %% charting(OHLC)
# use mplfinance to plot a OHLC (Open,High,Low,Close) chart
mpf.plot(df["2020-12-01":])
# and High and Low lines to bracket in or chart
extra_plot = mpf.make_addplot(df.loc["2020-12-01":, ["High", "Low"]])
mpf.plot(df["2020-12-01":], addplot=extra_plot)

# %% CandleChart
#  plot a candle chart
mpf.plot(df["2020-12-01":], type="candle")

# %% Show all days
# show non trading days to get all dates to show in chart
mpf.plot(df["2020-12-01":], type="candle", show_nontrading=True)

# %%
# chart to showm MovingAverage of last 10, 20 days
mpf.plot(df, type="candle", mav=(10, 20), volume=True)
# Renko chart built using price movement of a certain specified amout,It doesn't take into account a standardized time interval liike candlestick and OHLC
# What it means is that a new block is created when the predetermined price movement occurs (set to 3, will create new block if price +-3, but not if it moves by 2.14.each subsequent block is added at a 45-degree angle to the prior one
# The most common use of the Renko chart is to filter out noise from the price series and to help with identifying trends in the prices..
mpf.plot(df, type="renko")
# change the brick size with extra argument
mpf.plot(df, type="renko", renko_params=dict(brick_size=2))
# xtra arguments to prettify our plots
mpf.plot(df, figratio=(10, 6), type="candle", mav=(21), volume=True, title=f"Price of {TICKER}",
         tight_layout=True, style="starsandstripes")
# %%
# list current styles
# different stylesbinance',
# 'blueskies',
# 'brasil',
# 'charles',
# 'checkers',
# 'classic',
# 'default',
# 'ibd',
# 'kenan',
# 'mike',
# 'nightclouds',
# 'sas',
# 'starsandstripes',
# 'yahoo'

# %%
# save plots to a file
mpf.plot(df, figratio=(10, 6), type="candle",
         mav=(21), volume=True,
         title=f"Price of {TICKER}",
         tight_layout=True, style="binance",
         savefig=f"{TICKER}.png")
