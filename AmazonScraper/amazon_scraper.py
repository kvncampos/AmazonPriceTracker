from bs4 import BeautifulSoup
import requests
from pprint import pp


def get_price(item_url: str) -> list:
    """
    Searches Price for Specified Item.
    :param item_url: item to search price
    :return: list = [title of item, float of current price]
    """
    item_url = item_url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'http://www.google.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }

    response = requests.get(item_url, headers=headers)

    wall_ap = response.text

    soup = BeautifulSoup(wall_ap, 'html.parser')
    # pp(soup)

    price = soup.find(name='span', class_="a-offscreen")
    title = soup.find(name='title')
    # Show Output
    print(title.get_text())
    print(price.get_text())

    tmp = price.get_text()
    stripped_price = tmp.split('$')

    return [title, float(stripped_price[1])]


def test_for_sale(price_to_beat: float, current_price: float) -> bool:
    if current_price < price_to_beat:
        print("LOW PRICE! Buy Now.")
        return True
    else:
        print("Item Not on Sale.")
        return False


def main():
    price = get_price(f'https://www.amazon.com/TP-Link-EAP235-Wall-Beamforming-Installation-Integrated' f'/dp'
                      f'/B08HSNYH57/ref=pd_ci_mcx_mh_mcx_views_0'
                      f'?pd_rd_w=GaIRR&content-id=amzn1.sym.225b4624-972d-4629-9040-f1bf9923dd95%3Aamzn1.symc'
                      f'.40e6a10e' f'-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=225b4624-972d-4629-9040-f1bf9923dd95'
                      f'&pf_rd_r' f'=SK3CVS35Z7GH3QE5X8FB&pd_rd_wg=sF92Q&pd_rd_r=6d15b03b-009f-40d8-9221-fcb025e3463d'
                      f'&pd_rd_i' f'=B08HSNYH57&th=1')

    print('--- Testing Higher Price ---')
    test_for_sale(19.99, price[1])

    print('--- Testing Lower Price ---')
    test_for_sale(199.99, price[1])


if __name__ == '__main__':
    main()
