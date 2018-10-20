from tkinter import *
from tkinter import messagebox
import sqlite3

#----  variables ---------

#--------------- funciones ---------------


#------------------------ ventana --------------------
root=Tk()

#----------- menu ---------------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=600, height=600)

#----- base de datos -----------------------------------
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

#----- CRUD --------------------------------------------
crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Buscar")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Eliminar")

#----- info --------------------------------------------

infoMenu=Menu(barraMenu, tearoff=0)
infoMenu.add_command(label="Acerca de...")

#----------------construccion menu ---------------------
barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Info",menu=infoMenu)

#------------ formulario -----------------------------
miFrame=Frame(root)
miFrame.pack()

# --- id ------
idLabel=Label(miFrame,text="Id:")
idLabel.grid(row=0,column=0,sticky="e",padx=1,pady=10)

idCampo=Entry(miFrame)
idCampo.grid(row=0,column=1,padx=1,pady=10)

# --- nombre ----
nameLabel=Label(miFrame,text="Nombre:")
nameLabel.grid(row=1,column=0,padx=1,pady=10,sticky="e")

nameCampo=Entry(miFrame)
nameCampo.grid(row=1,column=1,padx=5,pady=10)

# --- apellido ---
apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=2,column=0,padx=1,pady=10)

apellidoCampo=Entry(miFrame)
apellidoCampo.grid(row=2,column=1,padx=5,pady=10)

#---------------- ejecucion ventana ------------------

root.mainloop()