import administrador_archivos as di
import calculoFacial as cf
# Personas para entrenar
path_Persona1 = ["img/"]

path_Persona2 = ["img/"]

path_Persona3 = ["img/"]
# Personas a reconocer
pathPruebas = ["img/"]

pathPaths = [path_Persona1, path_Persona2, path_Persona3]

cf.encontrar(cf.getPromedios_local(
    pathPaths, path_Persona1, path_Persona2, path_Persona3), pathPruebas)
