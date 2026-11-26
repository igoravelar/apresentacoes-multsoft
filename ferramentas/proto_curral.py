"""Telas do protótipo do App MB Curral reproduzidas do vídeo tutorial (MBCURRAL1 11-11-26).
Rotina de recepção de animais com dez eventos, seletor genérico ("Selecione"), ficha do animal,
tipo de ação dos campos da rotina e calendário. Nomes de fazendas, pessoas e animais são fictícios."""
import json
from tablet import campo, seg, lado, tit, obs, app, ICO

FAZ = '<span data-fazenda-nome>FAZENDA BOA FORTUNA</span>'
RESP1, RESP2 = 'CARLOS BRANDÃO', 'RAFAEL MOURA'

# listas dos seletores (todas fictícias ou genéricas)
LISTAS = {
 'tipo': ['Engorda', 'Reprodução', 'Doadora', 'Receptora'],
 'raca': ['NELORE', 'ANGUS', 'BRANGUS', 'TABAPUÃ', 'GUZERÁ', 'SENEPOL', 'GIROLANDO', 'CRUZADO'],
 'grau': ['1/2', '1/4', '3/4', '5/8', '11/16', 'CARA LIMPA', 'LIVRO ABERTO', 'NÃO IDENTIFICADO', 'PURO DE CRUZA', 'PURO DE ORIGEM'],
 'pelagem': ['BRANCA', 'CASTANHA', 'CINZA', 'NÃO INFORMADA', 'PADRÃO', 'PRETA', 'VERMELHA'],
 'rebanho': ['COML', 'ELITE', 'CONFINAMENTO', 'RECRIA', 'PO', 'MB24', 'REPOSIÇÃO'],
 'lote_aval': ['0 DENTES', '2 DENTES', '4 DENTES', '6 DENTES', 'BOCA CHEIA', 'REFUGO'],
 'lote_final': ['ENGORDA', 'REPRODUÇÃO', 'RECRIA', 'DESCARTE', 'VENDA', 'REPOSIÇÃO'],
 'lote_alim': ['CONFINAMENTO 2026', 'ENGORDA 2026', 'SEMICONFINAMENTO', 'CREEP', 'PASTO SUPLEMENTADO', 'RECRIA ÁGUAS 2026'],
 'local': ['CURRAL 1', 'CURRAL 2', 'CURRAL 3', 'PASTO 1', 'PASTO 2', 'PASTO MORRO', 'PASTO A', 'PASTO B', 'PASTO C', 'PIQUETE 1', 'PIQUETE 2', 'EMBARQUE'],
 'advertencia': ['ANIMAIS COM REAÇÃO', 'ANIMAL PERDEU CHIP', 'ANIMAL PERDEU O NÚMERO VISUAL', 'ANIMAL SEM ID USUAL', 'BOI SEM ORELHAS',
                 'CONFERIR CHIP ELETRÔNICO', 'CONFERIR SEXO', 'CONFIRMAR LOCALIDADE', 'DESCARTE', 'VERIFICAR DIAS DE GESTAÇÃO'],
 'vacina': ['POLIGUARD FC', 'DECTOMAX', 'AFTOSA', 'BRUCELOSE B19', 'CLOSTRIDIOSE', 'RAIVA', 'IVOMEC GOLD'],
 'responsavel': [RESP1, RESP2, 'MARCOS VIEIRA', 'JOÃO PEDRO LIMA', 'ANA PAULA REIS'],
 'tipo_parto': ['Normal', 'Puxado', 'Cesariana', 'Aborto', 'Morte Embrionária'],
 'situacao_cria': ['Vivo', 'Descartado', 'Natimorto'],
 'tamanho': ['Pequeno', 'Médio', 'Grande'],
 'sexo': ['Macho', 'Fêmea'],
 'animais': ['ID Usual: 2210-25|Sexo: Fêmea|Data nascimento: 09/08/2019|Raça: NELORE|Tipo: Reprodução',
             'ID Usual: 0014|Sexo: Fêmea|Data nascimento: 02/08/2018|Tipo: Receptora',
             'ID Usual: AC201|Sexo: Fêmea|Data nascimento: 10/01/2020|Raça: NELORE|Tipo: Reprodução',
             'ID Usual: AC202|Sexo: Fêmea|Data nascimento: 10/01/2020|Raça: NELORE|Tipo: Reprodução',
             'ID Usual: AC204|Sexo: Fêmea|Data nascimento: 10/01/2020|Raça: NELORE|Tipo: Reprodução',
             'ID Usual: TT301|Sexo: Fêmea|Data nascimento: 02/01/2019|Raça: NELORE|Tipo: Reprodução'],
 'fazendas': ['FAZENDA BOA FORTUNA', 'FAZENDA GADO MANSO', 'FAZENDA SANTA LUZIA', 'FAZENDA RIO VERDE', 'FAZENDA TRÊS BARRAS',
              'FAZENDA SÃO BENTO', 'FAZENDA ÁGUA LIMPA', 'FAZENDA PEDRA BRANCA', 'FAZENDA BELA VISTA', 'FAZENDA CAPÃO ALTO'],
}

# eventos da rotina de recepção -> página do tablet
EXEC_NOVOS = {'Alteração de Animais': 25, 'Movimentação entre Lote Avaliação': 26, 'Movimentação entre Lote Finalidade': 27,
              'Movimentação entre Lote Alimentar': 28, 'Pesagem': 29, 'Pesagens': 29, 'Apartação': 30, 'Medições': 31,
              'Inventário': 32, 'Advertência': 33, 'Vacinação': 34, 'Parto': 35}

ROTINA_RECEPCAO = ('Recepção de Animais', ' &gt; '.join(['Alteração de Animais', 'Movimentação entre Lote Avaliação', 'Movimentação entre Lote Finalidade',
                   'Movimentação entre Lote Alimentar', 'Pesagem', 'Apartação', 'Medições', 'Inventário', 'Advertência', 'Vacinação']))

def _volta(p, h):
    return h.replace(f'<button class="{p}-volta" type="button" aria-label="Voltar">', f'<button class="{p}-volta" type="button" data-acao="nav-volta:" aria-label="Voltar">')

def _lado(p, peso='Não identificado'):
    return lado(p, '<span data-exec-id>MB-001</span>', [('Sexo / Tipo', 'Macho / Engorda'), ('Raça / G. Sangue', 'NELORE / CL'), ('Data nascimento (Idade)', '10/11/2025 (1a0m)'),
                                                        ('Pasto', 'CURRAL 1')], [('Último Peso', peso, 'amarela')], ficha=True)

def sel(p, rotulo, chave, obrig=False, valor=None, det=None, ref=None):
    """campo "Selecione" que abre o seletor; preenchido mostra a lixeira."""
    ob = ' <b>*</b>' if obrig else ''
    ini = f' data-ini="{valor}"' if valor else ''
    dt = f' data-det="{det}"' if det else ''
    rf = f' data-ref="{ref}"' if ref else ''
    span = f'<span>{valor}</span>' if valor else f'<span class="{p}-ph">Selecione</span>'
    return (f'<div class="{p}-campo{" is-preenchido" if valor else ""}" data-preenchivel{ini}{dt}{rf}><label>{rotulo}{ob}</label>'
            f'<div class="{p}-input {p}-input--toque">{span}<button class="{p}-bt {p}-bt--lupa" type="button" aria-label="Buscar">{ICO["lupa"]}</button>'
            f'<button class="{p}-bt {p}-bt--lixo" type="button" data-acao="limpar-campo" aria-label="Limpar">{ICO["lixo"]}</button>'
            f'<button class="{p}-toque" type="button" data-acao="picker:{chave}" data-titulo="{rotulo}" aria-label="Selecionar {rotulo}"></button></div></div>')

def txt(p, rotulo, sugestao, obrig=False, det=None, ph='Digite', extra=''):
    """campo de digitação: o toque preenche o valor de demonstração."""
    ob = ' <b>*</b>' if obrig else ''
    dt = f' data-det="{det}"' if det else ''
    return (f'<div class="{p}-campo"{dt}><label>{rotulo}{ob}</label><div class="{p}-input {p}-input--toque">'
            f'<input class="{p}-entrada" type="text" inputmode="decimal" placeholder="{ph}" aria-label="{rotulo}" data-tap="{sugestao}"{extra} autocomplete="off">'
            f'<button class="{p}-toque" type="button" data-acao="tap-fill" aria-label="{rotulo}"></button></div></div>')

def confirma(p, popup, texto, sim, nao):
    return (f'<div class="{p}-modal" data-popup="{popup}"><div class="{p}-dialogo" data-acao=""><h4>Confirmação</h4><p>{texto}</p>'
            f'<div><button type="button" data-acao="{sim}">SIM</button><button type="button" data-acao="{nao}">NÃO</button></div></div></div>')

def avancar(p, acao='exec-next'):
    return f'<button class="{p}-avancar" type="button" data-acao="{acao}">AVANÇAR</button>'

def _evento(p, titulo, corpo, modal='', peso='Não identificado'):
    h = app(p, FAZ, ('execucao', '<span data-exec-data>27/10/2026</span>'), tit(p, titulo, info=False) + obs(p) + corpo, _lado(p, peso), modal=modal, gaveta=True, vaca='nav:3')
    return _volta(p, h)

# ---------------------------------------------------------------- eventos da rotina de recepção
def tela_alteracao(p):
    c = (f'<div class="{p}-campo"><label>ID Usual <b>*</b></label><div class="{p}-input"><input class="{p}-entrada" type="text" value="MB-001" data-exec-input aria-label="ID Usual"></div></div>'
         + seg(p, 'Sexo', ['Fêmea', 'Macho'], 1) + sel(p, 'Tipo', 'tipo') + txt(p, 'Idade (Meses)', '12') + sel(p, 'Raça', 'raca')
         + sel(p, 'Grau de sangue', 'grau') + sel(p, 'Pelagem', 'pelagem') + sel(p, 'Rebanho', 'rebanho') + avancar(p))
    return _evento(p, 'Alteração de Animais', c)

def tela_lote_aval(p):
    return _evento(p, 'Movimentação entre Lote Avaliação', sel(p, 'Lote', 'lote_aval', True, det='Lote: {v}') + avancar(p))

def tela_lote_final(p):
    m = confirma(p, 'entrada', 'Deseja executar o evento de Movimentação entre Lote Finalidade para o animal?', 'fechar', 'exec-next')
    return _evento(p, 'Movimentação entre Lote Finalidade', sel(p, 'Lote', 'lote_final', True, det='Lote: {v}') + avancar(p), m)

def tela_lote_alim(p):
    return _evento(p, 'Movimentação entre Lote Alimentar', sel(p, 'Lote', 'lote_alim', True, valor='ENGORDA 2026', det='Lote: {v}') + avancar(p))

def tela_pesagem_rec(p):
    m = confirma(p, 'entrada', 'Deseja pesar o animal?', 'fechar', 'exec-next')
    return _evento(p, 'Pesagem', txt(p, 'Peso', '286', True, det='Peso: {v} KG') + avancar(p), m)

def tela_apartacao(p):
    m = confirma(p, 'avancar', 'Confirma a movimentação do animal para a localização <b data-ref-txt="loc"></b>?', 'exec-next', 'fechar')
    return _evento(p, 'Apartação', sel(p, 'Localização', 'local', True, det='Apartado para: {v}', ref='loc') + avancar(p, 'confirma-avancar'), m, peso='11/11/2026 (0m)<br>286.00 Kg<br>GMD: 0.38')

def tela_medicao(p):
    c = (f'<p class="{p}-slot__sub">1º Medição</p>' + campo(p, 'Avaliação', 'ALTURA', False, True) + txt(p, 'Valor', '35', True, det='ALTURA ({v})')
         + campo(p, 'Responsável', RESP2, False, True)
         + f'<p class="{p}-slot__sub">2º Medição</p>' + campo(p, 'Avaliação', 'APRUMOS', False, True) + txt(p, 'Valor', '4', True, det='APRUMOS ({v})')
         + campo(p, 'Responsável', RESP2, False, True) + avancar(p))
    return _evento(p, 'Medição', c, peso='11/11/2026 (0m)<br>286.00 Kg<br>GMD: 0.38')

def tela_inventario_rec(p):
    return _evento(p, 'Inventário', sel(p, 'Responsável', 'responsavel', True, valor=RESP1) + avancar(p), peso='11/11/2026 (0m)<br>286.00 Kg<br>GMD: 0.38')

def tela_advertencia(p):
    m = confirma(p, 'entrada', 'Deseja registrar Advertência ao animal?', 'fechar', 'exec-next')
    return _evento(p, 'Advertência', sel(p, 'Tipo', 'advertencia', True, det='Tipo: {v}') + avancar(p), m, peso='11/11/2026 (0m)<br>286.00 Kg<br>GMD: 0.38')

def tela_vacinacao_rec(p):
    c = (f'<p class="{p}-slot__sub">1º Vacina</p>' + sel(p, 'Vacina', 'vacina', True, valor='POLIGUARD FC', det='{v}', ref='vac')
         + txt(p, 'Dose', '5', True) + campo(p, 'Unidade de uso', 'MILILITRO', False, True) + sel(p, 'Responsável', 'responsavel', False, valor=RESP1)
         + f'<p class="{p}-slot__sub">2º Vacina</p>' + sel(p, 'Vacina', 'vacina', True, valor='DECTOMAX', det='{v}')
         + txt(p, 'Dose', '4', True) + campo(p, 'Unidade de uso', 'UNIDADE', False, True) + sel(p, 'Responsável', 'responsavel', False, valor=RESP1)
         + avancar(p, 'confirma-avancar'))
    m = confirma(p, 'avancar', 'Confirma a aplicação de: <b data-ref-txt="vac"></b>?', 'exec-next', 'fechar')
    return _evento(p, 'Vacinação', c, m, peso='11/11/2026 (0m)<br>286.00 Kg<br>GMD: 0.38')

# ---------------------------------------------------------------- telas de apoio
def tela_picker(p):
    corpo = (f'<div class="{p}-busca"><input type="text" placeholder="Digite para filtrar" aria-label="Filtrar" data-filtro-opcao autocomplete="off">{ICO["lupa"]}'
             f'<button class="{p}-toque" type="button" data-acao="focar" aria-label="Filtrar"></button></div><div data-pick-lista></div>')
    h = app(p, '', ('titulo', '<span data-pick-titulo>Selecione</span>', ''), corpo, attrs=' data-proto data-sem-appbar')
    return _volta(p, h)

def tela_ficha(p):
    def sec(t, pares):
        it = ''.join(f'<div><small>{r}</small><b>{v}</b></div>' for r, v in pares)
        return f'<fieldset class="{p}-ficha-sec"><legend>{t}</legend><div class="{p}-ficha-grade">{it}</div></fieldset>'
    corpo = (sec('Dados Gerais', [('Sexo / Tipo', 'Macho / Engorda'), ('Raça / G. Sangue', 'NELORE / CL'), ('Data Nascimento', '10/11/2025'), ('Idade', '1a0m'),
                                  ('Compra', '27/03/2026'), ('Fornecedor', 'AGROPECUÁRIA MODELO'), ('Peso Entrada', '200.00'), ('Rebanho', 'COML')])
             + sec('Genealogia', [('Pai', '- / -'), ('Mãe', '- / -'), ('Avô Materno', '- / -'), ('Mãe Receptora', '- / -')])
             + sec('Localidades', [('Localização Atual', 'PASTO A'), ('Setor', '-'), ('Mov. entre Lote Avaliação', '2 DENTES'), ('Mov. entre Lote Alimentar', 'ENGORDA 2026'),
                                   ('Lote Genético', '-'), ('Mov. entre Lote Finalidade', 'ENGORDA')])
             + sec('Pesagens', [('Data Peso Anterior', '27/03/2026'), ('Peso Anterior', '200.00'), ('Data Peso Atual', '11/11/2026'), ('Peso Atual', '286.00'), ('GPD', '0.38'), ('GMD', '0.38')])
             + f'<fieldset class="{p}-ficha-sec"><legend>Parto(s)</legend><div class="{p}-ficha-tab"><span>Data</span><span>ID Usual</span><span>Desmame</span><span>Peso</span><span>Situação</span></div>'
               f'<p class="{p}-ficha-vazio">Sem registros.</p></fieldset><div style="height:4cqh;flex:0 0 auto"></div>')
    h = app(p, '', ('titulo', 'Ficha do Animal <b class="' + p + '-ficha-id" data-exec-id>MB-001</b><small class="' + p + '-ficha-sub">INFORMAÇÕES COMPLEMENTARES</small>', ''), corpo,
            attrs=' data-proto data-sem-appbar')
    return _volta(p, h)

def tela_tipo_acao(p):
    barras = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 5h2v14H3zm4 0h1v14H7zm3 0h2v14h-2zm4 0h1v14h-1zm3 0h2v14h-2zm4 0h1v14h-1z"/></svg>'
    pino = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M15 3l6 6-3 1-3 3 1 5-2 2-4-4-5 5-1-1 5-5-4-4 2-2 5 1 3-3z"/></svg>'
    xis = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>'
    corpo = (f'<h3 class="{p}-acao-tit" data-acao-titulo>Campo</h3>'
             f'<button class="{p}-acao-op {p}-acao-op--ler" type="button" data-acao="acao-tipo:ler">{barras}Ler a cada vez</button>'
             f'<div class="{p}-acao-ler" data-ler-conf style="display:none"><label data-ler-rot>Campo</label><p data-ler-val></p>'
             f'<button class="{p}-acao-ok {p}-acao-ok--ler" type="button" data-acao="acao-ler-ok">OK</button></div>'
             f'<button class="{p}-acao-op {p}-acao-op--fixar" type="button" data-acao="acao-tipo:fixar">{pino}Fixar valor</button>'
             f'<div class="{p}-acao-fixar" data-fixar style="display:none"><label>Valor</label><div class="{p}-input {p}-input--toque">'
             f'<input class="{p}-entrada" type="text" placeholder="Digite" aria-label="Valor" data-tap="" autocomplete="off"><button class="{p}-toque" type="button" data-acao="tap-fill" aria-label="Valor"></button></div>'
             f'<button class="{p}-acao-ok" type="button" data-acao="acao-ok">OK</button></div>'
             f'<button class="{p}-acao-op {p}-acao-op--nao" type="button" data-acao="acao-tipo:nao">{xis}Não utilizar</button>')
    h = app(p, '', ('titulo', 'Selecione o tipo de ação', ''), corpo, attrs=' data-proto data-sem-appbar')
    return _volta(p, h)

def calendario(p):
    """calendário: o mês é desenhado pelo JS (setas para meses anteriores/seguintes)."""
    return (f'<div class="{p}-modal" data-popup="calendario"><div class="{p}-cal" data-acao=""><div class="{p}-cal__cab"><p class="{p}-cal__mes" data-cal-mes></p>'
            f'<button type="button" data-acao="cal-mes:-12" aria-label="Ano anterior">«</button><button type="button" data-acao="cal-mes:-1" aria-label="Mês anterior">‹</button>'
            f'<button type="button" data-acao="cal-mes:1" aria-label="Próximo mês">›</button><button type="button" data-acao="cal-mes:12" aria-label="Próximo ano">»</button></div>'
            f'<div class="{p}-cal__sem"><span>D</span><span>S</span><span>T</span><span>Q</span><span>Q</span><span>S</span><span>S</span></div>'
            f'<div class="{p}-cal__dias" data-cal-dias></div><div class="{p}-cal__bt"><button type="button" data-acao="fechar">CANCELAR</button>'
            f'<button type="button" data-acao="cal-selecionar">SELECIONAR</button></div></div></div>')

def progresso_carga(p):
    return (f'<div class="{p}-modal" data-popup="carga"><div class="{p}-dialogo {p}-carga-prog" data-acao=""><i class="{p}-spin"></i>'
            f'<p>Carregando dados de: <b data-carga-item>Animais</b></p><strong data-carga-pct>0% Concluído</strong></div></div>')

# ---------------------------------------------------------------- evento Parto (vídeo MBCURRAL - PARTOS)
PAI = ('0870 SERRA ALTA', 'SERRA ALTA FIV 2207')

def _lado_parto(p):
    return lado(p, '<span data-exec-id>2210-25</span>', [('Sexo / Tipo', 'Fêmea / Reprodução'), ('Raça / G. Sangue', 'NELORE / CEIP'), ('Data nascimento (Idade)', '09/08/2019 (7a3m)'),
                                                          ('Ordem', 'Multípara'), ('Situação / Estado', 'Servida / Solteira'), ('Pasto', 'PASTO MORRO')],
                [('Última cobertura', f'IA - 05/02/2026 (293 Dias)<br>{PAI[0]} - Previsão do Parto: 13/11/2026', 'verde'),
                 ('Último parto', 'Normal - 10/11/2025', 'verde'), ('Último Peso', '14/08/2026 (7a0m)<br>455.00 Kg<br>GMD: 0.42', 'amarela')], ficha=True)

def _passos(p, rotulo, ph='Toque'):
    return (f'<div class="{p}-campo" data-passos><label>{rotulo}</label>'
            f'<div class="{p}-input {p}-input--off"><span class="{p}-ph" data-valor="" data-ph="{ph}">{ph}</span></div>'
            f'<div class="{p}-passos"><button type="button" data-passo="1">+1</button><button type="button" data-passo="0.5">+0,5</button>'
            f'<button type="button" data-passo="0.25">+0,25</button><button type="button" data-passo="0" aria-label="Zerar">{ICO["lixo"]}</button></div></div>')

def tela_parto(p):
    data = (f'<div class="{p}-campo" data-det-data><label>Data <b>*</b></label><div class="{p}-input {p}-input--toque"><span class="{p}-ph" data-cal-data>Selecione a data...</span>'
            f'<button class="{p}-bt" type="button" data-acao="limpar-data" aria-label="Limpar">{ICO["lixo"]}</button>'
            f'<button class="{p}-toque" type="button" data-acao="calendario" data-cal-ini="17/11/2026" aria-label="Selecionar data"></button></div></div>')
    crias = (f'<div class="{p}-campo"><label>Crias <b>*</b> <i class="{p}-mais" role="button" data-acao="cria-nova" aria-label="Nova cria">{ICO["mais"]}</i></label>'
             f'<ul class="{p}-lista" data-crias-exec data-vazio-texto="Sem registros."><li class="{p}-item {p}-item--vazio" data-vazio>Sem registros.</li></ul></div>')
    corpo = (data + sel(p, 'Tipo de Parto', 'tipo_parto', True, valor='Normal', det='Tipo: {v}') + sel(p, 'Rebanho', 'rebanho', False, valor='ELITE')
             + _passos(p, 'Score Corpóreo') + sel(p, 'Responsável', 'responsavel', True, valor=RESP1)
             + campo(p, 'Localização após o parto', 'PASTO 2', False) + crias + txt(p, 'Observação', 'Nasceu 100% saudável', ph='Digite')
             + f'<div class="{p}-toast" data-toast-parto></div>' + avancar(p, 'parto-avancar'))
    h = app(p, FAZ, ('execucao', '<span data-exec-data>27/10/2026</span>'), tit(p, 'Parto', info=False) + obs(p) + corpo, _lado_parto(p), modal=calendario(p), gaveta=True, vaca='nav:3')
    return _volta(p, h)

def tela_cria(p):
    pai = (f'<div class="{p}-cria-dados"><b>Dados da Mãe</b><small>ID Usual: <span data-exec-id>2210-25</span></small>'
           f'<b>Dados do Pai</b><small>ID Usual: {PAI[0]}<br>Nome: {PAI[1]}</small></div>')
    corpo = (pai + seg(p, '', ['Fêmea', 'Macho'], 0) + sel(p, 'Situação da Cria', 'situacao_cria', True, valor='Vivo')
             + txt(p, 'ID Usual', '', True, extra=' data-cria-id') + txt(p, 'ID Secundário', '', extra=' data-cria-id2') + txt(p, 'SISBOV', '')
             + txt(p, 'Nome', 'NV 456', extra=' data-cria-nome') + campo(p, 'Identificação eletrônica', '', False, bt=None)
             + txt(p, 'Peso', '35', True) + sel(p, 'Raça', 'raca', True, valor='NELORE') + sel(p, 'Tipo', 'tipo', True)
             + _passos(p, 'Score Corpóreo') + seg(p, 'Tamanho Cria', ['Pequeno', 'Médio', 'Grande'], 1)
             + sel(p, 'Pelagem', 'pelagem', False, valor='BRANCA') + sel(p, 'Grau de sangue', 'grau', False, valor='PURO DE ORIGEM')
             + sel(p, 'Movimentação entre Lote Avaliação', 'lote_aval', False)
             + f'<button class="{p}-avancar" type="button" data-acao="cria-salvar">SALVAR</button>')
    m = (f'<div class="{p}-modal" data-popup="cria-nome"><div class="{p}-dialogo" data-acao=""><h4>Confirmação</h4><p>O Animal <b data-cria-dup></b> está usando o mesmo nome, deseja prosseguir?</p>'
         f'<div><button type="button" data-acao="cria-salvar-ok">SIM</button><button type="button" data-acao="fechar">NÃO</button></div></div></div>')
    acoes = f'<span class="{p}-subacoes"><button type="button">{ICO["ajuda"]} Ajuda</button></span>'
    h = app(p, '', ('titulo', 'Cria', acoes), corpo, modal=m, attrs=' data-proto data-sem-appbar')
    return _volta(p, h)

def listas_json():
    return '<script type="application/json" data-listas>' + json.dumps(LISTAS, ensure_ascii=False) + '</script>'

def paginas(p):
    """páginas 22 a 34 do protótipo: data-texto="manter" preserva o texto do slide (seletor e ficha)."""
    pags = [(22, tela_picker(p), ' data-texto="manter"'), (23, tela_ficha(p), ' data-texto="manter"'), (24, tela_tipo_acao(p), ''),
            (25, tela_alteracao(p), ' data-texto="rotina"'), (26, tela_lote_aval(p), ' data-texto="rotina"'), (27, tela_lote_final(p), ' data-texto="rotina"'),
            (28, tela_lote_alim(p), ' data-texto="rotina"'), (29, tela_pesagem_rec(p), ' data-texto="rotina"'), (30, tela_apartacao(p), ' data-texto="rotina"'),
            (31, tela_medicao(p), ' data-texto="rotina"'), (32, tela_inventario_rec(p), ' data-texto="rotina"'), (33, tela_advertencia(p), ' data-texto="rotina"'),
            (34, tela_vacinacao_rec(p), ' data-texto="rotina"'), (35, tela_parto(p), ' data-texto="rotina"'), (36, tela_cria(p), ' data-texto="manter"')]
    return listas_json() + ''.join(f'<div class="{p}-pag" data-pag="{n}"{a}>{h}</div>' for n, h, a in pags)
