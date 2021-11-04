import requests
from bs4 import BeautifulSoup
import slack_bot

def amazon(name, headers):
    """ Amazon Product Price will published to the Slack Channel
    """
    product_name = name
    align1 = product_name.title()
    align1 = align1.replace(' ', '+')
    home = 'https://www.amazon.in'
    k = ""
    v = ''
    res = requests.get(f'https://www.amazon.in/s?k={align1}', headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    for html in soup.find_all('div', {'class': 'sg-col-inner'}):
        for heading,p in zip(html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}), html.find_all('span', {'class': 'a-price-whole'})):
                title = heading.text + ","
                price = p.text + ""
                price = price.replace(",", "")
                # price = float(price)
                keys = title.split("(")
                values = price.split(" ")
                dictionary1 = {}
                dictionary1 = dict(zip(keys, values))
                k,v  = list(dictionary1.items())[0] 
                # print(v)
    total = "Amazon Product Name :", name,"\nPrice : Rs.",v
    final1 = ' '.join(total)
    slack_bot.post_to_slack(final1)
    # print(final1)      
       
             
            
                
                

def flipkart(name):
    pass



            
        
