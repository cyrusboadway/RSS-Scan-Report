'''
Created on Mar 5, 2012

@author: cyrusboadway
'''


class RSSScanReport:

    """
    Configure the RSS scraper with the url
    and report contact details.
    """
    def __init__(self, emailName, emailAddress, rssUrl, rssUser, rssPassword):

        self.__emailName = emailName
        self.__emailAddress = emailAddress
        self.__rssUrl = rssUrl
        self.__rssUser = rssUser
        self.__rssPassword = rssPassword


    """
    Run this bastard.
    """
    def run(self):
        return


    """
    Call the RSS feed, parse unique nodes. 
    """
    def __fetch(self):
        return


    """
    Check the string against the possible
    
    """
    def __match(self):
        return


    """
    Check the local db to verify that the
    particular match hasn't already been
    handled. If not previously matched,
    stores the match event and returns
    true, otherwise returns false.
    """
    def __newMatch(self, uniqueid):
        return


    """
    Notify the user about the link. 
    """
    def __email(self, content, url):
        return