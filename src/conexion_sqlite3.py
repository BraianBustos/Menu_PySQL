import sqlite3
import os
import funciones

##cursor.execute("CREATE TABLE USUARIOS (ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), DOMICILIO VARCHAR(50), EDAD INTEGER)")
##conexion.close()

OPC  = "C";

while (OPC == "C"):
    print(" ");
    print(" ");
    print("...................................................................Menú.......................................................................");
    print(" ");
    print("1-Agregar cliente\n2-Buscar cliente.");
    print("3-Agregar o modificar datos\n4-Borrar cliente\n5-Cerrar.");
    print(" ");
    print(" ");
    Op = str(input("Seleccione una opción: "));
    print(" ");
    print("");

    if(Op == "1"):
        funciones.ingresar_cliente();
        OPC = funciones.opcion();
        print(" ");
        print("");
    elif (Op == "2"):
        Op2 = input("Para buscar por Apellido presione 1\nPara buscar por DNI presione 2\nPara volver al menú anterior presione V: ");
        print("");
        print("");
        if (Op2 == "1"):
            funciones.buscar_cliente_Apellido();
            OPC = funciones.opcion();
            print(" ");
            print("");
        elif (Op2 == "2"):
            funciones.buscar_cliente_DNI();
        else:
            OPC = "C";
    elif(Op == "3"):
        print("");
        print("1-Modificar Nombre\n2-Modificar Apellido.");
        print("3-Modificar Domicilio\n4-Modificar DNI\n5-Volver al menú anterior.");
        print(" ");
        print(" ");
        Op3 = str(input("Seleccione una opción: "));
        print(" ");
        if (Op3 == "1"):
            funciones.modificar_nombre_Cliente();
        elif(Op3 == "2"):
            funciones.modificar_apellido_Cliente();
        elif(Op3 == "3"):
            funciones.modificar_domicilio_Cliente();
        elif(Op3 == "4"):
            funciones.modificar_DNI_Cliente();
    elif(Op == "4"):
        funciones.eliminar_Cliente();
    elif(Op == "5"):
        break;
    else:
        print("Error, intente nuevamente");


    
        
        
        

        


































    
    
    
    
    
    
    
    


