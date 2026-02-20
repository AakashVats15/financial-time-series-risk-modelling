import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def line(series, title=None):
    fig, ax = plt.subplots()
    ax.plot(series.index, series.values)
    if title:
        ax.set_title(title)
    return fig

def multi_line(df, title=None):
    fig, ax = plt.subplots()
    for col in df.columns:
        ax.plot(df.index, df[col], label=col)
    ax.legend()
    if title:
        ax.set_title(title)
    return fig

def acf_plot(series, lags=40, title=None):
    fig = plot_acf(series, lags=lags)
    if title:
        fig.suptitle(title)
    return fig

def pacf_plot(series, lags=40, title=None):
    fig = plot_pacf(series, lags=lags)
    if title:
        fig.suptitle(title)
    return fig

def hist(series, bins=50, title=None):
    fig, ax = plt.subplots()
    ax.hist(series.values, bins=bins)
    if title:
        ax.set_title(title)
    return fig

def scatter(x, y, title=None):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    if title:
        ax.set_title(title)
    return fig