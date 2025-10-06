from datetime import date
from typing import List, Optional

# Objetos de valor e entidades básicas
class Endereco:
    def __init__(self, id: int, rua: str, cidade: str, estado: str, cep: str):
        self.id = id
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

class Produto:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

class Terminal:
    def __init__(self, id: int, nome: str, endereco: Endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

class Programador:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

class Duto:
    def __init__(self, id: int, nome: str, capacidade: float, endereco_inicio: Endereco, endereco_fim: Endereco):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade
        self.endereco_inicio = endereco_inicio
        self.endereco_fim = endereco_fim

class Operador:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

class AnalistaFaturamento:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

### contexto Solicitacao de Transporte
class Cliente:
    def __init__(self, id: int, razao_social: str, cnpj: str, endereco: Endereco):
        self.id = id
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.endereco = endereco

class SolicitacaoTransporte:
    def __init__(self, id: int, cliente: Cliente, produto: Produto, quantidade: float, terminal_origem: Terminal, terminal_destino: Terminal, data_produto_disponivel: date, data_esperada_entrega: date):
        self.id = id
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.terminal_origem = terminal_origem
        self.terminal_destino = terminal_destino
        self.data_produto_disponivel = data_produto_disponivel
        self.data_esperada_entrega = data_esperada_entrega

class SolicitacaoTransporteService:
    @staticmethod
    def criar_solicitacao(id: int, cliente: Cliente, produto: Produto, quantidade: float, terminal_origem: Terminal, terminal_destino: Terminal, data_produto_disponivel: date, data_esperada_entrega: date) -> 'SolicitacaoTransporte':
        # Aqui pode incluir validações e regras de negócio
        return SolicitacaoTransporte(
            id=id,
            cliente=cliente,
            produto=produto,
            quantidade=quantidade,
            terminal_origem=terminal_origem,
            terminal_destino=terminal_destino,
            data_produto_disponivel=data_produto_disponivel,
            data_esperada_entrega=data_esperada_entrega
        )

### contexto Rota
class Rota:
    def __init__(self, id: int, solicitacao: SolicitacaoTransporte, terminais_intermediarios: Optional[List[Terminal]], dutos_intermediarios: Optional[List[str]], programador: Programador):
        self.id = id
        self.solicitacao = solicitacao
        self.terminais_intermediarios = terminais_intermediarios or []
        self.dutos_intermediarios = dutos_intermediarios or []
        self.programador = programador

class RotaService:
    @staticmethod
    def calcular_rota(id: int, solicitacao: SolicitacaoTransporte, terminais_intermediarios: Optional[List[Terminal]], dutos_intermediarios: Optional[List[Duto]], programador: Programador) -> 'Rota':
        # Lógica de cálculo de rota baseada nos terminais e dutos
        # Aqui pode incluir algoritmos de otimização, regras de negócio, etc.
        return Rota(
            id=id,
            solicitacao=solicitacao,
            terminais_intermediarios=terminais_intermediarios,
            dutos_intermediarios=[duto.nome for duto in (dutos_intermediarios or [])],
            programador=programador
        )

### contexto Transporte
class Transporte:
    def __init__(self, id: int, rota: Rota, etapa: str, operador: Operador):
        self.id = id
        self.rota = rota
        self.etapa = etapa
        self.operador = operador

class TransporteService:
    @staticmethod
    def iniciar_transporte(id: int, rota: Rota, operador: Operador) -> 'Transporte':
        # Lógica para iniciar o transporte
        return Transporte(
            id=id,
            rota=rota,
            etapa="Iniciado",
            operador=operador
        )

### contexto Fatura
class Fatura:
    def __init__(self, id: int, transporte: Transporte, valor: float, data_emissao: date, analista: AnalistaFaturamento):
        self.id = id
        self.transporte = transporte
        self.valor = valor
        self.data_emissao = data_emissao
        self.analista = analista

class FaturaService:
    @staticmethod
    def calcular_fatura(id: int, transporte: Transporte, analista: AnalistaFaturamento) -> 'Fatura':
        # Lógica de cálculo do valor da fatura baseada no transporte
        # Exemplo simples: valor proporcional à quantidade transportada
        valor = transporte.rota.solicitacao.quantidade * 100  # Exemplo de regra
        data_emissao = date.today()
        return Fatura(
            id=id,
            transporte=transporte,
            valor=valor,
            data_emissao=data_emissao,
            analista=analista
        )

