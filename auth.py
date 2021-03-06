import requests
from requests.auth import HTTPBasicAuth
from config import USERNAME, PASSWORD

requests.packages.urllib3.disable_warnings()

# URL per l'API di autenticazione
api = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'

def getAuthToken():
    """
    Crea ed invia la richiesta di POST per l'autenticazione, ottenendo il token
    """
    # Effettua la richiest di POST autenticandosi con username e password in basicAuth
    response = requests.post(api, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    # Ottiene il token dalla risposta in Json
    token = response.json()['Token']

    # Ritorna il token per poterlo riutilizzare
    return token

