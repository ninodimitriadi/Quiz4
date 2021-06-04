import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint


f = open('books.csv', 'w', encoding='UTF-8_sig', newline='\n')
file_obj = csv.writer(f)
file_obj.writerow(['სათაური', 'ავტორი', 'ფასი'])

payload = {'swoof': '1', 'top_category': 'proza-thargmnili', 'paged': 1}
url = 'https://www.sulakauri.ge/wignebi/'

while payload['paged'] <= 16:
    r = requests.get(url, params=payload)
    content = r.text


    soup = BeautifulSoup(content, 'html.parser')
    main_block = soup.find('div', class_='mkdf-pl-main-holder')
    all_books = main_block.find_all('div', class_='mkdf-pl-text-wrapper')



    for each in all_books:
        author = each.find('div', class_='mkdf-pl-author-holder').text
        title = each.h5.a.text
        price = each.find('span', class_='woocommerce-Price-amount amount').bdi.text
        file_obj.writerow([title, author, price])

    payload['paged'] += 1
    sleep(randint(15, 20))


f.close()
