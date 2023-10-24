from task7 import ProyectiveGeometry 
if __name__ == "__main__":
    # Instanciamos la clase
    geom = ProyectiveGeometry()

    #Preguntas..
    # puntos y el plano para las pruebas:
    A = [0, 0, 0, 1]
    B = [1, 1, 1, 1]
    plane_pi = [1, 1, 1, 3]  # Ejemplo de coeficientes para un plano

    # 1. Punto de intersección entre línea AB y plano Pi
    intersection = geom.find_point_from_line_plane_intersection(A, B, plane_pi)
    print(f"La línea que une A y B intersecta al plano Pi en el punto: {intersection}")

    # 2. Plano que contiene línea AB y punto X
    X = [2, 2, 0, 1]
    plane_from_line_and_point = geom.find_plane_from_line_and_point(A, B, X)
    print(f"El plano que contiene la línea AB y el punto X tiene coeficientes: {plane_from_line_and_point}")

    # 4. ¿L1 y L2 son coplanares?
    L1_A = [0, 0, 0, 1]
    L1_B = [1, 0, 0, 1]
    L2_A = [0, 1, 0, 1]
    L2_B = [1, 1, 0, 1]
    coplanar = geom.are_lines_coplanar(L1_A, L1_B, L2_A, L2_B)
    print(f"Las líneas L1 y L2 {'son' if coplanar else 'no son'} coplanares.")

    # 5. ¿La línea L pertenece al plano Pi?
    L_A = [0, 1, 0, 1]
    L_B = [1, 1, 0, 1]
    on_plane = geom.is_line_on_plane(L_A, L_B, plane_pi)
    print(f"La línea L {'pertenece' if on_plane else 'no pertenece'} al plano Pi.")