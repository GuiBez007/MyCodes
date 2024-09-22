from os import system

class Matriz:
    count = 0

    def __init__(self):
        try:
            Matriz.count += 1
            self.count = Matriz.count
            self.x = int(input('\033[33mLINHAS> \033[m'))
            self.y = int(input('\033[33mCOLUNAS> \033[m'))
            self.values = self.matrizInicialization()
            self.addValues()
        except:
            print('\033[31mEssa matriz não pode ser criada! \033[m') ### tenho que ver dps


    def matrizInicialization(self):
        x_list = []
        y_list = []
        for i in range(self.x):
            for j in range(self.y):
                y_list.append(' ')
            x_list.append(y_list[:])
            y_list.clear()
        return x_list[:]


    def addValues(self):
        for i in range(self.x):
            for j in range(self.y):
                system('cls')
                self.showMatriz()
                self.values[i][j] = int(input('> '))
        system('cls')
        self.showMatriz()
        system('cls')


    def showMatriz(self):
        print('='*(self.y) + f' Matriz {self.count} ' + '='*(self.y))
        for i in range(self.x):
            print(' [', end='')
            for j in range(self.y):
                if j == self.y-1:
                    break
                print(f'{self.values[i][j]:3}', end=',')
            print(f'{self.values[i][j]:3}', end=']\n')


    @classmethod
    def showAll(cls, m_1, m_2, m_3, sign):
        _max = max(m_1.x, m_2.x, m_3.x)
        aux = len(str(m_1.values[0]))
        print(f'{'=== Matriz 1 ===':^{aux}}    {sign}    {'=== Matriz 2 ===':^{aux}}    =    {'=== Matriz 3 ===':^{aux}}')

        for i in range(_max):
            print(f'{str(m_1.values[i]):^16}         {str(m_2.values[i]):^16}         {str(m_3.values[i]):^16}')



    @classmethod
    def sumOrSubtract(cls, operation, m_1, m_2):
        m_3 = []
        aux = []
        for i in range(m_1.x):
            for j in range(m_1.y):
                if operation == '+':
                    aux.append(m_1.values[i][j] + m_2.values[i][j])
                elif operation == '-':
                    aux.append(m_1.values[i][j] - m_2.values[i][j])
            m_3.append(aux[:])
            aux.clear()
        return m_3


    @classmethod
    def multiplyMatrix(cls, m_1, m_2):
        if m_1.y != m_2.x:
            print('Não dá pra multiplicar, inseto!!')
            return

        m_3 = []
        aux = []
        for line_m1 in range(m_1.x):
            for column_m2 in range(m_2.y):
                _sum = 0
                for key in range(m_2.x):
                    _sum += m_1.values[line_m1][key] * m_2.values[key][column_m2]
                aux.append(_sum)
            m_3.append(aux[:])
            aux.clear()
        return m_3


    @classmethod
    def calculateDeterminant(cls, m):
        m = m.values
        if len(m) == 1 and len(m[0]) == 1:
            return m[0][0]
        elif len(m) == 2 and len(m[0]) == 2:
            multiply_1 = m[0][0] * m[1][1]
            multiply_2 = m[0][-1] * m[1][-2] * -1
            return multiply_1 + multiply_2
        elif len(m) == 3 and len(m[0]) == 3:
            # transform the 3x3 matriz in 3x5
            for i in range(3):
                for j in range(2):
                    m[i].append(m[i][j])

            multiply_1 = (m[0][0] * m[1][1] * m[2][2]) + (m[0][1] * m[1][2] * m[2][3]) + (m[0][2] * m[1][3] * m[2][4])
            multiply_2 = (m[0][-1] * m[1][-2] * m[2][-3] * -1) + (m[0][-2] * m[1][-3] * m[2][-4] * -1) + (m[0][-3] * m[1][-4] * m[2][-5] * -1)
            return multiply_1 + multiply_2
        else:
            print('\033[31mNão pode ser calculado no momento! \033[m')
            return


    @classmethod
    def resultOfOperation(cls, m_3, matrices):
        system('cls')
        print('RESULTADO')
        matrices.append(Matriz.__new__(Matriz))
        matrices[-1].values = m_3[:]
        matrices[-1].y = len(matrices[-1].values[0])
        matrices[-1].x = len(matrices[-1].values)
        if Matriz.count != 3:
            Matriz.count += 1
        matrices[-1].count = Matriz.count


    @classmethod
    def createMatrix(cls, matrices):
        matrices.append(Matriz())
        if matrices[-1].x < 1 or matrices[-1].y < 1:
            print('\033[31mEssa matriz não pode ser criada! \033[m') ###
            Matriz.count -= 1
            del matrices[-1]


# main()
def main():
    matrices = []

    while True:
        print('\n\033[7m=== CÁLCULO DE MATRIZES ===  \033[m   \n'
              '[00] - criar matriz;                           \n'
              '[01] - somar;                                  \n'
              '[02] - subtrair;                               \n'
              '[03] - multiplicar;                            \n'
              '[04] - dividir [AINDA NÃO];                    \n'
              '[05] - determinante;                           \n'
              '[06] - SAIR.                                    ')
        option = int(input('\033[32mopção> \033[m'))
        print()

        if option == 0:
            Matriz.createMatrix(matrices)
        elif option == 1:
            if len(matrices) < 2:
                system('cls')
                print('\033[33mPrimeiro crie duas matrizes! \033[m')
            else:
                matriz_3 = Matriz.sumOrSubtract('+', matrices[0], matrices[1]) #mudar matrizes para var (tipo matriz A/B...)
                Matriz.resultOfOperation(matriz_3, matrices)
                Matriz.showAll(matrices[0], matrices[1], matrices[-1], '+')
        elif option == 2:
            if len(matrices) < 2:
                system('cls')
                print('\033[33mPrimeiro crie duas matrizes! \033[m')
            else:
                matriz_3 = Matriz.sumOrSubtract('-', matrices[0], matrices[1]) #
                Matriz.resultOfOperation(matriz_3, matrices)
                Matriz.showAll(matrices[0], matrices[1], matrices[-1], '-')
        elif option == 3:
            if len(matrices) < 2:
                system('cls')
                print('\033[33mPrimeiro crie duas matrizes! \033[m')
            else:
                matriz_3 = Matriz.multiplyMatrix(matrices[0], matrices[1]) #
                Matriz.resultOfOperation(matriz_3, matrices)
                matrices[-1].showMatriz() # tenho que arrumar para mostrar tudo
        elif option == 4:
            print(matrices[0].showMatriz()) #teste
            #                                sem sentido
        elif option == 5:
            if len(matrices) < 1:
                system('cls')
                print('\033[33mPrimeiro crie uma matriz! \033[m')
            else:
                print(f'Determinante da matriz> {Matriz.calculateDeterminant(matrices[0])}')
        elif option == 6:
            break


if __name__ == '__main__':
    main()