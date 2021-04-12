from bs4 import BeautifulSoup
import requests
import schedule

def bot_send_text(bot_message):

    bot_token= '1766341912:AAHlMEOaPKwGXltXkc6fz-hrNlbegloCMjE'
    bot_chatID = '1300756765'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def dlr_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    format_result = result.text

def report():
    dlr_price = f'El precio del Dolar es de {dlr_scraping()}'
    bot_send_text(dlr_price)

    return format_result


if __name__ == '__main__':
    schedule.every().day.at('15:46').do(report)

    while True:
        schedule.run_pending()


