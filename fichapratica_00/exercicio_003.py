def calculate_circunference_area(raio):
    perimetro = 2*3.14*float(raio)
    print(perimetro)
    area = 3.14*(raio**2)
    print(area)
    #return area, perimetro

radius = int(input("Digite o valor do raio"))
calculate_circunference_area(radius)
#area, perimeter = calculate_circunference_area(radius)