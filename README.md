# CoinCap

A small CLI to display data from coinmarketcap.com in the terminal.

## Price & Prices
```bash
$ python3 coincap.py prices
```
![Imgur](https://i.imgur.com/QqrPPvU.png)

#### Set the number of results
```bash
$ python3 coincap.py prices -l 20
```

#### Get a specific coin
```bash
$ python3 coincap.py price ethereum
```

#### Get results in a different currency
```bash
$ python3 coincap.py prices -c EUR
```


## Data
```bash
$ python3 coincap.py data
```
![Imgur](https://i.imgur.com/THbtspR.png)

#### Get results in a different currency
```bash
$ python3 coincap.py data -c EUR
```