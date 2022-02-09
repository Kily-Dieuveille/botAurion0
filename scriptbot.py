from selenium import webdriver
from time import localtime, sleep,strptime
import argparse
import os

# Variables globales

jours=["Lundi", "Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]


def get_args():
    parser=argparse.ArgumentParser("Schedule Taker")

    parser.add_argument("--date", type=str, default='',help="Entrer une date au format jj/mmm/aaaa (à voir)")
    parser.add_argument("--output", type=str,default="")
    args = parser.parse_args()
    return args

def main(opt):

    time=localtime()
    # definition de la date 
    if opt.date!='': 
        time=strptime(opt.date,"%d/%m/%y")

    dateEntry=f"{time.tm_mday}/{time.tm_mon}/{time.tm_year}"

    # connexion 
    chrome_options=webdriver.ChromeOptions()
    chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    botAurion = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    botAurion.get("https://aurion.junia.com/faces/Login.xhtml")

    # autentificaion
    username=botAurion.find_element_by_id("username")
    password=botAurion.find_element_by_id("password")
    connecter=botAurion.find_element_by_id("j_idt28")

    username.send_keys(os.environ.get("USERNAME"))
    password.send_keys(os.environ.get("PASSWORD"))
    connecter.click()

    # Page Mon planning 
    monPlanning=botAurion.find_element_by_xpath("//a[@tabindex='-1']")
    monPlanning.click()

    # Aller à la date (dateEntry)
    date=botAurion.find_element_by_id("form:date_input")
    date.clear()
    sleep(3)
    date.send_keys(dateEntry)
    date.submit()

    #recuperer les evenements du jour 
    sleep(3)
    emploidutemps=botAurion.find_elements_by_xpath("//div[@class='fc-event-container']")

    # Avoir le programme de la semaine

    for k in range(len(emploidutemps)):

        print(f"****************************{jours[k]}****************************")
        journee=emploidutemps[k].find_elements_by_xpath("descendant::div[@class='fc-title']")

        for cours in journee:
            element=cours.text
            print(element)



def weekSchedule(date=''):
    emploi=[]
    time=localtime()
    jours=["Lundi", "Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

    if date!="":
        time=strptime(date.strip(),"%d/%m/%y")
    dateEntry=f"{time.tm_mday}/{time.tm_mon}/{time.tm_year}"
        
    # connexion 
    chrome_options=webdriver.ChromeOptions()
    chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    botAurion = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    botAurion.get("https://aurion.junia.com/faces/Login.xhtml")

    ## autentificaion
    username=botAurion.find_element_by_id("username")
    password=botAurion.find_element_by_id("password")
    connecter=botAurion.find_element_by_id("j_idt28")

    username.send_keys(os.environ.get("USERNAME"))
    password.send_keys(os.environ.get("PASSWORD"))
    connecter.click()

    ## Page Mon planning 
    monPlanning=botAurion.find_element_by_xpath("//a[@tabindex='-1']")
    monPlanning.click()

    # Aller à la date (dateEntry)
    date=botAurion.find_element_by_id("form:date_input")
    date.clear()
    sleep(3)
    date.send_keys(dateEntry)
    date.submit()

    #recuperer les evenements du jour 
    sleep(3)
    emploidutemps=botAurion.find_elements_by_xpath("//div[@class='fc-event-container']")

    # Avoir le programme de la semaine

    for k in range(len(emploidutemps)):

        print(f"*****{jours[k]}********")
        emploi+=[f"*****{jours[k]}********"]
        journee=emploidutemps[k].find_elements_by_xpath("descendant::div[@class='fc-title']")

        for cours in journee:
            element=cours.text
            print(element)
            emploi+=[element]

    return emploi

def jour(date=""):
    time=localtime()
    if date!="":
        time=strptime(date.strip(),"%d/%m/%y")
    emploi=[]
    dateEntry=f"{time.tm_mday}/{time.tm_mon}/{time.tm_year}"

    # connexion 
    chrome_options=webdriver.ChromeOptions()
    chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    botAurion = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    botAurion.get("https://aurion.junia.com/")

    ## autentificaion
    username=botAurion.find_element_by_id("username")
    password=botAurion.find_element_by_id("password")
    connecter=botAurion.find_element_by_id("j_idt28")

    username.send_keys(os.environ.get("USERNAME"))
    password.send_keys(os.environ.get("PASSWORD"))
    connecter.click()

    ## Page Mon planning 
    monPlanning=botAurion.find_element_by_xpath("//a[@tabindex='-1']")
    monPlanning.click()

    # Aller à la date (dateEntry)
    date=botAurion.find_element_by_id("form:date_input")
    date.clear()
    sleep(3)
    date.send_keys(dateEntry)
    date.submit()

    #recuperer les evenements du jour 
    sleep(3)
    emploidutemps=botAurion.find_elements_by_xpath("//div[@class='fc-event-container']")


    emploi+=[f"*****{jours[time.tm_wday]}********"]
    journee=emploidutemps[time.tm_wday].find_elements_by_xpath("descendant::div[@class='fc-title']")
    for cours in journee:
            element=cours.text
            print(element)
            emploi+=[element]

    return emploi

    


def ceJour(opt, date=''):
    time=localtime()
    emploi=[]
    aux=opt.strip().lower()
    jour=aux[0].upper()+aux[1:]
    indJourJ=-1

    if date!="":
        time=strptime(date.strip(),"%d/%m/%y")
    dateEntry=f"{time.tm_mday}/{time.tm_mon}/{time.tm_year}"

    #trouver le numéro du jour
    for k in range(7):
        if jours[k]==jour:
            indJourJ=k
            print(jours[k])
            break

    if indJourJ==-1:
        raise ValueError(f"Jour non trouvé, {opt}")
    
    # connexion 
    chrome_options=webdriver.ChromeOptions()
    chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    botAurion = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    botAurion.get("https://aurion.junia.com/faces/Login.xhtml")

    ## autentificaion
    username=botAurion.find_element_by_id("username")
    password=botAurion.find_element_by_id("password")
    connecter=botAurion.find_element_by_id("j_idt28")

    username.send_keys(os.environ.get("USERNAME"))
    password.send_keys(os.environ.get("PASSWORD"))
    connecter.click()

    ## Page Mon planning 
    monPlanning=botAurion.find_element_by_xpath("//a[@tabindex='-1']")
    monPlanning.click()

    # Aller à la date (dateEntry)
    date=botAurion.find_element_by_id("form:date_input")
    date.clear()
    sleep(3)
    date.send_keys(dateEntry)
    date.submit()

    #recuperer les evenements du jour 
    sleep(3)
    emploidutemps=botAurion.find_elements_by_xpath("//div[@class='fc-event-container']")


    emploi+=[f"*****{jours[indJourJ]}********"]
    journee=emploidutemps[indJourJ].find_elements_by_xpath("descendant::div[@class='fc-title']")

    for cours in journee:
            element=cours.text
            print(element)
            emploi+=[element]

    return emploi
    

# ceJour("mercredi","03/02/22")

    # fichier.close()
# if __name__ == '__main__':
#     opt = get_args()
#     main(opt)



