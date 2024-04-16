class Mision:
    def _init_(self, tipo, reino_destino, dios_solicitante):
        self.tipo = tipo
        self.reino_destino = reino_destino
        self.dios_solicitante = dios_solicitante
        self.recursos = {}

    def es_prioritaria(self):
        return self.dios_solicitante in ['Odín', 'Loki']

class GestorDeMisiones:
    def _init_(self):
        self.misiones = []

    def agregar_mision(self, tipo, reino, dios):
        mision = Mision(tipo, reino, dios)
        self.asignar_recursos(mision)
        self.misiones.append(mision)

    def asignar_recursos(self, mision):
        if mision.es_prioritaria():
            mision.recursos['Valkirias'] = 10
            mision.recursos['Unidades'] = 50
        else:
            if mision.tipo == 'defensa':
                mision.recursos['Valkirias'] = 5
                mision.recursos['Unidades'] = 20
            elif mision.tipo == 'exploración':
                mision.recursos['Valkirias'] = 3
                mision.recursos['Unidades'] = 10
            elif mision.tipo == 'conquista':
                mision.recursos['Valkirias'] = 7
                mision.recursos['Unidades'] = 30

    def mostrar_recursos(self):
        for mision in self.misiones:
            print(f"Misión a {mision.reino_destino} ({mision.tipo}):")
            print(f"  Valkirias asignadas: {mision.recursos['Valkirias']}")
            print(f"  Unidades asignadas: {mision.recursos['Unidades']}")

# Crear gestor de misiones
gestor = GestorDeMisiones()

# Interfaz de usuario para agregar misiones
while True:
    tipo = input("Ingrese el tipo de misión (defensa, exploración, conquista): ")
    reino = input("Ingrese el reino destino: ")
    dios = input("Ingrese el dios que solicita la misión: ")
    gestor.agregar_mision(tipo, reino, dios)
    gestor.mostrar_recursos()

    continuar = input("¿Desea agregar otra misión? (s/n): ")
    if continuar.lower() != 's':
        break
