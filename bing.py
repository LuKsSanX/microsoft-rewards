class Bing:
    def __init__(self) -> None:
        self.pc_pesquisa_diaria = 90
        self.celular_pesquisa_diaria = 60
        self.celular_noticias_diarias = 30
        self.conjunto_diario = 30
        self.mais_atividades_diarias = 40

        self.quebra_cabeca_pecas = 0

        self.total = 0

    def checkin(self, dia: int = 1) -> int:
        if 1 > dia > 7:
            raise Exception("Dia de checkin deve estar entre 1 e 7")

        dias = {1: 5, 2: 5, 3: 10, 4: 10, 5: 15, 6: 15, 7: 50}

        if dia == 7:
            self.add_quebra_cabeca_peca()

        return dias[dia]

    def tripla_pesquisa_diaria(self, dia: int = 1):
        if dia == 7:
            self.add_quebra_cabeca_peca()
            pontos = 100
        elif 0 < dia < 7:
            pontos = 9
        else:
            raise Exception("Dia de tripla_pesquisa_diaria deve estar entre 1 e 7")

        return pontos

    def add_quebra_cabeca_peca(self):
        self.quebra_cabeca_pecas += 1

        if self.quebra_cabeca_pecas == 12:
            self.total += 1_000
        elif self.quebra_cabeca_pecas == 13:
            self.quebra_cabeca_pecas = 1

    def dia(self, dia: int = 1):
        checkin = self.checkin(dia)
        self.total += checkin
        tripla_pesquisa_diaria = self.tripla_pesquisa_diaria(dia)
        self.total += tripla_pesquisa_diaria

        self.total += self.pc_pesquisa_diaria
        self.total += self.celular_pesquisa_diaria
        self.total += self.celular_noticias_diarias
        self.total += self.conjunto_diario
        self.total += self.mais_atividades_diarias

    def semana(self):
        for d in range(1, 8):
            self.dia(d)

    def mes(self):
        for _ in range(1, 5):
            self.semana()
