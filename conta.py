

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}.".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def transferencia(self, valor, destinatario):
        self.saque(valor)
        destinatario.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite