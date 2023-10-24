"""
Proyective Geometry in P^3

Este módulo define operaciones y visualizaciones en el espacio proyectivo tridimensional (P^3). 

Funciones principales:

- Conversiones entre coordenadas homogéneas y no homogéneas.
- Representación y graficación de puntos, líneas y planos en P^3.
- Graficación de cuádricas y cónicas en P^3.
- Operaciones auxiliares para determinar la intersección de líneas y planos, determinar coplanaridad y algunas auxiliares0.

Nota sobre operaciones en P^3:
al trabajar en P^3, muchos de los puntos, líneas y planos se representan en coordenadas homogéneas, 
lo que significa que tienen una componente adicional para representar el 'peso'. 

Maestría en Ingeniería Eléctrica .

@Kevin D. Ortega
"""



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ProyectiveGeometry:
    def __init__(self):
        pass

    def to_homogeneous(self, coords):
        return [coord/coords[-1] for coord in coords]

    def from_homogeneous(self, coords):
        w = coords[-1]
        if w == 0:
            raise ValueError("Cannot convert from homogeneous coordinates if last value is zero.")
        return [coord/w for coord in coords[:-1]]

    def plot_point(self, x, y, z, w):
        x, y, z = self.from_homogeneous([x, y, z, w])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, c='r', marker='o')
        
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        
        plt.show()
#xt+pi
    def plot_plane_from_points(self, p1, p2, p3, size=10):
        a, b, c, d = self.find_plane_from_points(p1, p2, p3)
        self.plot_plane(a, b, c, d, size)

    def plot_plane(self, a, b, c, d, size=10):
        x = np.linspace(-size, size, 100)
        y = np.linspace(-size, size, 100)
        X, Y = np.meshgrid(x, y)
        
        Z = (-a*X - b*Y - d) / c
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100)
        
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        
        plt.show()

    def plot_line_from_points(self, p1, p2, color='b'):
        p1 = self.to_homogeneous(p1)
        p2 = self.to_homogeneous(p2)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color=color)
        
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        
        plt.show()

    def plot_quadric(self, a, b, c, d, f, g, h, i, j, k, l, size=10):
        """Visualizar una cuádrica en P^3"""
        x = np.linspace(-size, size, 100)
        y = np.linspace(-size, size, 100)
        X, Y = np.meshgrid(x, y)

        # Usamos dos ecuaciones para Z, debido a la ecuación de segundo grado
        discriminant1 = b*b*Y*Y - 4*a*(c*X*X + d - 2*f*X*Y + g*Y*Y)
        Z1 = np.where(discriminant1 >= 0, (-b*Y - np.sqrt(discriminant1)) / (2*a), np.nan)
        Z2 = np.where(discriminant1 >= 0, (-b*Y + np.sqrt(discriminant1)) / (2*a), np.nan)

        #Z1 = (-b*Y - np.sqrt(b*b*Y*Y - 4*a*(c*X*X + d - 2*f*X*Y + g*Y*Y))) / (2*a)
        #Z2 = (-b*Y + np.sqrt(b*b*Y*Y - 4*a*(c*X*X + d - 2*f*X*Y + g*Y*Y))) / (2*a)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z1, alpha=0.5)
        ax.plot_surface(X, Y, Z2, alpha=0.5)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.show()

    def plot_conic_on_plane(self, a, b, c, d, e, f, g, size=10):
        """Visualizar una cónica en un plano proyectivo en P^3"""
        x = np.linspace(-size, size, 100)
        y = np.linspace(-size, size, 100)
        X, Y = np.meshgrid(x, y)

        # Usamos dos ecuaciones para Z, debido a la ecuación de segundo grado
        #Z1 = (-d*Y - np.sqrt(d*d*Y*Y - 4*a*(c*X*X + g - 2*e*X*Y + f*Y*Y))) / (2*a)
        #Z2 = (-d*Y + np.sqrt(d*d*Y*Y - 4*a*(c*X*X + g - 2*e*X*Y + f*Y*Y))) / (2*a)
        discriminant2 = d*d*Y*Y - 4*a*(c*X*X + g - 2*e*X*Y + f*Y*Y)
        Z1 = np.where(discriminant2 >= 0, (-d*Y - np.sqrt(discriminant2)) / (2*a), np.nan)
        Z2 = np.where(discriminant2 >= 0, (-d*Y + np.sqrt(discriminant2)) / (2*a), np.nan)


        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z1, alpha=0.5)
        ax.plot_surface(X, Y, Z2, alpha=0.5)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.show()


    # Funciones auxiliares

    def find_plane_from_points(self, p1, p2, p3):
        matrix = np.array([p1, p2, p3, [1, 1, 1, 1]])
        if np.linalg.det(matrix) == 0:
            raise ValueError("Los puntos son colineales o coincidentes")
        a, b, c, d = np.linalg.solve(matrix, [0, 0, 0, 1])
        return a, b, c, d

    def find_line_from_points(self, p1, p2):
        return p1, p2

    def find_line_from_planes(self, plane1, plane2):
        return plane1, plane2

    def find_point_from_planes(self, plane1, plane2, plane3):
        A = np.array([plane1[:3], plane2[:3], plane3[:3]])
        b = [-plane1[3], -plane2[3], -plane3[3]]
        x, y, z = np.linalg.solve(A, b)
        return x, y, z, 1
    def find_point_from_line_plane_intersection(self, A, B, plane):
        """Encuentra el punto de intersección entre la línea AB y el plano."""
        a, b, c, d = plane
        t = (-d - a*A[0] - b*A[1] - c*A[2]) / (a*(B[0]-A[0]) + b*(B[1]-A[1]) + c*(B[2]-A[2]))
        x = A[0] + t*(B[0]-A[0])
        y = A[1] + t*(B[1]-A[1])
        z = A[2] + t*(B[2]-A[2])
        return [x, y, z, 1]
    def find_plane_from_line_and_point(self, A, B, X):
        """Encuentra un plano basado en la línea definida por los puntos A, B y el punto adicional X."""
        normal_vector = np.cross(np.array(B[:3]) - np.array(A[:3]), np.array(X[:3]) - np.array(A[:3]))
        a, b, c = normal_vector
        d = -(a*X[0] + b*X[1] + c*X[2])
        return [a, b, c, d]

    def are_lines_coplanar(self, A, B, C, D):
        """Verifica si las líneas AB y CD son coplanares."""
        volume = np.linalg.det([[B[0]-A[0], C[0]-A[0], D[0]-A[0]],
                                [B[1]-A[1], C[1]-A[1], D[1]-A[1]],
                                [B[2]-A[2], C[2]-A[2], D[2]-A[2]]])
        return abs(volume) < 1e-6

    def is_line_on_plane(self, A, B, plane):
        """Verifica si la línea AB está en el plano definido por los coeficientes del plano."""
        return all(self.is_point_on_plane(P, plane) for P in [A, B])

    def is_point_on_plane(self, point, plane):
        """Verifica si un punto está en un plano."""
        a, b, c, d = plane
        return abs(a*point[0] + b*point[1] + c*point[2] + d) < 1e-6



