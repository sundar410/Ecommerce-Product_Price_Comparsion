import requests
from bs4 import BeautifulSoup
import slack_bot

def amazon_search(name, headers):
    """ Based on the Slack Input it will list of product from the amazon and posted the result in the slack channel
    """
    product_name = name
    align1 = product_name.title()
    align1 = align1.replace(' ', '+')
    res = requests.get(f'https://www.amazon.in/s?k={align1}', headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    for html in soup.find_all('div', {'class': 'sg-col-inner'}):
        for heading,p in zip(html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}), html.find_all('span', {'class': 'a-price-whole'})):
                title = heading.text + ","
                price = p.text + ""
                price = price.replace(",", "")
                total = "Amazon Product Name :", title,"\nPrice : Rs.",price
                final1 = ' '.join(total)
                # slack_bot.post_to_slack(final1)
                print(final1) 
                            
def amazon_lowest(name, headers):
    """Based on the Slack input it will posted lowest product on amazon to the Slack channel"""
    product_name = name
    align1 = product_name.title()
    align1 = align1.replace(' ', '+')
    res = requests.get(f'https://www.amazon.in/s?k={align1}', headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    value = []
    for html in soup.find_all('div', {'class': 'sg-col-inner'}):
        for heading,p in zip(html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}), html.find_all('span', {'class': 'a-price-whole'})):
                title = heading.text + ","
                price = p.text + ""
                price = price.replace(",", "")
                price = float(price)
                print(price)
                value.append(price)
    print(value)            
    value.sort()
    low = value[0]
    low= str(low)
    print("Lowest: " , low)
    final = "Amazon Lowest Product: ", name , "\nPrice: Rs." ,low
    final = ' '.join(final)
    slack_bot.post_to_slack(final)
    print(final)
                
    
                



def flipkart(name):
    pass



            
        
