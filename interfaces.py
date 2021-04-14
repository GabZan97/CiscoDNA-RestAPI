import requests


def getDeviceInterfaces(token, id):
    """
    Crea ed invia la richiesta di GET per ottenere lo stato delle interfacce di un device
    """
    # URL per l'API delle interfacce dei network device
    url = "https://sandboxdnac.cisco.com/api/v1/interface"
    # Crea l'header per la richiesta GET contenente il token di autorizzazione
    header = {'x-auth-token': token, 'content-type': 'application/json'}
    # Crea il parametro aggiuntivo di ricerca tramite ID
    querystring = {"id": id}
    # Effettua la richiesta di GET e ottiene lo stato delle interfacce del device richiesto
    response = requests.get(url, headers=header, params=querystring)
    interfaces_info = response.json()

    return interfaces_info

def getInterfaceDetails(token, id):
    """
    Crea ed invia la richiesta di GET per ottenere il dettaglio di un interfaccia
    """
    url = "https://sandboxdnac.cisco.com/api/v1/interface/{}".format(id)
    header = {'x-auth-token': token, 'content-type': 'application/json'}

    response = requests.request("GET", url, headers=header, verify=False)
    return response.json()["response"]


def printInterfaceInfo(interfacesList):
    """
    Stampa in modo fancy la lista di interfacce
    """
    print("{0:42}{1:17}{2:12}{3:18}{4:17}{5:10}{6:15}".
          format("portName", "vlanId", "portMode", "portType", "duplex", "status", "lastUpdated"))
    for int in interfacesList['response']:
        print("{0:42}{1:10}{2:12}{3:18}{4:17}{5:10}{6:15}".
              format(str(int['portName']),
                     str(int['vlanId']),
                     str(int['portMode']),
                     str(int['portType']),
                     str(int['duplex']),
                     str(int['status']),
                     str(int['lastUpdated'])))