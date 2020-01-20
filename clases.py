class venta:
    '''
    tupla_venta = (prenda, precio, modo de pago, nombre de tarjeta, cuotas)
    '''

    def pedir_prenda(self):
        print()
        self.prenda = str(input('Prenda: '))
        return self.prenda
    
    def pedir_tarjeta_y_cuotas(self):
        tarjetas = ['visa', 'master', 'maestro', 'cabal', 'naranja', 'american express']
        while(True):
            self.credito_o_debito = str(input('Introduzca credito o debito: ')).lower()
            if ['credito', 'debito'].count(self.credito_o_debito) != 1:
                print('Introduzca los datos nuevamente')
                continue 
            break

        while(True):
            self.nombre_targ = str(input('Nombre de tarjeta: ')).lower()
            if tarjetas.count(self.nombre_targ) != 1:
                print('Introduzca los datos nuevamente')
                continue    
        
            if self.credito_o_debito == 'debito':
                self.cuotas = 0
            else:
                while True:   
                    try:
                        self.cuotas = int(input('Cuotas: '))
                        break
                    except ValueError:
                        print('Las cuotas no son validas')    
            break	
        return (self.credito_o_debito, self.nombre_targ, self.cuotas)	  

    def venta_input(self):
        self.prenda = ', '.join(self.pedir_prenda().split()).upper()
        while True:
            try:
                self.precio = int(input('Precio: '))
                break
            except ValueError:
                print('El precio es incorrecto')    
        while True:
            self.modo = str(input('tarjeta o Efectivo: ')).lower()
            if self.modo == 'tarjeta':
                self.tupla_venta = (self.prenda, self.precio,) + self.pedir_tarjeta_y_cuotas()
                break
            elif self.modo == 'efectivo':
                self.tupla_venta = (self.prenda, self.precio, 'Efectivo', '-', 0)
                break  
            else:
                print('Introduzca los datos nuevamente')


    def venta_manual(self, caract):
        self.prenda = caract[0]
        self.precio = int(caract[1])
        self.modo = caract[2]
        self.credito_o_debito = caract[3]
        self.cuotas = int(caract[4])
        self.tupla_venta = (self.prenda, self.precio, self.modo, self.credito_o_debito, self.cuotas)

class dia():
    '''
    fecha = (dia, mes, año) tuple(int)
    libro_del_dia = {
        'efectivo' : [tupla_venta1, ... , tupla_ventaN]

        'efectivo' : [tupla_venta1, ... , tupla_ventaN]
    }
    '''

    def __init__(self, fecha):
        self.fecha = (fecha[0], fecha[1], fecha[2])
        self.libro_del_dia = {'efectivo': [], 'tarjeta': []}

    def añadir_venta(self):
        venta_aux = venta()
        venta_aux.venta_input()
        if venta_aux.modo == 'efectivo':
            self.libro_del_dia['efectivo'].append(venta_aux.tupla_venta)
        else:
            self.libro_del_dia['tarjeta'].append(venta_aux.tupla_venta)
        
    def añadir_venta_manual(self, caract):
        venta_aux = venta()
        venta_aux.venta_manual(caract)
        if venta_aux.modo == 'efectivo':
            self.libro_del_dia['efectivo'].append(venta_aux.tupla_venta)
        else:
            self.libro_del_dia['tarjeta'].append(venta_aux.tupla_venta)
    