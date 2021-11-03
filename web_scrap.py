import requests
from bs4 import BeautifulSoup
import slack_bot
def amazon(name, headers):
    product_name = name
    align1 = product_name.title()
    res = requests.get(f'https://www.amazon.in/s?k={align1}', headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    for html in soup.find_all('div', {'class': 'a-section'}):
        title = None
        for heading,p in zip(html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}), html.find_all('span', {'class': 'a-price-whole'})):
                title = heading.text
                price = p.text
                total = "Product Name :",title,"\n Price : Rs.",price
                final1 = ' '.join(total)
                slack_bot.post_to_slack(final1)   
                            
def flipkart(name):
    pass



            
        
