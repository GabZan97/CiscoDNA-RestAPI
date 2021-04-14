import auth
import devices

if __name__ == "__main__":
    # Ottiene il token
    token = auth.get_auth_token()

    # Stampa il token in console
    print("Token Retrieved: {}".format(token))

    devices_list = devices.getDevicesList(token)

    ip_input = input("Inserisci l'IP del device da cercare: ")
    device = devices.getDeviceByIP(token, ip_input)
    print(device)
    print(type(device))

    mac_input = input("Inserisci il MAC del device da cercare: ")
    device = devices.getDeviceByIP(token, mac_input)
    print(device)