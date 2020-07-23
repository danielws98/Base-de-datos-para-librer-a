from tkinter import*
import tkinter.messagebox
import LibBksDatabase
sb=None


class Libreria:
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema de Administración de Librería")
        self.root.geometry("1350x750+0+0")
        
        MTy=StringVar()
        Ref=StringVar()
        Tit=StringVar()
        fna=StringVar()
        sna=StringVar()
        Adr1=StringVar()
        Adr2=StringVar()
        pcd=StringVar()
        Mno=StringVar()
        
        BKID=StringVar()
        BKT=StringVar()
        Atr=StringVar()
        DBo=StringVar()
        Adu=StringVar()
        sPr=StringVar()
        Lrf=StringVar()
        DoD=StringVar()
        DonL=StringVar()
        
        
        
        # FUNCIONES
        def iExit():
            iExit=tkinter.messagebox.askyesno("Sistema de Administración de librería","¡Confirme si desea salir!")
            if iExit>0:
                root.destroy()
                return
        
        def LimpiarDatos():
            self.txtMType.delete(0,END)
            self.txtReference.delete(0,END)
            self.txtTitulo.delete(0,END)
            self.txtPnombre.delete(0,END)
            self.txtApellido.delete(0,END)
            self.txtDireccion.delete(0,END)
            self.txtSDireccion.delete(0,END)
            self.txtCodPostal.delete(0,END)
            self.txtNCelular.delete(0,END)
            self.txtLibID.delete(0,END)
            self.txtLIBTIT.delete(0,END)
            self.txtDevolucion.delete(0,END)
            self.txtAutor.delete(0,END)
            self.txtDiasPrestamo.delete(0,END)
            self.txtFprestamo.delete(0,END)
            self.txtDevtarde.delete(0,END)
            self.txtfvencimiento.delete(0,END)
            self.txtPventa.delete(0,END)
        
        def AgregarDatos():
            if (len(MTy.get())!=0):
                LibBksDatabase.AddDataRec(MTy.get(),Ref.get(),Tit.get(),\
                fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(),Mno.get(),\
                BKID.get(),BKT.get(),Atr.get(),DBo.get(),Adu.get(),sPr.get(),\
                Lrf.get(),DoD.get(),DonL.get())
            
                listaLibros.delete(0,END)
                listaLibros.insert(END,(MTy.get(),Ref.get(),Tit.get(),fna.get(),\
                    sna.get(),Adr1.get(),Adr2.get(),pcd.get(),Mno.get(),\
                    BKID.get(),BKT.get(),Atr.get(),DBo.get(),Adu.get(),\
                    sPr.get(),Lrf.get(),DoD.get(),DonL.get()))   
                
        def MostrarData():
            listaLibros.delete(0,END)
            for row in LibBksDatabase.viewData():
                listaLibros.insert(END,row)
        
        def SelecionarLibro(event):
            global sb
            searchL=listaLibros.curselection()[0]
            sb=listaLibros.get(searchL)
            
            self.txtMType.delete(0,END)
            self.txtMType.insert(END,sb[1])
            self.txtReference.delete(0,END)
            self.txtReference.insert(END,sb[2])
            self.txtTitulo.delete(0,END)
            self.txtTitulo.insert(END,sb[3])
            self.txtPnombre.delete(0,END)
            self.txtPnombre.insert(END,sb[4])
            self.txtApellido.delete(0,END)
            self.txtApellido.insert(END,sb[5])
            self.txtDireccion.delete(0,END)
            self.txtDireccion.insert(END,sb[6])
            self.txtSDireccion.delete(0,END)
            self.txtSDireccion.insert(END,sb[7])
            self.txtCodPostal.delete(0,END)
            self.txtCodPostal.insert(END,sb[8])
            self.txtNCelular.delete(0,END)
            self.txtNCelular.insert(END,sb[9])
            self.txtLibID.delete(0,END)
            self.txtLibID.insert(END,sb[10])
            self.txtLIBTIT.delete(0,END)
            self.txtLIBTIT.insert(END,sb[11])
            self.txtDevolucion.delete(0,END)
            self.txtDevolucion.insert(END,sb[12])
            self.txtAutor.delete(0,END)
            self.txtAutor.insert(END,sb[13])
            self.txtDiasPrestamo.delete(0,END)
            self.txtDiasPrestamo.insert(END,sb[14])
            self.txtFprestamo.delete(0,END)
            self.txtFprestamo.insert(END,sb[15])
            self.txtDevtarde.delete(0,END)
            self.txtDevtarde.insert(END,sb[16])
            self.txtfvencimiento.delete(0,END)
            self.txtfvencimiento.insert(END,sb[17])
            self.txtPventa.delete(0,END)
            self.txtPventa.insert(END,sb[18])
            
        def BorrarDatos():
            if (len(MTy.get())!=0):
                LibBksDatabase.deleteRec(sb[0])
                LimpiarDatos()
                MostrarData()
        
        def BuscarDatos():
            listaLibros.delete(0,END)
            for row in LibBksDatabase.searchData(MTy.get(),Ref.get(),Tit.get(),fna.get(),\
                sna.get(),Adr1.get(),Adr2.get(),pcd.get(),Mno.get(),BKID.get(),BKT.get(),\
                Atr.get(),DBo.get(),Adu.get(),sPr.get(),Lrf.get(),DoD.get(),DonL.get()):
                listaLibros.insert(END,row)
        
        def update():
            if (len(MTy.get())!=0):
                LibBksDatabase.DataUpdate(sb[0],MTy.get(),Ref.get(),Tit.get(),fna.get(),\
                sna.get(),Adr1.get(),Adr2.get(),pcd.get(),Mno.get(),BKID.get(),BKT.get(),\
                Atr.get(),DBo.get(),Adu.get(),sPr.get(),Lrf.get(),DoD.get(),DonL.get())
                
        # AQUI VAN LOS FRAMES
        
        MainFrame=Frame(self.root)
        MainFrame.grid()
        
        TitFrame=Frame(MainFrame,bd=2,padx=40,pady=8,bg="Cadet blue",relief=RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lb1Tit=Label(TitFrame,font=('arial',46,'bold'),text="Sistema de Administración de Librería")
        self.lb1Tit.grid(sticky=W)
        
        ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=100,padx=20,pady=20,bg="Cadet Blue",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        FrameDetail=Frame(MainFrame,bd=0,width=1350,height=50,padx=20,pady=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)
        
        DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=800,height=300,padx=20,relief=RIDGE 
                                 ,font=('arial',12,'bold'),bg='Cadet Blue',text="Información de Membresía:")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=20,pady=3,relief=RIDGE,
                                  font=('arial',12,'bold'),bg="Cadet blue",text="Detalles:")
        DataFrameRIGHT.pack(side=RIGHT)
        
        # LABEL & WIDGET
        
        self.lblMemberType=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Tipo de membresía",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblMemberType.grid(row=0,column=0,sticky=W)
        self.txtMType=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=MTy,width=25)
        self.txtMType.grid(row=0,column=1,sticky=W)
        
        self.lblReference=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Referencia",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblReference.grid(row=1,column=0,sticky=W)
        self.txtReference=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ref,width=25)
        self.txtReference.grid(row=1,column=1,sticky=W)
        
        self.lblTitulo=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Título:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblTitulo.grid(row=2,column=0,sticky=W)
        self.txtTitulo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Tit,width=25)
        self.txtTitulo.grid(row=2,column=1,sticky=W)
        
        self.lblPNombre=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Nombre",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblPNombre.grid(row=3,column=0,sticky=W)
        self.txtPnombre=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=fna,width=25)
        self.txtPnombre.grid(row=3,column=1,sticky=W)
        
        self.lblApellido=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Apellido",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblApellido.grid(row=4,column=0,sticky=W)
        self.txtApellido=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=sna,width=25)
        self.txtApellido.grid(row=4,column=1,sticky=W)
        
        self.lblDireccion=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Dirección",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblDireccion.grid(row=5,column=0,sticky=W)
        self.txtDireccion=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Adr1,width=25)
        self.txtDireccion.grid(row=5,column=1,sticky=W)
        
        self.lblSDirecccion=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Segunda Dirección:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblSDirecccion.grid(row=6,column=0,sticky=W)
        self.txtSDireccion=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Adr2,width=25)
        self.txtSDireccion.grid(row=6,column=1,sticky=W)
        
        self.lblCodPostal=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Código Postal:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblCodPostal.grid(row=7,column=0,sticky=W)
        self.txtCodPostal=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=pcd,width=25)
        self.txtCodPostal.grid(row=7,column=1,sticky=W)
        
        self.lblNCelular=Label(DataFrameLEFT,font=('arial',12,'bold'),text="N° Celular:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblNCelular.grid(row=8,column=0,sticky=W)
        self.txtNCelular=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Mno,width=25)
        self.txtNCelular.grid(row=8,column=1,sticky=W)
        
        #SEGUNDA COLUMNA
        
        self.lblLibID=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Libro ID",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblLibID.grid(row=0,column=2,sticky=W)
        self.txtLibID=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=BKID,width=25)
        self.txtLibID.grid(row=0,column=3,sticky=W)
        
        self.lblTITlib=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Título del Libro",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblTITlib.grid(row=1,column=2,sticky=W)
        self.txtLIBTIT=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=BKT,width=25)
        self.txtLIBTIT.grid(row=1,column=3,sticky=W)
        
        self.lblAutor=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Autor:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblAutor.grid(row=2,column=2,sticky=W)
        self.txtAutor=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Atr,width=25)
        self.txtAutor.grid(row=2,column=3,sticky=W)
        
        self.lblFPrestamo=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Fecha Prestamo:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblFPrestamo.grid(row=3,column=2,sticky=W)
        self.txtFprestamo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DBo,width=25)
        self.txtFprestamo.grid(row=3,column=3,sticky=W)
        
        self.lblFDevolicion=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Fecha Devolución:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblFDevolicion.grid(row=4,column=2,sticky=W)
        self.txtDevolucion=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Adu,width=25)
        self.txtDevolucion.grid(row=4,column=3,sticky=W)
        
        self.lblDiasPrestamo=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Días de prestamo",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblDiasPrestamo.grid(row=5,column=2,sticky=W)
        self.txtDiasPrestamo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=sPr,width=25)
        self.txtDiasPrestamo.grid(row=5,column=3,sticky=W)
        
        self.lblDevTarde=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Devolucion Tarde:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblDevTarde.grid(row=6,column=2,sticky=W)
        self.txtDevtarde=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Lrf,width=25)
        self.txtDevtarde.grid(row=6,column=3,sticky=W)
        
        self.lblFVENCIMIENTO=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Vencimiento:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblFVENCIMIENTO.grid(row=7,column=2,sticky=W)
        self.txtfvencimiento=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DoD,width=25)
        self.txtfvencimiento.grid(row=7,column=3,sticky=W)
        
        self.lblPVenta=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Precio de Venta:",padx=2,pady=2,
                                 bg="Cadet blue")
        self.lblPVenta.grid(row=8,column=2,sticky=W)
        self.txtPventa=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DonL,width=25)
        self.txtPventa.grid(row=8,column=3,sticky=W)
        
        # LIST BOX Y EL SCROLL!!!
        
        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=0,sticky='ns')
        
        listaLibros=Listbox(DataFrameRIGHT,width=45,height=12,font=('arial',12,'bold'),
                            yscrollcommand=scrollbar.set)
        listaLibros.bind('<<ListboxSelect>>',SelecionarLibro)
        listaLibros.grid(row=0,column=0,padx=8)
        scrollbar.config(command=listaLibros.yview)
        
        #BOTONES DE COMANDO
        
        self.btnAddDate=Button(ButtonFrame,text="Agregar Datos",font=('arial',12,'bold'),height=2,width=13,bd=4,command=AgregarDatos)
        self.btnAddDate.grid(row=0,column=0)
        
        self.btnMostrarDatos=Button(ButtonFrame,text="Mostrar Datos",font=('arial',12,'bold'),height=2,width=13,bd=4,command=MostrarData)
        self.btnMostrarDatos.grid(row=0,column=1)
        
        self.btnLimpiarDatos=Button(ButtonFrame,text="Limpiar Datos",font=('arial',12,'bold'),height=2,width=13,bd=4,command=LimpiarDatos)
        self.btnLimpiarDatos.grid(row=0,column=2)
        
        self.btnBorrarDatos=Button(ButtonFrame,text="Borrar Datos",font=('arial',12,'bold'),height=2,width=13,bd=4,command=BorrarDatos)
        self.btnBorrarDatos.grid(row=0,column=3)
        
        self.btnActualizar=Button(ButtonFrame,text="Actualizar Datos",font=('arial',12,'bold'),height=2,width=13,bd=4,command=update)
        self.btnActualizar.grid(row=0,column=4)
        
        self.btnBuscar=Button(ButtonFrame,text="Buscar Datos",font=('arial',12,'bold'),height=2,width=13,bd=4,command=BuscarDatos)
        self.btnBuscar.grid(row=0,column=5)
        
        self.btnSalir=Button(ButtonFrame,text="Salir",font=('arial',12,'bold'),height=2,width=13,bd=4,command=iExit)
        self.btnSalir.grid(row=0,column=6)
        
if __name__=='__main__':
    root=Tk()
    applicaton=Libreria(root)
    root.mainloop()