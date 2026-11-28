"""Monitoramento do Confinamento: submenu por abas (slide 10) e protótipo navegável do Sistema Web
MultBovinos dentro de um navegador em tela cheia (slide 125). Dados fictícios.
Aplicado por aplica_web.py entre os marcadores WEB-MB:* do deck de Confinamento."""

ABAS = [('reprodutivo', 'Reprodutivo', 'Dashboards da reprodução'), ('producao', 'Produção', 'Pesagens e desempenho'),
        ('confinamento', 'Confinamento', 'Tratos e consumo'), ('sisbov', 'SISBOV', 'Rastreabilidade'),
        ('zoossanitario', 'Zoossanitário', 'Vacinas e tratamentos'), ('insumos', 'Insumos', 'Estoque e consumo'),
        ('administrativo', 'Administrativo', 'Financeiro e custos'), ('auditoria', 'Auditoria', 'Conferências e registros')]

ICONES = {
 'reprodutivo': '<path d="M12 21s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.6-7 10-7 10z"/>',
 'producao': '<path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/>',
 'confinamento': '<path d="M3 21V9l9-6 9 6v12"/><path d="M8 21v-6h8v6M3 13h18"/>',
 'sisbov': '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h8M8 11h8M8 15h5"/>',
 'zoossanitario': '<path d="m18 2 4 4M15 5l4 4M8 12l4 4M5 19l-2 2M16.5 7.5 7 17l-3-3 9.5-9.5z"/>',
 'insumos': '<path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M3 7v10l9 4 9-4V7M12 11v10"/>',
 'administrativo': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18M7 15h4"/>',
 'auditoria': '<circle cx="11" cy="11" r="7"/><path d="m21 21-5-5M8 11l2 2 4-4"/>',
}

def svg_ic(chave, cls):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="url(#cd-ic-grad)" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONES[chave]}</svg>')

import os
_DIR = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(_DIR, 'web_mb.css')).read()
JS = open(os.path.join(_DIR, 'web_mb.js')).read()

def html_submenu(n=10, web=125):
    cols = [2.75, 27.1, 51.45, 75.8]; rows = [16, 49]
    cards = ''
    for i, (k, nome, sub) in enumerate(ABAS):
        l, tp = cols[i % 4], rows[i // 4]
        cards += (f'        <button class="cd-card mc-card" type="button" style="left:{l}%;top:{tp}%;--d:{.14 + i * .04:.2f}s" onclick="abreWebMB(\'{k}\')" aria-label="{nome}">\n'
                  f'          {svg_ic(k, "cd-card__ic")}\n'
                  f'          <span class="cd-card__txt"><span class="cd-card__t">{nome}</span><span class="cd-card__s">{sub}</span></span>\n        </button>\n')
    return f'''      <!-- ===================== SLIDE {n} — Monitoramento do Confinamento (submenu por abas do Sistema Web) ===================== -->
      <section class="slide cd" data-slide="{n}" data-screen-label="{n}" aria-label="Slide {n} — Monitoramento do Confinamento">
        <img class="slide__bg" src="assets/erp-senior/fundo-claro-topo.webp?v=1" alt="" aria-hidden="true">
        <img class="cd-faixa" src="assets/erp-senior/faixa-topo.webp?v=1" alt="" aria-hidden="true">
        <h2 class="cd-topo" style="--d:.04s"><img src="assets/erp-senior/icone-mb.webp?v=1" alt="" aria-hidden="true">Monitoramento do Confinamento</h2>
        <svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
          <linearGradient id="cd-ic-grad" gradientUnits="userSpaceOnUse" x1="0" y1="2" x2="0" y2="22"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c9f2c2"/></linearGradient>
        </defs></svg>
{cards}
        <button class="ms-nav" type="button" style="top:2%;width:5.2%;height:6.2%;left:90.3%;--d:.26s" onclick="goToSlide(2)" aria-label="Menu" title="Menu">
          <svg viewBox="0 0 24 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="10" r="8.2"/><path d="M8.8 6.9h6.4M8.8 10h6.4M8.8 13.1h6.4"/></svg>
        </button>
        <img class="ms-logo cd-logo" src="assets/erp-senior/logo-mb-multsoft-h.webp?v=1" alt="MB | MultSoft" style="--d:.5s">
      </section>

'''

VACA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 4c-1.5 0-2.5 1.2-2.5 2.6S2.6 9 4 9h1.2l1.3 4.5c.4 1.4 1.6 2.3 3 2.3h5c1.4 0 2.6-.9 3-2.3L18.8 9H20c1.4 0 2.5-1 2.5-2.4S21.5 4 20 4h-3l-1 2.5H8L7 4zm5.5 7.5a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm5 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2zM9 17h6v3H9z"/></svg>'

def html_web(n=125, sub=10):
    abas = ''.join(f'<button class="wb-aba" type="button" data-wb-aba="{k}">{nome}</button>' for k, nome, _ in ABAS)
    casa = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3 2 12h3v8h5v-5h4v5h5v-8h3z"/></svg>'
    glob = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>'
    return f'''      <!-- ===================== SLIDE {n} — Sistema Web MultBovinos (protótipo navegável) ===================== -->
      <section class="slide cd wb" data-slide="{n}" data-screen-label="{n}" aria-label="Slide {n} — Sistema Web MultBovinos: dashboards">
        <img class="cd-faixa" src="assets/erp-senior/faixa-topo.webp?v=1" alt="" aria-hidden="true">
        <h2 class="cd-topo" style="--d:.04s"><img src="assets/erp-senior/icone-mb.webp?v=1" alt="" aria-hidden="true">Monitoramento do Confinamento</h2>
        <div class="wb-janela">
          <div class="wb-chrome"><i></i><i></i><i></i><div class="wb-url"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a5 5 0 0 0-5 5v3H5v12h14V10h-2V7a5 5 0 0 0-5-5zm-3 8V7a3 3 0 0 1 6 0v3z"/></svg>app.multbovinos.com.br/#/app/dashboard</div></div>
          <div class="wb-tela">
            <header class="wb-top"><span class="wb-logo">{VACA}</span>
              <button type="button" data-wb="menu">Menu</button><button type="button" data-wb="dash">Dashboard</button><button type="button" data-wb="toast" data-msg="Abrindo Indicadores">Indicadores</button>
              <button type="button" class="wb-faz" data-wb="faz" data-wb-faz>FAZENDA BOA FORTUNA</button>
              <button type="button" class="wb-sino" data-wb="sino" aria-label="Notificações"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 16V11a6 6 0 0 0-12 0v5l-2 2h16zM10 21h4"/></svg><em>12</em></button>
              <button type="button" data-wb="busca">Busca de Animais</button><button type="button" data-wb="user">MultSoft ▾</button></header>
            <nav class="wb-abas">{abas}<span class="wb-escopo"><button type="button" class="is-ativa" data-wb-escopo="esta">{casa}Desta<br>Fazenda</button><button type="button" data-wb-escopo="todas">{glob}Todas as<br>Fazendas</button></span></nav>
            <div class="wb-migalha"><button type="button" data-wb="dash">Dashboard</button><span>&gt;</span><span data-wb-mig></span><button type="button" class="wb-ajudalink" data-wb="ajuda" data-aj="estacao">? Ajuda</button></div>
            <div class="wb-corpo" data-wb-corpo></div>
            <div class="wb-menu"><nav></nav><section></section></div>
            <div class="wb-drop" data-wb-drop="user"><button type="button" data-wb="toast" data-msg="Abrindo Perfil">Perfil</button><button type="button" data-wb="toast" data-msg="Idioma: Português (Brasil)">Idioma <span>▸</span></button><hr><button type="button" data-wb="toast" data-msg="Sair desabilitado no protótipo">Sair</button></div>
            <div class="wb-drop wb-drop--sino" data-wb-drop="sino"><p><b>Pesagem sincronizada</b>App MB Curral · Lote 14 · há 12 min</p><p><b>Diagnóstico de gestação</b>351 registros importados · hoje</p><p><b>Rotina Partos</b>Executada no curral · ontem</p><p><b>Estação de Monta EM 25/26</b>Fim previsto em 31/03/2026</p></div>
            <div class="wb-modal" data-wb-modal></div>
            <aside class="wb-ajuda" data-wb-ajuda><header>? Ajuda<button type="button" data-wb="fajuda" aria-label="Fechar">×</button></header><div class="wb-ajc"></div></aside>
            <div class="wb-toast" data-wb-toast></div>
          </div>
        </div>
        <div class="wb-nav">
          <button class="ms-nav" type="button" style="top:2%;width:5.2%;height:6.2%;left:84%;--d:.2s" onclick="goToSlide({sub})" aria-label="Voltar" title="Voltar">
            <svg viewBox="0 0 24 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 3 3 7l4 4M3 7h12.5a4.5 4.5 0 0 1 0 9H12"/></svg>
          </button>
          <button class="ms-nav" type="button" style="top:2%;width:5.2%;height:6.2%;left:90.3%;--d:.26s" onclick="goToSlide(2)" aria-label="Menu" title="Menu">
            <svg viewBox="0 0 24 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="10" r="8.2"/><path d="M8.8 6.9h6.4M8.8 10h6.4M8.8 13.1h6.4"/></svg>
          </button>
        </div>
      </section>

'''
