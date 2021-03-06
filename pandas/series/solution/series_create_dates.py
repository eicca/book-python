import pandas as pd


data = pd.date_range(
    start='1961-04-12',
    end='1969-07-21',
    freq='D')

s = pd.Series(data)

s
# 0      1961-04-12
# 1      1961-04-13
# 2      1961-04-14
# 3      1961-04-15
# 4      1961-04-16
#           ...
# 3018   1969-07-17
# 3019   1969-07-18
# 3020   1969-07-19
# 3021   1969-07-20
# 3022   1969-07-21
# Length: 3023, dtype: datetime64[ns]

len(s)
# 3023
