from pypdf import PdfReader
from pathlib import Path
import os

class course:
    def __init__(self, subject, course_title, course_code, instructor, exam_dates):
        self.subject = subject
        self.course_title = title
        self.course_code = 000
        self.instructor = professor
        self.exam_dates = [] 

    def find_file(self):
        download_folder = Path.home() / "Downloads"
        contents = sorted(download_folder.iterdir(), key=lambda x: x.stat().st_mtime)
        latest = contents[-1]
        latest = str.latest
        if '.pdf' not in latest:
            raise Exception("File provided is not a pdf")
        return latest

    # maybe not latest, what if we want to instantiate multiple without having to download in order??? idk

    def initialize_course(self, subject, course_title, course_code, instructor, exam_dates, latest):  #the purpose of this is to do the initial parsing of the pdf or whatever that you download

        download_folder = Path.home() / "Downloads"
        os.chdir(download_folder)
        # creating a pdf reader object
        reader = PdfReader("Syllabus-MEEN357-Sec501_Spring2024.pdf")
        # printing number of pages in pdf file
        print(len(reader.pages))
        docsize = len(reader.pages)
        # getting a specific page from the pdf file
        pages = []

        for page in reader.pages:
            text = page.extract_text()
            text = text.split()
            current_page = []

            for word in text:
                current_page.append(word)

            pages.append(current_page)

        print(pages)

        #print(len(numbers))

        #print(len(numbers)-1)

        upper_bound = (len(numbers)-3)




        for value in range(len(numbers)):
            if value + 3 < upper_bound:
                sub_list = []
                sub_list.append(numbers[value])
                sub_list.append(numbers[value+1])
                sub_list.append(numbers[value+2])
                sub_list.append(numbers[value+3])
                if 9 in sub_list:
                    print (sub_list)
                    break


            else:
                break

    def confirm_course_data(self): #the purpose of this is to allow the user an opportunity to confirm the data as correct

    def get_file_data(self):  #the purpose of this is to get the file data anytime we use the programm