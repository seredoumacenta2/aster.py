#!/bin/bash
#Variables
ip_interne=192.168.1.100
ip_externe=178.25.12.50
num_interne=1001
num_externe=33456789
#Installation d'Asterisk
echo "Installation d'Asterisk..."
apt update
apt install asterisk -y
Configuration SIP
echo "Configuration du fichier sip.conf..."
echo "listen=${ip_interne}:5060" >> /etc/asterisk/sip.conf
echo "externalrtpaddress=${ip_externe}" >> /etc/asterisk/sip.conf
#Configuration des extensions
echo "Configuration du fichier extensions.conf..."
echo "[from-internal]">/etc/asterisk/extensions.conf
echo "exten => ${num_interne},1,Dial(SIP/${num_externe})" >> /etc/asterisk/extensions.conf
#Redémarrage d'Asterisk
echo "Redémarrage d'Asterisk..."
asterisk -rx "core restart"
#Test de la configuration
echo "Test de la configuration..."
asterisk -rx "core show channels"
echo "Configuration Asterisk terminée!"
