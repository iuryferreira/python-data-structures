class Fila:

    def __init__(self, tamanho):

        self.fila = [None] * tamanho
        self.tamanho = tamanho
        self.inicio = 0
        self.fim = 0

    def __repr__(self):

        queue = ""
        def get_formated_queue(queue):
            for i in range(self.tamanho):
                if i != self.inicio:
                    queue += " [  %s  ] " % self.fila[i]
                else:
                    queue +=" [→ %s ←] " % self.fila[i]

            return queue
        
        queue = get_formated_queue(queue)

        return "Queue: {0}".format(queue)

    def indice_seguinte(self, ponteiro):

        if ponteiro == "Inicio":
            if self.inicio == self.tamanho:
                return 0
            else:
                return self.inicio
        elif ponteiro == "Fim":
            if self.fim == self.tamanho:
                return 0
            else:
                return self.fim
        else:
            print("Ponteiro escrito errado.")

    def fila_cheia(self):

        if (self.fim == self.tamanho and self.inicio == 0) or self.fila[self.indice_seguinte("Fim")] is not None:
            return True
        else:
            return False

    def fila_vazia(self):

        return True if self.fila[self.indice_seguinte("Inicio")] is None else False

    def enfileirar(self, valor):

        if self.fila_cheia():
            return "Fila Cheia"
        else:
            if self.fim == self.tamanho:
                self.fim = 0
            self.fila[self.fim] = valor
            self.fim = self.fim + 1

    def desenfileirar(self):

        if self.fila_vazia():
            return "Fila Vazia"
        else:
            if self.inicio == self.tamanho:
                self.inicio = 0
            valor = self.fila[self.inicio]
            self.fila[self.inicio] = None
            self.inicio = self.inicio + 1
            return valor

if __name__ == "__main__":
    
    f = Fila(3)
    f.enfileirar(4)
    print(f)

