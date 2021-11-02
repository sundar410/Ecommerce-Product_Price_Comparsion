import requests
from bs4 import BeautifulSoup

def amazon(name, headers):
    
    product_name = name
    align1 = product_name.title()
    spacing  = align1.replace(" ", "+")
    # print(web_scrap.amazon(product_name, headers))
    import requests
    from bs4 import BeautifulSoup
    # product_name = product_name.replace(' ', '+')
    res = requests.get(f'https://www.amazon.in/s?k={align1}', headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    for html in soup.find_all('div', {'class': 'a-section'}):
        title = None
        for heading,p in zip(html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}), html.find_all('span', {'class': 'a-price-whole'})):
                title = heading.text
                price = p.text
                print("Product Name :",title,"\n Price : Rs.",price)
def flipkart(name):
    pass



            
        
