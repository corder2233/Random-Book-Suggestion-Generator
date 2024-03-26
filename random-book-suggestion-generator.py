import requests

def random_book_suggestion():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        book_data = data["data"]
        book_name = book_data["volumeInfo"]["title"]
        book_titel = book_data["volumeInfo"]["subtitle"]
        book_author = book_data["volumeInfo"]["publisher"]

        return book_name, book_titel, book_author
        # return book_name
    else:
        raise Exception("Invalid fatch")
    

def main():
    try:
        bookname, booktitel, bookauthor = random_book_suggestion()
        print(f"Book Name: {bookname} \n Titel: {booktitel} \n Author: {bookauthor}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
    
