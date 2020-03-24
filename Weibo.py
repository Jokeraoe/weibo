import requests
import tkinter 
from lxml import etree 
from tkinter import Listbox
 
url="https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6" 

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'} 

def get_trending(): 
    html=etree.HTML(requests.get(url,headers=header).text)
    
    rank=html.xpath('//td[@class="td-01 ranktop"]/text()') 
    affair=html.xpath('//td[@class="td-02"]/a/text()') 
    view = html.xpath('//td[@class="td-02"]/span/text()') 
    
    top=affair[0] 
    affair=affair[1:]
    
    Gui = tkinter.Tk()

    title = Gui.title('微博热搜')

    topnew = Listbox(Gui,height = 1,width = 40,font = '黑体',foreground= 'red')
    hotnews = Listbox(Gui,height = 39 , width = 40,font = '黑体')

    # print('{0:<10}\t{1:<40}'.format("top",top))
    topnew.insert(0,'置顶:' + top)


    for i in range(0, len(affair)):
        # print("{0:<10}\t{1:{3}<30}\t{2:{3}>20}".format(rank[i],affair[i],view[i],chr(12288))) 
        hotnews.insert(i,'%d.'%(i+1) + affair[i])

    topnew.pack()
    hotnews.pack()

    Gui.mainloop()

get_trending()