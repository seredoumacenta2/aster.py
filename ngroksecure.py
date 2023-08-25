import re
import ngrok 

# Lance ngrok et récupère l'adresse publique
public_addr = ngrok.connect(8080, 'tcp').public_url 

# Définit une fonction pour remplacer les chaînes
def replace_strings(text):

  # Remplace l'IP par l'adresse ngrok 
  text = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', public_addr, text)  

  # Remplace le port SIP
  text = re.sub(r':5060', ':8080', text)

  return text

# Test sur un message 
message = "INVITE sip:alice@192.168.1.100:5060 SIP/2.0"
print(replace_strings(message))
