import numpy as np
import pandas as pd
import calmap

Checkmarks = pd.read_csv('Checkmarks.csv')
Checkmarks['Date'] = pd.to_datetime(Checkmarks['Date'])
Date = Checkmarks['Date']

for i in range(1, Checkmarks.shape[1]):
    fig, ax = calmap.calendarplot(pd.Series(Checkmarks.iloc[:, i].values, index = Date))
    ax[0].set_title(Checkmarks.columns[i])
    fig.savefig(Checkmarks.columns[i] + ".pdf")