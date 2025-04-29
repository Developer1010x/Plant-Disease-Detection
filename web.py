from bs4 import BeautifulSoup
import requests
import textwrap
import json

url021="https://ipm.ucanr.edu/agriculture/tomato/late-blight/"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
tomatolatebl=soup007.find("div",{"class":"col-md-12 col-lg-10"}).text
sep = 'Monitoring and Treatment Decisions'
tomatolatebl = tomatolatebl.split(sep, 1)[0]
tomatolatebl = tomatolatebl.replace("\n\n", "\n")

url021="https://ipm.ucanr.edu/agriculture/apple/apple-scab/"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
applescab=soup007.find("div",{"class":"col-md-12 col-lg-10"}).text
sep = 'Monitoring'
applescab = applescab.split(sep, 1)[0]
applescab = applescab.replace("\n\n", "\n")

url021="https://ipm.ucanr.edu/agriculture/potato/early-blight/"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
potatoearlybl=soup007.find("div",{"class":"col-md-12 col-lg-10"}).text
sep = 'Watch for disease symptoms'
potatoearlybl = potatoearlybl.split(sep, 1)[0]
potatoearlybl = potatoearlybl.replace("\n\n", "\n")

url021="https://ipm.ucanr.edu/agriculture/tomato/tomato-yellow-leaf-curl/"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
tomatoyellowcurl=soup007.find("div",{"class":"col-md-12 col-lg-10"}).text
sep = 'Important Links'
tomatoyellowcurl = tomatoyellowcurl.split(sep, 1)[0]
tomatoyellowcurl = tomatoyellowcurl.replace("\n\n", "\n")

url021="https://ipm.ucanr.edu/agriculture/grape/esca-black-measles/"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
grapesca=soup007.find("div",{"class":"col-md-12 col-lg-10"}).text
sep = 'Management'
grapesca = grapesca.split(sep, 1)[0]
grapesca = grapesca.replace("\n\n", "\n")

url021="https://ipm.ucanr.edu/agriculture/corn/common-rust/"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
cornrust=soup007.find("div",{"class":"col-md-12 col-lg-10"}).text
sep = 'UC IPM'
cornrust = cornrust.split(sep, 1)[0]
cornrust = cornrust.replace("\n\n", "\n")

url021="https://agritech.tnau.ac.in/crop_protection/black_gram_disease/blackgram_d1.html"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
blanthra=soup007.find("table",{"width":"100%"}).text
sep = 'Anthracnose infected plants'
blanthra = blanthra.split(sep, 1)[0]
blanthra = blanthra.replace("\n\n", "\n")
#blanthra=textwrap.shorten(text=blanthra,width=10000)

url021="https://agritech.tnau.ac.in/crop_protection/black_gram_disease/blackgram_d4.html"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
blpowd=soup007.find("table",{"width":"100%"}).text
sep = 'Powdery mildew infected plants'
blpowd = blpowd.split(sep, 1)[0]
blpowd = blpowd.replace("\n\n", "\n").replace("Powdery mildew infected plants","")
#blpowd=textwrap.shorten(text=blpowd,width=10000)
print(blpowd)

url021="https://agritech.tnau.ac.in/crop_protection/black_gram_disease/blackgram_d8.html"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
blmosaic=soup007.find("table",{"width":"100%"}).text
blmosaic = blmosaic.replace("\n\n", "\n")
#blmosaic = blmosaic.split(sep, 1)[0]
#blmosaic=textwrap.shorten(text=blmosaic,width=10000)

url021="https://agritech.tnau.ac.in/crop_protection/black_gram_disease/blackgram_d9.html"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
blcrinkle=soup007.find("table",{"width":"100%"}).text
blcrinkle = blcrinkle.replace("Leaf crinkle infected plants", "")
blcrinkle = blcrinkle.replace("\n\n", "\n")
#blcrinkle=textwrap.shorten(text=blcrinkle,width=10000)

dict={"intents":[ {"tag" :"greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hi there, how can I help?"
      ]
    },
                  {
                      "tag": "goodbye",
                      "patterns": ["Bye", "See you later", "Goodbye"],
                      "responses": [
                          "See you later",
                          "Have a nice day",
                          "Bye!"
                      ]
                  },
                  {
                      "tag": "tomato late blight",
                      "patterns": ["tomato late blight", "treatment for tomato late blight","information on tomato late blight"],
                      "responses": [tomatolatebl]
                  },
                  {
                      "tag": "apple scab",
                      "patterns": ["apple scab", "treatment for apple scab","information on apple scab"],
                      "responses": [applescab]
                  },
{
                      "tag": "potato early blight",
                      "patterns": ["potato early blight", "treatment for potato early blight","information on potato early blight"],
                      "responses": [potatoearlybl]
                  },
{
                      "tag": "tomato yellow leaf curl",
                      "patterns": ["tomato yellow leaf curl", "treatment for tomato yellow leaf curl","information on tomato yellow leaf curl"],
                      "responses": [tomatoyellowcurl]
                  },
{
                      "tag": "grape esca",
                      "patterns": ["grape esca", "treatment for grape esca","information on grape esca"],
                      "responses": [grapesca]
                  },
{
                      "tag": "corn rust",
                      "patterns": ["corn rust", "treatment for corn rust","information on corn rust"],
                      "responses": [cornrust]
                  },
{
                      "tag": "Blackgram Anthracnose",
                      "patterns": ["Blackgram Anthracnose", "treatment for Blackgram Anthracnose","information on Blackgram Anthracnose"],
                      "responses": [blanthra]
                  },
{
                      "tag": "Blackgram Powdery Mildew",
                      "patterns": ["Blackgram Powdery Mildew", "treatment for Blackgram Powdery Mildew","information on Blackgram Powdery Mildew"],
                      "responses": [blpowd]
                  },
{
                      "tag": "Blackgram Yellow Mosaic",
                      "patterns": ["Blackgram Yellow Mosaic", "treatment for Blackgram Yellow Mosaic","information on Blackgram Yellow Mosaic"],
                      "responses": [blmosaic]
                  },
{
                      "tag": "Blackgram Leaf Crinkle",
                      "patterns": ["Blackgram Leaf Crinkle", "treatment for Blackgram Leaf Crinkle","information on Blackgram Leaf Crinkle"],
                      "responses": [blcrinkle]
                  }
                  ]}


with open('intents.json','w') as _f:
    json.dump(dict,_f)
