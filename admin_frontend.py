from tkinter import *
from tkinter import messagebox
import admin_backend


def borrar_command():
    """Borrar todos los campos."""
    listing.delete(0, END)

    entry0.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


def campos_obligatorios():
    messagebox.showinfo("Acción necesaria", "Los campos NIF, nombre y primer apellido son obligatorios")
    return ####### hay que poner mensaje de rellenar campos obligatorios

def insert_command():
    """Search entry via button."""
    if nif.get()=="" or nombre.get() =="" or primerapellido.get()=="":
        campos_obligatorios()
        return

    if len(admin_backend.nifcomprueba(nif.get())) > 0:
        messagebox.showinfo("Cuidado", """El NIF introducido ya existe en la base de datos,
        para modificarlo utilice el botón modificar""")
        return

    admin_backend.insert(nif.get(),
                        nombre.get(),
                        primerapellido.get(),
                        segundoapellido.get())
    listing.delete(0, END)
    listing.insert(END,nif.get(),nombre.get(),
                        primerapellido.get(),
                        segundoapellido.get())

def get_selected_row(event):
    """Pre-fill fields for selected entry."""
    global selected_tuple
    index = listing.curselection()[0]
    selected_tuple = listing.get(index)

    entry0.delete(0, END)
    entry0.insert(END, selected_tuple[1])

    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])

    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])

    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])

def modificar():
    
    if len(admin_backend.nifcomprueba(nif.get())) == 0:
        messagebox.showinfo("Comprueba", """El NIF introducido no existe en la base de datos, por favor compruebe el dato y vuelva a intentarlo.""")
        return
    else:
        datos = admin_backend.nifcomprueba(nif.get())
        entry1.delete(0, END)
        entry1.insert(0, datos[0][2])
        entry2.delete(0, END)
        entry2.insert(0, datos[0][3])
        if len(datos[0])>3:
            entry3.delete(0,END)
            entry3.insert(0, datos[0][4])

        button5 = Button(window,
                        text = "Confirmar cambios",
                        width = 20,
                        cursor="hand2",
                        command = window.destroy) ### aquí habrá que llamar a una función hace saltar un mensaje
                        #### de confirmación y despueés eliminará el registro original y se insertará el nuevo.
                        ### no se si desactivar la tecla borrar campos mientras se esté en modificar

        button5.configure(font=(10))
        button5.place(relx=0.41, rely = 0.15)

        messagebox.showinfo("Instrucciones", """Modifica los campos que necesites y una vez realizados pulsa el botón Confirmar cambios.""")


    return

window = Tk()

window.wm_title("Introducir/Modificar datos")
window.wm_iconbitmap('veria.ico')
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))

# Labels for entry fields.

label9 = Label(window, text = "VERIA Face Rec  -  Introducir o modificar datos", fg="gray",
        font="times 20 bold")    ##x 0.03, 0.30, 0.60 y 0.10, 0.15.0.20
label9.place(relx = 0.23, rely= 0.01)
#label9.config(font=(50))

label0 = Label(window, text = "NIF")    ##x 0.03, 0.30, 0.60 y 0.10, 0.15.0.20
label0.place(relx = 0.03, rely= 0.10)
label0.config(font=(40))

label1 = Label(window, text = "Nombre")
label1.place(relx = 0.03, rely= 0.15)
label1.config(font=(40))

label2 = Label(window, text = "1er Apellido")
label2.config(font=(40))
label2.place(relx = 0.03, rely= 0.2)

label3 = Label(window, text = "2º Apellido")
label3.config(font=(40))
label3.place(relx = 0.03, rely = 0.25)

label4 = Label(window, text = "Entrada grabada en la base de datos:", fg="gray")
label4.config(font=(40))
label4.place(relx = 0.031, rely = 0.37)

label5 = Label(window, text = "Instrucciones:", fg="gray")
label5.config(font=(40))
label5.place(relx = 0.03, rely = 0.7)

label6 = Label(window, text = """a) Para añadir nuevos datos rellenar los campos NIF,nombre, primer apellido, segundo apellido y pulsar el botón Grabar nuevo.""", fg="gray")
label6.config(font=(30))
label6.place(relx = 0.05, rely = 0.75)

label6 = Label(window, text = """b) Para modificar datos existentes rellenar el campo NIF y pulsar Modificar.""", fg="gray")
label6.config(font=(30))
label6.place(relx = 0.05, rely = 0.79)


# Entry Fields.
nif = StringVar()
entry0 = Entry(window, textvariable = nif)
entry0.config(font=(40))
entry0.place(relx=0.12, rely=0.10)

nombre = StringVar()
entry1 = Entry(window, textvariable = nombre)
entry1.config(font=(40))
entry1.place(relx=0.12, rely=0.15)

primerapellido = StringVar()
entry2 = Entry(window, textvariable = primerapellido)
entry2.config(font=(40))
entry2.place(relx=0.12, rely=0.2)

segundoapellido = StringVar()
entry3 = Entry(window, textvariable = segundoapellido)
entry3.config(font=(40))
entry3.place(relx=0.12, rely = 0.25)



# List all data.
listing = Listbox(window, height = 8, width = 100, font=40)
listing.place(relx=0.03, rely=0.4)

# Scrollbar.
#scroller = Scrollbar(window)
#scroller.place(relx = 0.81, rely = 0.32)

# Configure scrollbar for Listbox.
#listing.configure(yscrollcommand = scroller.set)
#scroller.configure(command = listing.yview)

listing.bind('<<ListboxSelect>>', get_selected_row)

# Buttons for various operations on data.

button1 = Button(window,
                text = "Grabar nuevo",
                width = 12,
                cursor="hand2",
                command = insert_command)
button1.configure(font=(10))
button1.place(relx=0.73, rely = 0.1)

button2 = Button(window,
                text = "Borrar campos",
                width = 12,
                cursor="hand2",
                command = borrar_command)
button2.configure(font=(10))
button2.place(relx=0.73, rely = 0.17)


button3 = Button(window,
                text = "Modificar",
                width = 12,
                cursor="hand2",
                command = modificar)
button3.configure(font=(10))
button3.place(relx=0.73, rely = 0.24)

button4 = Button(window,
                text = "Cerrar",
                width = 12,
                cursor="hand2",
                command = window.destroy)
button4.configure(font=(10))
button4.place(relx=0.73, rely = 0.31)

# Keep window open until closed.
window.mainloop()
