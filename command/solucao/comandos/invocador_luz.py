from datetime import datetime


class Switch(object):
    def __init__(self):
        self._comandos = {}
        self._historico = []

    @property
    def historico(self):
        return self._historico

    def registrar(self, comandoNome, comando):
        self._comandos[comandoNome] = comando

    def execute(self, comandoNome):
        if(comandoNome in self._comandos):
            self._comandos[comandoNome].execute()
            self._historico.append(
                (datetime.now().strftime('%d/%m/%Y %H:%M'), comandoNome))
        else:
            print("Comando não encontrado")
