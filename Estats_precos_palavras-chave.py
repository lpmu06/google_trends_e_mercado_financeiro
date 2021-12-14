# Comparção entre preços e google trends

import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import matplotlib.dates as mdates
import pandas_datareader.data as web
import datetime as dt
import seaborn as sns


# Conexão com o servidor
pytrends = TrendReq(hl='en-US', tz=360)

# Lista com palavra-chave
kw_list = ['minério']

# Figura da frequencia das palavras-chace
figura = plt.figure()
ax1 = plt.subplot(111)
plt.title('GoogleTrends -Palavra chave')

# Download google trends
pytrends.build_payload(kw_list, cat=0,
                       timeframe='2018-07-01 2019-11-29',
                       geo='BR', gprop='')

teste = pytrends.interest_over_time()

# Formatação da figura
ax1.plot(teste[kw_list[0]], '--ok')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.setp(ax1.get_xticklabels(), rotation=45)
plt.legend((kw_list[0]), loc='upper left', shadow=True)
ax1.text(x=teste.index[-1], y=teste[kw_list[0]][-1], s=kw_list[0], fontsize=14, color='black', weight='bold')

# DataReader
inicio = dt.datetime(2018, 7, 1)
fim = dt.datetime(2019, 11, 29)
df = web.DataReader('VALE3.SA', 'yahoo', inicio, fim)
ax2 = ax1.twinx()
ax2.plot(df.index, df['Close'], color='black')
ax2.set_ylabel('VALE3(R$)', fontsize=14, weight='bold')
ax2.text(x=teste.index[51], y=30, s='VALE3', fontsize=12, weight='bold')

# Amostragem dos pontos de ação
med = df['Close'].resample('w').mean()
ax2.plot(med.index, med, '-k', linewidth=1)

# Reta de regressão linear
plt.figure()
dados1 = sns.regplot(teste['minério'].values, med, color='black')
dados1.set_xlabel('Palavra "minério"', fontsize=14)
dados1.set_ylabel('Preço VALE3(R$)', fontsize=14)

# Plotagem conjunta dos histogramas das series
dados2 = sns.jointplot(teste['minério'].values, med, kind='scatter', color='black')
dados2.set_axis_labels('Palavra "minério', 'Preço VALE3(R$)', fontsize=14)

# Coeficiente da correlação de Pearson
# Não consegui mostrar o stats.pearsonr, ver isso melhor.
# AttributeError: 'JointGrid' object has no attribute 'annotate'
# dados2.annotate(stats.pearsonr)
plt.show()
