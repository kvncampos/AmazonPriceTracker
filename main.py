import AmazonScraper.amazon_scraper
from SMTP import gmail
from SMTP.creds import *
from datetime import datetime

ITEM_URL = f'https://www.amazon.com/TP-Link-EAP235-Wall-Beamforming-Installation-Integrated/dp/B08HSNYH57/ref' \
           f'=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=GaIRR&content-id=amzn1.sym.225b4624-972d-4629-9040-f1bf9923dd95' \
           f'%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=225b4624-972d-4629-9040-f1bf9923dd95&pf_rd_r' \
           f'=SK3CVS35Z7GH3QE5X8FB&pd_rd_wg=sF92Q&pd_rd_r=6d15b03b-009f-40d8-9221-fcb025e3463d&pd_rd_i=B08HSNYH57&th=1'

PRICE_TO_BEAT = 49.99
results = AmazonScraper.amazon_scraper.get_price(ITEM_URL)
outcome = AmazonScraper.amazon_scraper.test_for_sale(PRICE_TO_BEAT, results[1])

# --------------------------- SNMP MESSAGE SETUP -----------------------------------
# EMAIL MESSAGE STRUCTURE IN HTML
current_date = datetime.utcnow()
MESSAGE = f"""
<div>
<h3>{results[0]}</h3>
</div>
<div>
<h3>Looking for ${PRICE_TO_BEAT} or Lower</h4>
</div>
<div>
<h3>Current Price: ${results[1]}</h3>
</div>
<div>
<p>{ITEM_URL}</p>
</div>
<b>Ran on {current_date} </b
"""
if outcome:
    gmail.send_gmail(gmail_server=GMAIL_SERVER, from_email=FROM_ADDRESS, to_email=TO_ADDRESS,
                     subject=SUBJECT, password=PASSWORD, message=MESSAGE)
