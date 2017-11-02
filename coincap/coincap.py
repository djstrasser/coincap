""" coincap.py: A CLI for displaying data from coinmarketcap.com """

import sys

import click
import crayons
from halo import Halo

from coinmarketcap import CoinmarketCap
from utils import echo_prices, echo_data

@click.group()
@click.pass_context
def cli(context):
    """ Main CLI function - a click group for nesting subcommands """
    context.obj["client"] = CoinmarketCap()

@click.command()
@click.pass_context
@click.option("-l", default=10, help="Limit currencies shown (default 10)")
@click.option("-c", default="USD", help="Conversion currency (default USD)")
def prices(context, l, c):
    """ Display cryptocurrency prices and their 24 hour change percentage """
    try:
        spinner = Halo(text='Loading price data', spinner='dots')
        spinner.start()
        coins = context.obj["client"].ticker(limit=l, convert=c)
        spinner.stop()
        echo_prices(coins, c)
    except ValueError:
        sys.exit(crayons.red("Invalid conversion currency: {}".format(c)))

@click.command()
@click.pass_context
@click.option("-c", default="USD", help="Conversion currency (default USD)")
@click.argument("coin_id")
def price(context, coin_id, c):
    """ Display the price and 24 hour change percentage of a specific currency """
    coin = context.obj["client"].ticker_specific(coin_id, convert=c)
    if isinstance(coin, list):
        echo_prices(coin, c)
    else:
        sys.exit(crayons.red("Invalid COIN_ID: {}".format(coin_id)))

@click.command()
@click.pass_context
@click.option("-c", default="USD", help="Conversion currency (default USD)")
def data(context, c):
    """ Display the global coinmarketcap.com data:
        * Total cap
        * 24 HR volume
        * BTC Dominance
        * Active Currencies
        * Acitve Assets
        * Active markets
    """
    try:
        data_obj = context.obj["client"].global_data(convert=c)
        echo_data(data_obj, c)
    except ValueError:
        sys.exit(crayons.red("Invalid conversion currency: {}".format(c)))

def add_all_commands():
    """ Add all available commands  """
    commands = [prices, price, data]
    for command in commands:
        cli.add_command(command)

if __name__ == '__main__':
    add_all_commands()
    cli(obj={})
