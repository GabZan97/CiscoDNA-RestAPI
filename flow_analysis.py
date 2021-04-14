from time import sleep
import requests
import sys
import urllib3
import interfaces

# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {'content-type': "application/json", 'x-auth-token': ""}


def print_interface_details(interface):
    """
    Stampa i dettagli di un interfaccia
    """

    # Print Standard Details
    print("Nome porta: {}".format(interface["portName"]))
    print("Stato amministrativo: {}".format(interface["adminStatus"]))
    print("Stato operativo: {}".format(interface["status"]))
    print("Velocità K/s: {}".format(interface["speed"]))
    print("Duplex: {}".format(interface["duplex"]))
    print("Modalità: {}".format(interface["portMode"]))
    print("VLAN: {}".format(interface["vlanId"]))

    # Blank line at the end
    print("")


def run_flow_analysis(token, source_ip, destination_ip):
    """
    Crea ed invia la richiesta di POST per eseguire la Flow Analysis tra due indirizzi
    """
    base_url = "https://sandboxdnac.cisco.com/api/v1/flow-analysis"
    headers["x-auth-token"] = token

    # initiate flow analysis
    body = {"destIP": destination_ip, "sourceIP": source_ip}
    initiate_response = requests.post(base_url, headers=headers, verify=False,json=body)

    # Verify successfully initiated.  If not error and exit
    if initiate_response.status_code != 202:
        print("Error: Flow Analysis Initiation Failed")
        print(initiate_response.text)
        sys.exit(1)

    # Check status of analysis and wait until completed
    flowAnalysisId = initiate_response.json()["response"]["flowAnalysisId"]
    detail_url = base_url + "/{}".format(flowAnalysisId)
    detail_response = requests.get(detail_url, headers=headers, verify=False)
    while not detail_response.json()["response"]["request"]["status"] == "COMPLETED":  # noqa: E501
        print("Analisi Flow in corso, ricontrollo tra 3 secondi...")
        sleep(3)
        detail_response = requests.get(detail_url, headers=headers,verify=False)

    # Return the flow analysis details
    return detail_response.json()["response"]


def print_flow_analysis_details(flow_analysis, token):
    """
    Stampa i dettagli della flow analysis
    """
    hops = flow_analysis["networkElementsInfo"]

    print("Numero di Hop tra l'IP di sorgente e di destinazione: {}".format(len(hops)))
    print("Mostro il primo Hop tra qualche secondo...")
    sleep(3)

    # Print Details per hop
    print("Dettagli: ")
    # Hop 1 (index 0) and the last hop (index len - 1) represent the endpoints
    for i, hop in enumerate(hops):
        if i == 0 or i == len(hops) - 1:
            continue

        print("*" * 40)
        print("Hop numero {}: Network Device - {}".format(i, hop["name"]))
        # If the hop is "UNKNOWN" continue along
        if hop["name"] == "UNKNOWN":
            print()
            continue

        print("IP: {}".format(hop["ip"]))
        print("Ruolo: {}".format(hop["role"]))

        # If type is an Access Point, skip interface details
        if hop["type"] == "Unified AP":
            continue
        print()

        # Step 4: Are there any problems along the path?
        # Print details about each interface
        print("Interfaccia d'Ingresso")
        print("-" * 20)
        ingress = interfaces.getInterfaceDetails(token, hop["ingressInterface"]["physicalInterface"]["id"])
        print_interface_details(ingress)
        print("Interfaccia d'Uscita")
        print("-" * 20)
        egress = interfaces.getInterfaceDetails(token, hop["egressInterface"]["physicalInterface"]["id"])
        print_interface_details(egress)

        if(i < len(hops) - 2):
            input("Premere Invio per mostrare l'Hop successivo \n")

    # Print blank line at end
    print("")

