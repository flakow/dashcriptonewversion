import schedule
import time
import requests
from datetime import datetime
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import print
from rich.text import Text
import pytz
import datetime
from logo import logo


logo('CRIPTO DASH')

print(Panel.fit("Desenvolvido por: Antônio Carlos"))

timezone = pytz.timezone("America/Sao_Paulo")


   

def display_data():
    
    global percent_change_24h
    global percent_change_7d
    global brazil_time
    
    global table
    api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
        "start": "1",
        "limit": "30",
        "convert": "USD"
    }

    headers = {
        "Accepts": "application/json",
        # SUA token AQUI
        "add seu token aqui"
    }

    response = requests.get(api_url, headers=headers, params=parameters)
    data = response.json()

    table = Table(title="LISTAGEM DE CRIPTOMOEDAS :rocket:", show_header=True, header_style="bold blue_violet on white")
    table.add_column("Posição", style="dim", width=12)
    table.add_column("Criptomoeda", style="dim", width=25)
    table.add_column("Símbolo", style="dim", width=12)
    table.add_column("Capitalização de mercado 'USD'", style="dim", width=20)
    table.add_column("Preço 'USD'", style="dim", width=20)
    table.add_column("Volume 'USD' (24h)", style="dim", width=20)
    table.add_column("Variação (24h)", style="dim", width=20)
    table.add_column("Variação (7d)", style="dim", width=20)
    table.add_column("Variação (30d)", style="dim", width=20)
    

              

    for coin in data["data"]:
        
        rank = str(coin['cmc_rank'])
        name = coin['name']
        symbol = coin['symbol']
        market_cap = "$ " + "{:,.2f}".format(float(coin['quote']['USD']['market_cap']))
        price = "$ " + "{:,.2f}".format(float(coin['quote']['USD']['price']))
        volume_24h = "$ " + "{:,.2f}".format(float(coin['quote']['USD']['volume_24h']))
        percent_change_24h = "{:,.2f} %".format(float(coin['quote']['USD']['percent_change_24h']))
        percent_change_7d = "{:,.2f} %".format(float(coin['quote']['USD']['percent_change_7d']))
        percent_change_30d = "{:,.2f} %".format(float(coin['quote']['USD']['percent_change_30d']))
        

        #corrigir cores

        if float(coin['quote']['USD']['percent_change_24h']) < 0:
            color24h = "red"
            
        else:
            color24h = "green"
            

        if float(coin['quote']['USD']['percent_change_7d']) < 0:
            color7d = "red"

        else:
            color7d = "green"
            

        if float(coin['quote']['USD']['percent_change_30d']) < 0:
            color30d = "red"
            
            
        else:
            color30d = "green"
            

        table.add_row(rank, name, symbol, market_cap, price, volume_24h,
              Text(percent_change_24h, style=color24h),
              Text(percent_change_7d, style=color7d),
              Text(percent_change_30d, style=color30d)) 
        
   
    console = Console()
    console.print(table, justify="left", overflow="ignore")
    
    
    
    brazil_time = datetime.datetime.now(timezone)
    console.print(brazil_time, justify="center")


console = Console()

schedule.every(5).minutes.do(display_data)

if __name__ == "__main__":
    
    display_data()
    
    
while True:
    schedule.run_pending()
    time.sleep(30)


       


