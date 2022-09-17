from fastapi import FastAPI
from model import Model

model = Model()
model.initialize()

app = FastAPI()

@app.get('/stock/{id_stock}')
async def stock(id_stock:str):

    if( id_stock == 'btc'):
        forecast = model.btc_model.predict(model.future)
        return {
            'ticker' : id_stock,
            'forecast': forecast['yhat'][0]
        }
    elif( id_stock == 'eth'):
        forecast = model.eth_model.predict(model.future)
        return {
            'ticker' : id_stock,
            'forecast': forecast['yhat'][0]
        }
    elif (id_stock == 'petr4'):
        forecast = model.petr4_model.predict(model.future)
        return {
            'ticker': id_stock,
            'forecast': forecast['yhat'][0]
        }
    else:
        return {
            'error' : 'Ticker not found'
        }
