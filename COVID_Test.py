import sys
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *


def sintomas():
    c_fiebre= fiebre.get()
    c_anosmia= anosmia.get()
    c_dolor_cab= dolor_cabeza.get()
    c_tos = tos.get()
    c_odino= odinofagia.get()
    c_resp= d_resp.get()
    c_contacto = contacto.get()
    c_area = area.get()
    c_salud = p_salud.get()
    
    print("Valor de Fiebre", c_fiebre)
    print("Valor de Anosmia", c_anosmia)
    print("Valor de Dolor de Cabeza", c_dolor_cab)
    print("Valor de OdinoFagia", c_odino)
    print("Valor de Dific Resp", c_resp)
    print("Valor de Contacto", c_contacto)
    print("Valor de Tos", c_tos)
    print("Valor de Area", c_area)
    print("Valor de P.Salud", c_salud)

#Criterio 1
    if c_fiebre + c_anosmia + c_dolor_cab + c_tos + c_contacto + c_odino + c_resp + c_area + c_salud <= 8 and c_fiebre + c_anosmia + c_dolor_cab + c_tos + c_contacto + c_odino + c_resp+ c_area + c_salud > 1 :
       messagebox.showerror(title="Diagnóstico", message="Usted posee síntomas compatibles con el COVID-19. Por favor solicite asistencia médica")
    
    elif c_anosmia == 1:
        messagebox.showinfo(title="Diagnóstico", message="Ante la presencia de este como único síntoma, se recomienda aislamiento durante 72 horas, indicando toma de muestra para diagnóstico por PCR, al tercer día de iniciado síntomas.")
    
    elif c_fiebre + c_anosmia + c_dolor_cab + c_tos + c_contacto + c_odino + c_resp + c_area + c_salud == 0:
        messagebox.showinfo(title="Diagnóstico", message="Seleccione una opción!")

    else:
         messagebox.showinfo(title="Diagnóstico", message="Usted no posee síntomas compatibles con el COVID-19")

ventana = tk.Tk()
ventana.geometry("780x500+200+50")
ventana.title("COVID-19 SelfCheck")
ventana.iconphoto(False, tk.PhotoImage(file='C:/Users/Demian/OneDrive/Escritorio/Data Scientist/Python/Practicas/covid.png'))

aviso = messagebox.showwarning(title= "Advertencia!", message="Este programa de ninguna manera reemplaza la consulta ante un médico.Presione Ok para continuar. ")

etiqueta = tk.Label(ventana,text="A continuación, marque las opciones según corresponda", font = "none 20", background = "#F50743").place(x=15, y=10)

fiebre = IntVar()
tos = IntVar()
dolor_cabeza = IntVar()
anosmia = IntVar()
odinofagia = IntVar()
d_resp= IntVar()
contacto = IntVar()
area = IntVar()
p_salud = IntVar()

#Contacto estrecho
chk_contacto = tk.Checkbutton(ventana, text="Contacto estrecho de caso confirmado de COVID-19", font = "none 16", variable=contacto , onvalue=1, offvalue=0)
chk_contacto.place(x=10, y=70)

#Area de riesgo
chk_area = tk.Checkbutton(ventana, text="Contagio en conglomerado(Areas definidas por el gobierno, ej: AMBA)", font = "none 16", variable=area , onvalue=1, offvalue=0)
chk_area.place(x=10, y=110)

#Personal de salud
chk_personal = tk.Checkbutton(ventana, text="Personal de salud que reside en áreas con transmisión local de SARS-Cov-2", font = "none 16", variable=p_salud , onvalue=1, offvalue=0)
chk_personal.place(x=10, y=150)

#Fiebre
chk_fiebre = tk.Checkbutton(ventana, text="Fiebre (37.5° o más)", font = "none 16", variable=fiebre , onvalue=1, offvalue=0)
chk_fiebre.place(x=10, y=190)

#Tos
chk_tos = tk.Checkbutton(ventana, text="Tos", font = "none 16", variable=tos , onvalue=1, offvalue=0)
chk_tos.place(x=10, y=230)

#Dolor de cabeza
chk_dolor_cabeza = tk.Checkbutton(ventana, text="Dolor de cabeza", font = "none 16", variable=dolor_cabeza , onvalue=1, offvalue=0)
chk_dolor_cabeza.place(x=10, y=270)

#Anosmia
chk_anosmia = tk.Checkbutton(ventana, text="Pérdida del sentido del olfato o del gusto", font = "none 16", variable=anosmia , onvalue=1, offvalue=0)
chk_anosmia.place(x=10, y=310)

#Odinofagia
chk_odinofagia = tk.Checkbutton(ventana, text="Dolor de garganta", font = "none 16", variable=odinofagia , onvalue=1, offvalue=0)
chk_odinofagia.place(x=10, y=350)

#Dificultad Respiratoria
chk_d_resp = tk.Checkbutton(ventana, text="Dificultad Respiratoria", font = "none 16", variable=d_resp , onvalue=1, offvalue=0)
chk_d_resp.place(x=10, y=390)







calcular= tk.Button(ventana, text="Realizar diagnóstico ahora", font = "none 16", command = sintomas, foreground="#F50743", relief="raised", borderwidth=3).place(x=230, y=450)


















































ventana.mainloop()