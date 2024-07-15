import requests

def get_route_info(api_key, from_city, to_city, route_type):
    route_types = {
        '1': 'fastest',
        '2': 'pedestrian',
        '3': 'bicycle',
        '4': 'multimodal'
    }
    
    if route_type not in route_types:
        print("Opción de transporte no válida.")
        return None
    
    url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={from_city}&to={to_city}&outFormat=json&unit=k&locale=es_ES&routeType={route_types[route_type]}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener la información de la ruta: {response.status_code}")
        return None

def display_route_info(route):
    if not route:
        return
    
    distance_km = route['route']['distance']
    distance_miles = distance_km * 0.621371  # Convertir kilómetros a millas
    time_seconds = route['route']['time']
    narrative = route['route']['legs'][0]['maneuvers']

    time_hours = int(time_seconds // 3600)
    time_minutes = int((time_seconds % 3600) // 60)
    time_seconds = int(time_seconds % 60)

    print(f"Distancia: {distance_km:.2f} km / {distance_miles:.2f} mi")
    print(f"Duración del viaje: {time_hours} horas, {time_minutes} minutos, {time_seconds} segundos")
    print("Narrativa del viaje:")
    for maneuver in narrative:
        print(maneuver['narrative'])

def main():
    api_key = '3NLZsQzQJcqMmNjLUlgOcNvXofucZzuy'
    while True:
        from_city = input("Ciudad de Origen: ")
        to_city = input("Ciudad de Destino: ")
        print("Seleccione el tipo de transporte:")
        print("1. Ruta más rápida en auto")
        print("2. Ruta para caminar")
        print("3. Ruta en bicicleta")
        print("4. Ruta multimodal")
        print("s. Salir")
        route_type = input("Opción: ")

        if route_type == 's':
            break

        route = get_route_info(api_key, from_city, to_city, route_type)
        if route is None:
            continue
        
        if 'info' in route and route['info']['statuscode'] == 0:
            display_route_info(route)
        else:
            print("Error al obtener la información de la ruta.")

        print("Ingrese 's' para salir del programa")

if __name__ == "__main__":
    main()
