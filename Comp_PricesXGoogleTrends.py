# Comparando relação entre preços de ativos e dados do GoogleTrends

import matplotlib.pyplot as fig
from pytrends.request import TrendReq
import matplotlib.dates as mdates
import pandas_datareader.data as web
import datetime as dt

# Conexão com o servidor
pytrends = TrendReq(hl='en-US', tz=360)

# Lista com palavra-chave
kw_list = ['petróleo']

# Figura da frequencia das palavras-chave
figura = fig.figure()
ax1 = fig.subplot(111)
fig.title('GoogleTrends -Palavra chave')

# Download Google Trends
pytrends.build_payload(kw_list, cat=0, timeframe='2018-07-01 2019-11-29', geo='BR', gprop='')

teste = pytrends.interest_over_time()

# Formatação da Figura
ax1.plot(teste[kw_list[0]], '--ok')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
fig.setp(ax1.get_xticklabels(), rotation=45)
fig.legend((kw_list[0]), loc='upper left', shadow=True)
ax1.text(x=teste.index[-1], y=teste[kw_list[0]][-1], s=kw_list[0],
         fontsize=14, color='black', weight='bold')

# DataReader
inicio = dt.datetime(2018, 7, 1)
fim = dt.datetime(2019, 11, 29)
df = web.DataReader('PETR4.SA', 'yahoo', inicio, fim)
ax2 = ax1.twinx()
ax2.plot(df.index, df['Close'], color='black')
ax2.set_ylabel('PETR4', fontsize=18, weight='bold')
ax2.text(x=teste.index[51], y=30, s='PETR4', fontsize=14, weight='bold')

fig.show()
