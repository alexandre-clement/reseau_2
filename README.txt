lancer server.py
lancer client.py

client.py envoie une requête de la forme "GET /index.html HTTP/1.1" au serveur
serveur.py renvoie le contenue du fichier index.html

Si le fichier n'existe pas, le serveur renvoie le client sur le fichier index.html

commandes disponibles :

    http://localhost:15555/index.html
    http://localhost:15555/cgi-bin/incr.py?val=100
    http://localhost:15555/logger.html
    http://localhost:15555/conversion.html


ROOT_PATH absolue utiliser :

    C:\Users\user\Desktop\server\root


url par défaut à utiliser :

    http://localhost:15555/

    alternatives :
        http://localhost:15555/index.html
        http://127.0.0.1:15555/
        http://127.0.0.1:15555/index.html


test-get :
    entrez l'url :
        http://localhost:15555/test-get.html
    ensuite tapez votre message puis appuyez sur "submit"
    le message "GET :" suivis de votre message devrait s'afficher




