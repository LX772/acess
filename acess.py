#!bin/env python 
import os, sys, time
os.system("clear")
print("""si puedes desbloquear este enlace tendras una hermosa shell en tu terminal\n buena suerte, ningun systema es seguro. menos una contraseña...""")
print()
H = input("desbloqueo of Shell: ")
if H =="ningun systema es seguro":
    print("CORRECTO EMPEZANDO INSTALACION")
    time.sleep(5)
    os.system("cd $HOME && git clone https://github.com/LX772/shell.git && bash shell/install")
else:
    print("ERROR CONTRASEÑA ERRONEA ARCHIVO BORRADO")
    os.system("rm -rf $HOME/acess")
