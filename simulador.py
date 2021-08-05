class Simulador:
    def __init__(self):
        self._estados = list()
        self._estadoInicial = ''
        self._estadosFinais = list()
        self._delta = dict()
        self._resultados = list()

    def generateFromInput(self, estados, estadoInicial, estadosFinais, delta):
        self._estadoInicial = estadoInicial
        self._estados = estados.split(', ')
        self._estadosFinais = estadosFinais.split(', ')
        for state in self._estados:
            self._delta[str(state)] = dict()
        for transition in delta.split(', '):
            t = transition.split('|')
            try:
                self._delta[t[0]][t[1]].append(t[2])
            except Exception as e:
                self._delta[t[0]][t[1]] = list()
                self._delta[t[0]][t[1]].append(t[2])


    def delta(self, q, s, w):
        try:
            for state in self._delta[q][s]:
                self.readTape(w, state)
        except Exception as e:
            return -1

    def program(self, q, w):
        if(q == -1 or len(w) == 0):
            return q

        return self.program(self.delta(q, w[0], w[1::]), w[1::])

    def readTape(self, t, s_inicial=0):
        if (s_inicial == 0):
            s_inicial = self._estadoInicial

        if(self.program(s_inicial, t) in self._estadosFinais):
            self._resultados.append('A')
        else:
            self._resultados.append('R')

    def handler(self, string):
        self.readTape(string)
        if('A' in self._resultados):
            self._resultados = list()
            return '1'
        else:
            return '0'
            self._resultados = list()

file_A = open('automatum.txt', 'r')
automatum = file_A.read()[:-1:].split('\n')

file_I = open('input.txt', 'r')
input = file_I.read()[:-1:].split('\n')

file_R = open('resultados.txt', 'w+')



a = Simulador()
a.generateFromInput(*automatum)

for i in input:
    file_R.write(a.handler(i) + '\n')

file_A.close()
file_I.close()
file_R.close()
