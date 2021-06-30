import numpy as np

class Problema01():
    def __init__(self, l1,l2,l3,pu,x,e,ine,y):
        self.l1 = float(l1)
        self.l2 = float(l2)
        self.l3 = float(l3)
        self.pu = float(pu)
        self.x = float(x)
        self.e = float(e)
        self.ine = float(ine)
        self.y = float(y)
        
    def procedimiento_principal(self, l1, l2, l3, x, elas, ine, pu, lt):
        # S = a * b * ( c * d - e)
        a = 1 /( elas*ine)
        b = (l1 - (l1**2)/lt)
        c = 1 / lt
        d = l1/3 + l2**2/(6 * l1) + l3**2/(6*l1) + l2/2 + l3/2 + (l2*l3)/(3*l2)
        e = l1**2 / 6

        valor_s = self.calcular_s(a, b, c, d, e)

        # D = a * b * (c*d-e*f)
        d = l1**2/(3*l3) + l2**2/(6*l3) + l3/6 + (l1+l2)/(6*l3) + l1/2 + l2/3
        e =l3/(l2+l3)
        f = l3**2/6

        valor_d = self.calcular_d(a,b,c,d,e,f)

        # F = a * (b - c + (d + e + f))
        b = (l3*l1*(l1+l2))/lt
        c = (l3*l1**3)/(3*lt)
        d = (l3*(l1+l2))/2
        e = ((l1+l2)**2)/6
        f = l3**2/3

        valor_f = self.calcular_f(a,b,c,d,e,f)

        # G = a * (b * (c + d + e) + f)
        b = (l3*(l1 + l2)**2)/lt**2
        c = (l3*(l1+l2))/2
        d = ((l1 + l2)**2)/6
        e = l3**2/3
        f = (l3*(l1+l2)**3)/(6*lt)

        valor_g = self.calcular_g(a,b,c,d,e,f)

        return [valor_s, valor_d, valor_f, valor_g]
        
    def procedimiento1(self, l1, l2, l3, x, elas, ine, pu,lt):
        print('procedimiento 1')

        
        # H = a * (b * c - d * e * f)
        a = pu / (elas * ine)
        b = x - ((x**2)/lt)
        c = (l2 + l3)**3 / (6*(lt-x))
        d = x - x**2/lt
        e =((2*x**2)/(3*lt))+(lt/6)-(x/2)
        f = (l2 + l3)
        print([a,b,c,d,e,f])
        valor_h = a * (b * c - d * e * f)
        print('valor h: '+ str(valor_h))
        # J  = a * (b * c - d * e)
        b = x - x**2/lt
        c = (l3)**3/(6*(lt-x))
        d = x - x**2/lt
        e = ((2*(x**2)*l3)/(3*lt)) + (lt*l3)/6 +(x*l3)/2

        valor_j = a * (b * c - d * e)
        print('valor j: '+str(valor_j))
        return [valor_h, valor_j]
        
    def procedimiento2(self, l1, l2, l3,x, elas, ine, pu, lt):
        print('procedimiento 2')

        # H = a * (b * c - d * e )
        a = pu / (elas * ine)
        b = x - x**2/lt
        c = (lt*l1)/2 - (l1*x)/6
        d = l1 -(x*l1)/lt
        e =l1**2/6
    

        valor_h = a * (b * c - d * e)

        # J  = a * (b * c - d * e)
        b = x - x**2/lt
        c = ((lt*l3)+(x*l3))/6
        d = (x*l3)/(lt-x) - (x**2*l3)/(lt**2-lt+x)
        e = l3**2/6

        valor_j = a * (b * c - d * e)

        return [valor_h, valor_j]


    def procedimiento3(self, l1, l2, l3, x, elas, ine, pu, lt):
        print('procedimiento 3')

        # H = a * (b * c - d * e )
        a = pu / (elas * ine)
        b = x - (x**2-l1-l2)/lt
        c = (lt-x)/(3*l1)
        d = (l1/6)*(1-(x**2-l1-l2)/(lt*x))
        e =(l1+l2)**2
    

        valor_h = a * (b * c - d * e)

        # J  = a * (b * c - d * e)
        b = 1/(3*(l1-l2))
        c = (x-(x**2-l1-l2)/lt)*(lt-x)
        d = ((l1+l2)**3)/6
        e = 1-((x**2-l1-l2)/(lt*x))

        valor_j = a * (b * c - d * e)

        return [valor_h, valor_j]

    def suma_longitudes(self, l1, l2, l3):
        return l1 + l2 + l3

    def calcular_s(self, a,b,c,d,e):
        return a * b * ( c * d - e)

    def calcular_d(self, a,b,c,d,e,f):
        return a * b * (c*d-e*f)

    def calcular_f(self, a,b,c,d,e,f):
        return a * (b - c + (d + e + f))

    def calcular_g(self, a,b,c,d,e,f):
        return a * (b * (c + d + e) + f)

    

    def armar_matriz(self, s,d,f,g):
        matriz = [[s,f],[d,g]]
        return np.array(matriz)

    def armar_vector(self,h,j):
        vector = [[-h],[-j]]
        return np.array(vector)

    def calcular_momento(self, ay, by, cy):
        
        termino_a = 1/(self.e*self.ine)
        # termino b
        if (self.y>self.l1):
            termino_b = by *(self.y-self.l1)
        elif(self.y<self.l1):
            termino_b = 0
        # termino c
        if (self.y>(self.l1+self.l2)):
            termino_c = cy*(self.y-self.l2-self.l1)
        elif(self.y<(self.l1+self.l2)):
            termino_c = 0
        # termino d
        if(self.y >self.x):
            termino_d = self.pu*(self.y-self.x)
        elif(self.y < self.x):
            termino_d = 0
        
        return termino_a * (ay + termino_b + termino_c - termino_d)
        

    def calcular_cortante(self, ay, by,cy):
       
        termino_a = 1/(self.e*self.ine)
        # termino_b
        if (self.y>self.l1):
            termino_b = by
        elif(self.y<self.l1):
            termino_b = 0
        # termino c
        if (self.y>(self.l1+self.l2)):
            termino_c = cy
        elif(self.y<(self.l1+self.l2)):
            termino_c = 0
        # termino d
        if(self.y>self.x):
            termino_d = self.pu
        elif(self.y<self.x):
            termino_d = 0
        
        return termino_a * (ay + termino_b + termino_c - termino_d)
        
    def calcular_deformacion(self,ay, by, cy):
        deformacion = 0
        if self.procedimiento == 1:
            if(self.y<self.l1):
                termino_1 = (1/6*ay*self.y**3-self.pu*(self.l1-self.x)**3)
                termino_2 = -ay*self.l1**2/6 + (self.pu*(self.l1-self.x)**3/(6*self.l1))*self.y
                deformacion = 1/(self.e*self.ine)* termino_1 + termino_2
            elif((self.y > self.l1) and (self.y < (self.l1+self.l2))):
                termino_z1 = 1/(6*self.l2)
                termino_z2 = ay*(self.l1+self.l2)**3 - by*self.l2**3
                termino_z3 = self.pu*((self.l1-self.x)**3-(self.l1+self.l2-self.x))
                termino_z4 = - ay*self.l1**3
                termino_z = termino_z1 *(termino_z2 + termino_z3 + termino_z3)

                termino_n1 = self.pu(self.l1-self.x) - ay*self.l1**3
                termino_n2 = - (ay*(self.l1+self.l2)**3)/self.l2 + by*self.l2**2
                termino_n3 = - (self.pu*((self.l1-self.x)**3 - (self.l1*self.l2 - self.x)**3))/self.l2 + (ay*self.l1**3)/(self.l2)
                termino_n = 1/6*(termino_n1 + termino_n2 + termino_n3)

                deformarcion = 1/(self.e*self.ine)*(1/6*(ay*self.y**3+by*(self.y-self.l1)**3-self.pu*(self.y-self.x)**3)+termino_z*self.y + termino_n)
            elif((self.y>(self.l1+self.l2)) and (self.y<(self.l1+self.l2+self.l3))):
                lt = self.suma_longitudes(self.l1,self.l2,self.l3)
                termino_z1 = -(self.pu*((self.l1+self.l2-self.x)**3-(lt-self.x)**3))/(6*self.l3)
                termino_z2 = - ay*lt**3/(6*self.l3)
                termino_z3 = -by*(self.l2+self.l3)**3/(6*self.l3)
                termino_z4 = -cy*self.l3**2/6
                termino_z5 = ay*(self.l1+self.l2)**3/(6*self.l3)
                termino_z6 = by*(self.l2)**3/(6*self.l3)
                termino_z = termino_z1 + termino_z2 + termino_z3 + termino_z4 + termino_z5 + termino_z6

                termino_n1 = self.pu*(self.l1+self.l2-self.x)**3/6
                termino_n2 = -ay*(self.l1+self.l2)**3/6
                termino_n3 = -by*self.l2**3/6
                termino_n4 = -termino_z*(self.l1+self.l2)
                termino_n = termino_n1 + termino_n2 + termino_n3 + termino_n4

                termino_d = 1/6*(ay*self.y**3+by*(self.y-self.l1)**3+cy*(self.y-self.l2-self.l1)**3 - self.pu*(self.y-self.x)**3)
                deformacion = (1/(self.e*self.ine))*(termino_d + termino_z*self.y + termino_n)


        elif self.procedimiento == 2:
            if(self.y<self.l1):
                deformacion = (1/(self.e*self.ine))*(ay/6*(self.y**3 - self.y*(self.l1)**2))
            elif((self.y > self.l1) and (self.y < (self.l1+self.l2))):
                termino_z1 = -ay*(self.l1+self.l2)**3
                termino_z2 = -by*self.l2**3
                termino_z3 = self.pu*(self.l1+self.l2-self.x)**3
                termino_z4 = ay*self.l1**3
                termino_z = (1/(6*self.l2))*(termino_z1 + termino_z2 + termino_z3 + termino_z4)

                termino_n = (1/6)*(-ay*self.l1**3)-termino_z*self.l1

                deformacion = (1/(self.e*self.ine))*((1/6)*(ay*self.y**3+by*(self.y-self.l1)**3-self.pu*(self.y-self.x)**3) + termino_z*self.y + termino_n)
            elif((self.y>(self.l1+self.l2)) and (self.y<(self.l1+self.l2+self.l3))):
                lt = self.suma_longitudes(self.l1,self.l2,self.l3)
                termino_z1 = -ay*lt**3 - by*lt**3 - cy*lt**3 + self.pu*(self.l1+self.l2-self.x)**3
                termino_z2 = -self.pu*(self.l1+self.l2-self.x)**3+cy*self.l1**3+by*self.l2**3+ay*(self.l1+self.l2)**3
                termino_z = (1/(6*self.l3))*(termino_z1 + termino_z2)

                termino_n1 = -ay*(self.l1+self.l2)**3 - by*self.l2**3 - cy*self.l1**3 + self.pu*(self.l1+self.l2-self.x)**3
                termino_n = (1/6)*(termino_n1) - termino_z * (self.l1 + self.l2)

                deformacion = (1/(self.e*self.ine))*(1/6*(ay*self.y**3+by*(self.y-self.l1)**3-self.pu*(self.y-self.x)**3)+termino_z*self.y+termino_n)

        elif self.procedimiento ==3:
            if(self.y<self.l1):
                deformacion = (1/(self.e*self.ine))*(ay/6*(self.y**3-self.l1**2*self.y))
            elif((self.y > self.l1) and (self.y < (self.l1+self.l2))):
                termino_z = (1/(6*self.l2))*(-ay*self.l1**3 + ay*(self.l1+self.l2)**3+by*self.l2**3)
                termino_n = -((ay*self.l1**3)/6 - termino_z*self.l1)
                deformacion = (1/(self.e*self.ine))*((ay*self.y**3)/6+by*(self.y-self.l1)**3/6 + termino_z * self.y + termino_n)
            elif((self.y>(self.l1+self.l2)) and (self.y<(self.l1+self.l2+self.l3))):
                lt = self.suma_longitudes(self.l1,self.l2,self.l3)
                termino_z1 = -ay*(self.l1+self.l2)**3 + ay*lt**3 - by*self.l2**3 + by*(lt-self.l1)**3
                termino_z2 = cy*self.l3**3 - (self.pu*(lt-self.x)**3)/6
                termino_z = (1/(6*self.l3))*(termino_z1 + termino_z2)

                termino_n = -(ay*(self.l1+self.l2)**3)/6 - (by*(self.l2)**3)/6 - termino_z *(self.l1+self.l2)

                deformacion = (1/(self.e*self.ine)) * (1/6*(ay*self.y**3 + by*(self.y-self.l1)**3 + cy*(self.y-self.l2-self.l1)**3 - self.pu*(self.y-self.x)**3) + termino_z*self.y + termino_n)


            

       
        return deformacion

        

    

    def calcular(self):
        #Datos de Entrada del problema
        l1 = self.l1
        l2 = self.l2
        l3 = self.l3
        pu = self.pu
        x = self.x
        elas = self.e
        ine = self.ine
        y = self.y

        lt = self.suma_longitudes(l1,l2,l3)

        valores_matricesSDFG = self.procedimiento_principal(l1,l2,l3, x, elas, ine,pu, lt) # Devuelve lista con S,D,F,G

    
        if ((x>0) and (x<l1)):
            valores_matricesHJ = self.procedimiento1(l1,l2,l3, x, elas, ine,pu, lt)
            self.procedimiento =1
        elif ((x>=l1) and (x<(l1 + l2))):
            valores_matricesHJ = self.procedimiento2(l1, l2,l3, x, elas, ine, pu, lt)
            self.procedimiento =2
        elif ((x>=(l1 + l2)) and (x<(l1 + l2 + l3)) ):
            valores_matricesHJ = self.procedimiento3(l1, l2, l3, x, elas, ine, pu, lt)
            self.procedimiento =  3

        valor_s = valores_matricesSDFG[0]
        valor_d = valores_matricesSDFG[1]
        valor_f = valores_matricesSDFG[2] 
        valor_g = valores_matricesSDFG[3]

        # Armar matrices
        matriz_a = self.armar_matriz(valor_s, valor_d, valor_f, valor_g) # Retorna arreglo numpy
        #print(valor_s)
        #print(valor_f)
        #print(valor_d)
        #print(valor_g)
        print(matriz_a)

        valor_h = valores_matricesHJ[0]
        valor_j = valores_matricesHJ[1]


        # Armar vector c
        vector_c = self.armar_vector(valor_h, valor_j)
        #print(valor_h)
        #print(valor_j)
        print(vector_c)

        # Inversa de matiz_a
        inversa_matriz_a = np.linalg.inv(matriz_a)
        #print(inversa_matriz_a)

        # Calcular valores incognitas
        vector_resultado = np.dot(inversa_matriz_a,vector_c)
        print(vector_resultado)
        

        # Calcular Ay y DY
        valor_ay = pu*(1-x/lt)
        valor_by = vector_resultado[0][0]
        valor_cy = vector_resultado[1][0]
        valor_dy = pu*x/lt
        print(f'AY = {valor_ay}')
        print(f'BY = {valor_by}')
        print(f'CY = {valor_cy}')
        print(f'DY = {valor_dy}')

        momento = self.calcular_momento(valor_ay,valor_by,valor_cy)
        cortante = self.calcular_cortante(valor_ay,valor_by,valor_cy)
        deformacion = self.calcular_deformacion(valor_ay,valor_by,valor_cy)

        # Devolver resultados
        resultados = {'ay': valor_ay,
                      'by': valor_by,
                       'cy': valor_cy,
                       'dy': valor_dy,
                       'M': momento,
                       'V':cortante,
                       'Def': deformacion}

        return resultados





