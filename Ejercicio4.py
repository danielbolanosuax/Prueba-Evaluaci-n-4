import numpy as np

class RootFinder:
    def __init__(self, function, derivative=None):
        self.function = function
        self.derivative = derivative

    def bisection(self, a, b, tol=1e-6, max_iter=1000):
        """Método de bisección para encontrar la raíz de la función."""
        try:
            iteraciones = 0
            while (b - a) / 2 > tol and iteraciones < max_iter:
                c = (a + b) / 2
                if self.function(c) == 0:
                    return c, iteraciones
                elif self.function(a) * self.function(c) < 0:
                    b = c
                else:
                    a = c
                iteraciones += 1
            return (a + b) / 2, iteraciones
        except Exception as e:
            raise Exception("Error en el método de bisección:", e)

    def secant(self, x0, x1, tol=1e-6, max_iter=1000):
        """Método de la secante para encontrar la raíz de la función."""
        try:
            iteraciones = 0
            while iteraciones < max_iter:
                x2 = x1 - (self.function(x1) * (x1 - x0)) / (self.function(x1) - self.function(x0))
                if abs(x2 - x1) < tol:
                    return x2, iteraciones
                x0 = x1
                x1 = x2
                iteraciones += 1
            return x2, iteraciones
        except Exception as e:
            raise Exception("Error en el método de la secante:", e)

    def newton_raphson(self, x0, tol=1e-6, max_iter=1000):
        """Método de Newton-Raphson para encontrar la raíz de la función."""
        try:
            iteraciones = 0
            while iteraciones < max_iter:
                x1 = x0 - self.function(x0) / self.derivative(x0)
                if abs(x1 - x0) < tol:
                    return x1, iteraciones
                x0 = x1
                iteraciones += 1
            return x1, iteraciones
        except Exception as e:
            raise Exception("Error en el método de Newton-Raphson:", e)

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir la función y su derivada
    def f(x):
        return x**3 - 2*x - 5

    def derivada_f(x):
        return 3*x**2 - 2

    # Crear un objeto RootFinder
    root_finder = RootFinder(f, derivada_f)

    # Parámetros para los métodos
    a, b = 1, 3  # Intervalo para el método de bisección
    x0, x1 = 1, 3  # Condiciones iniciales para el método de la secante
    x_ini = 3  # Condición inicial para el método de Newton-Raphson
    tol = 1e-6  # Tolerancia
    max_iter = 1000  # Máximo de iteraciones permitidas

    # Ejecutar los métodos y obtener los resultados
    try:
        raiz_biseccion, iter_biseccion = root_finder.bisection(a, b, tol, max_iter)
        raiz_secante, iter_secante = root_finder.secant(x0, x1, tol, max_iter)
        raiz_newton, iter_newton = root_finder.newton_raphson(x_ini, tol, max_iter)

        # Imprimir los resultados
        print("Método de Bisección:")
        print("Raíz:", raiz_biseccion)
        print("Iteraciones:", iter_biseccion)

        print("\nMétodo de la Secante:")
        print("Raíz:", raiz_secante)
        print("Iteraciones:", iter_secante)

        print("\nMétodo de Newton-Raphson:")
        print("Raíz:", raiz_newton)
        print("Iteraciones:", iter_newton)
    except Exception as e:
        print("Se produjo un error:", e)
