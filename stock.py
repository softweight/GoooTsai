import twstock
from datetime import date

# https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=20220127&stockNo=2330


name_attribute = ['Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change', 'Trascation']

def getStockstate(name):
    stock = twstock.realtime.get(name)
    openprice = twstock.Stock(name).price[-2]
    aftername = name
    # print(openprice)
    if stock['success']:
        newprice = float(stock["realtime"]["latest_trade_price"])
        # print(newprice)
        if newprice >= openprice:
            aftername = f"{name}🔴{newprice}"
        else:
            aftername = f"{name}🟢{newprice}"
        aftername = aftername.replace(".","_")
    return aftername

time = date.today().strftime('%Y-%m-%d')

print(getStockstate('0050'))



