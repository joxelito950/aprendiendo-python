from tkinter import *
from tkinter import messagebox
import sqlite3

# ----  variables ---------
stateDocumentEntry = "active"

# --------------- functions ---------------


def data():
    connection = sqlite3.connect("Users")
    cursor = connection.cursor()
    try:
        cursor.execute('''
            CREATE TABLE USERS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DOCUMENT INTEGER UNIQUE,
            NAME VARCHAR(20),
            LAST_NAME VARCHAR(20),
            DIRECTION VARCHAR(50),
            DATE_BIRTH DATE,
            COMMENTARIES VARCHAR(500)
            )
        ''')
        messagebox.showinfo("BBDD", "Base de datos creada con éxito.")
    except:
        messagebox.showwarning("BBDD", "La base de datos ya existe.")
    finally:
        connection.close()


def create():
    connection = sqlite3.connect("Users")
    cursor = connection.cursor()
    dates = dni.get(), name.get(), lastName.get(), direction.get(), commentariesText.get(0.1, END)
    try:
        cursor.execute("INSERT INTO USERS VALUES(NULL,?,?,?,?,NULL,?)", dates)
        connection.commit()
        messagebox.showinfo("BBDD", "Registro creado con éxito")
        clean()
    except sqlite3.IntegrityError:
        messagebox.showerror("BBDD", "error creando el registro, el DNI: {}, ya existe".format(dni.get()))
    finally:
        connection.close()


def find():
    connection = sqlite3.connect("Users")
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM USERS WHERE DOCUMENT="+dni.get())
        users = cursor.fetchall()
        clean()
        for user in users:
            idUser.set(user[0])
            dni.set(user[1])
            name.set(user[2])
            lastName.set(user[3])
            direction.set(user[4])
            dateBirth.set(user[5])
            commentariesText.insert(1.0, user[6])
    except:
        messagebox.showwarning("BBDD", "el campo DNI No puede estar  vacio")
    finally:
        connection.close()


def update():
    connection = sqlite3.connect("Users")
    cursor = connection.cursor()
    try:
        dates = dni.get(), name.get(), lastName.get(), direction.get(), commentariesText.get(0.1, END)
        cursor.execute('''UPDATE USERS SET 
                       DOCUMENT=?, NAME=?, LAST_NAME=?, DIRECTION=?, DATE_BIRTH=NULL, COMMENTARIES=? 
                       WHERE ID=''' + idUser.get(), dates)
        connection.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con éxito")
        clean()
    except:
        messagebox.showerror("BBDD", "No se pudo actualizar el usuario con DNI: {}".format(dni.get()))
    finally:
        connection.close()


def delete():
    connection = sqlite3.connect("Users")
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM USERS WHERE ID=" + idUser.get())
        connection.commit()
        messagebox.showinfo("BBDD", "Reistro eliminado con éxito")
        clean()
    except:
        messagebox.showinfo("BBDD", "El resgistro: {} con dni: {}, no se pudo eliminar".format(idUser.get(), dni.get()))
    finally:
        connection.close()


def close():
    confirmation = messagebox.askokcancel("CONFIRME", "¿Desea Salir?")
    if confirmation:
        root.destroy()


def clean():
    idUser.set("")
    dni.set("")
    name.set("")
    lastName.set("")
    direction.set("")
    dateBirth.set("")
    commentariesText.delete(1.0, END)


def info():
    information = '''
        Creado por: Jose Luis Baez \n
        version 0.0.1
    '''
    messagebox.showinfo("Acerca de...", information)


# ------------------------ window --------------------
root = Tk()

# ----------- menu ---------------------------------

barrMenu = Menu(root)
root.config(menu=barrMenu, width=600, height=600)

# ----- Data base -----------------------------------
bbddMenu = Menu(barrMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=data)
bbddMenu.add_command(label="Salir", command=close)

# ----- CRUD --------------------------------------------
crudMenu = Menu(barrMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=create)
crudMenu.add_command(label="Buscar", command=find)
crudMenu.add_command(label="Actualizar", command=update)
crudMenu.add_command(label="Eliminar", command=delete)

# ----- info --------------------------------------------

infoMenu = Menu(barrMenu, tearoff=0)
infoMenu.add_command(label="Acerca de...", command=info)

# ---------------construction menu ---------------------
barrMenu.add_cascade(label="BBDD", menu=bbddMenu)
# ---- clean --------------------------------------
barrMenu.add_command(label="Borrar", command=clean)
barrMenu.add_cascade(label="CRUD", menu=crudMenu)
barrMenu.add_cascade(label="Info", menu=infoMenu)

# ----------- form -----------------------------
miFrame = Frame(root)
miFrame.pack()

idUser = StringVar()
dni = StringVar()
name = StringVar()
lastName = StringVar()
direction = StringVar()
dateBirth = StringVar()
commentaries = StringVar()

# --- id ------
idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=1, pady=10)

idEntry = Entry(miFrame, justify="center", state="disabled", textvariable=idUser)
idEntry.grid(row=0, column=1, padx=1, pady=10)

# --- document ----
documentLabel = Label(miFrame, text="DNI:")
documentLabel.grid(row=1, column=0, padx=1, pady=10, sticky="e")

documentEntry = Entry(miFrame, textvariable=dni)
documentEntry.grid(row=1, column=1, padx=5, pady=10)

# --- name ----
nameLabel = Label(miFrame, text="Nombre:")
nameLabel.grid(row=2, column=0, padx=1, pady=10, sticky="e")

nameEntry = Entry(miFrame, textvariable=name)
nameEntry.grid(row=2, column=1, padx=5, pady=10)

# --- lastName ---
lastNameLabel = Label(miFrame, text="Apellido:")
lastNameLabel.grid(row=3, column=0, padx=1, pady=10, sticky="e")

lastNameEntry = Entry(miFrame, textvariable=lastName)
lastNameEntry.grid(row=3, column=1, padx=5, pady=10)

# --- direction ---
directionLabel = Label(miFrame, text="Dirección:")
directionLabel.grid(row=4, column=0, padx=1, pady=10, sticky="e")

directionEntry = Entry(miFrame, textvariable=direction)
directionEntry.grid(row=4, column=1, padx=5, pady=10)

# --- dateBirth ---


# --- commentaries ---
commentariesLabel = Label(miFrame, text="Comentatios:")
commentariesLabel.grid(row=6, column=0, padx=1, pady=10, sticky="e")

commentariesText = Text(miFrame, width=16, height=5)
commentariesText.grid(row=6, column=1, padx=5, pady=10)
scrollVerticalText=Scrollbar(miFrame, command=commentariesText.yview)
scrollVerticalText.grid(row=6, column=2, sticky="snew")
commentariesText.config(yscrollcommand=scrollVerticalText.set)

# ------------ buttons -----------------------------
buttonsFrame = Frame(root)
buttonsFrame.pack()

# --- buttonCreate ---
buttonCreate = Button(buttonsFrame, text="Crear", command=create)
buttonCreate.grid(row=0, column=0, padx=1, pady=10, sticky="e")

# --- buttonFind ---
buttonFind = Button(buttonsFrame, text="Buscar", command=find)
buttonFind.grid(row=0, column=1, padx=1, pady=10, sticky="e")

# --- buttonActualize ---
buttonActualize = Button(buttonsFrame, text="Actualizar", command=update)
buttonActualize.grid(row=0, column=2, padx=1, pady=10, sticky="e")

# --- buttonRemove ---
buttonRemove = Button(buttonsFrame, text="Eliminar", command=delete)
buttonRemove.grid(row=0, column=3, padx=1, pady=10, sticky="e")

# --------------- execution window ------------------

root.mainloop()