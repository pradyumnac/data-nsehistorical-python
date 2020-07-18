from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from datetime import date

from nsepy import get_history

app = FastAPI()

eq_numeric_columns = ['Open', 'High', 'Low', 'Close', 'Prev Close', 'Last',
                'VWAP', 'Volume', 'Turnover', ]

@app.get("/equity")
def get_eq_history(symbol: str, start_dt: date, end_dt: date):
    ret = []
    df = get_history(symbol=symbol,
                    start=start_dt, 
                    end=end_dt)
    for ind in df.index: 
        ret.append([ind.strftime('%d/%m/%y'), df['Symbol'][ind]]+
                   [ float(df[col_name][ind]) for col_name in eq_numeric_columns ])  
    return ret


@app.get("/index/{symbol}")
def get_index_history(item_id: int, q: Optional[str] = None):
    ret = []
    df = get_history(symbol=symbol,
                    start=start_dt, 
                    end=end_dt, 
                    index=True)
    for ind in df.index: 
        ret.append([ind.strftime('%d/%m/%y'), df['Symbol'][ind]]+ 
                   [ float(df[col_name][ind]) for col_name in eq_numeric_columns ])  
    return ret

@app.get("/index-futures/{symbol}")
def get_eq_futures_history(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/eq-futures/{symbol}")
def get_eq_futures_history(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/options/{symbol}")
def get_eq_futures_history(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/")
def read_root():
    return {"Status": "Ok"}