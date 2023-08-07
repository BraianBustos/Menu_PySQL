import os;
from os import system;
import sqlite3;



def ingresar_cliente():
    conexion=sqlite3.connect(r"C:\Users\USUARIO\Desktop\Diseño_web\Menu_PySQL\src\database/midbase");
    cursor= conexion.cursor();
    Nombre_Cliente = input("Nombre del cliente: ");
    print("");
    Apellido_Cliente = input("Apellido del cliente: ");
    print("");
    Domicilio_Cliente = input("Domicilio del cliente: ");
    print("");
    DNI = input("DNI: ");
    print("");
    cursor.execute("INSERT INTO USUARIOS(Nombre_Cliente,Apellido_Cliente,Domicilio_Cliente,DNI) VALUES (?,?,?,?)",(Nombre_Cliente,Apellido_Cliente,Domicilio_Cliente,DNI));
    conexion.commit();
    conexion.close();



def opcion():
    OPC = input("Para continuaar presione C, para salir presione S: ");
    while (OPC != "C") and(OPC != "S"):
            if (OPC == "c") or (OPC == "s"):
                OPC = OPC.upper();
                if (OPC == "C"):
                    system("cls");
                    OPC == "C";
                elif (OPC == "S"):
                    break;
            else:
                print("Error!! Intente nuevamente \n");
                print("")
                OPC = input("Para continuar presione C, para salir presione S: \n");
                print("");
    return OPC;


def buscar_cliente_DNI(): 
    conexion=sqlite3.connect(r"C:\Users\USUARIO\Desktop\Diseño_web\Menu_PySQL\src\database/midbase");
    cursor= conexion.cursor();
    DNI1 = input("Ingrese el DNI del cliente: ");
    print("");
    DNI="'" + DNI1 + "'"
    medcons = "SELECT * FROM USUARIOS WHERE DNI=" + str(DNI);
    consulta = medcons;
    cursor.execute(consulta);
    for fila in cursor:
        print("ID: ",fila[0],"Nombre:",fila[1],"   Apellido:",fila[2],"   Domicilio:",fila[3],"   DNI:",fila[4]);
    print("");
    conexion.close();
    print("");
   
def buscar_cliente_Apellido(): 
    conexion=sqlite3.connect(r"C:\Users\USUARIO\Desktop\Diseño_web\Menu_PySQL\src\database/midbase");
    cursor= conexion.cursor();
    Apellido1 = input("Ingrese el Apellido del cliente: ");
    print("");
    Apellido="'" + Apellido1 + "'"
    medcons = "SELECT * FROM USUARIOS WHERE Apellido_Cliente=" + str(Apellido);
    consulta = medcons;
    cursor.execute(consulta);
    for fila in cursor:
        print("ID: ",fila[0],"Nombre:",fila[1],"   Apellido:",fila[2],"   Domicilio:",fila[3],"   DNI:",fila[4]);
    print("");
    conexion.close();
    print("");
   
   
def modificar_nombre_Cliente():
    conexion=sqlite3.connect(r"C:\Users\USUARIO\Desktop\Diseño_web\Menu_PySQL\src\database/midbase");
    cursor= conexion.cursor();
    DNI1 = input("Ingrese el DNI del cliente que desea modificar: ");
    print("");
    DNI="'" + DNI1 + "'"
    medcons = "SELECT * FROM USUARIOS WHERE DNI=" + str(DNI);
    consulta = medcons;
    cursor.execute(consulta);
    for fila in cursor:
        print("ID: ",fila[0],"Nombre:",fila[1],"   Apellido:",fila[2],"   Domicilio:",fila[3],"   DNI:",fila[4]);
    print("");
    print("");
    Nombre_Cliente1 = input("Ingrese el nuevo nombre : ");
    print(" ");
    Nombre_Cliente="'" + Nombre_Cliente1 + "'"
    medcons = "UPDATE USUARIOS SET Nombre_Cliente=" + str(Nombre_Cliente) + " WHERE DNI= "+ str(DNI);
    cursor.execute(medcons);
    print(" ");
    conexion.commit();
    conexion.close();
    print("Dato modificado satisfactoriamente.");
    print("");
    system("cls");
    
def modificar_apellido_Cliente():
    conexion=sqlite3.connect(r"C:\Users\USUARIO\Desktop\Diseño_web\Menu_PySQL\src\database/midbase");
    cursor= conexion.cursor();
    DNI1 = input("Ingrese el DNI del cliente que desea modificar: ");
    print("");
    DNI="'" + DNI1 + "'"
    medcons = "SELECT * FROM USUARIOS WHERE DNI=" + str(DNI);
    consulta = medcons;
    cursor.execute(consulta);
    for fila in cursor:
        print("ID: ",fila[0],"Nombre:",fila[1],"   Apellido:",fila[2],"   Domicilio:",fila[3],"   DNI:",fila[4]);
    print("");
    print("");
    Apellido_Cliente1 = input("Ingrese el nuevo Apellido : ");
    print(" ");
    Apellido_Cliente="'" + Apellido_Cliente1 + "'"
    medcons = "UPDATE USUARIOS SET Apellido_Cliente=" + str(Apellido_Cliente) + " WHERE DNI= "+ str(DNI);
    cursor.execute(medcons);
    print(" ");
    conexion.commit();
    conexion.close();
    print("Dato modificado satisfactoriamente.");
    print("");
    system("cls");
    
def modificar_domicilio_Cliente():
    conexion=sqlite3.connect(r"C:\Users\USUARIO\Desktop\Diseño_web\Menu_PySQL\src\database/midbase");
    cursor= conexion.cursor();
    DNI1 = input("Ingrese el DNI del cliente que desea modificar: ");
    print("");
    DNI="'" + DNI1 + "'"
    medcons = "SELECT * FROM USUARIOS WHERE DNI=" + str(DNI);
    consulta = medcons;
    cursor.execute(consulta);
    for fila in cursor:
        print("ID: ",fila[0],"Nombre:",fila[1],"   Apellido:",fila[2],"   Domicilio:",fila[3],"   DNI:",fila[4]);
    print("");
    print("");
    Domicilio_Cliente1 = input("Ingrese el nuevo Domicilio: ");
    print(" ");
    Domicilio_Cliente="'" + Domicilio_Cliente1 + "'"
    medcons = "UPDATE USUARIOS SET Domicilio_Cliente=" + str(Domicilio_Cliente) + " WHERE DNI= "+ str(DNI);
    cursor.execute(medcons);
    print(" ");
    conexion.commit();
    conexion.close();
    print("Dato modificado satisfactoriamente.");
    print("");
    system("cls");
    
def modificar_DNI_Cliente():
    conexion=sqlite3.connect(r"C:\Users\USUARIO\Desktop\Diseño_web\Menu_PySQL\src\database/midbase");
    cursor= conexion.cursor();
    Apellido1 = input("Ingrese el Apellido del cliente que desea modificar: ");
    print("");
    Apellido="'" + Apellido1 + "'"
    medcons = "SELECT * FROM USUARIOS WHERE Apellido_Cliente=" + str(Apellido);
    consulta = medcons;
    cursor.execute(consulta);
    for fila in cursor:
        print("ID: ",fila[0],"   Nombre:",fila[1],"   Apellido:",fila[2],"   Domicilio:",fila[3],"   DNI:",fila[4]);
    print("");
    print("");
    ID1 = input("Ingrese el ID del cliente que desea modificar: ");
    print("");
    ID="'" + ID1 + "'"
    DNI1 = input("Ingrese el nuevo DNI: ");
    print(" ");
    DNI="'" + DNI1 + "'"
    medcons = "UPDATE USUARIOS SET DNI=" + str(DNI) + " WHERE ID_Cliente= "+ str(ID);
    cursor.execute(medcons);
    print(" ");
    conexion.commit();
    conexion.close();
    print("Dato modificado satisfactoriamente.");
    print("");
    system("cls");

def eliminar_Cliente():
    conexion=sqlite3.connect(r"C:\Users\USUARIO\Desktop\Diseño_web\Menu_PySQL\src\database/midbase");
    cursor= conexion.cursor();
    Apellido1 = input("Ingrese el Apellido del cliente que desea eliminar: ");
    print("");
    Apellido="'" + Apellido1 + "'"
    medcons = "SELECT * FROM USUARIOS WHERE Apellido_Cliente=" + str(Apellido);
    consulta = medcons;
    cursor.execute(consulta);
    for fila in cursor:
        print("ID: ",fila[0],"   Nombre:",fila[1],"   Apellido:",fila[2],"   Domicilio:",fila[3],"   DNI:",fila[4]);
    print("");
    print("");
    ID1 = input("Ingrese el ID del cliente que desea eliminar: ");
    print("");
    ID="'" + ID1 + "'"
    medcons = "DELETE FROM USUARIOS WHERE ID_Cliente= "+ str(ID);
    cursor.execute(medcons);
    print(" ");
    conexion.commit();
    conexion.close();
    print("Dato eliminado satisfactoriamente.");
    print("");
    system("cls");
    
    
    
    
























