#-*-encoding:utf8-*-
from requests_html import HTMLSession,HTML

import asyncio
import requests

async def render_page(r):
    while True:
        try:
            await r.page.click('li.btn-link')
        except:
            break
        content = await r.page.content()
    html = HTML(url=r.url, html=content.encode('utf8'), default_encoding='utf8')    
    r.__dict__.update(html.__dict__)
    ret = []
    ret1 = []
    print (r.absolute_links)
    ele = r.find('span.read-count')
    print (ele)
    for k in ele:
        ret.append(k.text)
    ele1 = r.find('a.chapter-item')
    for k in ele1:
        ret1.append(list(k.absolute_links)[0])
    return ret,ret1

def main():
    url = 'https://read.douban.com/column/7709247/'
    sess = HTMLSession()
    r = sess.get(url)
    r.html.render(keep_page=True)
    loop = asyncio.get_event_loop()
    ret = loop.run_until_complete(render_page(r.html))
    print (ret)
if __name__ == '__main__':
    main()
