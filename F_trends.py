# Obtendo dados do GoogleTrends (sobre o que as pessoas estão pesquisando), utilizando pytrends, para comparar 2 trends.
# Importante discorrer sobre o funcionamento do googletrends e dos parâmetros de "pytrends.build_payload"

import matplotlib.pyplot as fig
from pytrends.request import TrendReq
import matplotlib.dates as mdates

# Fazendo a conexão com os servidores(EUA) da google:
pytrends = TrendReq(hl='en-US', tz=360)

# Palavras-chave desejadas:
kw_list = ['Petrobrás', 'dólar']

# Tipos de dados a serem pesquisados:
pytrends.build_payload(kw_list, cat=0, timeframe='all', geo='BR', gprop='')
teste = pytrends.interest_over_time()
# Construção do gráfico:
fig.style.use('ggplot')
figure = fig.figure()
ax1 = fig.subplot(111)
fig.title('GoogleTrends -Palavra chave')

# Formatando eixo:
ax1.plot(teste[kw_list[0]], '-k', teste[kw_list[1]], '--k')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
fig.setp(ax1.get_xticklabels(), rotation=45)

# Legenda:
fig.legend((kw_list[0], kw_list[1]), loc='upper left', shadow=True)

# Identificação da palavra-chave no gráfico:
ax1.text(x=teste.index[-1], y=teste[kw_list[0]][-1], s=kw_list[0], fontsize=12, color='black', weight='bold')
ax1.text(x=teste.index[-1], y=teste[kw_list[1]][-1], s=kw_list[1], fontsize=12, color='black', weight='bold')

fig.show()
