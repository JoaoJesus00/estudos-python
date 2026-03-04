from urllib.request import urlopen, Request
import ssl


context = ssl._create_unverified_context()
try:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req, timeout=10, context=context) as resp:
        if resp.getcode() == 200:
            print('\033[0;34mSite acessível\033[m')
except Exception as e:
    print(f'\033[0;31mSite inacessível, Motivo: {e.__class__}\033[m')