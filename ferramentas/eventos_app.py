"""Conteúdo dos slides de eventos (Rotinas de Manejo Salvas) e das telas do App MB Curral.
Transcrito dos slides 103–118 do deck de Reprodução e Cria. Usado por aplica_eventos.py."""
from tablet import campo, seg, radios, variante, passos, area, lista, linha, lado, tit, obs, avancar, app, ICO

PESO_438 = '23/07/2019 (3a7m)<br>438.00 kg<br>GMD: 0.01'

# animais fictícios do fluxo de Desmame (PRÓXIMO ANIMAL passa para o seguinte)
ANIMAIS_DESMAME = [
 {
  "id": "100732/26",
  "sexo": "Macho / Reprodutor",
  "raca": "NELORE / 1/2",
  "nasc": "29/05/2026 (4m)",
  "pasto": "maria teste",
  "pesokg": "215"
 },
 {
  "id": "100741/26",
  "sexo": "Fêmea / Reprodução",
  "raca": "NELORE / PO",
  "nasc": "14/06/2026 (4m)",
  "pasto": "Pasto 02",
  "pesokg": "198"
 },
 {
  "id": "100758/26",
  "sexo": "Macho / Reprodutor",
  "raca": "ANGUS / 3/4",
  "nasc": "02/07/2026 (3m)",
  "pasto": "Pasto 02",
  "pesokg": "232"
 },
 {
  "id": "100763/26",
  "sexo": "Fêmea / Reprodução",
  "raca": "NELORE / 1/2",
  "nasc": "21/07/2026 (3m)",
  "pasto": "maria teste",
  "pesokg": "205"
 }
]
ANIMAIS_JSON = __import__('json').dumps(ANIMAIS_DESMAME, ensure_ascii=False)

def lado_rec(p, variante):
    base = [('ID Secundário', 'REC_T06'), ('Sexo / Tipo', 'Fêmea / Receptora'), ('Raça / G. Sangue', 'NELORE'),
            ('Data de Nascimento (idade)', '23/07/2021 (2a3m)')]
    if variante == 'movimentacao':
        return lado(p, 'REC_T06', base + [('Ordem', 'Primípara'), ('Situação / Estado', 'Vazia / Parida'), ('Pasto', '36 B')],
                    [('Último Parto', 'Normal - 15/08/2022', 'verde'), ('Último Peso', PESO_438, 'amarela')], lapis=False)
    comum = base + [('Ordem', 'Novilha'), ('Situação / Estado', 'Vazia / Solteira'), ('Pasto', '36 B')]
    if variante == 'morte':
        return lado(p, 'REC_T06', comum, [('Último Peso', PESO_438, 'amarela')], lapis=False)
    if variante == 'vacinacao':
        return lado(p, 'REC_T06', comum, [('Situação da Mãe', 'Vazia', 'verde'), ('Último Peso', PESO_438, 'amarela')], lapis=False)
    if variante == 'pesagem':
        return lado(p, 'REC_T06', comum, [('Última Cobertura', 'TE - 29/06/2022 (259 dias)<br>0002 - NE<br>Prev. Parto: 20/04/2023', 'verde'),
                                          ('Último Peso', '23/07/2019 (3a7m)<br>180.00 kg<br>GMD: não identificado', 'amarela')])
    if variante == 'protocolo':
        return lado(p, 'REC_T06', comum[1:], [('Situação da Mãe', 'Vazia', 'verde', True),
                                              ('Último Peso', '23/07/2023 (3a7m)<br>180.00 kg<br>GMD: não identificado', 'amarela')])
    if variante == 'perda':
        return lado(p, 'REC_T06', [('Sexo / Tipo', 'Fêmea / Reprodução'), ('Raça / G. Sangue', 'NELORE'), ('Data de Nascimento (idade)', '01/05/2019 (4a8m)'),
                                   ('Ordem', 'Primípara'), ('Situação / Estado', 'Vazia / Parida'), ('Pasto', '36 B')],
                    [('Nome do Implante', 'SINCROGEST (D9) em 11/01', 'amarela'), ('Retirando em', 'D7', 'amarela'),
                     ('Observação', 'Retirada - 45 horas', 'verde'), ('Último Parto', 'Normal - 15/08/2022', 'verde'),
                     ('Último Peso', '21/07/2022 (1a5m)<br>412.00 kg<br>GMD: 0.34', 'amarela')])
    raise ValueError(variante)

def lado_mb001(p, raca, caixas):
    return lado(p, 'MB001', [('Sexo / Tipo', 'Fêmea / Reprodução'), ('Raça / G. Sangue', raca), ('Data de Nascimento (idade)', '10/09/2022 (1a4m)'),
                             ('Ordem', 'Novilha'), ('Situação / Estado', 'Vazia / Solteira'), ('Pasto', 'Não informado')], caixas)

def lado_dgs10(p):
    return lado(p, 'DGS10', [('ID Secundário', 'DGS10'), ('Sexo / Tipo', 'Fêmea / Reprodução'), ('Raça / G. Sangue', 'ABERDEEN / PO'),
                             ('Data nascimento (Idade)', '01/01/2016 (7a9m)'), ('Ordem', 'Novilha'), ('Situação / Estado', 'Gestante / Solteira'), ('Pasto', 'Não Informado')],
                [('Última cobertura', 'IA - 27/01/2023 (257 Dias)<br>ROTAM - NE<br>Data (DG): 02/03/2023<br>Prev. Parto: 04/11/2023', 'verde'),
                 ('Último Peso', '01/01/2020 (3a9m)<br>485.00 Kg<br>GMD: Não Identificado', 'amarela')])

def lado_part01(p):
    return lado(p, 'PART01', [('ID Secundário', 'PART01'), ('Sexo / Tipo', 'Fêmea / Reprodução'), ('Raça / G. Sangue', 'NELORE / PO'),
                              ('Data nascimento (Idade)', '01/01/2021 (3a0m)'), ('Ordem', 'Novilha'), ('Situação / Estado', 'Vazia / Solteira'), ('Pasto', 'PASTO 01')],
                [('Nome do implante', 'FERTILCARE IMPLANTES DT (D8) em 04/01', 'verde'), ('Observação', 'Retirada: Sim. 07:00 Hs', 'verde'),
                 ('Observação', 'Intervalo IA e Retirada Implante: 33 hs', 'amarela'), ('Peso', 'Não Identificado', 'amarela')])

# ---------------------------------------------------------------- telas
def tela_entrada(p, sexo='f'):
    f = (f'<div class="{p}-var {p}-var--f">'
         + linha(p, campo(p, 'Tipo', 'Reprodução', True, True), campo(p, 'Ordem', 'Novilha', False, True))
         + linha(p, campo(p, 'Idade (Meses)', '16', False, True, bt=None), campo(p, 'Estado Inicial', 'Solteira', False))
         + linha(p, campo(p, 'Raça', 'ABERDEEN', False, bt=None), campo(p, 'Grau de Sangue', 'PURO SANGUE'))
         + linha(p, campo(p, 'Rebanho', 'COML'), campo(p, 'Pelagem', 'PRETA'))
         + campo(p, 'Produtor', 'MULTBOVINOS', False, True) + '</div>')
    m = (f'<div class="{p}-var {p}-var--m">'
         + linha(p, campo(p, 'Tipo', 'Reprodução', True, True), campo(p, 'Idade (Meses)', '16', False, True, bt=None))
         + linha(p, campo(p, 'Raça', 'ABERDEEN', False, bt=None), campo(p, 'Grau de Sangue', 'PURO SANGUE'))
         + linha(p, campo(p, 'Rebanho', 'COML'), campo(p, 'Pelagem', 'PRETA'))
         + campo(p, 'Produtor', 'MULTBOVINOS', False, True) + '</div>')
    corpo = tit(p, 'Entrada do Animal') + obs(p) + seg(p, 'Sexo', ['Fêmea', 'Macho'], 0 if sexo == 'f' else 1, True, sexo=True) + f + m + avancar(p)
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/07/2023'), corpo, attrs=f' data-sexo="{sexo}"')

def tela_movimentacao(p):
    corpo = (tit(p, 'Movimentação Entre Propriedades', info=False) + obs(p)
             + campo(p, 'Tipo', 'Saída', False, True) + campo(p, 'Documento', '090120241027', False, True)
             + campo(p, 'Propriedade de Destino', 'Fazenda MULTSOFT', True, True)
             + campo(p, 'Localidade de Destino', 'Selecione', True, True, bt='lupa', ph=True)
             + campo(p, 'Produtor Origem', 'Diogo Lopes', False, True)
             + campo(p, 'Produtor de Destino', 'Selecione', True, True, bt='lupa', ph=True) + avancar(p))
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/10/2023'), corpo, lado_rec(p, 'movimentacao'))

def tela_morte(p):
    corpo = (tit(p, 'Morte', info=False) + obs(p)
             + campo(p, 'Data', 'Selecione', True, True, ph=True) + campo(p, 'Causa', 'Selecione', True, bt='lupa', ph=True)
             + campo(p, 'Responsável', 'Diogo Lopes', False) + avancar(p))
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/10/2023'), corpo, lado_rec(p, 'morte'))

def tela_vacinacao(p):
    corpo = (tit(p, 'Vacinação') + obs(p) + campo(p, 'Vacina', 'FEBRE AFTOSA', True, True)
             + linha(p, campo(p, 'Dose', '1', False, True), campo(p, 'Unidade de Uso', 'DOSE', False, True))
             + linha(p, campo(p, 'Data Validade', '09/01/24', False), campo(p, 'Fabricante', 'MSD'))
             + campo(p, 'Responsável', 'Igor Avelar') + avancar(p))
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/10/2023'), corpo, lado_rec(p, 'vacinacao'))

def tela_pesagem(p):
    corpo = (tit(p, 'Pesagem') + obs(p)
             + f'<div class="{p}-campo"><div class="{p}-input"><span>438,00</span><button class="{p}-bt" type="button" aria-label="Limpar">{ICO["lixo"]}</button></div></div>'
             + f'<p class="{p}-nota">Balança conectada!<br><u>Clique AQUI para atualizar peso.</u></p>' + avancar(p))
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/10/2023'), corpo, lado_rec(p, 'pesagem'))

def tela_conferencia(p):
    def lote(nome, total, comp, incl, falt, transf, entrev):
        z = ICO['zoom']
        inc = f'<small>(Inclusos: <b>+{incl}</b>)</small>' if incl else ''
        return (f'<div class="{p}-lote"><div class="{p}-lote-cab">{ICO["seta-baixo"]}<b>Lote:</b> {nome}<span><b>Total do Lote:</b> {total} {ICO["info"]}</span></div>'
                f'<div class="{p}-lote-tab"><div><span>Compareceram</span><span>Faltantes</span><span>Transferidos</span><span>Entreveros</span></div>'
                f'<div><span>{comp} {z}{inc}</span><span class="{p}-vermelho">{falt} {z}</span><span>{transf}{" " + z if transf else ""}</span><span class="{p}-vermelho">{entrev} {z}</span></div></div></div>')
    corpo = (f'<div class="{p}-conf-cab"><b>Resumo do dia:</b><i>Dia 18/01/2023 desde 09:23.</i></div>'
             f'<div class="{p}-conf-resumo"><div><small>Compareceram<br>no Dia:</small><b>389</b></div><div><small>Animais<br>Entreveros:</small><b>14</b></div><div><small>Total de<br>Animais:</small><b>403</b></div></div>'
             + lote('Lote 01 Novilhas', 188, 182, 4, 6, 0, 5) + lote('Lote 02 Secundíparas', 215, 207, 0, 8, 4, 9)
             + f'<p class="{p}-conf-rodape">* Animais Entreveiros não contabilizam na soma total de animais inseminados.</p>')
    acoes = f'<span class="{p}-subacoes"><button type="button">{ICO["info"]} Ajuda</button></span>'
    return app(p, 'Fazenda Treinamento', ('titulo', 'Animais Faltantes', acoes), corpo)

def tela_perda(p):
    corpo = tit(p, 'Perda de Implante') + obs(p) + seg(p, 'Perdeu?', ['Não', 'Sim'], 1, True) + campo(p, 'Responsável', 'Diogo Lopes', False) + avancar(p)
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/10/2023'), corpo, lado_rec(p, 'perda'))

def tela_partos(p, estado=''):
    crias = [('Cria número 1 / Vivo / CRIA01', True), ('Cria número 2 / Vivo / CRIA02', True)] if estado == 'crias' else []
    corpo = (tit(p, 'Parto') + obs(p, 'Este evento é obrigatório')
             + campo(p, 'Data', '11/10/2023', True, True) + campo(p, 'Tipo de Parto', 'Normal', True, True) + campo(p, 'Responsável', 'PAULO SOARES', True, True)
             + lista(p, 'Crias', crias, True, mais='abrir-cria', vazio='Sem registros.', attr=' data-crias', escuro=True)
             + area(p, 'Observação') + avancar(p))
    painel = (f'<div class="{p}-modal{" is-aberto" if estado == "cria" else ""}"><div class="{p}-painel">'
              f'<div class="{p}-painel-topo"><button class="{p}-volta" type="button" data-acao="fechar-cria" aria-label="Fechar">{ICO["chevron"]}</button><span>Cria</span><em>{ICO["info"]} Ajuda</em></div>'
              f'<div class="{p}-painel-corpo"><h4>Dados da Mãe</h4><p>ID Usual: DGS10</p>'
              + seg(p, '', ['Fêmea', 'Macho'], 0)
              + campo(p, 'Situação da Cria', 'Vivo', True, True) + campo(p, 'ID Usual', 'CRIA TESTE', True, True, bt='link')
              + campo(p, 'ID Secundário', 'CRIA TESTE', True, bt=None) + campo(p, 'SISBOV', 'Digite', True, bt=None, ph=True)
              + campo(p, 'Nome', 'CRIA01', True, bt=None) + campo(p, 'Raça', 'ABERDEEN', True, True) + campo(p, 'Tipo', 'Reprodução')
              + campo(p, 'Pelagem', 'BRANCA') + campo(p, 'Grau de sangue', 'PURO DE ORIGEM')
              + f'<button class="{p}-avancar" type="button" data-acao="salvar-cria">SALVAR</button></div></div></div>')
    return app(p, 'PAULO FARM - 23', ('execucao', '11/10/2023'), corpo, lado_dgs10(p), modal=painel)

def tela_protocolo(p):
    corpo = (tit(p, 'Aplicação de Protocolo IATF') + obs(p) + campo(p, 'Protocolo', 'IATF 2024 - NOVILHAS', True, True)
             + lista(p, 'Eventos', [('D0 - SINCROGEST / 1 ML', False), ('D0 - FOLLIGON / 0.02 ML', True), ('D8 - NOVORMON / 2 ML', True), ('D9 - Retirada', True)])
             + campo(p, 'Responsável', 'Selecione', True, ph=True) + area(p, 'Observações', 'Escreva...') + avancar(p))
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/10/2023'), corpo, lado_rec(p, 'protocolo'))

def tela_inseminacao(p):
    corpo = (tit(p, 'Inseminação artificial') + obs(p, 'Este evento é obrigatório')
             + seg(p, 'Cio', ['Sim', 'Não'], 0) + campo(p, 'Macho', 'GOODZILA', True, True) + campo(p, 'Partida', '1234', True, bt='lupa')
             + campo(p, 'Dose', '1', False, True, bt=None) + seg(p, 'Tipo do sêmen', ['Congelado', 'Fresco'], 0)
             + seg(p, 'Sêmen sexado', ['Fêmea', 'Macho', 'Convencional'], 2) + campo(p, 'Proprietário do Sêmen', 'ALDO AUFIERO E OUTRA', False)
             + campo(p, 'Responsável / Inseminador', 'LUCAS SALES', True, True) + area(p, 'Observação') + avancar(p))
    return app(p, 'PAULO FARM - 23', ('execucao', '05/01/2024'), corpo, lado_part01(p))

def tela_trat_doencas(p):
    extra = f'<i class="{p}-mais" aria-hidden="true">{ICO["mais"]}</i><i class="{p}-relogio" aria-hidden="true">{ICO["relogio"]}</i>'
    corpo = (tit(p, 'Aplicação de Tratamento (Doenças)', info=False) + obs(p) + campo(p, 'Doença', 'VERMINOSE', True, True)
             + campo(p, 'Tratamentos', 'IVOMEC GOLD 1000ML / 2,5 ML', True, True, extra=extra) + campo(p, 'Responsável', 'Igor Avelar') + avancar(p))
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/10/2023'), corpo,
               lado_mb001(p, 'NELORE / Puro Sangue', [('Situação da Mãe', 'Vazia', 'verde'), ('Último Peso', PESO_438, 'amarela')]))

def tela_trat_iatf(p):
    corpo = (tit(p, 'Aplicação de Tratamento', info=False) + obs(p) + campo(p, 'Tratamento', 'BIOGESTROGEN', True, True)
             + passos(p, 'Quantidade / DS', '2') + campo(p, 'Responsável', 'DIOGO LOPES') + avancar(p))
    return app(p, 'Fazenda Boa Sorte', ('execucao', '13/10/2023'), corpo,
               lado_mb001(p, 'NELORE / PO', [('Protocolo', 'Não encontrado', 'verde'), ('Situação da Mãe', 'Vazia', 'verde'), ('Último Peso', PESO_438, 'amarela')]))

def tela_venda(p):
    chip = lambda r, v: f'<div class="{p}-chip"><small>{r}</small><b>{v}</b></div>'
    corpo = (f'<p class="{p}-rot-label">Título da Rotina</p><div class="{p}-rot-titulo">Venda de Animais</div>'
             f'<div class="{p}-rot-card"><div class="{p}-rot-alca">{ICO["alca"]}</div><div class="{p}-rot-conteudo">'
             f'<div class="{p}-rot-cab">1ª Venda de Animais{ICO["lixo"]}</div><div class="{p}-rot-grade">'
             + chip('Tipo Venda', 'NÃO IDENTIFI...') + chip('Data', '09/01/2024') + chip('Documento', '22092022')
             + chip('Produtor de Origem', 'DIOGO LOPES') + chip('Destino', 'FAZENDA MB') + chip('Embarque', 'EMB-010124') + chip('Sexo', 'AMBOS')
             + f'</div></div></div><div class="{p}-rot-botoes"><button type="button">{ICO["maisb"]} Evento</button><button type="button">{ICO["check"]} Salvar</button></div>')
    acoes = f'<span class="{p}-subacoes"><button type="button">{ICO["lixo"]} Excluir</button><button type="button" class="is-escuro">{ICO["bandeira"]} Iniciar</button></span>'
    return app(p, 'Fazenda Treinamento', ('titulo', 'Edição de Rotina', acoes), corpo)

def tela_desmame(p):
    """sequência: Desmame (com confirmação) -> Pesagem -> Resumo da rotina. Só SIM, o campo de peso,
    AVANÇAR e PRÓXIMO ANIMAL funcionam; PRÓXIMO ANIMAL volta ao início com outro animal fictício."""
    A = ANIMAIS_DESMAME[0]
    v = lambda k: f'<span data-animal="{k}">{A[k]}</span>'
    def lado_(caixas, lapis=True, situacao=True):
        pares = [('ID Secundário', v('id')), ('Sexo / Tipo', v('sexo')), ('Raça / G. Sangue', v('raca')),
                 ('Data nascimento (Idade)', v('nasc'))] + ([('Situação', 'Mamando')] if situacao else []) + [('Pasto', v('pasto'))]
        return lado(p, v('id'), pares, caixas, lapis=lapis, ficha=True)
    peso_box = ('Último Peso', '27/10/2026 (0m)<br><span data-peso-kg>215</span>.00 Kg<br>GMD: Não Identificado', 'amarela')      # resumo: peso digitado
    peso_anim = ('Último Peso', '27/10/2026 (0m)<br>' + v('pesokg') + '.00 Kg<br>GMD: Não Identificado', 'amarela')           # tela 1: último peso do animal
    bloqueia = lambda h: h.replace(f'<button class="{p}-volta" type="button"', f'<button class="{p}-volta" type="button" disabled')
    # 1) Desmame com o diálogo de confirmação aberto (só o SIM funciona)
    dialogo = (f'<div class="{p}-modal is-aberto" data-inicial><div class="{p}-dialogo"><h4>Confirmação</h4><p>Deseja desmamar o animal?</p>'
               f'<div><button type="button" data-acao="ir:2">SIM</button><button type="button" disabled>NÃO</button></div></div></div>')
    pag1 = app(p, 'ANITA RANCHO', ('execucao', '27/10/2026'), tit(p, 'Desmame', info=False) + obs(p, 'Este evento é obrigatório')
               + f'<button class="{p}-avancar" type="button" disabled>AVANÇAR</button>',
               lado_([('Situação da mãe', 'Vazia', 'verde'), peso_anim]), modal=dialogo)
    # 2) Pesagem: campo editável + AVANÇAR
    corpo2 = (tit(p, 'Pesagem', info=False) + obs(p, 'Este evento é obrigatório')
              + f'<div class="{p}-campo"><label>Peso <b>*</b></label><div class="{p}-input {p}-input--toque"><input class="{p}-entrada" type="text" inputmode="decimal" value="" placeholder="Digite" aria-label="Peso" data-peso data-sugestao="215"><button class="{p}-toque" type="button" data-acao="tocar-peso" aria-label="Informar peso"></button></div></div>'
              + f'<button class="{p}-avancar" type="button" data-acao="ir:3">AVANÇAR</button>')
    pag2 = app(p, 'ANITA RANCHO', ('execucao', '27/10/2026'), corpo2, lado_([('Situação da mãe', 'Vazia', 'verde'), ('Peso', 'Não Identificado', 'amarela')]))
    # 3) Resumo da rotina: PRÓXIMO ANIMAL volta ao início com outro animal
    corpo3 = (tit(p, 'Resumo da rotina', info=False)
              + f'<ul class="{p}-res"><li>{ICO["ok-circulo"]}Pesagem</li><li class="{p}-res--sub">{ICO["check"]}Peso: <span data-peso-resumo>215</span> KG</li><li>{ICO["ok-circulo"]}Desmame</li></ul>'
              + f'<button class="{p}-avancar {p}-avancar--largo" type="button" data-acao="ir:1" data-proximo>PRÓXIMO ANIMAL</button>')
    acoes = f'<span class="{p}-subacoes"><button type="button" disabled>{ICO["desfazer"]} Desfazer</button></span>'
    pag3 = app(p, 'ANITA RANCHO', ('simples', 'Resumo', acoes), corpo3, lado_([peso_box], lapis=False, situacao=False))
    dados = '<script type="application/json" data-animais>' + ANIMAIS_JSON + '</script>'
    return (dados + f'<div class="{p}-pag is-ativa" data-pag="1">{bloqueia(pag1)}</div><div class="{p}-pag" data-pag="2">{bloqueia(pag2)}</div>'
            f'<div class="{p}-pag" data-pag="3">{bloqueia(pag3)}</div>')

ANIMAIS_DIAGNOSTICO = [
 {
  "id": "LL206",
  "sexo": "Fêmea / Reprodução",
  "raca": "TABAPUÃ / NI",
  "nasc": "01/03/2020 (6a7m)",
  "ordem": "Novilha",
  "sit": "Gestante / Solteira",
  "pasto": "Pasto A",
  "cob": "IA - 01/06/2026 (148 Dias)<br>Touro desconhecido -<br>Data (DG): 24/06/2026<br>Previsão do Parto:<br>23/03/2027",
  "peso": "01/03/2022 (4a7m)<br>350.00 Kg<br>GMD: Não Identificado",
  "dgdata": "24/06/2026",
  "dias": "148",
  "qtd": "1",
  "lote": "Não encontrado"
 },
 {
  "id": "LL214",
  "sexo": "Fêmea / Reprodução",
  "raca": "NELORE / PO",
  "nasc": "15/08/2021 (5a2m)",
  "ordem": "Primípara",
  "sit": "Gestante / Parida",
  "pasto": "Pasto B",
  "cob": "IA - 20/06/2026 (129 Dias)<br>Touro 0045 - NE<br>Data (DG): 10/07/2026<br>Previsão do Parto:<br>11/04/2027",
  "peso": "12/05/2025 (3a9m)<br>412.00 Kg<br>GMD: 0.21",
  "dgdata": "10/07/2026",
  "dias": "129",
  "qtd": "2",
  "lote": "Lote 02"
 },
 {
  "id": "LL231",
  "sexo": "Fêmea / Reprodução",
  "raca": "TABAPUÃ / PO",
  "nasc": "10/11/2022 (3a11m)",
  "ordem": "Novilha",
  "sit": "Gestante / Solteira",
  "pasto": "Pasto A",
  "cob": "TE - 05/07/2026 (114 Dias)<br>Touro 0012 - SE<br>Data (DG): 02/08/2026<br>Previsão do Parto:<br>26/04/2027",
  "peso": "03/02/2026 (3a3m)<br>380.00 Kg<br>GMD: 0.35",
  "dgdata": "02/08/2026",
  "dias": "114",
  "qtd": "1",
  "lote": "Lote 01"
 }
]

def tela_diagnostico(p):
    """Diagnóstico de Gestação: confirmação (SIM fecha) e campos que mudam conforme Positivo / Negativo / Dúvida.
    AVANÇAR volta ao início com o próximo animal fictício."""
    A = ANIMAIS_DIAGNOSTICO[0]
    v = lambda k: f'<span data-animal="{k}">{A[k]}</span>'
    lado_html = lado(p, v('id'), [('Sexo / Tipo', v('sexo')), ('Raça / G. Sangue', v('raca')), ('Data nascimento (Idade)', v('nasc')),
                                  ('Ordem', v('ordem')), ('Situação / Estado', v('sit')), ('Pasto', v('pasto'))],
                     [('Última cobertura', v('cob'), 'verde'), ('Último Peso', v('peso'), 'amarela'),
                      ('Qtd de Ias', v('qtd'), 'verde'), ('Lote Atual', v('lote'), 'verde')], ficha=True, historico=True)
    dias = campo(p, 'Dias de Gestação', v('dias'), False, True, bt=None)
    resp = campo(p, 'Responsável', 'ADRIANO BRANCO')
    positivo = dias + radios(p, 'Avaliação ovariana', ['Normal', 'Reabsorvendo', 'Gemelar'], 0) + resp + area(p, 'Observação')
    negativo = (dias + radios(p, 'Avaliação ovariana', ['S/ Avaliação', 'Em Anestro', 'C. Luteo', 'Folículo', 'Cisto'], 0) + resp
                + seg(p, 'Aplicar Protocolo', ['Sim', 'Não'], 0) + area(p, 'Observação'))
    duvida = dias + resp + area(p, 'Observação')
    corpo = (tit(p, 'Diagnóstico de Gestação') + obs(p, 'Este evento é obrigatório')
             + seg(p, 'Diagnóstico', ['Positivo', 'Negativo', 'Dúvida'], -1, escolha=['positivo', 'negativo', 'duvida'])
             + variante(p, 'positivo', positivo) + variante(p, 'negativo', negativo) + variante(p, 'duvida', duvida)
             + f'<button class="{p}-avancar" type="button" data-acao="ir:1" data-proximo>AVANÇAR</button>')
    dialogo = (f'<div class="{p}-modal is-aberto" data-inicial><div class="{p}-dialogo"><h4>Confirmação</h4>'
               f'<p>Fêmea Gestante com diagnóstico Positivo na data {v("dgdata")}. Deseja fazer um novo diagnóstico?</p>'
               f'<div><button type="button" data-acao="fechar">SIM</button><button type="button" disabled>NÃO</button></div></div></div>')
    html = app(p, 'ANITA RANCHO', ('execucao', '27/10/2026'), corpo, lado_html, modal=dialogo)
    dados = '<script type="application/json" data-animais>' + __import__('json').dumps(ANIMAIS_DIAGNOSTICO, ensure_ascii=False) + '</script>'
    return dados + html.replace(f'<button class="{p}-volta" type="button"', f'<button class="{p}-volta" type="button" disabled')

ANIMAIS_SEXAGEM = [
 {
  "id": "LL206",
  "sexo": "Fêmea / Reprodução",
  "raca": "TABAPUÃ / NI",
  "nasc": "01/03/2020 (6a7m)",
  "ordem": "Novilha",
  "sit": "Gestante / Solteira",
  "pasto": "Pasto A",
  "cob": "IA - 01/06/2026 (148 Dias)<br>Touro desconhecido -<br>Data (DG): 27/10/2026<br>Previsão do Parto:<br>23/03/2027",
  "peso": "01/03/2022 (4a7m)<br>350.00 Kg<br>GMD: Não Identificado"
 },
 {
  "id": "LL214",
  "sexo": "Fêmea / Reprodução",
  "raca": "NELORE / PO",
  "nasc": "15/08/2021 (5a2m)",
  "ordem": "Primípara",
  "sit": "Gestante / Parida",
  "pasto": "Pasto B",
  "cob": "IA - 20/06/2026 (129 Dias)<br>Touro 0045 - NE<br>Data (DG): 10/07/2026<br>Previsão do Parto:<br>11/04/2027",
  "peso": "12/05/2025 (3a9m)<br>412.00 Kg<br>GMD: 0.21"
 },
 {
  "id": "LL231",
  "sexo": "Fêmea / Reprodução",
  "raca": "TABAPUÃ / PO",
  "nasc": "10/11/2022 (3a11m)",
  "ordem": "Novilha",
  "sit": "Gestante / Solteira",
  "pasto": "Pasto A",
  "cob": "TE - 05/07/2026 (114 Dias)<br>Touro 0012 - SE<br>Data (DG): 02/08/2026<br>Previsão do Parto:<br>26/04/2027",
  "peso": "03/02/2026 (3a3m)<br>380.00 Kg<br>GMD: 0.35"
 }
]

def tela_sexagem(p):
    """Sexagem: seletor Fêmea / Macho / Dúvida e responsável; AVANÇAR passa ao próximo animal fictício."""
    A = ANIMAIS_SEXAGEM[0]
    v = lambda k: f'<span data-animal="{k}">{A[k]}</span>'
    lado_html = lado(p, v('id'), [('Sexo / Tipo', v('sexo')), ('Raça / G. Sangue', v('raca')), ('Data nascimento (Idade)', v('nasc')),
                                  ('Ordem', v('ordem')), ('Situação / Estado', v('sit')), ('Pasto', v('pasto'))],
                     [('Última cobertura', v('cob'), 'verde'), ('Último Peso', v('peso'), 'amarela')], ficha=True)
    corpo = (tit(p, 'Sexagem') + obs(p, 'Este evento é obrigatório')
             + seg(p, 'Resultado', ['Fêmea', 'Macho', 'Dúvida'], 0, True)
             + campo(p, 'Responsável', 'MULTSOFT COM. ASS. MICRO')
             + f'<button class="{p}-avancar" type="button" data-acao="ir:1" data-proximo>AVANÇAR</button>')
    html = app(p, 'ANITA RANCHO', ('execucao', '27/10/2026'), corpo, lado_html)
    dados = '<script type="application/json" data-animais>' + __import__('json').dumps(ANIMAIS_SEXAGEM, ensure_ascii=False) + '</script>'
    return dados + html.replace(f'<button class="{p}-volta" type="button"', f'<button class="{p}-volta" type="button" disabled')

def tela_inventario(p):
    """Inventário: uma tela, sem interação (responsável e AVANÇAR)."""
    lado_html = lado(p, 'LL206', [('Sexo / Tipo', 'Fêmea / Reprodução'), ('Raça / G. Sangue', 'TABAPUÃ / NI'), ('Data nascimento (Idade)', '01/03/2020 (6a7m)'),
                                  ('Ordem', 'Novilha'), ('Situação / Estado', 'Gestante / Solteira'), ('Pasto', 'MA TESTE 02')],
                     [('Última cobertura', 'IA - 01/06/2026 (148 Dias)<br>Touro desconhecido -<br>Data (DG): 24/06/2026<br>Previsão do Parto:<br>23/03/2027', 'verde'),
                      ('Último Peso', '01/03/2022 (4a7m)<br>350.00 Kg<br>GMD: Não Identificado', 'amarela')], ficha=True)
    corpo = (tit(p, 'Inventário', info=False) + obs(p, 'Este evento é obrigatório')
             + campo(p, 'Responsável', 'MULTSOFT COM. ASS. MICRO', True, True)
             + f'<button class="{p}-avancar" type="button" disabled>AVANÇAR</button>')
    html = app(p, 'ANITA RANCHO', ('execucao', '27/10/2026'), corpo, lado_html)
    html = html.replace(f'<button class="{p}-bt" type="button"', f'<button class="{p}-bt" type="button" disabled')
    return html.replace(f'<button class="{p}-volta" type="button"', f'<button class="{p}-volta" type="button" disabled')

def tela_identificacao(p):
    """Identificação Eletrônica: bastão desconectado; o link reconecta e dispara a leitura do brinco (cena no slide)."""
    lado_html = lado(p, 'LL206', [('Sexo / Tipo', 'Fêmea / Reprodução'), ('Raça / G. Sangue', 'TABAPUÃ / NI'), ('Data nascimento (Idade)', '01/03/2020 (6a7m)'),
                                  ('Ordem', 'Novilha'), ('Situação / Estado', 'Gestante / Solteira'), ('Pasto', 'MA TESTE 02')],
                     [('Última cobertura', 'IA - 01/06/2026 (148 Dias)<br>Touro desconhecido -<br>Data (DG): 24/06/2026<br>Previsão do Parto:<br>23/03/2027', 'verde'),
                      ('Último Peso', '01/03/2022 (4a7m)<br>350.00 Kg<br>GMD: Não Identificado', 'amarela')], ficha=True)
    corpo = (tit(p, 'Identificação eletrônica', info=False) + obs(p, 'Este evento é obrigatório')
             + f'<div class="{p}-campo {p}-ident"><label>Identificação eletrônica <b>*</b></label><div class="{p}-input {p}-input--off" data-ident="982 000412345678"><span></span></div></div>'
             + f'<p class="{p}-nota {p}-nota--erro">Bastão desconectado.<br><button type="button" data-acao="reconectar"><u>Clique aqui para reconectar</u></button></p>'
             + f'<button class="{p}-avancar" type="button" disabled>AVANÇAR</button>')
    html = app(p, 'ANITA RANCHO', ('execucao', '27/10/2026'), corpo, lado_html)
    return html.replace(f'<button class="{p}-volta" type="button"', f'<button class="{p}-volta" type="button" disabled')

def cena_identificacao(p):
    return (f'        <div class="{p}-cena" aria-hidden="true">\n'
            f'          <div class="{p}-boi"><img src="assets/confinamento/ident-boi.webp?v=2" alt=""><i class="{p}-brinco"></i></div>\n'
            f'          <div class="{p}-bastao"><img src="assets/confinamento/ident-bastao.webp?v=1" alt=""><i class="{p}-led"></i></div>\n'
            f'          <i class="{p}-onda"></i>\n'
            f'        </div>\n')

# ---------------------------------------------------------------- eventos (texto do slide + tela)
EVENTOS = {
 'entrada':      dict(aria='Entrada de Animais', titulo='Entrada de Animais', tag='Estoque de Animais', linhas=1,
                      texto='Permite a inclusão<br>de novos animais<br>via aplicativo.', tela=lambda p, e='': tela_entrada(p, e or 'f')),
 'movimentacao': dict(aria='Movimentação entre Propriedades', titulo='Movimentação<br>entre Propriedades', tag='Estoque de Animais', linhas=2,
                      texto='Permite realizar a<br>movimentação de<br>animais via aplicativo.', tela=lambda p, e='': tela_movimentacao(p)),
 'venda':        dict(aria='Venda de Animais', titulo='Venda de Animais', tag='Estoque de Animais', linhas=1,
                      texto='Permite lançar a<br>venda de animais<br>via aplicativo.', tela=lambda p, e='': tela_venda(p)),
 'morte':        dict(aria='Morte de Animais', titulo='Morte de Animais', tag='Estoque de Animais', linhas=1,
                      texto='Permite lançar a morte<br>de animais via<br>aplicativo.', tela=lambda p, e='': tela_morte(p)),
 'vacinacao':    dict(aria='Vacinação de Animais', titulo='Vacinação de Animais', tag='Zoosanitário', linhas=1,
                      texto='Permite realizar o<br>lançamento de<br>vacinas nos animais<br>aplicativo.', tela=lambda p, e='': tela_vacinacao(p)),
 'pesagem':      dict(aria='Pesagem de Animais', titulo='Pesagem de Animais', tag='Controle Ponderal', linhas=1,
                      texto='Permite realizar o<br>lançamento de<br>pesagem dos animais<br>via aplicativo.', tela=lambda p, e='': tela_pesagem(p)),
 'conferencia':  dict(aria='Conferência de Lote: Animais Faltantes', titulo='Conferência de Lote<br>“Animais Faltantes”', tag='Reprodução', linhas=2,
                      texto='Permite identificar<br>animais faltantes,<br>transferidos e<br>entreveros dos lotes<br>processados no curral.', tela=lambda p, e='': tela_conferencia(p)),
 'perda':        dict(aria='Controle Perda de Implante', titulo='Controle Perda<br>de Implante', tag='Reprodução', linhas=2,
                      texto='Permite lançar os<br>animais que perderam<br>o implante no<br>momento do manejo<br>de retirada do mesmo<br>no protocolo de<br>sincronização.', tela=lambda p, e='': tela_perda(p)),
 'partos':       dict(aria='Lançamento de Partos', titulo='Lançamento de<br>Partos', tag='Reprodução', linhas=2,
                      texto='Permite lançar<br>informações do parto<br>de fêmeas no campo.', tela=lambda p, e='': tela_partos(p, e)),
 'protocolo':    dict(aria='Edição do Protocolo de IATF', titulo='Edição do Protocolo<br>de IATF', tag='Reprodução', linhas=2,
                      texto='Permite alterar tipo de<br>hormônio, marca e<br>dosagem durante o<br>lançamento do<br>protocolo de IATF.', tela=lambda p, e='': tela_protocolo(p)),
 'inseminacao':  dict(aria='Inseminação Artificial', titulo='Inseminação Artificial', tag='Reprodução', linhas=1,
                      texto='Permite lançar as informações<br>de sexagem da Inseminação<br>Artificial nas fêmeas via<br>aplicativo.', tela=lambda p, e='': tela_inseminacao(p)),
 'trat_doencas': dict(aria='Aplicação de Tratamento Doenças', titulo='Aplicação de<br>Tratamento Doenças', tag='Zoosanitário', linhas=2,
                      texto='Permite aplicar<br>tratamentos para doenças<br>específicas em todo o lote<br>ou em determinados<br>animais.', tela=lambda p, e='': tela_trat_doencas(p)),
 'desmame':      dict(aria='Desmame', titulo='Desmame', tag='Reprodução', linhas=1,
                      texto='Permite lançar o desmame<br>dos animais, com a pesagem,<br>via aplicativo.', tela=lambda p, e='': tela_desmame(p)),
 'diagnostico':  dict(aria='Diagnóstico de Gestação', titulo='Diagnóstico de Gestação', tag='Reprodução', linhas=1,
                      texto='Permite lançar o diagnóstico<br>de gestação das fêmeas<br>via aplicativo.', tela=lambda p, e='': tela_diagnostico(p)),
 'sexagem':      dict(aria='Sexagem', titulo='Sexagem', tag='Reprodução', linhas=1,
                      texto='Permite lançar o resultado<br>da sexagem fetal das fêmeas<br>via aplicativo.', tela=lambda p, e='': tela_sexagem(p)),
 'inventario':   dict(aria='Inventário', titulo='Inventário', tag='Estoque de Animais', linhas=1,
                      texto='Permite registrar a<br>conferência do inventário<br>de animais via aplicativo.', tela=lambda p, e='': tela_inventario(p)),
 'identificacao': dict(aria='Identificação Eletrônica', titulo='Identificação Eletrônica', tag='Estoque de Animais', linhas=1,
                      texto='Permite registrar o brinco<br>eletrônico dos animais com<br>o bastão leitor via aplicativo.', tela=lambda p, e='': tela_identificacao(p),
                      extra=cena_identificacao('tb')),
 'trat_iatf':    dict(aria='Aplicação de Tratamento IATF', titulo='Aplicação de<br>Tratamento IATF', tag='Reprodução', linhas=2,
                      texto='Utilizado como<br>possibilidade de aplicar<br>tratamentos específicos<br>de IATF em alguns<br>animais.', tela=lambda p, e='': tela_trat_iatf(p)),
}

# ordem e estado inicial por número de slide (mesmos números nos dois decks a partir de 105)
SEQUENCIA = [(105, 'movimentacao', ''), (106, 'venda', ''), (107, 'morte', ''), (108, 'vacinacao', ''), (109, 'pesagem', ''),
             (110, 'conferencia', ''), (111, 'perda', ''), (112, 'partos', ''), (113, 'partos', 'cria'), (114, 'partos', 'crias'),
             (115, 'protocolo', ''), (116, 'inseminacao', ''), (117, 'trat_doencas', ''), (118, 'trat_iatf', ''), (119, 'desmame', ''), (120, 'diagnostico', ''), (121, 'sexagem', ''), (122, 'inventario', ''), (123, 'identificacao', '')]
