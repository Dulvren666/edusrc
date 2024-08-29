
import  requests
from lxml import etree
for p in range(1,17):
    url = f'https://src.sjtu.edu.cn/rank/company/?page={p}'
    resp = requests.get(url).text
    html = etree.HTML(resp)
    for i in range(1,55):
        try:
            comp = html.xpath(f"//tr[{i}]/td[2]/a/text()")[0].strip()
            num  = html.xpath(f"//tr[{i}]/td[3]/text()")[0].strip()
            open("info.csv","a").write(f"{comp},{num}\n")
            print(comp)
        except:
            continue
