import feedparser
import datetime

######################################################################################
#
# RSS_Feed(company_dict, num_days)
#
# Purpose:
#   This function takes in a dict of companies and an integer of days and iterates over
#   the entries within each of the RSS feeds within the dict and determines if any of them 
#   have been modified within the number of days passed as a parameter and returns a list 
#   of all the companies that have no activity within the specified number of days.
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
    # check if parameters are correct type
    if not type(company_dict) is dict:
        print('Exiting program: Incorrect Parameter 1, please make sure a dictionary is passed')
        exit()
    if not type(num_days) is int:
        print('Exiting program: Incorrect Parameter 2, please make sure an integer is passed')
        exit()

    #establish a date to check against using the durrent date minue the num_days value
    delta = datetime.timedelta(days=num_days)
    now_datetime = datetime.datetime.now() - delta
    check_datetime = now_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    no_activity_list =[]

    #iterate over each company within the dict
    for company in company_dict:
        found = False
        #iterate over each rss feed url within the list value of the dict
        for url in company_dict[company]:
            feed = feedparser.parse(url)

            if len(feed.entries) == 0:
                print("No entries found under RSS feed \'" + str(url) + "\'")
                found = True
                continue

            #iterate over each entry within the rss feed url
            for f in feed.entries:
                date = f.updated
                date = date[:-6]
                #check if the modified date of the entry is within the specified time
                if date > check_datetime:
                    found = True
                    break
            if found == True:
                break
        if found == False:
            no_activity_list.append(company)
    return(no_activity_list)