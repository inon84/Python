from flask import Flask, render_template, request
import requests
from io import StringIO
import csv

app = Flask(__name__)

def fetch_app_ads_txt(url):
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'https://' + url
    if not url.endswith('/app-ads.txt'):
        url += '/app-ads.txt'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching app-ads.txt: {e}"

def parse_app_ads_txt(content):
    reader = csv.reader(StringIO(content), delimiter=',')
    highlighted_domains = [
        "startapp.com, 150291354",
        "start.io, 150291354",
        "pubmatic.com, 157559, RESELLER, 5d62403b186f2ace",
        "pubnative.net, 1007349, RESELLER, d641df8625486a7b",
        "Verve.com, 15503, RESELLER, 0c8f5958fc2d6270",
        "pubnative.net, 1008289, RESELLER, d641df8625486a7b",
        "google.com, pub-4236520483129668, DIRECT, f08c47fec0942fa0",
        "pubmatic.com, 160233, RESELLER, 5d62403b186f2ace",
        "yahoo.com, 50987, RESELLER",
        "pubmatic.com, 161162, RESELLER, 5d62403b186f2ace",
        "conversantmedia.com, 100339, RESELLER, 03113cd04947736d",
        "appnexus.com, 4052, RESELLER",
        "opera.com, pub5925993551616, RESELLER, 55a0c5fd61378de3",
        "outbrain.com, 002d7f7ba0bd74452f2b155d0dfb5cd6c8, RESELLER",
        "contextweb.com, 562791, RESELLER, 89ff185a4c4e857c",
        "rubiconproject.com, 24400, DIRECT, 0bfd66d529a55807",
        "pubmatic.com, 163420, RESELLER, 5d62403b186f2ace",
        "contextweb.com, 562669, RESELLER, 89ff185a4c4e857c",
        "video.unrulymedia.com, 2464975885, RESELLER",
        "target.my.com, 13033031, DIRECT",
        "conversantmedia.com, 100269, RESELLER, 03113cd04947736d",
        "yahoo.com, 59338, RESELLER",
        "yeahmobi.com, 114122, RESELLER",
        "pubmatic.com, 161136, RESELLER, 5d62403b186f2ace",
        "loopme.com, 11318, RESELLER, 6c8d5f95897a5a3b",
        "ssp.e-volution.ai, AJxF6R118a9M6CaTvK, RESELLER",
        "lunamedia.io, 2fb901cd79f4453b90b68bee79da71b5, RESELLER, 524ecb396915caaf",
        "advlion.com, 3083, RESELLER",
        "lijit.com, 420355, RESELLER, fafdf38b16bf6b2b",
        "minutemedia.com, 01gjjdge6zcz, RESELLER",
        "iqzone.com, IQ154, RESELLER",
        "adcolony.com, c7b2bb9f944ae42a, RESELLER, 1ad675c9de6b5176",
        "meitu.com, 755, RESELLER",
        "pubmatic.com, 157654, RESELLER, 5d62403b186f2ace",
        "openx.com, 540899687, RESELLER, 6a698e2ec38604c6",
        "inmobi.com, 3d54d7dda27a4552a8184e9120251b9f, RESELLER, 83e75a7ae333ca9d",
        "themediagrid.com, 6XGFYQ, DIRECT, 35d5010d7789b49d",
        "acexchange.co.kr, 1746357004, RESELLER",
        "adiiix.com, par-AA7B236BA32DD484C838E249362437B8, RESELLER",
        "aralego.com, par-AA7B236BA32DD484C838E249362437B8, RESELLER",
        "ucfunnel.com, par-AA7B236BA32DD484C838E249362437B8, RESELLER",
        "bematterfull.com, 22289765, RESELLER",
        "outbrain.com, 0023749a2264ea0429a71b54ac9ca0de9a, RESELLER",
        "appnexus.com, 7597, RESELLER, f5ab79cb980f11d1",
        "sonobi.com, 1cdc3b298d, RESELLER, d1a215d9eb5aee9e",
        "vidoomy.com, 5053058, RESELLER",
        "zmaticoo.com, 114122, RESELLER",
        "pubmatic.com, 156517, RESELLER, 5d62403b186f2ace",
        "smartadserver.com, 4655, RESELLER, 060d053dcf45cbf3",
        "mgid.com, 782767, RESELLER, d4c29acad76ce94f",
        "rubiconproject.com, 9655, RESELLER, 0bfd66d529a55807",
        "pubmatic.com, 161673, RESELLER, 5d62403b186f2ace",
        "rubiconproject.com, 14558, RESELLER, 0bfd66d529a55807",
        "inmobi.com, 12a9a79d60214a40a444a6103b81747c, RESELLER, 83e75a7ae333ca9d",
        "inmobi.com, 22e5354e453f49348325184e25464adb, RESELLER, 83e75a7ae333ca9d",
        "inmobi.com, 300bb0e4e3704cd495136c09d57448b9, RESELLER, 83e75a7ae333ca9d",
        "inmobi.com, 3a4f7da341dd490cbb7dde02b126275e, RESELLER, 83e75a7ae333ca9d",
        "webeyemob.com, 70171, RESELLER",
        "openx.com, 540679900, RESELLER, 6a698e2ec38604c6",
        "pubmatic.com, 158060, RESELLER, 5d62403b186f2ace",
        "conversantmedia.com, 100358, RESELLER, 03113cd04947736d",
        "smartadserver.com, 4573, RESELLER, 060d053dcf45cbf3",
        "outbrain.com, 00dbc7a68d0cd51d55ac0aa9e1918c9a34, RESELLER",
        "pubmatic.com, 163476, RESELLER, 5d62403b186f2ace",
        "pubmatic.com, 161151, RESELLER, 5d62403b186f2ace",
        "pubmatic.com, 162588, RESELLER, 5d62403b186f2ace",
        "pubmatic.com, 163120, RESELLER, 5d62403b186f2ace",
        "gitberry.com, 405100012, RESELLER",
        "rubiconproject.com, 24362, RESELLER, 0bfd66d529a55807",
        "inmobi.com, edd282ac8f29464792bf2b7f3df2f9df, RESELLER, 83e75a7ae333ca9d",
        "inmobi.com, 38e36193f3c944d0b6254c71e511041b, RESELLER, 83e75a7ae333ca9d",
        "toponad.com, 164b751901a8b7, RESELLER, 1d49fe424a1a456d",
        "pubmatic.com, 162968, RESELLER, 5d62403b186f2ace",
        "loopme.com, 11635, RESELLER, 6c8d5f95897a5a3b",
        "vidoomy.com, 7646534, RESELLER",
        "conversantmedia.com, 100569, RESELLER, 03113cd04947736d",
        "adelement.com, 36011, RESELLER",
        "adelement.com, 36012, RESELLER",
        "Pubnative.net, 1008770, RESELLER, d641df8625486a7b",
        "ushareit.com, LC2d7ebe00c3f9364a, RESELLER",
        "webeyemob.com, 70121, RESELLER",
        "loopme.com, 11633, RESELLER, 6c8d5f95897a5a3b",
        "lenovoads.com, 4000, RESELLER",
        "smartyads.com, 100016, RESELLER, fd2bde0ff2e62c5d",
        "inmobi.com, 95ef2003a2c742db81a45303d6e4cf8b, RESELLER, 83e75a7ae333ca9d",
        "video.unrulymedia.com, 251620492, RESELLER",
        "smartadserver.com, 4728, RESELLER, 060d053dcf45cbf3",
        "advangelists.com, a5cdd4aa0048b187f7182f1b9ce7a6a7, RESELLER, 60d26397ec060f98",
        "rubiconproject.com, 25978, RESELLER, 0bfd66d529a55807",
        "rubiconproject.com, 25482, RESELLER, 0bfd66d529a55807",
        "indexexchange.com, 206797, RESELLER, 50b1c356f2c5c8fc",
        "rubiconproject.com, 24400, RESELLER, 0bfd66d529a55807",
        "rubiconproject.com, 15278, RESELLER, 0bfd66d529a55807",
        "openx.com, 559912325, DIRECT, 6a698e2ec38604c6"
    ]

    matching_lines = []
    missing_lines = []

    for line in reader:
        if line and not line[0].startswith('#'):
            line_data = line[:3]
            if line[:2] in [entry.split(",")[:2] for entry in highlighted_domains]:
                line_data.append("highlight")
                matching_lines.append(line_data)
            else:
                missing_lines.append(line_data)

    return matching_lines, missing_lines

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        app_ads_txt_content = fetch_app_ads_txt(url)
        if not app_ads_txt_content.startswith("#"):
            return render_template('index.html', error="Invalid app-ads.txt format")

        app_ads_txt_data = parse_app_ads_txt(app_ads_txt_content)
        return render_template('index.html', data=app_ads_txt_data)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
