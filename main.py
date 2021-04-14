import auth
import devices
import interfaces

if __name__ == "__main__":

    input("Premere Invio per autenticarsi tramite le credenziali del file dnac_config")
    # Ottiene il token
    token = auth.getAuthToken()

    # Stampa il token in console
    print("Token Ottenuto: ", token)

    # Ottiene la lista completa dei device di rete
    input("Premere Invio per ottenere la lista dei device")
    devicesList = devices.getDevicesList(token)
    devices.printDeviceList(devicesList)

    # Trova un device di rete per IP
    ipInput = input("Inserisci l'IP del device da cercare: ")
    device = devices.getDeviceByIP(token, ipInput)
    devices.printDeviceList(device)
    id = device['response'][0]['id']
    print("L'ID del device cercato è: ", id)

    """
    # Trova un device di rete per MAC
    mac_input = input("Inserisci il MAC del device da cercare: ")
    device = devices.getDeviceByIP(token, mac_input)
    devices.printDeviceList(device)
    id = device['response'][0]['id']
    print("L'ID del device cercato è: ", id)
    """

    # Ottiene la lista delle interfacce del device appena cercato
    input("Premere Invio per ottenere la lista delle interfacce del device cercato qui sopra")
    interfacesList = interfaces.getDeviceInterfaces(token, id)
    interfaces.printInterfaceInfo(interfacesList)