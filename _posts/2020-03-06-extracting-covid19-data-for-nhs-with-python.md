---
layout: post
title: "Extracting Covid19 Data for NHS with Python"
menutitle: "Extracting Covid19 Data for NHS with Python"
date: 2020-03-05 21:35:00 +0000
tags: Python Tutorial Learning covid19 coronavirus 2019-nCov SARS-CoV-2
category: Python Tutorial
author: am
published: true
redirect_from: "/2020-03-06-extracting-covid19-data-for-nhs-with-python/"
language: EN
comments: true
---

## Contents
{:.no_toc}

* This will become a table of contents (this text will be scraped).
{:toc}

Lets assume you happen to stumble across the NHS data for Covid19 found at https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-daily-deaths/

# Parse an Excel with Pandas

We can extract th dat for a funky plot like

```python
import datetime
import pandas as pd

dt = datetime.date.today()
url_root = r'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2020/04/'
url_ts = url_root + f'COVID-19-total-announced-deaths-{dt.strftime("%-d-%B-%Y")}.xlsx'

_parser = lambda x: x in ['NHS England Region', 'Name'] or isinstance(x, datetime.datetime)
raw = pd.read_excel(url_ts, sheet_name=0, skiprows=15, usecols=_parser)
raw = raw.iloc[2:]
raw.index = pd.to_datetime(raw.index)
```

I opened the Excel file initially in Excel. There were 15 useless rows at the top.
There was also an annoying column format where I only wanted dates, `Name` of hospital and `NHS England Region`. This is achieved by passing a function that will return `True` for any of these fields.
There are also two junk rows athe the start of the dataframe and always convert date fields into datetime objects.

# Cleaning Data

If you read the note in the excel file we see that numbers are rastically changed as and when the data comes in. This means that the last 5 days are highly variable. We want to separate this out and make it clear on any plot. Also the data is noisey. We can smooth with EWMA. I thought EWMA is a bit better than moving average because you get a continuous smoothing rather than a plot that jumps around as data moves in and out of the moving average window. 

```python
span = 10
unstable_region = 5
raw_diffs = raw.sum(axis=1).diff() # useful later
smoothed = raw_diffs.diff().ewm(span=span).mean()

stable = smoothed.iloc[:-unstable_region+1]
unstable = smoothed.iloc[-unstable_region:]
```

# Plotting

This is pretty easy
```python
import matplotlib.pyplot as plt
plt.ion()

fig, ax = plt.subplots()
stable.plot(title='Acceleration of Cumulative UK Deaths in NHS Hospitals',
            label='stable data',
            ax=ax) 
unstable.plot(ax=ax, color='red', ls='--', label='unstable data')
```

We can now plot the unstable dataset like

```python
fig, ax = plt.subplots()
stable.plot(title='Acceleration of Cumulative UK Deaths in NHS Hospitals',
            label='stable data',
            ax=ax) 
unstable.plot(ax=ax, color='red', ls='--', label='unstable data')

ax.set_ylabel('change in daily fatalities')
```

# Estimating Expected Updates
Now wehave the problem where the last 5 days of data are potentially garbage. WEe need to estimate somehow what the update might look like. That last few days of updates are available on the same landing page.

```python
import requests
import bs4

# adjust the unstable data to take into account updated data
url_page = r'https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-daily-deaths/'
html = requests.get(url_page).content
soup = bs4.BeautifulSoup(
    html,
    "html.parser",
    parse_only=bs4.SoupStrainer('a')
)
url_updates = [
    l['href']
    for l in soup if 'xls' in l.get('href', '')
    and 'daily announced' in l.text.lower()
]
```

IN the above I parse the page for all `a` tags which are hyperlinks in HTML. Then I look for all hyperlinks that end in `".xls"` and that also have the text `"daily announced"` in the link text.

Now I want to parse the date the update was given by. THis is a bit tricky because it's clearly a human process as the files have slightly different names. We are at risk of the process breaking if someone changes the naming convention. I take the assumption `"deaths"` will always be the end of the file text name and be next to the date.

```python
def get_offset_from_url(u):
    d = datetime.datetime.strptime(u[u.index('deaths-') + 7: u.index('-2020') + 5], '%d-%B-%Y')
    return (dt - d.date()).days

kws = dict(sheet_name='COVID19 daily deaths by age',
           skiprows=14, usecols=_parser, nrows=1)
updates_raw = pd.DataFrame(
    {
        get_offset_from_url(u): pd.read_excel(u, **kws).iloc[0]
        for u in url_updates
    }
)
```
I pass the data into a dataframe and read from the sheet name skipping useless rows and using the same column parser as before because we only want the dates and it doesn't need to be recreated.

I'll let you figure this next bit out, basically I'm recreating the data as it previously was.


```python
updates_raw.columns.name = 'Adjustments n days ago'
updates_abs = updates_raw.copy()
updates_pct = updates_raw.copy()

all_cols = set(updates_raw.columns)
for i in reversed(sorted(updates_raw.columns)):
    # this is because of some errors in the data
    raw_as_of_date = (diff1 - updates_raw[all_cols].sum(axis=1))
    raw_as_of_date.iloc[-i-1:] = 0
    updates_pct[i] = updates_raw[i] / raw_as_of_date
    all_cols.remove(i)
    updates_abs[i] = updates_abs[i].shift(i)
    updates_pct[i] = updates_pct[i].shift(i)

updates_abs.index = pd.Index([(datetime.datetime.today() - i).days for i in updates_abs.index],
                         name='The date that was updated (n days ago)')
updates_pct.index = pd.Index([(datetime.datetime.today() - i).days for i in updates_pct.index],
                         name='The date that was updated (n days ago)')
```

There is a mistake in the dataset as well which I remove by `raw_as_of_date.iloc[-i-1:] = 0`. I add in the name parameters because I'm a bit OCD.

I then plot the data to make sure there isn't any drastic change in the updates each day. What is possible is that in a stressed system there might be an increasing backlog. 

```python
fig2, (ax2, ax2b) = plt.subplots(2, sharex=True)
l = 0
colors = itertools.cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
for col in updates_abs.iloc[-l:].columns:
    c = next(colors)
    (100*updates_pct.iloc[-l:][col].dropna()).plot(
        ax=ax2, lw=1, ls='--', color=c,
        label=f'update for previous days made {col} days ago'
    )
    (updates_abs.iloc[-l:][col].dropna()).plot(ax=ax2b, lw=1, ls='--', color=c, label=None)

c = next(colors)
(100*(updates_pct.iloc[-l:].mean(axis=1)).dropna()).plot(ax=ax2, color=c, label='mean')
((updates_abs.iloc[-l:].mean(axis=1)).dropna()).plot(ax=ax2b, color=c, label=None)

fig2.suptitle('Percentage change in the daily figures')
ax2.set_title("percentage daily adjustments aren't drastically increasing day by day",
              fontsize=8)
ax2.set_ylabel('Percentage change')
ax2.legend(fontsize=8)
ax2b.set_ylabel('Absolute change')
```

AS it turns out this isn't the case and the updates are roughly the same each day and there is only about a 10% increase after the 5th day so the NHS note is correct in saying the last 5 days are the unstable region.

Estimating the expected updates is just done by integrating under the curve to get the expected updates as a percentage.

```python
raw_diffs_adj = raw_diffs.copy()
for i in range(unstable_region):
    raw_diffs_adj.iloc[-i] = (updates_pct.mean(axis=1) + 1).iloc[-unstable_region:-i].prod() * raw_diffs.iloc[-i]
```

# The updated plot
We use the axis handle from the plot above and update for the new estimates of what we expect the data to show.

```python
smoothed_adj = raw_diffs_adj.diff().ewm(span=span).mean()

stable_adj = smoothed_adj.iloc[:-unstable_region+1]
unstable_adj = smoothed_adj.iloc[-unstable_region:]

fig3, ax3 = plt.subplots()
raw_diffs.plot(title='Daily fatalities in NHS Hospitals',
               label='original data', ax=ax3)
raw_diffs_adj.iloc[-unstable_region:].plot(ax=ax3, color='green', ls='--',
                   label='expected future adjustments')
ax3.set_ylabel('Fatalities attributed to each date')
ax3.legend(loc='upper left')

unstable_adj.plot(ax=ax, color='green', ls='--',
              label='expected future adjustments')
```

# Estimating Impact of Government Measures

We now want to annotate where the UK government introduced quarantine phases. I found the parameters for the offset of 13 days byreading a load of medical papers which showed it took 13 days from infection to fatality as the low end of the interquartile range. I assume this would be where we start to see effects really feeding back into the data.

We can add labels for where we expect the data to be affected by isolation like

```python
d0 = datetime.datetime(2020, 3, 16)
d1 = datetime.datetime(2020, 3, 23)
d2 = d0 + datetime.timedelta(days=13)
d3 = d1 + datetime.timedelta(days=13)

ax.axvspan(d3, smoothed_adj.index[-1], color='darkred', alpha=0.3, lw=0,
           label='national isolation + 13 days')
ax.axvspan(d2, d3, color='darkorange', alpha=0.3, lw=0,
           label='blanket symptomatic isolation + 13 days')
ax.legend(loc='lower left', fontsize=8)
```

Layout is better with

```python
fig.tight_layout()
```

# Full Example Script

```python
import datetime
import pandas as pd
import itertools
import bs4
import requests
from urllib.request import HTTPError

dt = datetime.date.today()
url_root = r'https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2020/04/'
url_ts = url_root + f'COVID-19-total-announced-deaths-{dt.strftime("%-d-%B-%Y")}.xlsx'

_parser = lambda x: x in ['NHS England Region', 'Name'] or isinstance(x, datetime.datetime)
raw = pd.read_excel(url_ts, sheet_name=0, skiprows=15, usecols=_parser)
raw = raw.iloc[2:]

raw = raw.set_index(['NHS England Region', 'Name']).T.cumsum()
raw.index = pd.to_datetime(raw.index)

span = 10
unstable_region = 5
raw_diffs = raw.sum(axis=1).diff() # useful later
smoothed = raw_diffs.diff().ewm(span=span).mean()

stable = smoothed.iloc[:-unstable_region+1]
unstable = smoothed.iloc[-unstable_region:]

fig, ax = plt.subplots()
stable.plot(title='Acceleration of Cumulative UK Deaths in NHS Hospitals',
            label='stable data',
            ax=ax) 
unstable.plot(ax=ax, color='red', ls='--', label='unstable data')

ax.set_ylabel('change in daily fatalities')

# adjust the unstable data to take into account updated data
url_page = r'https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-daily-deaths/'
html = requests.get(url_page).content
soup = bs4.BeautifulSoup(
    html,
    "html.parser",
    parse_only=bs4.SoupStrainer('a')
)
url_updates = [
    l['href']
    for l in soup if 'xls' in l.get('href', '')
    and 'daily announced' in l.text.lower()
]

def get_offset_from_url(u):
    d = datetime.datetime.strptime(u[u.index('deaths-') + 7: u.index('-2020') + 5], '%d-%B-%Y')
    return (dt - d.date()).days

kws = dict(sheet_name='COVID19 daily deaths by age',
           skiprows=14, usecols=_parser, nrows=1)
updates_raw = pd.DataFrame(
    {
        get_offset_from_url(u): pd.read_excel(u, **kws).iloc[0]
        for u in url_updates
    }
)
updates_raw.columns.name = 'Adjustments n days ago'
updates_abs = updates_raw.copy()
updates_pct = updates_raw.copy()

all_cols = set(updates_raw.columns)
for i in reversed(sorted(updates_raw.columns)):
    # this is because of some errors in the data
    raw_as_of_date = (raw_diffs - updates_raw[all_cols].sum(axis=1))
    raw_as_of_date.iloc[-i-1:] = 0
    updates_pct[i] = updates_raw[i] / raw_as_of_date
    all_cols.remove(i)
    updates_abs[i] = updates_abs[i].shift(i)
    updates_pct[i] = updates_pct[i].shift(i)

updates_abs.index = pd.Index([(datetime.datetime.today() - i).days for i in updates_abs.index],
                         name='The date that was updated (n days ago)')
updates_pct.index = pd.Index([(datetime.datetime.today() - i).days for i in updates_pct.index],
                         name='The date that was updated (n days ago)')

# check that daily adjustment aren't drastically increasing
# ie. that we can use an average of the last few days without
# implicitly concealing some exponential growth

fig2, (ax2, ax2b) = plt.subplots(2, sharex=True)
l = 0
colors = itertools.cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
for col in updates_abs.iloc[-l:].columns:
    c = next(colors)
    (100*updates_pct.iloc[-l:][col].dropna()).plot(
        ax=ax2, lw=1, ls='--', color=c,
        label=f'update for previous days made {col} days ago'
    )
    (updates_abs.iloc[-l:][col].dropna()).plot(ax=ax2b, lw=1, ls='--', color=c, label=None)

c = next(colors)
(100*(updates_pct.iloc[-l:].mean(axis=1)).dropna()).plot(ax=ax2, color=c, label='mean')
((updates_abs.iloc[-l:].mean(axis=1)).dropna()).plot(ax=ax2b, color=c, label=None)

fig2.suptitle('Percentage change in the daily figures')
ax2.set_title("percentage daily adjustments aren't drastically increasing day by day",
              fontsize=8)
ax2.set_ylabel('Percentage change')
ax2.legend(fontsize=8)
ax2b.set_ylabel('Absolute change')

# we only see about 10% increase to data that was more than 5 days ago
# therefore we can adjust accordingly
raw_diffs_adj = raw_diffs.copy()
for i in range(unstable_region):
    raw_diffs_adj.iloc[-i] = (updates_pct.mean(axis=1) + 1).iloc[-unstable_region:-i].prod() * raw_diffs.iloc[-i]

smoothed_adj = raw_diffs_adj.diff().ewm(span=span).mean()

stable_adj = smoothed_adj.iloc[:-unstable_region+1]
unstable_adj = smoothed_adj.iloc[-unstable_region:]

fig3, ax3 = plt.subplots()
raw_diffs.plot(title='Daily fatalities in NHS Hospitals',
               label='original data', ax=ax3)
raw_diffs_adj.iloc[-unstable_region-1:].plot(ax=ax3, color='red', ls='--',
                   label='taking into account expected future adjustments')
ax3.set_ylabel('Fatalities attributed to each date')
ax3.legend(loc='upper left')

unstable_adj.plot(ax=ax, color='green', ls='--',
              label='expected future adjustments')

d0 = datetime.datetime(2020, 3, 16)
d1 = datetime.datetime(2020, 3, 23)
d2 = d0 + datetime.timedelta(days=13)
d3 = d1 + datetime.timedelta(days=13)

ax.axvspan(d3, smoothed_adj.index[-1], color='darkred', alpha=0.3, lw=0,
           label='national isolation + 13 days')
ax.axvspan(d2, d3, color='darkorange', alpha=0.3, lw=0,
           label='blanket symptomatic isolation + 13 days')
ax.legend(loc='lower left', fontsize=8)
fig.tight_layout()
```