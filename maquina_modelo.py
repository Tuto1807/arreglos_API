class Empleado_modelo:
    def __init__(self, codigo, nombre, estado, modelo):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado
        self.modelo = modelo
    
    def set_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo
    
    def get_codigo(self):
        return self.codigo
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_nombre(self):
        return self.nombre
    
    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def get_estado(self):
        return self.estado
    
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    def get_modelo(self):
        return self.modelo
    
    def ver_info_maquina(self):
        return f"{self.codigo} - {self.modelo} - {self.estado} - {self.nombre}"
    
    
        