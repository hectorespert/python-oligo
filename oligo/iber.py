from requests import Session
from datetime import datetime


class ResponseException(Exception):
    pass


class LoginException(Exception):
    pass


class SessionException(Exception):
    pass


class NoResponseException(Exception):
    pass


class SelectContractException(Exception):
    pass


class Iber:

    __domain = "https://www.i-de.es"
    __login_url = __domain + "/consumidores/rest/loginNew/login"
    __watthourmeter_url = __domain + "/consumidores/rest/escenarioNew/obtenerMedicionOnline/24"
    __icp_status_url = __domain + "/consumidores/rest/rearmeICP/consultarEstado"
    __contracts_url = __domain + "/consumidores/rest/cto/listaCtos/"
    __contract_detail_url = __domain + "/consumidores/rest/detalleCto/detalle/"
    __contract_selection_url = __domain + "/consumidores/rest/cto/seleccion/"
    __obtener_escenarios_url = __domain + "/consumidores/rest/escenarioNew/obtenerEscenariosRest/"
    __obtener_escenario_url = __domain + "/consumidores/rest/escenarioNew/refrescarEscenario/"
    __guardar_escenario_url = __domain + "/consumidores/rest/escenarioNew/confirmarMedicionOnLine/{}/1/{}"
    __borrar_escenario_url = __domain + "/consumidores/rest/escenarioNew/borrarEscenario/"
    __headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36",
        'accept': "application/json; charset=utf-8",
        'content-type': "application/json; charset=utf-8",
        'cache-control': "no-cache"
    }

    def __init__(self):
        """Iber class __init__ method."""
        self.__session = None

    def login(self, user, password):
        """Creates session with your credentials"""
        self.__session = Session()
        login_data = "[\"{}\",\"{}\",null,\"Linux -\",\"PC\",\"Chrome 77.0.3865.90\",\"0\",\"\",\"s\"]".format(user, password)
        response = self.__session.request("POST", self.__login_url, data=login_data, headers=self.__headers)
        if response.status_code != 200:
            self.__session = None
            raise ResponseException("Response error, code: {}".format(response.status_code))
        json_response = response.json()
        if json_response["success"] != "true":
            self.__session = None
            raise LoginException("Login error, bad login")

    def __check_session(self):
        if not self.__session:
            raise SessionException("Session required, use login() method to obtain a session")

    def measurement(self):
        """Returns a measurement from the powermeter."""  
        self.__check_session()
        response = self.__session.request("GET", self.__watthourmeter_url, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        return {
            "id": json_response['codSolicitudTGT'],
            "consumption": json_response['valMagnitud'],
            "icp": json_response['valInterruptor'],
            "raw_response" : json_response
        }

    def watthourmeter(self):
        """Returns your current power consumption."""
        return self.measurement()['power']

    def icpstatus(self):
        """Returns the status of your ICP."""
        self.__check_session()
        response = self.__session.request("POST", self.__icp_status_url, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        if json_response["icp"] == "trueConectado":
            return True
        else:
            return False

    def contracts(self):
        self.__check_session()
        response = self.__session.request("GET", self.__contracts_url, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        if json_response["success"]:
            return json_response["contratos"]

    def contract(self):
        self.__check_session()
        response = self.__session.request("GET", self.__contract_detail_url, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        return response.json()

    def contractselect(self, id):
        self.__check_session()
        response = self.__session.request("GET", self.__contract_selection_url + id, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        if not json_response["success"]:
            raise SelectContractException

    def scene_list(self):
        self.__check_session()
        response = self.__session.request("GET", self.__obtener_escenarios_url, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        return {
            "scene_names": json_response['y']['smps'],
            "raw_response" : json_response
        }

    def scene_get(self, name):
        self.__check_session()
        get_data = "{{\"nomEscenario\":\"{}\"}}".format(name)
        response = self.__session.request("POST", self.__obtener_escenario_url, data=get_data, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        return {
            "name": json_response['nomEscenario'],
            "description": json_response['descripcion'],
            "consumption": json_response['numLcaInsta'],
            "raw_response" : json_response
        }


    def scene_save(self, consumption, measurement_id, description):
        self.__check_session()
        name = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        save_data = "{{\"nomEscenario\":\"{}\",\"descripcion\":\"{}\"}}".format(name, description)
        response = self.__session.request("POST", self.__guardar_escenario_url.format(consumption, measurement_id), data=save_data, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        return {
            "name": json_response['nomEscenario'],
            "raw_response" : json_response
        }

    def scene_delete(self, name):
        self.__check_session()
        delete_data = "{{\"nomEscenario\":\"{}\"}}".format(name)
        response = self.__session.request("POST", self.__borrar_escenario_url, data=delete_data, headers=self.__headers)
        if response.status_code != 200:
            raise ResponseException
        return True

