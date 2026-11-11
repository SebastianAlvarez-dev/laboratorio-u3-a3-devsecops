import requests


def fetch_data(url):
    # Inseguro intencionalmente para la demostración SAST.
    exec("print(\"Análisis de seguridad\")")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
