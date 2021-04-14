import auth
import devices
import interfaces
import flow_analysis

if __name__ == "__main__":

    input("Premere Invio per autenticarsi tramite le credenziali salvate nel file di configurazione")
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


    print("Premere Invio per eseguire Flow Analysis tra due indirizzi IP di test")
    source_ip = "10.10.22.98"
    destination_ip = "10.10.22.114"
    print("IP Sorgente: ", source_ip)
    print("IP Destinazione: ", destination_ip)

    # Esegue la Flow Analysis tra i due indirizzi
    flow = flow_analysis.runFlowAnalysis(token, source_ip, destination_ip)

    # Stampa i dettagli dell'analisi
    flow_analysis.printFlowDetails(flow, token)

    print("Trial Version, Demo terminata!")