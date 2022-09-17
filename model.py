import yfinance
from prophet import Prophet
from singleton_decorator import singleton


@singleton
class Model:

    btc_model = None
    future = None

    def initialize(self):
        btc_data = yfinance.download(tickers='btc-usd', period='1Y')
        self.btc_model = self.prepare(btc_data)

        eth_data = yfinance.download(tickers='eth-usd', period='1Y')
        self.eth_model = self.prepare(eth_data)

        petr4_data = yfinance.download(tickers='PETR4.SA', period='1Y')
        self.petr4_model = self.prepare(petr4_data)

        self.future = self.btc_model.make_future_dataframe(periods=1)[-1:]


    def prepare(self, df):
        target_df = df['Close']

        target_df = target_df.reset_index('Date')
        target_df.columns = ['ds', 'y']

        model = Prophet( interval_width=0.9,
                         changepoint_prior_scale=0.2,
                         yearly_seasonality=10)
        model.fit(target_df)
        return model


