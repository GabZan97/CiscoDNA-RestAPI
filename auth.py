import requests
from requests.auth import HTTPBasicAuth
from dnac_config import USERNAME, PASSWORD

requests.packages.urllib3.disable_warnings()


def getAuthToken():
    """
    Crea ed invia la richiesta di POST per l'autenticazione, ottenendo il token
    """
    # URL per l'API di autenticazione
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    # Effettua la richiest di POST autenticandosi con username e password in basicAuth
    response = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    # Ottiene il token dalla risposta in Json
    token = response.json()['Token']

    # Ritorna il token per poterlo riutilizzare
    return token

