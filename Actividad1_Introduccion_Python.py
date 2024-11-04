################
##Actividad 1##
###############


nombre = input(" Ingresa el nombre del estudiante: ")
nota = int (input("Por favor ingresa la nota: "))

if nota > 90 :
    print("El alumno" + nombre + ("Tiene un desempeño Excelente"))
elif 80 <= nota < 90:
    print("El alumno" + nombre + ("Tiene un desempeño Sobresaliente"))
elif 70 <= nota < 80:
    print("El alumno" + nombre + ("Tiene un desempeño Aceptable"))
elif 60 <= nota < 70:
    print("El alumno" + nombre + ("Tiene un desempeño Insufiente"))
else :
    print("El alumno" + nombre + ( "Tiene un desempeño Deficiente"))
