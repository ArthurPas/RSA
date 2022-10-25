from fonctions import *
message = 1234
tailleEmpreinte = 10000
p = 999979
q = 999983
n = p*q
clePublique = genere_cle(p,q)[0]
clePrivee = genere_cle(p,q)[1]
empreinte = creerEmpreinte(message,tailleEmpreinte)
messageEtEmpreinte = concatMessageEmpreinte(message, empreinte, tailleEmpreinte)
chiffreMessageEtEmpreinte = chiffrer(messageEtEmpreinte,clePublique,n)
print("le message initial : "+str(message))
print("l'empreinte : " + str(empreinte))
print("le message concaténé avec l'empreinte : "+str(messageEtEmpreinte))
print("le chiffré de l'empreinte et du message : " + str(chiffreMessageEtEmpreinte))
print("dechifrement de l'empreinte et du message : "+ str(dechiffrer(chiffreMessageEtEmpreinte,clePrivee,n)))