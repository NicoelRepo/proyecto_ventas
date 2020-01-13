# -*- coding: utf-8 -*-
from clases import venta, dia

DIAS = {}

def crear_nuevo_dia(day):
	day_aux = dia(day)
	DIAS['/'.join(day_aux.fecha)] = day_aux

def display_day_edition_menu(dia_a_editar):
    while True:
        print('''
           ---------*---------
            MENU DE EDICION
            [A]ñadir venta
            [E]liminar venta
            [L]ista de ventas
            [S]alir
           ---------*---------
            ''')
        
        command = str(input('Que quieres hacer? '))
        
        if command == 'a':
            dia_a_editar.añadir_venta()
        
        elif command == 'e':
            modo_a_eliminar = str(input('Introduzca el modo de la venta: '))
            venta_a_elimnar = int(input('Introduzca numero de venta a eliminar: '))
            try:
                if modo_a_eliminar == 'efectivo':
                    basura = dia_a_editar.libro_del_dia['efectivo'].pop(venta_a_elimnar)
                elif modo_a_eliminar == 'targeta':
                    basura = dia_a_editar.libro_del_dia['targeta'].pop(venta_a_elimnar)
            except IndexError:
                print('La venta no ha sido encontrada')        

        elif command == 'l':
            print('-----------------*-----------------')
            print('LISTA DE VENTAS:')
            print('Efectivo')
            for i,value in enumerate((dia_a_editar.libro_del_dia['efectivo'])):
                print(str(i) + '|', '$' + str(value[1]), value[2] + '|', value[0])
            print()
            print('Targeta')
            for i,value in enumerate(dia_a_editar.libro_del_dia['targeta']):
                print(str(i) + '|', '$' + str(value[1]), value[2], value[3], str(value[4]) + '|', value[0])
            print('-----------------*-----------------')

        elif command == 's':
            break

        else:
            print('ESA OPCION NO EXISTE')    



def display_main_menu():
    while True:
        print('''
            MENU PRINCIPAL
            [C]mpezar día
            [E]ditar día
            [M]ostrar lista de dias
            [S]salir
            ''')

        command = str(input('Que quieres hacer? ')).lower()

        if command == 'c':
            day_aux = str(input('Introduce fecha: '))
            day = tuple(day_aux.split('/'))
            try:
                crear_nuevo_dia(day)
                display_day_edition_menu(DIAS[day_aux])
            except (IndexError, KeyError):
                print('La fecha es incorrecta')
                display_main_menu()    
        
        elif command == 'e':
            dia_a_editar = str(input('Que dia desea editar? '))
            if dia_a_editar in DIAS.keys():
                display_day_edition_menu(DIAS[dia_a_editar])
            else:
                print('Introdujiste mal la fecha o las misma no existe')
                display_main_menu()
        
        elif command == 'm':
            print()
            print('LISTA COMPLETA DE DIAS:')
            for days in DIAS.values():
                print(days.fecha[0] + '/' + days.fecha[1] + '/' + days.fecha[2])
            print('-----------------*-----------------')
        
        elif command == 's':
            break

        else:
            print('ESA OPCION NO EXISTE')

def run():
    display_main_menu()

if __name__ == '__main__':
	run()