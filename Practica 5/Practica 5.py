from bs4 import BeautifulSoup as bs
import re, requests

def BuscarRed(listaexp,fuenteurl,soup,listared):
    po1=soup.select("a")
    for ele in po1:
        links=ele.get("href")
        if links != None:
            for red in range(len(listaexp)):
                redlinks=listaexp[red].search(links)
                if redlinks!=None:
                    if (redlinks.group(1) in listared)==False:
                        listared.append(redlinks.group(1))
    return listared #lista red social buscada

#https://www.alkapone.tv/
fuenteurl= input("Ingresa una url a escanear: ")

#EXP REGULARES
print("Buscando redes sociales...")
#Redes sociales
facebook=re.compile(r"(https://www\.facebook\.com/\S+)\s*")
twitter=re.compile(r"(https://twitter\.com/\S+)\s*")
instagram=re.compile(r"(https://www\.instagram\.com/\S+)\s*")
youtube=re.compile(r"(https://www\.youtube\.com/\S+)\s*")
tiktok=re.compile(r"(https://www\.tiktok\.com/\S+)\s*")
listaexp=[facebook,twitter,instagram,youtube,tiktok]
#WEB SCRAPING
listanoticias=list()
listacorreo=list()
listatel=list()
linkred=list()
try:
    page=requests.get(fuenteurl)
    if page.status_code==200:
        soup=bs(page.content,"html.parser")
        BuscarRed(listaexp,fuenteurl,soup,linkred)#busca redes, guarda listaexp
        print(linkred)
    else:
        print("Página no responde")
except ValueError:
    print("No es una página válida")
