from requests_html import HTMLSession                     #install in Visual : pip install requests-html
import speech_to_text                                   #install in Visual : pip install lxml

def weather():
    s  =  HTMLSession()
    query = "jaipur"
    url = f'https://in.search.yahoo.com/search?fr=mcafee&type=E211IN714G91802&p=whether+in+{query}'
    r  = s.get(url , headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})

    temp  = r.html.find('span#wob_tm' , first= True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
    desc  = r.html.find('span#wob_dc' , first= True).text
    return temp+" "+unit+" "+ desc
