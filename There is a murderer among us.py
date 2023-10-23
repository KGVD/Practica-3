import json
import random
respuestas_correctas=0

def elegir_testimonio(buscar,tipo):
    global respuestas_correctas
    equivocado="Estas seguro?"
    correcto="Puedes sentir como suda el asesino"
    if tipo == 0:
        if buscar == 1:
            return testimonio1
        if buscar == 2:
            return testimonio2
        if buscar == 3:
            return testimonio3
        if buscar == 4:
            return testimonio4
        if buscar == 5:
            return sospechoso
        if buscar == 6:
            return lugar
        if buscar == 7:
            return arma
    else:
        if buscar in (1,2,3,4):
            return equivocado
        if buscar in (5,6,7):
            respuestas_correctas=respuestas_correctas+1
            return correcto

def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data  

def buscar(sospechosos,revisar,tipo):
    revisar=int(revisar)-1
    if 0 <= revisar < len(sospechosos):
        objetivo=sospechosos[revisar]
        if objetivo in testimonios:
            print(elegir_testimonio(testimonios[objetivo],tipo))
        y=1
        return y
    else:
        print("\nInsertar el numero de la opcion\n")
        y=0
        return y

def investigar_Personas():
    y=0
    sospechosos=list(Personas.keys())
    
    while y==0:
        revisar=input("Selecciona un sospechoso al que desa interrogar: \n1) Siegfried el caballero\n2) Pomni la Bufona\n3) Isabel la Reina\n4) Sanson el Verdugo\n5) Pacha el Plebeyo\n")
        y=buscar(sospechosos,revisar,0)
    
def investigar_Ubicaciones():
    y=0
    sospechosos=list(Ubicaciones.keys())
    
    while y==0:
        revisar=input("Selecciona un lugar para investigar: \n1) Castillo\n2) Cocina\n3) Molino\n4) Muralla\n5) Cementerio\n")
        y=buscar(sospechosos,revisar,0)
    
    
def investigar_Arma():
    y=0
    sospechosos=list(Armas.keys())
    
    while y==0:
        revisar=input("Selecciona un arma para inspeccionar: \n1) Espadon\n2) Ballesta\n3) Arco\n4) Daga\n5) Hacha\n")
        y=buscar(sospechosos,revisar,0)
    

def alazar_borrar_Personas(numero):
    borrar=random.choice(list(Personas2.keys()))
    del informacion2["evidencia"][0]["Personas"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_Ubicacion(numero):
    borrar=random.choice(list(Ubicaciones2.keys()))
    del informacion2["evidencia"][1]["Ubicaciones"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_Arma(numero):
    borrar=random.choice(list(Armas2.keys()))
    del informacion2["evidencia"][2]["Armas"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_acciones(numero):
    borrar=random.choice(list(Acciones.keys()))
    del informacion2["evidencia"][3]["Acciones"][borrar]
    testimonios[borrar]=numero
    return borrar

informacion: dict = cargar_base_de_datos('clue_base_de_datos.json')

informacion2: dict = cargar_base_de_datos('clue_base_de_datos.json')


#Se designa un asesino, lugar y arma#
Personas = informacion['evidencia'][0]['Personas']
asesino = random.choice(list(Personas.keys()))
informacion["evidencia"][0]["Personas"][asesino] = True    

Ubicaciones = informacion['evidencia'][1]['Ubicaciones']
escena_crimen = random.choice(list(Ubicaciones.keys()))
informacion["evidencia"][1]["Ubicaciones"][escena_crimen] = True    

Armas = informacion['evidencia'][2]['Armas']
arma_homicida = random.choice(list(Armas.keys()))
informacion["evidencia"][2]["Armas"][arma_homicida] = True    
##


#Se crea el desarrollo, tanto del asesino como de las personas#
testimonios={}

Personas2 = informacion2['evidencia'][0]['Personas']
Ubicaciones2 = informacion2['evidencia'][1]['Ubicaciones']
Armas2 = informacion2['evidencia'][2]['Armas']
Acciones= informacion2['evidencia'][3]['Acciones']

sospechoso=asesino+" No se presentó a la interrogacion"
testimonios[asesino]=5
lugar="Todos dicen no haber estado en "+escena_crimen
testimonios[escena_crimen]=6
arma="Todos dicen no haber visto o usado el/la "+arma_homicida
testimonios[arma_homicida]=7
final_resultado=asesino+" rapto al Rey y asesino a los guardias usando "+arma_homicida+" en "+escena_crimen

del informacion2["evidencia"][0]["Personas"][asesino]
del informacion2["evidencia"][1]["Ubicaciones"][escena_crimen]
del informacion2["evidencia"][2]["Armas"][arma_homicida]

testimonio1= alazar_borrar_Personas(1)+" dice haber estado en "+alazar_borrar_Ubicacion(1)+" usando "+alazar_borrar_Arma(1)+" mientras "+alazar_borrar_acciones(1)
testimonio2= alazar_borrar_Personas(2)+" dice haber estado en "+alazar_borrar_Ubicacion(2)+" usando "+alazar_borrar_Arma(2)+" mientras "+alazar_borrar_acciones(2)
testimonio3= alazar_borrar_Personas(3)+" dice haber estado en "+alazar_borrar_Ubicacion(3)+" usando "+alazar_borrar_Arma(3)+" mientras "+alazar_borrar_acciones(3)
testimonio4= alazar_borrar_Personas(4)+" dice haber estado en "+alazar_borrar_Ubicacion(4)+" usando "+alazar_borrar_Arma(4)+" mientras "+alazar_borrar_acciones(4)


print("Atentos todo el Mundo, el Rey esta perdido y los guardias fueron asesinados\n")
print("Tenemos que descubrir al culpable de esta atrocidad\n")

x=7

while x!=0:
    a_investigar= input("Aun tienes "+str(x)+" Horas hasta el amanecer\nQue sera lo proximo que investigara\n 1. Persona\n 2. Ubicacion\n 3. Arma\n")
    
    switch = {
        '1': investigar_Personas,
        '2': investigar_Ubicaciones,
        '3': investigar_Arma
    }
    
    if a_investigar in switch:
        switch[a_investigar]()
        x=x-1
    else:
        print("Opción no invalida")
        
print("\nYa fue suficiente tiempo, es hora de decidir al culpable, el lugar donde ocurrio el asesinto y el arma que utilizo1\n")

y=0

while y==0:
    final_culpable=input("Selecciona un culpable: \n1) Caballero\n2) Bufon\n3) Reina\n4) Verdugo\n5) Plebeyo\n")
    y=buscar(list(Personas.keys()),final_culpable,1)
    
y=0
while y==0:
    final_lugar=input("Selecciona el lugar del asesinato: \n1) Castillo\n2) Cocina\n3) Molino\n4) Muralla\n5) Cementerio\n")
    y=buscar(list(Ubicaciones.keys()),final_lugar,1)
    
y=0
while y==0:
    final_arma=input("Selecciona el arma utilizada: \n1) Espadon\n2) Ballesta\n3) Arco\n4) Daga\n5) Hacha\n")
    y=buscar(list(Armas.keys()),final_arma,1)
   
print("\n"+final_resultado+"\n")
print(str(respuestas_correctas)+" De tus elecciones fueron correctas")
if respuestas_correctas == 3:
    print("\nMuchas gracias, el asesino sera ejecutado al amanecer, FELICIDADES!!!!!")
else:
    print("\nTus deducciones no son consistentes, acaso, tu seras el culpable?")