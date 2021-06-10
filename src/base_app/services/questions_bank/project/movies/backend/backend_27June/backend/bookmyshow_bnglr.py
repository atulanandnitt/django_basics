from bs4 import BeautifulSoup as Soup
import requests
from . db_api import get_movie_db_session
from . db_api import Movie
from . db_api import Theaters
import time
from . soup_creation import get_page_contents
from . soup_creation import get_movie_page_contents
from . price_details import get_particular_movie_booking_link_from_price_details
from . price_details import get_all_theater_of_particular_movie_from_price_details
# cd PycharmProjects/MyProject
#env / bin / activate
#(venv) atul@atul-HP-Pavilion-15-Notebook-PC:~/PycharmProjects$ python -m  bookmyshow.bookmyshow_bnglr

#mysql -u root -p   show databases; show tables
#select * from  movie_atul_4 where movie_name like "%Aven%";





"""

def parse_particular_movie_content(particular_movie_content):
    theaters = particular_movie_content.find('cookieUserCine')
    #print("theaters",theaters)

    return theaters
    #cookieUserCine
"""
def get_movie_name(name_content):
    """
    Get movie name
    :param name_content: Soup object
    :return: str: Movie Name
    """
    name_content = name_content.find('a', {'class': '__movie-name'})

    try:
        return name_content.getText().strip()
    except:
        return None

def get_movie_dimension(movie_container):
    """

    :param movie_container:
    :return:
    """
    exp_list = list()
    experience = movie_container.find('div', {'class': 'experience-holder'})

    exp_list_content = experience.find_all('div', {'class':'experience-list'})

    for item in exp_list_content:
        text = item.getText().strip()

        if text:
            exp_list.append(text[-2:])
    dimensions=",".join(exp_list)

    if dimensions:
        return dimensions
    else:
        return "By default 2D"

def get_show_times(movie_container):
    """

    :param movie_container:
    :return:
    """





def get_movie_ref_link(name_content):
    """
    Get Movie detail link
    :param name_content:  Soup object
    :return: URL link
    """
    link  = name_content['href'].strip()

    if link:
        return link
    else:
        return None

def get_language_str(language_content):
    """
    Get list of language for given Movie
    :param language_content: Soup Object
    :return: List of language

    """
    lang_list = list()
    language_tag = language_content.find('div', {'class':'languages'})
    language=language_tag.find_all('li', {'class': '__language'})

    for item in language:
        text = item.getText().strip()
        if item:
            lang_list.append(text)

    lang_str=",".join(lang_list)
    return lang_str


def get_movie_genere(movie_content):
    """


    :param movie_content:
    :return:
    """
    tag_list=list()
    details_tag = movie_content.find('div',{'class':'genre-list'})
    details=details_tag.find_all('div',{'class' : '__rounded-box __genre'})

    for item in details:
        text = item.getText().strip()
        if item:
            tag_list.append(text)

    tag_str=",".join(tag_list)
    return tag_str

def get_particular_movie_link(movie_content):
    """

    :param movie:
    :return:
    """
    url_for_movie = movie_content.find('a', {'class': '__movie-name'})
    full_url="https://in.bookmyshow.com"+url_for_movie['href']
    #print(name_content['href'])

    return full_url

def get_particular_movie_booking_link(particular_movie_link):
    if particular_movie_link:
        booking_link = get_particular_movie_booking_link_from_price_details(particular_movie_link)

    return booking_link


def get_all_theaters_of_particular_movie(particular_movie_link):
    if particular_movie_link:
        booking_link = get_all_theater_of_particular_movie_from_price_details(particular_movie_link)

    return booking_link


def add_movie_atul(movie_entry, session=None):
    """
    :param movie_entry: Dictionary having movie related details
    Add movie table entry
    :return: None
    """
    #print("movie_entry : ", movie_entry)
    if session is None:
        session = get_movie_db_session()


    session.add(movie_entry)
    session.commit()#ACID

def parse_content(html_content):
    listOfAllMovieLinks=[]
    """
    Function parses html content to get required data from the
    web object
    :param html_content: html parsed content
    :return: movie_list: list of dict:movie_dict, dictionary having movie name, type and published date
    """
    movie_list = list()
    table_content = html_content.find('div', {'class': 'mv-row'})

    movie_container_list = table_content.find_all(
        'div', {'class':'wow fadeIn movie-card-container'})


    #print(movie_container_list)
    for movie_container in movie_container_list:
        movie_dict = {}

        detail = movie_container.find('div', {'class':'detail'})
        movie_dict['movie_name'] = get_movie_name(detail)
        movie_dict['movie_languages'] = get_language_str(movie_container)
        movie_dict['movie_genere'] = get_movie_genere(movie_container)

        movie_dict['data_dimension']= get_movie_dimension(movie_container)

        movie_dict['particular_movie_link'] = get_particular_movie_link(movie_container)
        listOfAllMovieLinks.append(movie_dict['particular_movie_link'])
        movie_dict['particular_movie_booking_link'] = get_particular_movie_booking_link(movie_dict['particular_movie_link'])
        movie_dict['all_theaters'] = get_all_theaters_of_particular_movie(
            movie_dict['particular_movie_booking_link'])

        movie_content=get_page_contents(movie_dict['particular_movie_link'])

        #movie_dict['theater'] = parse_particular_movie_content(movie_content)

        print("movie_dict : ", movie_dict)
        movie_list.append(movie_container)
        entry = Movie(
            movie_name=movie_dict['movie_name'] ,
            movie_languages=movie_dict['movie_languages'] ,
            movie_genere=movie_dict['movie_genere'],
            data_dimension=movie_dict['data_dimension'],
            particular_movie_link=movie_dict['particular_movie_link'],
            theater=movie_dict['theater']
        )

        #print(entry)
        print("uncomment to insert data into DB atul")
        break
        #add_movie_atul(entry)
        #time.sleep(1)
    """
    movie_genere_raw = ['Biography1', 'Biography2', 'Biography3']
    movie_genere_processed = ",".join(movie_genere_raw)
    entry3 = Movie(
        movie_name='NadiyaKePar',
        movie_genere=movie_genere_processed,
        movie_languages='English',
        theater='forum',
        particular_movie_link='bengaluru/movies/coco/ET00052365',
        data_dimension='3D'
    )
    
    add_movie_atul(entry3)
    """
    print("listOfAllMovieLinks",listOfAllMovieLinks)
    return movie_list


def process_movie_page(source):
    """
    Main function which process web page and
    display page content
    :return:
    """

    content = get_page_contents(source)
    movies = parse_content(content)
    #print("list of all movies : ", movies)
    #return listOfAllMovieLinks

"""

if __name__ == "__main__":

    process_movie_page(source)
"""