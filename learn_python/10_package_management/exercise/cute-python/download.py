
import requests
def download():
    url = 'https://inews.co.uk/wp-content/uploads/2018/03/Nobody-expects-the-Spanish-Inquisition_.jpg'
    with open('cute-python.jpg', 'wb') as file:
        r = requests.get(url, allow_redirects=True)
        file.write(r.content)

if __name__ == '__main__':
    download()
