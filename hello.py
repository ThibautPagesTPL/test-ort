from datetime import datetime
import requests

print("hello")
print(datetime.now())
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    # 2. On envoie une requête GET
    response = requests.get(url)

    # 3. On vérifie si la requête a réussi (code 200)
    # raise_for_status() génère une erreur si le code est 4xx ou 5xx
    response.raise_for_status()

    # 4. On transforme la réponse en dictionnaire Python (JSON)
    data = response.json()

    # 5. On affiche les données proprement
    print(f"Nom de l'utilisateur : {data['name']}")
    print(f"Ville : {data['address']['city']}")
    print(f"Email : {data['email']}")

except requests.exceptions.HTTPError as err:
    print(f"Erreur HTTP : {err}")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
