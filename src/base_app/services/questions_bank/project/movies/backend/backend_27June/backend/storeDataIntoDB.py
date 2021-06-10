from . bookmyshow_bnglr import process_movie_page


SOURCE = 'https://in.bookmyshow.com/bengaluru/movies'



if __name__ == "__main__":

    process_movie_page(SOURCE)
    print("completed the execution")
