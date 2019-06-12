import feedparser
import datetime
import Metabolon_RSS_Feed as feed

def main():
    days = 5
    dict = build_test_dict()
    feed.RSS_Feed(dict, days)

def build_test_dict():
    dict = {'Reddit': 'http://www.reddit.com/.rss', 
            'Bill Maher': 'http://billmaher.hbo.libsynpro.com/rss',
            'Craigslist': 'https://www.craigslist.org/about/best/all/index.rss'
            }
    return dict


if __name__ == "__main__":
    main()