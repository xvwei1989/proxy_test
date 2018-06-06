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
        await content = r.page.content()
    html = HTML(url=r.url, html=content.encode('utf8'), default_encoding='utf8')    
    r.__dict__.update(html.__dict__)
    return r.links

def main():
    url = ''
    sess = HTMLSession()
    r = sess.get(url)
    r.html.render(keep_page=on)
    loop = asyncio.get_event_loop()
    ret = loop.run_until_complete(render_page(r.html))
    print ret

if __name__ == '__main__':
    main() 