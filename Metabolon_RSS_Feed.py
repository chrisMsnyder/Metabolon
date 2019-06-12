import feedparser
import datetime

def main():
    dict = build_test_dict()
    RSS_Feed(dict)

def build_test_dict():
    dict = {'Reddit': 'http://www.reddit.com/.rss', 
            'Bill Maher': 'http://billmaher.hbo.libsynpro.com/rss',
            'Craigslist': 'https://www.craigslist.org/about/best/all/index.rss'
            }
    return dict

def RSS_Feed(company_dict):
    now_datetime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    for company in company_dict.values():
        feed = feedparser.parse(company)

        for f in feed.entries:
            date = f.updated
            date = date[:-6]
            print(f.title, '\n', date)

        print('\n\n')

if __name__ == "__main__":
    main()