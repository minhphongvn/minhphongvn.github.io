---
layout:            post
title:             "Picking a Backtesting Library"
menutitle:         "Picking a Backtesting Library"
date:              2017-08-24 20:43:00 +0000
tags:              Backtesting Quantitative Strategies Quant Trading
category:          Quant Trading
author:            am
published:         false
redirect_from:     "/backtesting-quant-strategies/"
language:          EN
comments:          true
---

# Contents
{:.no_toc}

* This will become a table of contents (this text will be scraped).
{:toc}

Picking a daunting task. Developing strategies to only realise half way through backtesting
that your backtesting engine is useless is a complete pain!

Below are some of the backtesting libraries I looked into

# The Libraries

| Library      | Language | Opensource | Speed      | Takes Custom Data Feeds | Ease of Use | Cross Platform |
| ------------ | -------- | ---------- | ---------- | ----------------------- | ----------- | -------------- |
| [Zorro Trader](http://www.zorro-trader.com/download.php) | C-lite   | No         | super fast | No (at least not clear) | Hard        | Windows only   |
| [PyAlgoTrade](https://github.com/gbeced/pyalgotrade)  | Python   | Yes        | Slow       | [Yes](https://stackoverflow.com/questions/37003788/how-do-i-feed-in-my-own-data-into-pyalgotrade)                     | Easy        | Yes            |
| [Zipline](https://github.com/quantopian/zipline)      | Python   | Yes        | Slow       | [Yes](https://www.quantinsti.com/blog/importing-csv-data-zipline-backtesting/?utm_source=medium&utm_medium=organic&utm_campaign=forum)                     | Easy        | Yes            |
| [AlgoCoin](https://github.com/timkpaine/algo-coin)     | Python   | Yes        | Slow       | Yes                     | Medium      | Yes            |
|              |          |            |            |                         |             |                |

## Zorro Trader
Zorro Trader was the most promising of the bunch with super fast backtesting times.
I ditched this solution as it was just a bit useless to use on Linux and furthermore, I didn't
like the idea of spending my time learning a non-transferable programming language.

The final nail in the coffin, however, was the inability to use custom data series. This
completely locked me out of backtesting strategies for crypto pairs.

## PyAlgoTrade
I initially ditched this solution for Zorro Trader. The only downside from my perspective seemed
to be the slowness of Python as a backtesting language.

## Zipline
Used in the backend of Quantopian. There is a large user base and hence a lot of support for
issues that you may encounter.

## AlgoCoin
I became aware of this from a python mail shot forwarded to me. The main issue I have
with this library is that it tries to be too many things. It is heavily under development but I can't
see why the dev didn't subclass `PyAlgoTrade` or `Zipline` for the backtesting.

This library is useful for its API endpoints, however.

# A minimal backtest
This minimal example uses the `zipline` library with a simple momentum strategy.
