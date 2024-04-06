import pandas as pd
from lightweight_charts import Chart

if __name__ == '__main__':
    chart = Chart()

    # Columns: time | open | high | low | close | volume
    df = pd.read_csv('C:/Users/chung/OneDrive/Documents/GitHub/lightweight-charts-python/examples/1_setting_data/ohlcv.csv')
    chart.set(df)

    chart.show(block=True)
