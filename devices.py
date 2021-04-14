import requests


def getDevicesList(token):
    """
    Crea ed invia la richiesta di GET inventory, ottenendo la lista dei device e le loro caratteristiche
    """
    # URL dell'inventory della Sandbox di Cisco DNA
    url = "https://sandboxdnac.cisco.com/api/v1/network-device"
    # Crea l'header per la richiesta GET contenente il token di autorizzazione
    header = {'x-auth-token': token, 'content-type': 'application/json'}
    # Effettua la richiesta di GET e ottiene la lista dei device
    response = requests.get(url, headers=header)
    device_list = response.json()

    return device_list

def getDeviceByIP(token, ip):
    """
    Crea ed invia la richiesta di GET per un device cercando tramite indirizzo IP
    """
    # URL dell'inventory della Sandbox di Cisco DNA
    url = "https://sandboxdnac.cisco.com/api/v1/network-device"
    # Crea l'header per la richiesta GET contenente il token di autorizzazione
    header = {'x-auth-token': token, 'content-type': 'application/json'}
    # Crea il parametro aggiuntivo di ricerca tramite IP
    querystring = {"managementIpAddress": ip}
    # Effettua la richiesta di GET e ottiene la lista dei device
    response = requests.get(url, headers=header, params=querystring)
    device = response.json()

    return device


def getDeviceByMAC(token, mac):
    """
    Crea ed invia la richiesta di GET per un device cercando tramite indirizzo IP
    """
    # URL dell'inventory della Sandbox di Cisco DNA
    url = "https://sandboxdnac.cisco.com/api/v1/network-device"
    # Crea l'header per la richiesta GET contenente il token di autorizzazione
    header = {'x-auth-token': token, 'content-type': 'application/json'}
    # Crea il parametro aggiuntivo di ricerca tramite MAC
    querystring = {"macAddress": mac}
    # Effettua la richiesta di GET e ottiene la lista dei device
    response = requests.get(url, headers=header, params=querystring)
    device = response.json()

    return device