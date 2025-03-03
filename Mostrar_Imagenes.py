import requests
from datetime import datetime, timedelta

api = "KGfUUoaqC6LQhITqUmGnNr1JzWD2MaRUM9LBliz6"
api_url = f"https://api.nasa.gov/planetary/apod?api_key={api}"

def obtener_imagen(enlace):
    respuesta = requests.get(enlace)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print(f"Titulo de la imagen del día:\n{datos['title']}")
        print(f"Descripción de la imagen del día :\n{datos['explanation']}")
        link_de_imagen = datos["url"]
        print(f"linck de la imagen del día:\n{link_de_imagen}")
    else:
        print("Erro no se puede ingresar al api")

def obtener_por_fecha():
    while True:
        fecha = input("Ingrese una fecha (año-mes-día): ")
        try:
            fecha_usuario = datetime.strptime(fecha, "%Y-%m-%d")
            fecha_minima = datetime(1995, 6, 16)
            fecha_actual = datetime.today()

            if fecha_minima <= fecha_usuario <= fecha_actual:
                parametro = {"api_key": api, "date": fecha}
                respuesta = requests.get(api_url, params=parametro)
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    print(
                        f"Titulo de l aimagen del {fecha_usuario}:\n{datos['title']}\n"
                    )
                    print(
                        f"Descripción de la imagen del {fecha_usuario}:\n{datos['explanation']}\n"
                    )
                    link_de_imagen = datos["url"]
                    print(f"linck de la imagen:\n{link_de_imagen}")
                else:
                    print("Erro no se puede ingresar al api")
            else:
                print(
                    "La fecha debe estar entre el 6 de julio de 1995 hasta la fecha actual"
                )
        except ValueError:
            print("Formato de fecha invalido ingrese, use el formato año, mes y dia")
            continue
        break
        
def obtener_galeria():
    fecha_act = datetime.today()
    hace_7_dias = fecha_act - timedelta(days=7)

    fecha_act = fecha_act.strftime("%Y-%m-%d")
    hace_7_dias = hace_7_dias.strftime("%Y-%m-%d")

    parametros = {"api_key": api, "start_date": hace_7_dias, "end_date": fecha_act}

    respuesta = requests.get(api_url, params=parametros)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        for dia in datos:
            print(f"Titulo: {dia['title']}")
            print(f"Descripción: {dia['explanation']}")
            print(f"Link de la imagen: {dia['url']}\n")
    else:
        print("Error no se puede ingresar al API")

while True:
    print("Eliga una opccion:")
    print("1. Mostrar imagen del dia")
    print("2. Mostrar imagen segun la fecha")
    print("3. Mostrar imagen desde 7 dias atras")
    n = input("Su opcion: ")
    if n == "1":
        obtener_imagen(api_url)
    elif n == "2":
        obtener_por_fecha()
    elif n == "3":
        obtener_galeria()
    else:
        print("Intente nuevamente...")
        continue

    continuar = input("Desea continuar (s/n)").strip().lower()
    if continuar == "n":
        print("Saliendo....")
        break
