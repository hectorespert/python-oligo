import requests
import json
from oligo.exceptions import ResponseException, LoginException, SessionException

class Iber:

    __loginurl = "https://www.iberdroladistribucionelectrica.com/consumidores/rest/loginNew/login"
    __watthourmeterurl = "https://www.iberdroladistribucionelectrica.com/consumidores/rest/escenarioNew/obtenerMedicionOnline/5"
    __headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        'accept': "application/json; charset=utf-8",
        'content-type': "application/json; charset=utf-8",
        'cache-control': "no-cache"
    }

    def __init__(self):
        self.__session = None

    def login(self, user, password):
        self.__session = requests.Session()
        logindata = [user, password, "", "", "", "", "", "0", "0", "0", "", "s"]
        payload = json.dumps(logindata)
        loginresponse = self.__session.request("POST", self.__loginurl, data=payload, headers=self.__headers)
        if loginresponse.status_code != 200:
            self.__session = None
            raise ResponseException
        jsonresponse = loginresponse.json()
        if jsonresponse["success"] != "true":
            self.__session = None
            raise LoginException

    def __checksession(self):
        if not self.__session:
            raise SessionException

    def watthourmeter(self):
        self.__checksession()
        response = self.__session.request("GET", self.__watthourmeterurl, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        jsonresponse = response.json()
        return jsonresponse[0]

    #def datos(self):
    #    self.__checksession()
    #    response = self.__session.request("GET", "https://www.iberdroladistribucionelectrica.com/consumidores/rest/consumoNew/obtenerDatosConsumo/fechaInicio/18-06-201700:00:00/colectivo/USUCMP/frecuencia/horas/acumular/false", headers=self.__headers)
    #    print(response.json())


def watthourmeter(user, password):
    try:
        iber = Iber()
        iber.login(user, password)
        return iber.watthourmeter()
    except ResponseException:
        return -1
    except LoginException:
        return -1
    except SessionException:
        return -1





