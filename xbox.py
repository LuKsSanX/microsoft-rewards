class Xbox:
    def __init__(self) -> None:
        self.console_diario = 20
        self.jewel_diario = 10
        self.pc_diario = 20
        self.app_diario = 32
        self.game_pass_diario = 20

        self.console_bonus_semanal = 175
        self.pc_bonus_semanal = 150
        self.game_pass_sequencia_semanal = 100

        self.game_pass_pacote_mensal_4_jogos = 80
        self.game_pass_pacote_mensal_8_jogos = 560

    def dia(self) -> list:
        return [
            self.console_diario,
            self.jewel_diario,
            self.pc_diario,
            self.app_diario,
            self.game_pass_diario,
        ]

    def semana(self, game_pass_multiplicador_sequencia: int = 1) -> list:
        if 1 > game_pass_multiplicador_sequencia > 4:
            raise Exception(
                "game_pass_multiplicador_sequencia precisa estar entre 1 e 4"
            )

        game_pass_sequencia_semanal = (
            self.game_pass_sequencia_semanal * game_pass_multiplicador_sequencia
        )

        return [
            *7 * self.dia(),
            self.console_bonus_semanal,
            self.pc_bonus_semanal,
            game_pass_sequencia_semanal,
        ]

    def mes(self, primeiro_mes=True) -> list:
        total = [
            self.game_pass_pacote_mensal_4_jogos,
            self.game_pass_pacote_mensal_8_jogos,
        ]

        for s in range(1, 5):
            total = [*total, *self.semana(s if primeiro_mes else 4)]

        return total

    def ano(self, incluir_primeiro_mes: bool = True) -> list:
        total = []

        for m in range(1, 13):
            primeiro_mes = m == 1 and incluir_primeiro_mes

            total = [*total, *self.mes(primeiro_mes)]

        return total
