class venta:
    '''
    tupla_venta = (prenda, precio, modo de pago, nombre de tarjeta, cuotas)
    '''

    def pedir_prenda(self):
        print()
        self.prenda = str(input('[C]ancelar   Prenda: '))
        if self.prenda.lower() == 'c':
            raise Exception
        return self.prenda
    
    def pedir_tarjeta_y_cuotas(self):
        tarjetas = ['visa', 'master', 'maestro', 'cabal', 'naranja', 'american express']
        while(True):
            self.credito_o_debito = str(input('[C]ancelar   Introduzca [Cred]ito o [D]ebito: ')).lower()
            if self.credito_o_debito == 'c':
                raise Exception    
            if ['cred', 'd'].count(self.credito_o_debito) != 1:
                print('Introduzca los datos nuevamente')
                continue
            self.credito_o_debito = 'debito'    
            break

        while(True):
            self.nombre_targ = str(input('[C]ancelar   Nombre de tarjeta: ')).lower()
            if self.nombre_targ == 'c':
                raise Exception
            if tarjetas.count(self.nombre_targ) != 1:
                print('Introduzca los datos nuevamente')
                continue    
        
            if self.credito_o_debito == 'debito':
                self.cuotas = 0
            else:
                while True:   
                    try:
                        self.cuotas = input('[C]ancelar   Cuotas: ')
                        if self.cuotas == 'c':
                            raise Exception
                        self.cuotas = int(self.cuotas)    
                        break
                    except ValueError:
                        print('Las cuotas no son validas')    
            break	
        return (self.credito_o_debito, self.nombre_targ, self.cuotas)	  

    def venta_input(self):    
        self.prenda = ', '.join(self.pedir_prenda().split('  ')).upper()
        while True:
            try:
                self.precio = input('[C]ancelar   Precio: ')
                if self.precio.lower() == 'c':
                    raise Exception
                self.precio = int(self.precio)    
                break
            except ValueError:
                print('El precio es incorrecto')    
        while True:
            modo_aux = str(input('[C]ancelar   [T]arjeta o [E]fectivo: ')).lower()
            if modo_aux.lower() == 'c':
                raise Exception
            if modo_aux.lower() == 't':
                self.modo = 'tarjeta'
                self.tupla_venta = (self.prenda, self.precio,) + self.pedir_tarjeta_y_cuotas()
                break
            elif modo_aux.lower() == 'e':
                self.modo = 'efectivo'
                self.tupla_venta = (self.prenda, self.precio, 'efectivo', '-', 0)
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
    fecha = (dia, mes, año) tuple(str)
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
        try:
            venta_aux.venta_input()
            if venta_aux.modo == 'efectivo':
                self.libro_del_dia['efectivo'].append(venta_aux.tupla_venta)
            else:
                self.libro_del_dia['tarjeta'].append(venta_aux.tupla_venta)
        except Exception:
            pass

    def añadir_venta_manual(self, caract):
        venta_aux = venta()
        venta_aux.venta_manual(caract)
        if venta_aux.modo.lower() == 'efectivo':
            self.libro_del_dia['efectivo'].append(venta_aux.tupla_venta)
        else:
            self.libro_del_dia['tarjeta'].append(venta_aux.tupla_venta)
    