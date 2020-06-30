
#%%
import pandas as pd
import pandas_profiling as pp
df_dollar = pd.read_csv('../Sample-Data/dollar_bars.csv', index_col=0, parse_dates=True)
df_volume = pd.read_csv('../Sample-Data/volume_bars.csv', index_col=0, parse_dates=True)
df_true = pd.read_csv('../Sample-Data/spx.csv', index_col=0, parse_dates=True,decimal='.',thousands=',').sort_index()

# %%
from scipy.stats import normaltest, probplot
import numpy as np

# normaltest(np.array(df.close.pct_change().dropna()))

# %%
import pylab
probplot(df_dollar.close.pct_change().dropna(), dist='norm', plot=pylab)
pylab.show()
#%%
probplot(df_volume.close.pct_change().dropna(), dist='norm', plot=pylab)
pylab.show()

# %%
probplot(df_true.Price.pct_change().dropna(), dist='norm', plot=pylab)
pylab.show()

# %%
from mlfinlab.datasets import load_tick_sample, load_stock_prices, load_dollar_bar_sample

tick_df = load_tick_sample()
dollar_bars_df = load_dollar_bar_sample()
stock_prices_df = load_stock_prices()

# %%
def f(x:pd.DataFrame=pd.DataFrame(data=[3])):
    return(x**2)

# %%
import aeqlib.time_series_analysis as tsa
from mlfinlab.features.fracdiff import frac_diff_ffd

# %%
frac_diff_ffd(df_true[['Price']], 0.5)

# %%
df_true[['Price']]

# %%
