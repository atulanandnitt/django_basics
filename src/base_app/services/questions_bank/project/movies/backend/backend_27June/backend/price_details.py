from . soup_creation import get_page_contents
from urllib.parse import urljoin


def get_absolute_url(base_url, url):
    """

    :param base_url:
    :param url:
    :return:
    """
    return urljoin(base_url, url)


def parse_content_to_get_booking_link(html_content):
    booking_link_detailed_data = html_content.find('div', {'class': 'more-showtimes'})
    booking_link_detailed_data_a = booking_link_detailed_data.find('a')
    #print("booking_link_detailed_data ***************", booking_link_detailed_data)
    booking_relative_link =booking_link_detailed_data_a["href"]
    #print("url_2",booking_relative_link)
    return booking_relative_link

def find_movie_ticket_details(theater_ticketDetails_data_list):
    """

    :param theater_ticketDetails_data_list:
    :return:
    """
    print("inside find_movie_ticket_details ************************************************************ ")
    ticket_details_list = list()

    #print("theater_ticketDetails_data_list : ", theater_ticketDetails_data_list)
    for item in theater_ticketDetails_data_list:
        ticket_details = {}
        show_Details = item.find('a', {'class':'__showtime-link time_vrcenter '})

        if show_Details is not None:
            ticket_details["show_Time"] = show_Details['data-display-showtime']
            ticket_details["ticket_prices"] = show_Details['data-cat-popup']
            ticket_details["dummy_ticket_prices"]= 5
            ticket_details_list.append(ticket_details)

    print(ticket_details_list)

    return ticket_details_list



def parse_content_to_get_theater(html_content):
    theater_detailed_data = html_content.find('ul', {'id' :'venuelist'})
    theater_container_list = theater_detailed_data.find_all('li',{'class':'list '})
    theater_name_list=[]

    for theater_container in theater_container_list:
        theater_dict={}
        theater_dict["theater_name"] = theater_container['data-name']
        theater_dict["theater_location_lat"] = theater_container['data-lat']
        theater_dict["theater_location_lng"] = theater_container['data-lng']

        theater_ticketDetails_data_list = theater_container.find_all('div', {"data-online":"Y"})
        theater_dict["movie_ticket_details"] = find_movie_ticket_details(theater_ticketDetails_data_list)

        #print("theater_dict ::: ",theater_dict)
        theater_name_list.append(theater_dict["theater_name"])
        theater_name_list.append('\n')
    #print("url_2",booking_relative_link)
    #print("theater_container_list_data ::::::",theater_dict)
    #return theater_dict["theater_name"]
    return theater_name_list



def get_particular_movie_booking_link_from_price_details(particular_movie_link):
    """

    :param particular_movie_link:
    :return:
    """
    if particular_movie_link:
        content = get_page_contents(particular_movie_link)
        booking_relative_link = parse_content_to_get_booking_link(content)
        base_url="https://in.bookmyshow.com/"
        booking_link = get_absolute_url(base_url, booking_relative_link)

    return booking_link


def get_all_theater_of_particular_movie_from_price_details(particular_movie_link):
    """

    :param particular_movie_link:
    :return:
    """
    if particular_movie_link:
        content = get_page_contents(particular_movie_link)
        all_theater = parse_content_to_get_theater(content)

    return all_theater










