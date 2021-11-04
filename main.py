import web_scrap
import os
from flask import Flask, request, Response

"""Amazon Headers """
amazon_headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }




app = Flask(__name__)

"""Export SLACK Webhook Secret in environment Variable
   USAGE:
   export SLACK_WEBHOOK_SECRET='Value'
"""
SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')


@app.route('/find', methods=['POST'])
def find():
    if request.method == 'POST':
        data = request.form
        prd_name = data.get('text')
        username = data.get('user_name')
        print(prd_name)
        web_scrap.amazon(prd_name, amazon_headers)
        return "Success", 200
    else:
        print("Please use POST Method")


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    """ Run the  Flask Application"""
    app.debug = True
    app.run(host="0.0.0.0")