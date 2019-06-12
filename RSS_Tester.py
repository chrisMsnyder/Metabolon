import feedparser
import datetime
import Metabolon_RSS_Feed as feed

def main():
    num_days = 'hello'
    dict = build_test_dict()
    print(feed.RSS_Feed(dict, num_days))

def build_test_dict():
    dict = {'Reddit': ['http://www.reddit.com/.rss'], 
            'Bill Maher': ['http://billmaher.hbo.libsynpro.com/rss'],
            'Craigslist': ['https://www.craigslist.org/about/best/all/index.rss'],
            'ESPN': ['https://www.espn.com/espn/rss/news', 
                     'http://www.espn.com/espn/rss/nfl/news', 
                     'http://www.espn.com/espn/rss/nba/news'
                     ],
            'Fox News': ['https://www.foxnews.com/about/rss/.rss']
            }
    return dict


if __name__ == "__main__":
    main()