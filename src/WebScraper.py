import requests
import bs4
from bs4 import BeautifulSoup
from GetTID import GetTID as gtid


class WebScraper:
    '''
    Takes in a professor's full name. Uses the GETTID class 
    to extract the teacher's id. Then through the BeautifulSoup library 
    it extracts data from HTML pages through their class tags. Each method 
    returns a different piece of information on the professor
    '''

    def __init__(self, name):
        self.name = name  # name of professor
        self.uni = gtid(957)  # Replace with your school's id
        self.url = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + \
            str(self.tid())
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.content, features="html.parser")

    def tid(self):
        self.prof_tid = self.uni.get_TEACHER_id(self.name)
        if self.prof_tid == None:
            return "404-Not Found"
        return self.prof_tid

    def professorDescription(self):
        '''
        Returns the professor's full description: The Department & School
        '''
        return str(self.soup.find(class_="NameTitle__Title-dowf0z-1 iLYGwn").get_text())

    def professorName(self):
        '''
        Returns the professor's full name
        '''
        return str(self.soup.find(class_="NameTitle__Name-dowf0z-0 cfjPUG").get_text())

    def num_of_ratings(self):
        '''
        Returns the professor's number of student ratings
        '''
        return str(self.soup.find(class_="TeacherRatingTabs__StyledTab-pnmswv-2 bOzrdx react-tabs__tab--selected").get_text().split()[0])

    def overall_rating(self):
        '''
        Returns the professor's overall rating (Out of 5)
        '''
        return str(self.soup.find(class_="RatingValue__Numerator-qw8sqy-2 liyUjw").get_text())

    def would_take_again(self):
        '''
        Returns the student's recommendation to take the course by percentage
        '''
        return str(self.soup.find_all(class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs")[0].get_text())

    def lvl_of_diff(self):
        '''
        Returns the professor's level of academic difficulty (Out of 5)
        '''
        try:
            return str(self.soup.find_all(class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs")[1].get_text())
        except:
            return None
            raise

    def top_tags(self):
        '''
        Returns the student's top tags on the professor
        '''
        tags = self.soup.find_all('span', class_="Tag-bs9vf4-0 hHOVKF")
        tag_list = []
        for tag in range(len(tags)):
            if len(tag_list) > 5:
                break
            else:
                tag_list.append(tags[tag].text)
        return tag_list

    def top_comment(self):
        '''
        Returns the top student's comment on the professor
        '''
        return str(self.soup.find(class_="Comments__StyledComments-dzzyvm-0 gRjWel").get_text())

    def get_link(self):
        '''
        Returns the link for the professor's website 
        '''
        return self.url
