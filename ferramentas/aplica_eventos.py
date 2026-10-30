"""Aplica os slides de eventos com tablet 3D (App MB Curral) nos dois decks, a partir de
tablet.py + eventos_app.py. Blocos marcados com TABLET-EVENTOS:... são substituídos a cada execução.
Uso: python3 ferramentas/aplica_eventos.py   (na raiz do repositório)"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tablet, eventos_app as EA

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = 'tb'
DECKS = [
  dict(arquivo='presentation/reproducao-cria-comercial.html', voltar=15,
       slides=[(103, 'entrada', 'f'), (104, 'entrada', 'm')] + EA.SEQUENCIA, destinos=None),
  dict(arquivo='presentation/confinamento-multbovinos.html', voltar=9,
       slides=[(15, 'entrada', 'f')] + EA.SEQUENCIA,
       destinos={'Entrada de Animais': 15, 'Pesagens': 109, 'Vacinação': 108, 'Venda com Pesagens': 106,
                 'Movimentação Por Localidade': 105, 'Confer. Por Lote Estação de Monta': 110, 'Tratamentos - Protocolo': 115, 'Desmame': 119, 'Diagnóstico de Gestação': 120, 'Sexagem': 121, 'Inventário': 122, 'Identificação Eletrônica': 123}),
]
M = {'css': ('  /* TABLET-EVENTOS:CSS:INICIO */\n', '  /* TABLET-EVENTOS:CSS:FIM */\n'),
     'html': ('      <!-- TABLET-EVENTOS:HTML:INICIO -->\n', '      <!-- TABLET-EVENTOS:HTML:FIM -->\n'),
     'js': ('    /* TABLET-EVENTOS:JS:INICIO */\n', '    /* TABLET-EVENTOS:JS:FIM */\n')}

def remove_secao(t, n):
    """remove a <section data-slide="n"> (e o comentário de título logo acima); devolve (texto, posição)."""
    m = re.search(r'(      <!-- =+ SLIDE %d —[^\n]*-->\n)?      <section class="slide[^>]*data-slide="%d"[^>]*>.*?</section>\n(\n)?' % (n, n), t, re.S)
    if not m: return t, None
    return t[:m.start()] + t[m.end():], m.start()

def substitui_bloco(t, chave, novo, insere_antes):
    ini, fim = M[chave]
    if ini in t:
        a = t.index(ini); b = t.index(fim) + len(fim)
        return t[:a] + ini + novo + fim + t[b:]
    for cand in ([insere_antes] if isinstance(insere_antes, str) else insere_antes):
        if cand in t:
            i = t.index(cand); return t[:i] + ini + novo + fim + t[i:]
    raise ValueError('ponto de inserção não encontrado: %r' % insere_antes)

for d in DECKS:
    arq = os.path.join(RAIZ, d['arquivo']); t = open(arq).read()
    # --- CSS (remove o bloco antigo do Confinamento, sem marcadores)
    a = t.find('  /* ================= EVENTOS COM TABLET 3D')
    if a >= 0 and M['css'][0] not in t:
        b = t.index('  /* ================= CONECTIVIDADE (2 slides)', a); t = t[:a] + t[b:]
    t = substitui_bloco(t, 'css', tablet.css(P), ['  /* ================= CONECTIVIDADE (2 slides)', '  /* ---- Footer / top-right nav hotspots ---- */', '</style>'])
    # --- Roboto para a tela do app
    if 'Roboto:ital' not in t:
        t = t.replace('family=Montserrat:wght@400;500;600;700;800&display=swap', 'family=Montserrat:wght@400;500;600;700;800&family=Roboto:ital,wght@0,400;0,500;0,700;1,400&display=swap', 1)
        assert 'Roboto:ital' in t, 'link de fontes não encontrado'
    # --- HTML: remove as seções antigas dos slides (imagens ou versão anterior) e insere o bloco
    pos = None
    if M['html'][0] in t:   # bloco já aplicado: substitui no mesmo lugar
        a = t.index(M['html'][0]); b = t.index(M['html'][1]) + len(M['html'][1]); t = t[:a] + t[b:]; pos = a
    for n, _, _ in d['slides']:
        t, p0 = remove_secao(t, n)
        if p0 is not None and (pos is None or p0 < pos): pos = p0
    if pos is None: pos = t.index('    </div>\n  </div>\n\n  <!-- Auto-hiding navigation -->')
    html = ''.join(tablet.html(P, n, EA.EVENTOS[ev], EA.EVENTOS[ev]['tela'](P, est), d['voltar']) for n, ev, est in d['slides'])
    t = t[:pos] + M['html'][0] + html + M['html'][1] + t[pos:]
    # --- JS (remove o bloco antigo do Confinamento, sem marcadores)
    a = t.find('    /* ---- Tablet 3D: inclina seguindo o mouse')
    if a >= 0 and M['js'][0] not in t:
        b = t.index('    /* ---- Restaura último slide visto ---- */', a); t = t[:a] + t[b:]
    t = substitui_bloco(t, 'js', tablet.js(P), '    /* ---- Restaura último slide visto ---- */')
    # --- TOTAL / BUILT
    nums = [n for n, _, _ in d['slides']]
    m = re.search(r'const TOTAL = (\d+);', t); total = max(int(m.group(1)), max(nums))
    t = t.replace(m.group(0), f'const TOTAL = {total};', 1)
    m = re.search(r'const BUILT = \[([^\]]*)\];', t)
    built = sorted(set(int(x) for x in re.findall(r'\d+', m.group(1))) | set(nums))
    t = t.replace(m.group(0), 'const BUILT = [' + ', '.join(map(str, built)) + '];', 1)
    # --- destinos dos botões do menu de eventos (slide 9 do Confinamento)
    if d['destinos']:
        for ev, n in d['destinos'].items():
            pat = re.compile(r'<button class="ev-btn"(?: disabled)? type="button" (style="[^"]*")( onclick="goToSlide\(\d+\)")?( data-evento="%s">)' % re.escape(ev))
            assert pat.search(t), ev
            t = pat.sub(lambda mm: '<button class="ev-btn" type="button" ' + mm.group(1) + f' onclick="goToSlide({n})"' + mm.group(3), t, count=1)
        # botões de evento sem tela ficam desativados (aparência apagada, sem hover)
        def marca(mm):
            tag = mm.group(0).replace(' disabled', '')
            return tag if 'onclick=' in tag else tag.replace('<button class="ev-btn"', '<button class="ev-btn" disabled', 1)
        t = re.sub(r'<button class="ev-btn"[^>]*>', marca, t)
    # --- deck de Cria: o botão "Voltar às opções de eventos" antigo não é mais adicionado a estes slides
    t = re.sub(r'    \[103, 104, [^\]]*\]\.forEach\(n => addReproBack\(n\)\);', '    /* slides 103 a 118 (tablet 3D) já trazem o botão de voltar aos eventos */', t)
    # --- deck de Cria: área ativa "Desmame" no slide 15 (lista Completo), ao lado de Parto / Perda de Implante
    hot = '        <button class="hotspot s2-hot" type="button" title="Desmame" aria-label="Desmame" style="left:41.2%;top:41.7%;width:14.6%;height:5.8%;" onclick="goToSlide(119)"></button>\n'
    if 'title="Parto" aria-label="Parto"' in t and hot not in t:
        i = t.index('        <button class="hotspot s2-hot" type="button" title="Parto" aria-label="Parto"')
        t = t[:i] + hot + t[i:]
    hot2 = '        <button class="hotspot s2-hot" type="button" title="Diagnóstico de Gestação" aria-label="Diagnóstico de Gestação" style="left:56.8%;top:73.5%;width:19.1%;height:5.8%;" onclick="goToSlide(120)"></button>\n'
    if 'title="Aplicação Protocolo IATF"' in t and hot2 not in t:
        i = t.index('        <button class="hotspot s2-hot" type="button" title="Aplicação Protocolo IATF"')
        t = t[:i] + hot2 + t[i:]
    hot3 = '        <button class="hotspot s2-hot" type="button" title="Sexagem" aria-label="Sexagem" style="left:41.2%;top:73.5%;width:14.6%;height:5.8%;" onclick="goToSlide(121)"></button>\n'
    if 'title="Parto" aria-label="Parto"' in t and hot3 not in t:
        i = t.index('        <button class="hotspot s2-hot" type="button" title="Parto" aria-label="Parto"')
        t = t[:i] + hot3 + t[i:]
    hot4 = '        <button class="hotspot s2-hot" type="button" title="Inventário" aria-label="Inventário" style="left:3.3%;top:49.4%;width:15.6%;height:5.8%;" onclick="goToSlide(122)"></button>\n'
    if 'title="Parto" aria-label="Parto"' in t and hot4 not in t:
        i = t.index('        <button class="hotspot s2-hot" type="button" title="Parto" aria-label="Parto"')
        t = t[:i] + hot4 + t[i:]
    hot5 = '        <button class="hotspot s2-hot" type="button" title="Identificação Eletrônica" aria-label="Identificação Eletrônica" style="left:19.9%;top:34%;width:19.7%;height:5.8%;" onclick="goToSlide(123)"></button>\n'
    if 'title="Parto" aria-label="Parto"' in t and hot5 not in t:
        i = t.index('        <button class="hotspot s2-hot" type="button" title="Parto" aria-label="Parto"')
        t = t[:i] + hot5 + t[i:]
    open(arq, 'w').write(t)
    print(d['arquivo'], 'slides', nums, 'TOTAL', total)
