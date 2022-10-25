from random import randint #Que me genera un número aleatorio

##JUEGO DE DADOS
#Puntuación
#Los 5 dados iguales suma 20 puntos
#4 dados iguales suma 12 puntos
#3 dados iguales y un par suma 9 puntos
#3 dados iguales suma 6 puntos
#2 pares de dados iguales suma 5 puntos 
#1 par de dados iguales suma 2 puntos 

#SE JUGARAN 5 RONDAS

ronda=1
dados=[] #Ejemplo de lo que puede darse [2,4,5,5,1]
puntaje = 0 

puntajeTotal= 0

while ronda <= 5:
    print(f".:: Ronda #{ronda}")
    tirarDados = input("Tirar dados?(s/n): ")
    if tirarDados =="n":
       print("Daleeeee...... tira los dados...") 
       continue

    # CARGA DE DADOS O LA TIRADA DE DADOS SOBRE LA MESA
    for i in range(5): # 0,1,2,3,4
        dados.append(randint(1,6)) #y los agregamos a medida que vayamos tirando

    print("Tus dados >>>", dados)

    trio=0
    par1=0
    par2=0
    puntaje=0


    for dado in dados:
        if dados.count(dado)==5: #Si aparece 5 veces [3,3,3,3,3]
            print(f"Felicitaciones todos iguales ({dado}) + 20")
            puntaje= puntaje + 20
            break
        elif dados.count(dado)==4: #Algo similar a [3,3,3,3,4]
            print(f"Felicitaciones 4 dados iguales ({dado}) + 12")
            puntaje= puntaje + 12
            break
        elif dados.count(dado)==3: #Algo similar a [3,3,3,4,6]
            if trio == 0:
                print(f"Sacaste un trio:{dado}")
                trio=dado

        elif dados.count(dado)==2: #[3,2,6,6,3]
            if par1 == 0:
                print(f"Sacaste un par:{dado}")
                par1=dado
            elif par1 != dado and par2==0:
                print(f"Sacaste un par:{dado}")
                par2=dado

    if par1 != 0 and par2 != 0:
        print(">>>> Doble par + 5")
        puntaje = puntaje + 5
    elif par1 != 0 or par2 != 0:
        if trio != 0:
            print(">>>> Full +  9") 
            puntaje= puntaje + 9
        else:
            print("Par simple + 2")  
            puntale= puntaje + 2
    else:
        if trio !=0:
            print(f">>>> Trio de {trio} + 6")
            puntaje= puntaje + 6

    print(f"Puntaje de la ronda: {puntaje}")

    ronda = ronda+1
    puntajeTotal=puntajeTotal + puntaje

    dados.clear() #Limpiar la lista

    print(f"Puntaje total: {puntajeTotal}")

    