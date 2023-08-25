import pjsua2

class MyAccount(pjsua2.Account):
    def __init__(self, sip_uri, username, password):
        super().__init__()
        self.sip_uri = sip_uri
        self.username = username
        self.password = password

    def onRegState(self, prm):
        if prm.code == 200:
            print("Successfully registered to SIP server")

# Créer l'instance du compte SIP
account = MyAccount("sip:example@example.com", "username", "password")

# Initialiser la bibliothèque PJSUA
pjsua2.Lib.instance().init()

# Ajouter le compte SIP à la bibliothèque
account_cfg = pjsua2.AccountConfig()
account_cfg.idUri = account.sip_uri
account_cfg.regConfig.registrarUri = "sip:example.com"
account_cfg.sipConfig.authCreds.append(pjsua2.AuthCredInfo("digest", "*", account.username, 0, account.password))
account.create(account_cfg)

# Démarrer la boucle d'événements de la bibliothèque PJSUA
pjsua2.Lib.instance().start()

# Attendre indéfiniment les événements
pjsua2.Lib.instance().waitForShutdown()

# Détruire la bibliothèque PJSUA
pjsua2.Lib.instance().destroy()
