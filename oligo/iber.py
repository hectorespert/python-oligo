from requests import Session
from json import dumps
from .exceptions import ResponseException, LoginException, SessionException, NoResponseException, SelectContractException


class Iber:

    __loginurl = "https://www.i-de.es/consumidores/rest/loginNew/login"
    __watthourmeterurl = "https://www.i-de.es/consumidores/rest/escenarioNew/obtenerMedicionOnline/24"
    __icpstatusurl = "https://www.i-de.es/consumidores/rest/rearmeICP/consultarEstado"
    __contractsurl = "https://www.i-de.es/consumidores/rest/cto/listaCtos/"
    __contractdetailurl = "https://www.i-de.es/consumidores/rest/detalleCto/detalle/"
    __contractselectionurl = "https://www.i-de.es/consumidores/rest/cto/seleccion/"
    __headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        'accept': "application/json; charset=utf-8",
        'content-type': "application/json; charset=utf-8",
        'cache-control': "no-cache"
    }

    def __init__(self):
        """Iber class __init__ method."""
        self.__session = None

    def login(self, user, password):
        """Create session with your credentials.
           Inicia la session con tus credenciales."""
        self.__session = Session()
        logindata = self.__logindata(user, password)
        response = self.__session.request("POST", self.__loginurl, data=logindata, headers=self.__headers)
        if response.status_code != 200:
            self.__session = None
            raise ResponseException
        jsonresponse = response.json()
        if jsonresponse["success"] != "true":
            self.__session = None
            raise LoginException

    def __logindata(self, user, password):
        logindata = [user, password, "", "Windows -", "PC", "Firefox 54.0", "", "0", "0", "0", "", "s"]
        return dumps(logindata)

    def __checksession(self):
        if not self.__session:
            raise SessionException

    def watthourmeter(self):
        """Returns your current power consumption.
           Devuelve tu consumo de energía actual."""
        self.__checksession()
        response = self.__session.request("GET", self.__watthourmeterurl, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        jsonresponse = response.json()
        return jsonresponse['valMagnitud']

    def icpstatus(self):
        """Returns the status of your ICP.
           Devuelve el estado de tu ICP."""
        self.__checksession()
        response = self.__session.request("POST", self.__icpstatusurl, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        jsonresponse = response.json()
        if jsonresponse["icp"] == "trueConectado":
            return True
        else:
            return False

    def contracts(self):
        self.__checksession()
        response = self.__session.request("GET", self.__contractsurl, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        jsonresponse = response.json()
        if jsonresponse["success"]:
            return jsonresponse["contratos"]

    def contract(self):
        self.__checksession()
        response = self.__session.request("GET", self.__contractdetailurl, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        return response.json()

    def contractselect(self, id):
        self.__checksession()
        response = self.__session.request("GET", self.__contractselectionurl + id, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        jsonresponse = response.json()
        if not jsonresponse["success"]:
            raise SelectContractException


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


def icpstatus(user, password):
    try:
        iber = Iber()
        iber.login(user, password)
        return iber.icpstatus()
    except ResponseException:
        return False
    except LoginException:
        return False
    except SessionException:
        return False






