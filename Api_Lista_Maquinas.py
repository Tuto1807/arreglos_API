class Api_Bd_maquinas:
    def __init__(self):
       self.api_maquina = [ 
           ["Codigo" , " Nombre maquina", "Modelo maquina ", "Estado Maquina"]
           ["1234", "Brazo Robotico", "XT320", "Activo"]
           ["3849", "Prensa", "PR105", "Inactivo"]
           ["9503", "Excavadora", "LL40", "En Mantenimiento"]
           ]
    
    def imprimir_info(self):
        for i in range(len(self.api_maquina)):
            print(self.api_maquina[i])
    
    def buscar_info(self):
        return self.api_maquina[0][1]