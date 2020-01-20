# -*- coding: utf-8 -*-
from clases import venta, dia
import os
import sys
import csv

DAYS = {}
#   DAYS[
#       fecha1(tripla) : dia1(objeto, dia) 
#       fecha2 : dia2
#       ... 
#       fechaN : diaN
#   ]

def _initialize_DAYS_from_storage():
    global DAYS

    DAYS_aux = []
    with open('.DAYS.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            DAYS_aux.append(row)
    
    try:
        dia_actual = (tuple(DAYS_aux[0]))
        create_new_day(dia_actual)
    except IndexError:
        pass    
    for i,value in enumerate(DAYS_aux):
        if i == 0 or DAYS_aux[i-1] == ['-']:
            continue
        if value == ['-']:
            try:
                dia_actual = (tuple(DAYS_aux[i+1]))
                create_new_day(dia_actual)
                continue
            except IndexError:
                continue    

        DAYS['/'.join(dia_actual)].añadir_venta_manual(DAYS_aux[i])


def _save_DAYS_to_storage():
    with open('.DAYS.csv.tmp', mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for day in DAYS:
            writer.writerow(DAYS[day].fecha)
            for venta in DAYS[day].libro_del_dia['efectivo']:
                writer.writerow(venta)
            for venta in DAYS[day].libro_del_dia['tarjeta']:
                writer.writerow(venta)
            writer.writerow('-')

    
    os.remove('.DAYS.csv')
    os.rename('.DAYS.csv.tmp', '.DAYS.csv')


def create_new_day(day):
    '''
    parametro: tupla(dia, mes, año)
    añade un objeto dia al diccionario DAYS
    '''
    global DAYS

    day_aux = dia(day)
    DAYS['/'.join(day_aux.fecha)] = day_aux


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
            _save_DAYS_to_storage()
        
        elif command == 'e':
            try:
                modo_a_eliminar = str(input('Introduzca el modo de la venta: '))
                venta_a_elimnar = int(input('Introduzca numero de venta a eliminar: '))
                if modo_a_eliminar == 'efectivo':
                    basura = dia_a_editar.libro_del_dia['efectivo'].pop(venta_a_elimnar)
                elif modo_a_eliminar == 'tarjeta':
                    basura = dia_a_editar.libro_del_dia['tarjeta'].pop(venta_a_elimnar)
                else:
                    raise ValueError    
            except (IndexError, ValueError):
                print()
                print('La venta no ha sido encontrada')
            else:
                print('La venta ha sido eliminada correctamente')
            _save_DAYS_to_storage()

        elif command == 'l':
            print('-----------------*-----------------')
            print('LISTA DE VENTAS:')
            print('Efectivo')
            for i,value in enumerate((dia_a_editar.libro_del_dia['efectivo'])):
                print(str(i) + '|', '$' + str(value[1]), value[2] + '|', value[0])
            print()
            print('tarjeta')
            for i,value in enumerate(dia_a_editar.libro_del_dia['tarjeta']):
                print(str(i) + '|', '$' + str(value[1]), value[2], value[3], str(value[4]) + '|', value[0])
            print('-----------------*-----------------')

        elif command == 's':
            _save_DAYS_to_storage()
            break

        else:
            print('ESA OPCION NO EXISTE')    


def display_main_menu():
    global DAYS

    while True:
        print('''
           ---------*---------
            MENU PRINCIPAL
            [C]mpezar día
            [E]ditar día
            [M]ostrar lista de dias
            [S]salir
           ---------*---------
            ''')

        command = str(input('Que quieres hacer? ')).lower()

        if command == 'c':
            day_aux = str(input('Introduce fecha: '))
            day = tuple(day_aux.split('/'))
            try:
                create_new_day(day)
                _save_DAYS_to_storage()
                display_day_edition_menu(DAYS[day_aux])
            except (IndexError, KeyError):
                print('La fecha es incorrecta')
                display_main_menu()    
        
        elif command == 'e':
            dia_a_editar = str(input('Que dia desea editar? '))
            if dia_a_editar in DAYS.keys():
                display_day_edition_menu(DAYS[dia_a_editar])
            else:
                print('Introdujiste mal la fecha o las misma no existe')
                display_main_menu()
        
        elif command == 'm':
            print()
            print('LISTA COMPLETA DE DAYS:')
            for days in DAYS.values():
                print(days.fecha[0] + '/' + days.fecha[1] + '/' + days.fecha[2])
            print('-----------------*-----------------')
        
        elif command == 's':
            break

        else:
            print('ESA OPCION NO EXISTE')


def run():
    _initialize_DAYS_from_storage()
    display_main_menu()
    _save_DAYS_to_storage()

if __name__ == '__main__':
	run()