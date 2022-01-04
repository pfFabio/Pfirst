from udemy.banco.utils.helper import formata_float_str_moeda
from udemy.banco.models.cliente import Cliente

class Conta:
    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.00
        self.__limite: float = 100.00
        self.__saldo_total: float = self.calcula_saldo_total
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero}\nCliente: {self.cliente.nome}\n' \
               f'Saldo Total {formata_float_str_moeda(self.saldo_total)}'

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def calcula_saldo_total(self: object) -> float:
        return self.__saldo + self.__limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self.calcula_saldo_total
            print('o depósito foi efetuado com sucesso')
        else:
            print('erro ao efetuar depósito')

    def sacar(self: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                valor -= self.saldo
                self.saldo = 0
                self.limite -= valor
            self.saldo_total = self.calcula_saldo_total
            print('o saque foi efetuado com sucesso')
        else:
            print('erro ao efetuar saquer')

    def transferir(self: object, destino: object, valor:float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                valor -= self.saldo
                self.saldo = 0
                self.limite -= valor
            self.saldo_total = self.calcula_saldo_total

            destino.saldo += valor
            destino.saldo_total = destino.calcula_saldo_total
            print('o depósito foi efetuado com sucesso')
        else:
            print('erro ao efetuar transferencia')






