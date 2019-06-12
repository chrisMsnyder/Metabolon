import feedparser
import datetime

######################################################################################
#
# RSS_Feed(company_dict, num_days)
#
# Purpose:
#   This function takes in a dict of companies and an integer of days and iterates over
#   the RSS feeds within the dict and determines if any of them have been modified within
#   the number of days passed as a parameter and returns a list of all the companies that
#   have no activity within the specified number of days.
#
# Parameters:
#   company_dict    - Dictionary object keyed by company names and valued by RSS Feed URLs
#   num_days        - integer that determines number of days to search through for activity
#
# Returns:
#   List of companies that have no activity within the specified number of days
#
#######################################################################################

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