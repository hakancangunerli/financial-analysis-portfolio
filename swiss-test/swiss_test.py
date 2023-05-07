# %%
import quantstats as qs
import pandas as pd

# %%
# UBS 
# Credit Suisse (CS)


# %%
cs = qs.utils.download_returns('CS')
qs.reports.full(cs.tz_localize(None,ambiguous='infer'))

# %%
ubs = qs.utils.download_returns('UBS')
qs.reports.full(ubs.tz_localize(None,ambiguous='infer'))

# %%
# analysis of ubs first 

# sharpe ration: 
''''The Sharpe ratio divides a portfolio's excess returns by a measure of its volatility to assess risk-adjusted performance'''

'''
A higher Sharpe ratio indicates that an investment or portfolio is providing a higher return relative to its risk, and is therefore more attractive. Conversely, a lower Sharpe ratio indicates that an investment or portfolio is providing a lower return relative to its risk, and is therefore less attractive.
'''

print(qs.stats.sharpe(ubs), 'sharpe ratio')

# avg loss
print(qs.stats.avg_loss(ubs), 'avg loss') # avg loss

# avg gain
print(qs.stats.avg_win(ubs), 'avg gain') # avg gain

# win-loss ratio 
print(qs.stats.win_loss_ratio(ubs), 'win loss ratio') # win/loss which means the higher it is the better


# distribution 

print(qs.plots.log_returns(ubs))

print(qs.plots.histogram(ubs))

# %%
# analysis of ubs first 

# sharpe ration: 
''''The Sharpe ratio divides a portfolio's excess returns by a measure of its volatility to assess risk-adjusted performance'''

'''
A higher Sharpe ratio indicates that an investment or portfolio is providing a higher return relative to its risk, and is therefore more attractive. Conversely, a lower Sharpe ratio indicates that an investment or portfolio is providing a lower return relative to its risk, and is therefore less attractive.
'''

print(qs.stats.sharpe(cs), 'sharpe ratio')

# avg loss
print(qs.stats.avg_loss(cs), 'avg loss') # avg loss

# avg gain
print(qs.stats.avg_win(cs), 'avg gain') # avg gain

# win-loss ratio 
print(qs.stats.win_loss_ratio(cs), 'win loss ratio') # win/loss which means the higher it is the better


# distribution 

print(qs.plots.log_returns(cs))

print(qs.plots.histogram(cs))

# %%
# win_loss_ratio for ubs, cs

print(qs.stats.win_loss_ratio(ubs))

print(qs.stats.win_loss_ratio(cs))


