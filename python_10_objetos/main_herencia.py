import os
from herencia import Trabajador, Secretaria, Conserje, Directivo
from tabulate import tabulate

trabajadores_ld = [
    {
        'id_trabajador': 'T1',
        'nombre': 'Juan',
        'apellido': 'Peña',
        'tipo_trabajador': "Conserje",
        'horas_trabajadas': 130,
        'incentivos': 0
    },
    {
        'id_trabajador': 'T2',
        'nombre': 'Pedro',
        'apellido': 'Perez',
        'tipo_trabajador': "Secretaria",
        'horas_trabajadas': 160,
        'incentivos': 200
    },
    {
        'id_trabajador': 'T3',
        'nombre': 'Maria',
        'apellido': 'Gutierrez',
        'tipo_trabajador': "Directivo",  
        'base': 1800,
        'dietas': 500,
        'metas': 600
    },
    {
        'id_trabajador': 'T4',
        'nombre': 'Luis',
        'apellido': 'Lopez',
        'tipo_trabajador': "Directivo",  
        'base': 1800,
        'dietas': 800,
        'metas': 800
    }
]

header = ["ID", "Nombre", "Apellido", "Clase", "Sueldo"]

def ejemplo1():
    for trabajador_d in trabajadores_ld:
        if trabajador_d['tipo_trabajador'] == "Conserje":
            trabajador = Conserje(trabajador_d['horas_trabajadas'])
            print(trabajador_d['nombre'], "Sueldo:", trabajador.sueldo())
        if trabajador_d['tipo_trabajador'] == "Secretaria":
            trabajador = Secretaria(trabajador_d['horas_trabajadas'], trabajador_d['incentivos'])
            print(trabajador_d['nombre'], "Sueldo:", trabajador.sueldo())
        if trabajador_d['tipo_trabajador'] == "Directivo":
            trabajador = Directivo(trabajador_d['base'], trabajador_d['dietas'], trabajador_d['metas'])
            print(trabajador_d['nombre'], trabajador_d['apellido'], "Sueldo:", trabajador.sueldo())

def sueldo():
    for trabajador in trabajadores_ld:
        if trabajador['tipo_trabajador'] == "Conserje":
            trabajador['sueldo'] = Conserje(trabajador['horas_trabajadas']).sueldo()
        elif trabajador['tipo_trabajador'] == "Secretaria":
            trabajador['sueldo'] = Secretaria(trabajador['horas_trabajadas'], trabajador['incentivos']).sueldo()
        elif trabajador['tipo_trabajador'] == "Directivo":
            trabajador['sueldo'] = Directivo(trabajador['base'], trabajador['dietas'], trabajador['metas']).sueldo()
        else:
            trabajador['sueldo'] = 0
    
    # Transformar los datos para tabular
    datos = [[t['id_trabajador'], t['nombre'], t['apellido'], t["tipo_trabajador"], t.get('sueldo', 0)] for t in trabajadores_ld]
    print(tabulate(datos, headers=header, tablefmt='fancy_grid'))

def main():
    os.system("clear")
    ejemplo1()
    print()
    sueldo()
          
if __name__ == "__main__":
   main()
