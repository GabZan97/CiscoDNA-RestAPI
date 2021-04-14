import requests
from requests.auth import HTTPBasicAuth
from dnac_config import USERNAME, PASSWORD

requests.packages.urllib3.disable_warnings()


def get_auth_token():
    """
    Crea ed invia la richiesta di autenticazione, ottenendo il token
    """
    # URL di autenticazione alla Sandbox di Cisco DNA
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    # Effettua la richiest di POST autenticandosi con username e password in basicAuth
    response = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    # Ottiene il token dalla risposta in Json
    token = response.json()['Token']

    # Ritorna il token per poterlo riutilizzare
    return token

