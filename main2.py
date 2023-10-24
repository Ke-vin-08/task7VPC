from task7 import ProyectiveGeometry 

if __name__ == "__main__":
    # Instanciamos la clase
    geom = ProyectiveGeometry()

    # Puntos para prueba
    point = [1, 2, 3, 1]
    p1 = [3, 2, 1, 1]
    p2 = [2, 4, 2, 1]
    p3 = [3, 1, 3, 1]

    # Graficar un punto en P^3
    print("Graficando un punto en P^3...")
    geom.plot_point(*point)

    # Graficar un plano en P^3 usando tres puntos
    print("Graficando un plano en P^3...")
    geom.plot_plane_from_points(p1, p2, p3)

    # Graficar una línea en P^3 usando dos puntos
    print("Graficando una línea en P^3...")
    geom.plot_line_from_points(p1, p2)

    # Graficar una cuádrica en P^3
    print("Graficando una cuádrica en P^3...")
    geom.plot_quadric(1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)

    # Graficar una cónica en un plano proyectivo en P^3
    print("Graficando una cónica en un plano proyectivo en P^3...")
    geom.plot_conic_on_plane(1, 1, 1, 2, 1, 0, 0)

