import requests


def getDevicesList(token):
    """
    Crea ed invia la richiesta di GET per ottenere la lista dei device e le loro caratteristiche
    """
    # URL per l'API di network device
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
    # Effettua la richiesta di GET e ottiene il device richiesto
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
    # Effettua la richiesta di GET e ottiene il device richiesto
    response = requests.get(url, headers=header, params=querystring)
    device = response.json()

    return device


def printDeviceList(devicesList):
    """
    Funzione rubata per stampare bene la lista di device
    """
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial", "platformId", "SW Version", "role", "Uptime"))
    for device in devicesList['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))
