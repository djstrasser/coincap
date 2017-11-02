""" utils.py: Utility functions for use by the main CLI coincap.py """

import click
import crayons

def echo_prices(coins, conversion):
    """ Echo the price stats for a list of coins

    args:
        coins: A list of objects representing the coin data
        conversion: the conversion currency used to get this data
    """
    header_text = "Ticker  Price ({})  24H Change".format(conversion)
    header = crayons.white(header_text, bold=True)
    click.echo(header)
    price_key = "price_" + conversion.lower()
    for coin in coins:
        try:
            changed = float(coin["percent_change_24h"])
            if changed <= 0:
                change = crayons.red("▼  {:<5.5} %".format(str(changed)))
            else:
                change = crayons.green("▲   {:<4.4} %".format(str(changed)))
            ticker = coin["symbol"]
            price = coin[price_key]
            line = "{:<7} {:<12.10} {}".format(ticker, price, change)
            click.echo(line)
        except TypeError:
            # The API occassionaly returns None for certain fields so skip the entire coin
            pass

def echo_data(data, conversion):
    """ Echo a table containing global coinmarketcap data

    args:
        data: A dict representing global data
        conversion: the conversion currency used to get this data
    """
    conversion_string = conversion.lower()
    dashes = crayons.green("--------------------------------------------")
    wall = crayons.green("|")
    template1 = wall + " {:<18}: {:<21,}" + wall
    template2 = wall + " {:<18}: {:<21}" + wall

    lines = []
    lines.append(template1.format("Total Market Cap",
                                  data["total_market_cap_" + conversion_string]))
    lines.append(template1.format("Total 24H Vol.",
                                  data["total_24h_volume_" + conversion_string]))
    lines.append(template2.format("BTC Dominance",
                                  str(data["bitcoin_percentage_of_market_cap"]) + " %"))
    lines.append(template1.format("Active Currencies", data["active_currencies"]))
    lines.append(template1.format("Active Assets", data["active_assets"]))
    lines.append(template1.format("Active Markets", data["active_markets"]))

    for line in lines:
        click.echo(dashes)
        click.echo(line)
    click.echo(dashes)
