import time
import random
from datetime import date
from datetime import datetime

Nombre = input ("Introduce tu nombre: ")
Contraseña = input ("Introduce tu contraseña,  Nota, tu contraseña por defecto es 4592: ")

if Contraseña == ("4592"):
  print ("bienvenido, " , (Nombre) )
  Eligeaplicacion = input ("""Aplicaciones:
   1. Gestor de archivos 
   2. Editor de textos 
   3. Info 
   4. Antivirus
   5. Adivina el numero
   6. Dado
   7. Fecha y hora
   8. Comprimir archivos
   9. Cambiar contraseña
      """)

  


  if Eligeaplicacion == ("1"):
    print ("""Tus archivos:
    main.py 
    commandos.py
    archivodeprueba.txt
    """)
    print ("""Tus discos:
    Disco local [Disco SSD](1 TB)
    Disco extraible [Pendrive 3.0](64 GB)""")
    
  
  if Eligeaplicacion == ("2"):
    Creardoc = input ("desea crear un documento nuevo (Y/N)")
    if Creardoc == "Y":
      documentonuevo = input ("documento nuevo:   ")
    if Creardoc == "N":
      print ("el documento no se ha creado")
      
  
  if Eligeaplicacion == ("3"):
    print ("""Esto es CommandOS un sistema operativo codigo abierto desarrollado por Nico y Javi, podeis ver el codigo en repl.it, este sistema operativo funciona con comandos, o sea, hay que meter comandos para abrir aplicaciones y mas, gracias por usar este sistema operatuvo y disfrutalo
    Discord del creador: https://discord.gg/rasQ3MevRQ """)
    

  if Eligeaplicacion == ("4"):
    acciones = input ("escanear en busca de virus [Y/N]")
    if acciones == "Y":
      print ("ESCANEANDO TU EQUIPO EN BUSCA DE VIRUS...................................")
      time.sleep (5)
      print ("no se ha encontrado ningún virus, reinicia tu equipo.")
  
  if Eligeaplicacion == ("5"):
    Eligueunnumero = input ("""Piensa en un numero del 1 al 10
    La maquina pensara otro el objetivo es pensar el mismo que la maquina
    """)
    if Eligueunnumero == (random.randrange(10)):
      print ("correcto")
    else:
      print ("incorrecto")
  if Eligeaplicacion == ("6"):
    print (random.randrange(6))
  
  if Eligeaplicacion == ("7"):
    today = date.today()
    now = datetime.now()
    #print("hoy es:" , today) 
    print("Fecha y hora:",now)
  
  if Eligeaplicacion == ("9"):
    print ("Hola, bienvenido al asistente de CommandOS")
    diasistente = input ("Ejemplos: Hola, Como estas, Que hora es")
    if diasistente == ("Hola"):
      print ("Hola")
    if diasistente == ("Como te llamas"):
      print ("Hmmm, no se ¿tu que piensas?")
    if diasistente == ("#secret1234"):
      print ("No deberias estar leyendo esto, se supone que era un secreto")
    if diasistente == ("Como estas"):
      print ("Bien")
    if diasistente == ("Que hora es"):
       today = date.today()
       now = datetime.now()
       #print("hoy es:" , today) 
       print("Fecha y hora:",now)
    
  
