import requests, json
import

class userInfo:

    def __init__(self):
        pass
    def getUsers(self):
        responseUsers = requests.get("https://datos.gov.co/resource/jtnk-dmga.json")
        dataJson =responseUsers.json()
        for ind in range(len(dataJson)):

            self.ListUsers.append(dataJson[ind]["email_addres"])

    def validateUsers(self):

prueba = userInfo()
prueba.getUsers()