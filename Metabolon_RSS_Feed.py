import feedparser
import datetime

def RSS_Feed(company_dict, num_days):
    delta = datetime.timedelta(days=num_days)
    now_datetime = datetime.datetime.now() - delta
    now_datetime = now_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    print(now_datetime)

    for company in company_dict:
        feed = feedparser.parse(company_dict[company])

        for f in feed.entries:
            date = f.updated
            date = date[:-6]
            #print(f.title, '\n', date)

        print('\n\n')