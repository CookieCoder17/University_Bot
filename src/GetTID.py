import json
import requests


class GetTID:
    '''
    Scraps a json page and returns the teacher id. Takes in a school's id as a parameter. 
    Takes the professors full name as a parameter for the get_TEACHER_id method and returns
    the professor's teacher id
    '''

    def __init__(self, id):
        self.id = id  # School's id

    def get_TEACHER_id(self, full_name):
        '''
        Takes in the professor's full name, scraps json page, and returns 
        the professor's teacher id
        '''

        url = "https://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=" + \
            full_name + "&queryoption=TEACHER&queryBy=schoolId&sid=" + \
            str(self.id)
        page = requests.get(url)
        professors_dict = json.loads(page.content)
        if len(professors_dict['professors']) == 0:
            return
        else:
            professor_tid = professors_dict['professors'][0]['tid']
            return professor_tid
