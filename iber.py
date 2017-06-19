import requests, json

def watthourmeter(user, password):
    session = requests.Session()
    loginurl = "https://www.iberdroladistribucionelectrica.com/consumidores/rest/loginNew/login"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        'accept': "application/json; charset=utf-8",
        'content-type': "application/json; charset=utf-8",
        'cache-control': "no-cache"
    }
    logindata = [user, password, "", "", "", "", "", "0", "0", "0", "", "s"]
    payload = json.dumps(logindata)
    loginresponse = session.request("POST", loginurl, data=payload, headers=headers)
    if loginresponse.status_code != 200:
        return -1
    jsonresponse = loginresponse.json()
    if jsonresponse["success"] != "true":
        return -1
    url = "https://www.iberdroladistribucionelectrica.com/consumidores/rest/escenarioNew/obtenerMedicionOnline/5"
    response = session.request("GET", url, headers=headers)
    if response.status_code != 200:
        return -1
    jsonresponse = response.json()
    return jsonresponse[0]

