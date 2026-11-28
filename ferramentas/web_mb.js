    /* ---- Sistema Web MultBovinos (slide 125): réplica navegável dos dashboards (dados fictícios) ---- */
    (function(){
      const sec = document.querySelector('.slide.wb'); if(!sec) return;
      const tela = sec.querySelector('.wb-tela'), corpo = sec.querySelector('[data-wb-corpo]');
      const $ = s => tela.querySelector(s), $$ = s => [...tela.querySelectorAll(s)];
      const IC = {
        ref: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12a8 8 0 0 1-14.3 4.9M4 12A8 8 0 0 1 18.3 7.1"/><path d="M19 3v4.5h-4.5M5 21v-4.5h4.5"/></svg>',
        fil: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 4h18l-7 8.5V20l-4-2v-5.5z"/></svg>',
        men: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>',
        zoom: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5M8 10.5h5M10.5 8v5"/></svg>',
        dl: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11 3h2v9l3-3 1.4 1.4L12 15.8 6.6 10.4 8 9l3 3zM4 18h16v3H4z"/></svg>',
        gear: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m19.4 13 1.9 1.5-2 3.4-2.3-.9a7 7 0 0 1-1.8 1l-.4 2.5h-4l-.4-2.5a7 7 0 0 1-1.8-1l-2.3.9-2-3.4L6.2 13a7 7 0 0 1 0-2L4.3 9.5l2-3.4 2.3.9a7 7 0 0 1 1.8-1L10.8 3.5h4l.4 2.5a7 7 0 0 1 1.8 1l2.3-.9 2 3.4-1.9 1.5a7 7 0 0 1 0 2zM12.8 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/></svg>',
        fim: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 5l9 7-9 7zM13 5l7 7-7 7zM20 5h2v14h-2z"/></svg>',
        lupa: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/></svg>',
        cal: '<svg viewBox="0 0 24 24" fill="none" stroke="#4da556" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="1"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'
      };
      const I = k => '<button type="button" class="wb-i" data-wb="ajuda" data-aj="' + (k || '') + '" aria-label="Ajuda">i</button>';
      const n0 = v => String(Math.round(v));
      const nm = v => Math.round(v).toLocaleString('pt-BR');
      const p2 = v => v.toFixed(2);
      const pc = v => v.toFixed(2).replace('.', ',');

      /* ---------------- dados fictícios ---------------- */
      const FAZ = [
        {n: 'FAZENDA BOA FORTUNA', rs: 'AGROPECUÁRIA BOA FORTUNA', doc: '- / 30412875 / -', dono: 'Carlos Brandão', k: 1},
        {n: 'FAZENDA GADO MANSO', rs: '', doc: '7310452209185 / - / -', dono: 'Carlos Brandão', k: .62},
        {n: 'FAZENDA SANTA LUZIA', rs: 'SANTA LUZIA PECUÁRIA', doc: '- / 58219034 / 21.478.903/0001-55', dono: 'Agropecuária Modelo Ltda', k: 1.38},
        {n: 'FAZENDA RIO VERDE', rs: 'RIO VERDE AGROPASTORIL', doc: '- / 47120956 / -', dono: 'Agropecuária Modelo Ltda', k: .85},
        {n: 'FAZENDA TRÊS BARRAS', rs: '', doc: '- / - / -', dono: 'Rafael Moura', k: .47}];
      const EMS = {'EM 25/26': {per: 'De 01/10/2025 até 31/03/2026', dgf: '(De 01/10/2025 Até 31/03/2026)', f: 1}, 'EM 24/25': {per: 'De 01/10/2024 até 31/03/2025', dgf: '(De 01/10/2024 Até 31/03/2025)', f: .93},
                   'EM 23/24': {per: 'De 01/10/2023 até 31/03/2024', dgf: '(De 01/10/2023 Até 31/03/2024)', f: .88}};
      const st = {faz: 0, escopo: 'esta', aba: 'reprodutivo', pag: 'dash', em: 'EM 25/26', fil: {}, carregando: false, boxCarregando: ''};
      const K = () => (st.escopo === 'todas' ? FAZ.reduce((a, f) => a + f.k, 0) : FAZ[st.faz].k) * (EMS[st.em].f);
      const KF = box => { const f = st.fil[box] || {}; return (f.raca && f.raca !== 'Todas' ? .78 : 1) * (f.mult || 1); };
      const TOUROS = ['SERRA ALTA 0870', 'VALE VERDE 1145', 'RIO CLARO 0932', 'BOA VISTA 1201', 'MONTE ALEGRE 0788'];
      const LOTES = ['LOTE EM 25/26 - 01', 'LOTE EM 25/26 - 02', 'LOTE EM 25/26 - 03', 'LOTE REPASSE 01'];
      const PASTOS = ['PASTO A', 'PASTO B', 'PASTO MORRO', 'RETIRO SÃO JOÃO', 'MÓDULO A1', 'BEIRA RIO'];

      /* ---------------- moldura dos boxes ---------------- */
      const ferr = (box, dias, tools) => '<div class="wb-ferr">' + (dias ? '<span>' + dias + '</span>' : '') + tools.map(t => '<button type="button" data-wb="' + t + '" data-box="' + box + '" title="' + ({ref: 'Atualizar', fil: 'Filtro', men: 'Opções', zoom: 'Detalhar', dl: 'Exportar', gear: 'Configurar', fim: 'Avançar'})[t] + '">' + IC[t] + '</button>').join('') + '</div>';
      const box = (key, cls, titulo, sub, dias, tools, conteudo, aj) => '<div class="wb-box ' + cls + '" data-box="' + key + '">' + ferr(key, dias, tools)
        + '<h4>' + titulo + (aj === false ? '' : ' ' + I(aj || key)) + '</h4><p class="wb-sub">' + (sub || '&nbsp;') + '</p>'
        + (st.carregando || st.boxCarregando === key ? '<div class="wb-car"><i></i><i></i><i></i></div>' : conteudo) + '</div>';
      const lk = (txt, drill, seta, val) => '<button type="button" class="wb-lk' + (seta ? ' wb-seta' : '') + '" data-wb="' + (seta ? 'pop' : 'lista') + '" data-drill="' + drill + '"' + (val != null ? ' data-n="' + val + '"' : '') + '>' + txt + '</button>';
      const it = (txt, drill, seta, aj, val) => '<span class="wb-it">' + lk(txt, drill, seta, val) + (aj === false ? '' : I(aj || drill)) + '</span>';
      const c = (v, t) => '<span class="wb-c' + (t ? ' wb-c--' + t : '') + '">' + v + '</span>';

      /* ---------------- dashboard Reprodutivo ---------------- */
      const D = () => { const k = K() * KF('resumo'); const r = x => Math.round(x * k);
        const fem = r(412), ins = r(468), pren = r(301), diag = Math.max(1, Math.round(pren / .8575));
        return {k, fem, ins, pren, diag, tx: 100 * pren / Math.max(1, Math.round(fem * .9998 - r(37) + 0)), conc: 100 * pren / Math.max(1, ins), semres: r(37), perdas: r(9)}; };
      const bxResumo = () => { const d = D(), k = d.k, em = EMS[st.em];
        const L = [['Fêmeas Inseminadas', 'femeas', 1, nm(6480 * k).replace(/\./g, ''), d.fem], ['Nº de Inseminações', 'insem', 0, n0(7520 * k), d.ins], ['Fêmeas Prenhez', 'prenhez', 1, n0(5930 * k), d.pren],
          ['Taxa de Prenhez', 'taxaprenhez', 1, '85%', p2(Math.min(99.9, 100 * d.pren / Math.max(1, d.fem - d.semres))) + '%'], ['Taxa de Concepção IA Média', 'concepcao', 0, '45%', p2(Math.min(99.9, d.conc + 6)) + '%'],
          ['Sem Resultados', 'semres', 0, '', d.semres], ['Perdas Gestacionais', 'perdas', 0, '10%', d.perdas]];
        return box('resumo', '', 'Estação Monta', em.per, '16 d', ['ref', 'fil', 'men'],
          '<table class="wb-tab"><thead><tr><th>Itens</th><th style="width:20%">Previsão</th><th style="width:20%">Realizado</th></tr></thead><tbody>'
          + L.map((l, i) => '<tr><td>' + it(l[0], l[1], l[2], l[1], l[4]) + '</td><td>' + (l[3] ? c(l[3], i === 6 ? 'a' : 'p') : '') + '</td><td>' + c(l[4], i === 6 ? 'A' : i >= 3 && i <= 4 ? 'v2' : '') + '</td></tr>').join('')
          + '</tbody></table><div class="wb-botoes"><button type="button" class="wb-pill" data-wb="prenhez60">Prenhez 60 Dias</button><button type="button" class="wb-pill" data-wb="pagina" data-pg="resumoEM">Resumo Estação de Monta</button></div>', false); };
      const bxAptas = () => { const k = K() * KF('aptas'), ins = Math.round(5912 * k), ains = Math.round(214 * k), tot = Math.round(5730 * k), p = (ins + ains) / Math.max(1, tot);
        const ang = Math.PI * (1 - Math.min(p, 1)), cx = 100, cy = 104, px = cx + 74 * Math.cos(ang), py = cy - 74 * Math.sin(ang);
        const arc = (a1, a2, cor) => { const P = a => [cx + 80 * Math.cos(Math.PI * (1 - a)), cy - 80 * Math.sin(Math.PI * (1 - a))], Q = a => [cx + 40 * Math.cos(Math.PI * (1 - a)), cy - 40 * Math.sin(Math.PI * (1 - a))];
          const [x1, y1] = P(a1), [x2, y2] = P(a2), [x3, y3] = Q(a2), [x4, y4] = Q(a1); return '<path d="M' + x1 + ' ' + y1 + 'A80 80 0 0 1 ' + x2 + ' ' + y2 + 'L' + x3 + ' ' + y3 + 'A40 40 0 0 0 ' + x4 + ' ' + y4 + 'Z" fill="' + cor + '"/>'; };
        const tick = a => { const x1 = cx + 82 * Math.cos(Math.PI * (1 - a)), y1 = cy - 82 * Math.sin(Math.PI * (1 - a)), x2 = cx + 72 * Math.cos(Math.PI * (1 - a)), y2 = cy - 72 * Math.sin(Math.PI * (1 - a)); return '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="#2f6b5c" stroke-width="1.4"/>'; };
        const g = '<svg class="wb-gauge" viewBox="0 -14 200 150">' + arc(0, .25, '#4bf9dd') + arc(.25, .75, '#20dbbe') + arc(.75, 1, '#0fbc9e') + [0, .25, .5, .75, 1].map(tick).join('')
          + '<text x="100" y="-4" text-anchor="middle" font-size="8.5" fill="#333">50%</text><text x="34" y="34" text-anchor="middle" font-size="8.5" fill="#333">25%</text><text x="166" y="34" text-anchor="middle" font-size="8.5" fill="#333">75%</text>'
          + '<text x="8" y="107" font-size="8.5" fill="#333">0%</text><text x="176" y="107" font-size="8.5" fill="#333">100%</text>'
          + '<polygon points="' + (cx + 3 * Math.sin(ang)) + ',' + (cy + 3 * Math.cos(ang)) + ' ' + (cx - 3 * Math.sin(ang)) + ',' + (cy - 3 * Math.cos(ang)) + ' ' + px + ',' + py + '" fill="#1f5f55"/><circle cx="' + cx + '" cy="' + cy + '" r="3.2" fill="#4bf9dd" stroke="#1f5f55" stroke-width="1.5"/>'
          + '<text x="100" y="130" text-anchor="middle" font-size="9.5" font-weight="700" fill="#222">' + p2(100 * p) + ' %</text></svg>';
        return box('aptas', '', 'Aptas', '', '1253 d', ['ref', 'fil', 'zoom'], g + '<div class="wb-aptas"><div>' + lk('Inseminadas', 'femeas', 0, ins) + '<b>' + nm(ins) + '</b></div><div>' + lk('A Inseminar', 'ainseminar', 0, ains) + '<b>' + nm(ains) + '</b></div><div>Total de Aptas<b>' + nm(tot) + '</b></div></div>'); };
      const bxDias = () => { const k = K(); const G = [['Fêmeas Descanso', 'descanso', 37, 812, 'Nº de Fêmeas Descanso'], ['Descanso > 40 dias', 'descanso40', 8, 2604, 'Nº de Fêmeas Descanso > 40 dias'], ['Dg > 30 dias', 'dg30', 3, 1098, 'Nº de Diagnósticos > 30 dias']];
        return box('dias', '', 'Dias Perdidos', '', '1253 d', ['ref'], '<table class="wb-tab"><thead><tr><th>Itens</th><th style="width:22%">Quantidade</th></tr></thead></table><div class="wb-dias">'
          + G.map(g => '<div class="wb-g">' + lk(g[0], g[1], 0, Math.round(g[3] * k)) + '</div><div class="wb-s">Média de Dias Perdidos por Vacas</div>' + c(g[2]) + '<div class="wb-s">' + g[4] + '</div>' + c(Math.round(g[3] * k), 'v')).join('') + '</div>'); };
      const linhasIA = () => { const k = K() * KF('ia'); const B = [[412, 0, 61, 351, 301, 2, 3, 48, 364, 4, 297, 297, 4], [56, 0, 9, 47, 38, 0, 1, 7, 49, 1, 37, 37, 1], [11, 0, 2, 9, 7, 0, 0, 2, 9, 0, 7, 7, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]];
        return B.map(r => r.map(x => Math.round(x * k))); };
      const bxIA = () => { const em = EMS[st.em], L = linhasIA(), T = L[0].map((_, j) => L.reduce((a, r) => a + r[j], 0));
        const td = (v, d, seta, txt) => '<td>' + lk(txt != null ? txt : v, d, seta, v) + '</td>';
        const row = (r, nome, tot) => { const tx = r[3] ? p2(100 * r[4] / r[3]) : '0.00', ci = r[8] ? p2(100 * r[10] / r[8]) : '0.00', gt = r[0] ? p2(100 * r[11] / r[0]) : '0.00';
          if(tot) return '<tr class="wb-total"><td>TOTAL</td><td>' + r[0] + '</td><td>' + r[1] + '</td><td>' + r[2] + '</td><td>' + r[3] + '</td><td>' + r[4] + '</td><td>' + tx + '</td><td>' + r[5] + '</td><td>' + r[6] + '</td><td>' + r[7] + '</td><td>' + r[8] + '</td><td>' + r[9] + ' (' + (r[11] ? p2(100 * r[9] / r[11]).replace(/\.?0+$/, '') : 0) + '%)</td><td>' + r[10] + ' (' + ci + ')</td><td>' + r[11] + ' (' + gt + ')</td><td>' + r[12] + '</td></tr>';
          return '<tr><td>' + nome + '</td>' + td(r[0], 'insem', 1) + td(r[1], 'perdas') + td(r[2], 'semres') + td(r[3], 'diag', 1) + td(r[4], 'prenhez', 1) + '<td>' + tx + '</td>' + td(r[5], 'descarte', 1) + td(r[6], 'perdas', 1)
            + td(r[7], 'semres') + td(r[8], 'diag', 1) + td(r[9], 'perdasdg', 1, r[9] + ' (' + (r[11] ? (100 * r[9] / r[11]).toFixed(0) : 0) + '%)') + td(r[10], 'conceppop', 1, r[10] + ' (' + ci + ')') + td(r[11], 'prenhez', 1, r[11] + ' (' + gt + ')') + td(r[12], 'perdas', 1) + '</tr>'; };
        return box('ia', 'wb-box--2', 'Estação Monta', em.per, '16 d', ['ref', 'fil', 'zoom'],
          '<table class="wb-tab wb-tab--grade"><thead><tr><th rowspan="2" style="text-align:center">Serviços<br>' + I('servicos') + '</th><th rowspan="2">Insem ' + I('insem') + '</th><th rowspan="2">Perdas<br>' + I('perdas') + '</th><th colspan="6">DG Inicial ' + I('dgini') + '</th><th colspan="5">DG Final<br><span style="font-weight:400">' + em.dgf + '</span> ' + I('dgfim') + '</th><th rowspan="2">Perdas<br>Final ' + I('perdas') + '</th></tr>'
          + '<tr class="wb-sub2"><th>S/DG</th><th>Diag</th><th>Gest</th><th>Tx Concep</th><th>Descarte</th><th>Perdas</th><th>S/DG</th><th>Diag</th><th>Perdas</th><th>Concep IA</th><th>Gest Total</th></tr></thead><tbody>'
          + L.map((r, i) => row(r, (i + 1) + ' ª IA')).join('') + row(T, '', 1) + '</tbody></table>', 'estacao'); };
      const bxPartos = () => { const k = K() * KF('partos'), P = Math.round(3874 * k), N = Math.round(3921 * k), Pe = Math.round(702 * k), M = Math.round(21 * k);
        const L = [['Partos', 'partospop', 1, P, ''], ['Bezerros Nascidos', 'nascidospop', 1, N, '100,00'], ['Bezerros a Nascer', 'anascer', 0, 0, '0,00'], ['Previsão Total Nascimentos', 'nascidos', 0, N, ''], ['Perdas Gestacionais', 'perdas', 0, Pe, pc(100 * Pe / Math.max(1, P + Pe))], ['Morte de Gestante', 'morte', 0, M, pc(100 * M / Math.max(1, P))]];
        return box('partos', '', 'Partos', 'De 08/2024 até 05/2025 ' + I('partosper'), '1253 d', ['ref', 'fil', 'zoom'],
          '<table class="wb-tab"><thead><tr><th>Itens</th><th style="width:22%">Quantidade</th><th style="width:22%">%</th></tr></thead><tbody>'
          + L.map((l, i) => '<tr><td>' + it(l[0], l[1], l[2], l[1], l[3]) + '</td><td>' + c(l[3], i > 3 ? 'a' : '') + '</td><td>' + (l[4] ? c(l[4], i > 3 ? 'a' : '') : '') + '</td></tr>').join('')
          + '</tbody></table><div class="wb-botoes"><button type="button" class="wb-pill" data-wb="lista" data-drill="aparir" data-n="' + Math.round(64 * k) + '">Fêmeas a Parir</button></div>', false); };
      const ESTQ = [['Novilha precoce', [0, 0, 0, 0, 0, 0]], ['Novilha', [2286, 1391, 1046, 522, 162, 2871]], ['Primípara', [131, 7, 41, 4, 9, 2]], ['Secundípara', [64, 2, 18, 1, 3, 0]], ['Multípara', [212, 9, 77, 5, 14, 3]]];
      const bxEstoque = () => { const k = K() * KF('estoque'), rows = ESTQ.map(([n, v]) => [n, v.map(x => Math.round(x * k))]);
        const linha = (n, v, tot) => { const t = [v[0] + v[2] + v[4], v[1] + v[3] + v[5]], cel = x => tot ? '<td>' + lk(x, 'estoque', 0, x) + '</td>' : '<td>' + lk(x, 'estoque', 0, x) + '</td>';
          return '<tr' + (tot ? ' class="wb-total"' : '') + '><td>' + n + (tot ? '' : ' ' + I('categoria')) + '</td>' + [v[0], v[1], v[0] + v[1], v[2], v[3], v[2] + v[3], v[4], v[5], v[4] + v[5], t[0], t[1], t[0] + t[1]].map(cel).join('') + '</tr>'; };
        const T = [0, 1, 2, 3, 4, 5].map(j => rows.reduce((a, r) => a + r[1][j], 0));
        return box('estoque', 'wb-box--2', 'Estoque Atual de Reprodutores', '', '297 d', ['ref', 'fil', 'zoom'],
          '<table class="wb-tab wb-tab--linhas"><thead><tr><th rowspan="2" style="vertical-align:bottom">Total</th><th colspan="3">Prenha ' + I('prenha') + '</th><th colspan="3">Servida ' + I('servida') + '</th><th colspan="3">Vazia ' + I('vazia') + '</th><th colspan="3">Total</th></tr>'
          + '<tr class="wb-sub2"><th>Parida ' + I('parida') + '</th><th>Solteira ' + I('solteira') + '</th><th>Total</th><th>Parida ' + I('parida') + '</th><th>Solteira ' + I('solteira') + '</th><th>Total</th><th>Parida ' + I('parida') + '</th><th>Solteira ' + I('solteira') + '</th><th>Total</th><th>Parida</th><th>Solteira</th><th>Total geral</th></tr></thead><tbody>'
          + rows.map(r => linha(r[0], r[1])).join('') + linha('Total', T, 1) + '</tbody></table>'); };
      const bxDescarte = () => { const k = K(), L = [['0 a 3 Meses', 4, 6, 431.5], ['4 a 6 Meses', 2, 3, 452.2], ['7 a 9 Meses', 0, 0, 0], ['10 a 12 Meses', 0, 1, 468], ['Acima de 12 Meses', 34, 39, 968.4]].map(l => [l[0], Math.round(l[1] * k), Math.round(l[2] * k), l[3]]);
        const tp = L.reduce((a, l) => a + l[1], 0), ts = L.reduce((a, l) => a + l[2], 0);
        return box('descarte', '', 'Estoque de Descartadas', 'Hoje', '752 d', ['ref'], '<table class="wb-tab wb-tab--linhas"><thead><tr><th>Tempo Pós Descarte</th><th>Paridas</th><th>Solteiras</th><th>Total</th><th>Peso médio (Kg) ' + I('pesomedio') + '</th></tr></thead><tbody>'
          + L.map(l => '<tr><td>' + lk(l[0], 'descarte', 0, l[1] + l[2]) + '</td><td>' + l[1] + '</td><td>' + l[2] + '</td><td>' + (l[1] + l[2]) + '</td><td>' + pc(l[1] + l[2] ? l[3] : 0) + '</td></tr>').join('')
          + '<tr class="wb-total"><td>' + lk('Total', 'descarte', 0, tp + ts) + '</td><td>' + tp + '</td><td>' + ts + '</td><td>' + (tp + ts) + '</td><td>' + pc(921.36) + '</td></tr></tbody></table>'); };
      const bxDesmame = () => { const k = K() * KF('desmame'), m = Math.round(18 * k), f = Math.round(131 * k), mm = Math.round(2 * k), mf = Math.round(1 * k);
        const L = [['Bezerros Desmamados', 'desmamepop', 1, m, f, m + f, ''], ['Bezerros a Desmamar', 'adesmamar', 0, 0, 0, 0, ''], ['Previsão Total', '', 0, m, f, m + f, 'n'], ['Idade Média', 'desmame', 0, 7, 7, 7, ''], ['Peso médio', 'desmame', 0, '198.40', '186.20', '187.67', ''], ['Ganho de Peso Diário', 'desmame', 0, '0.712', '0.668', '0.673', ''], ['Mortes na Maternidade', 'morte', 0, mm, mf, mm + mf, 'a']];
        return box('desmame', '', 'Desmame', 'De 02/2025 até 10/2025 (de 08/2024 até 01/2025) ' + I('desmameper'), '235 d', ['ref', 'fil', 'men', 'zoom'],
          '<table class="wb-tab"><thead><tr><th>Itens</th><th style="width:20%">Macho</th><th style="width:20%">Fêmea</th><th style="width:20%">Total</th></tr></thead><tbody>'
          + L.map(l => '<tr><td>' + (l[1] ? it(l[0], l[1], l[2], l[1], l[5]) : '<span class="wb-it">' + l[0] + ' ' + I('previsao') + '</span>') + '</td><td>' + c(l[3], l[6] === 'a' ? 'a' : 'b') + '</td><td>' + c(l[4], l[6] === 'a' ? 'a' : 'b') + '</td><td>' + c(l[5], l[6] === 'a' ? 'A' : '') + '</td></tr>').join('') + '</tbody></table>', false); };
      const bxMonit = () => { const k = K(); const L = [['Coberturas sem Comunicação', 'cobpop', Math.round(31 * k)], ['Nascimentos Realizados sem Comunicação', 'nascpop', 0], ['Registros Pendentes', 'regpop', Math.round(2 * k)]];
        return box('monit', '', 'Monitoramento de Registros de Animais', 'Hoje', '235 d', ['ref'], '<table class="wb-tab"><thead><tr><th>Itens</th><th style="width:22%">Quantidade</th></tr></thead><tbody>'
          + L.map(l => '<tr><td>' + it(l[0], l[1], 1, l[1], l[2]) + '</td><td>' + c(l[2]) + '</td></tr>').join('') + '</tbody></table>'); };
      const bxAtiv = () => { const f = st.fil.ativ || {}, k = K() * (f.mult || 1), per = f.per || 'De 07/03/2025 até 28/11/2026';
        const L = [['Entrada de animais', 5102], ['Entrada em Lote EM', 44], ['Aplicação de Protocolo', 51], ['Score', 21], ['Inseminação Artificial', 412], ['Repasse', 6], ['Diagnóstico de gestação', 351]];
        return box('ativ', '', 'Resumo de Atividades', per, '235 d', ['ref', 'fil'], '<table class="wb-tab"><thead><tr><th>Itens</th><th style="width:22%">Quantidade</th></tr></thead><tbody>'
          + L.map(l => '<tr><td><span class="wb-it">' + l[0] + ' ' + I('ativ') + '</span></td><td>' + c(Math.round(l[1] * k)) + '</td></tr>').join('') + '</tbody></table>'); };

      /* ---------------- dashboard Produção ---------------- */
      const bxPEst = () => { const k = K(), ini = Math.round(13820 * k), e = Math.round(126 * k), s = Math.round(88 * k), m = Math.round(3 * k);
        return box('pest', '', 'Estoque de Animais', 'De 28/10/2026 até 28/11/2026', '70 d', ['ref', 'fil', 'men', 'zoom'],
          '<table class="wb-tab"><thead><tr><th>Itens</th><th style="width:22%">Quantidade</th></tr></thead><tbody>'
          + [['Inicial', 'estoque', 0, ini], ['Entrada', 'entradapop', 1, e], ['Saídas', 'saidapop', 1, s], ['Mortes', 'morte', 0, m]].map(l => '<tr><td>' + lk(l[0], l[1], l[2], l[3]) + '</td><td>' + c(l[3]) + '</td></tr>').join('')
          + '<tr class="wb-total"><td>Saldo</td><td>' + c(ini + e - s - m, 'v2') + '</td></tr></tbody></table><div class="wb-botoes"><button type="button" class="wb-pill" data-wb="toast" data-msg="Abrindo Demonstrativo de Movimentação de Gado">Demonstrativo de Movimentação de Gado</button></div>'); };
      const bxPLot = () => box('plot', '', 'Taxa de Lotação', '', '', ['ref', 'gear'], '<div class="wb-vazio">Sem dados para exibir</div>');
      const bxPCons = () => { const k = K(), L = [['RETIRO SÃO JOÃO', 94], ['CONFINAMENTO', 241], ['CONFINAMENTO (ANTIGO)', 80], ['CURRAL', 215], ['BEIRA RIO', 27], ['MÓDULO A1', 231]];
        return box('pcons', '', 'Consumo por Retiro Pasto', 'De 17/04/2025 até 28/11/2026', '70 d', ['ref', 'fil', 'dl', 'men'],
          '<table class="wb-tab wb-tab--linhas wb-tab--grade"><thead><tr><th rowspan="2">Setor</th><th rowspan="2">Qtde animais ' + I('qtde') + '</th><th colspan="3">Oferta nutricional</th><th rowspan="2">UA/ha ' + I('uaha') + '</th></tr><tr class="wb-sub2"><th>Qtde (Kg) ' + I('kg') + '</th><th>Cab/dia ' + I('cab') + '</th><th>%Var ' + I('var') + '</th></tr></thead><tbody>'
          + L.map(l => '<tr><td>' + l[0] + '</td><td>' + Math.round(l[1] * k) + '</td><td></td><td></td><td></td><td></td></tr>').join('') + '</tbody></table>'); };
      const FAIXAS = [['Até 180', 1, 54, 304.2], ['180 a 270', 324, 880, 9605.5], ['270 a 360', 1431, 1161, 26440.4], ['360 a 450', 112, 104, 2845.2], ['450 a 540', 5, 1106, 18657.6], ['Acima de 540', 3, 5429, 114489.4]];
      const bxPFaixa = () => { const k = K(), L = FAIXAS.map(f => [f[0], Math.round(f[1] * k), Math.round(f[2] * k), f[3] * k]);
        const T = [1, 2, 3].map(j => L.reduce((a, l) => a + l[j], 0));
        return box('pfaixa', '', 'Estoque por Faixa de Peso', '31/12/2025 - animais de engorda e reprodução', '70 d', ['ref', 'fil', 'zoom'],
          '<table class="wb-tab wb-tab--linhas wb-tab--grade"><thead><tr><th>Faixas de pesos</th><th>Machos</th><th>Fêmeas</th><th>Total</th><th>Peso @ ' + I('arroba') + '</th><th>Valor estoque ' + I('valor') + '</th></tr></thead><tbody>'
          + L.map(l => '<tr><td>' + l[0] + '</td><td>' + l[1] + '</td><td>' + l[2] + '</td><td>' + (l[1] + l[2]) + '</td><td>' + l[3].toLocaleString('pt-BR', {minimumFractionDigits: 1, maximumFractionDigits: 1}) + '</td><td>0,00</td></tr>').join('')
          + '<tr class="wb-total"><td>Total</td><td>' + T[0] + '</td><td>' + T[1] + '</td><td>' + (T[0] + T[1]) + '</td><td>' + T[2].toLocaleString('pt-BR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + '</td><td>0,00</td></tr></tbody></table>'); };
      const bxPFaixaG = () => { const k = K(), L = FAIXAS.map(f => [f[0], Math.round(f[1] * k), Math.round(f[2] * k)]), mx = Math.max(...L.map(l => l[1] + l[2]));
        const W = 600, H = 190, bw = 26; let s = '<svg class="wb-graf" viewBox="0 0 ' + W + ' ' + (H + 40) + '">';
        for(let g = 0; g <= 4; g++){ const y = 10 + (H - 20) * g / 4; s += '<line x1="40" x2="' + (W - 10) + '" y1="' + y + '" y2="' + y + '" stroke="#e6e6e6"/><text x="34" y="' + (y + 3) + '" font-size="9" text-anchor="end" fill="#666">' + Math.round(mx * (1 - g / 4)) + '</text>'; }
        L.forEach((l, i) => { const x = 70 + i * 88, hm = (H - 20) * l[1] / mx, hf = (H - 20) * l[2] / mx;
          s += '<rect x="' + x + '" y="' + (H - 10 - hm) + '" width="' + bw + '" height="' + hm + '" fill="#1b5e20"/><rect x="' + (x + bw + 4) + '" y="' + (H - 10 - hf) + '" width="' + bw + '" height="' + hf + '" fill="#66bb6a"/>'
            + '<text x="' + (x + bw + 2) + '" y="' + (H + 6) + '" font-size="9" text-anchor="middle" fill="#444">' + l[0] + '</text>'; });
        s += '</svg><div class="wb-leg"><span><i style="background:#1b5e20"></i>Machos</span><span><i style="background:#66bb6a"></i>Fêmeas</span></div>';
        return '<div class="wb-box wb-box--2" data-box="pfaixag"><div class="wb-ferr"><button type="button" class="wb-pill" data-wb="toast" data-msg="Abrindo Previsão de vendas" style="color:#333">Previsão de vendas</button><button type="button" data-wb="ref" data-box="pfaixag">' + IC.ref + '</button><button type="button" data-wb="toast" data-msg="Próximo período">' + IC.fim + '</button></div><h4>Estoque por Faixa de Peso ' + I('faixa') + '</h4><p class="wb-sub">&nbsp;</p>'
          + (st.carregando || st.boxCarregando === 'pfaixag' ? '<div class="wb-car"><i></i><i></i><i></i></div>' : s) + '</div>'; };
      const bxPPes = () => { const k = K(), L = [['MB2841', 'Macho', 412.5], ['MB2847', 'Macho', 398.0], ['MB3012', 'Fêmea', 356.5], ['MB3020', 'Fêmea', 341.0], ['MB2903', 'Macho', 427.0]];
        return box('ppes', '', 'Últimas Pesagens', 'Hoje', '', ['ref', 'fil', 'men', 'zoom'], '<table class="wb-tab wb-tab--linhas"><thead><tr><th>ID Usual</th><th>Sexo</th><th>Peso (Kg)</th><th>GMD</th></tr></thead><tbody>'
          + L.slice(0, Math.max(2, Math.round(5 * Math.min(1, k)))).map((l, i) => '<tr><td>' + lk(l[0], 'pesagem', 0, 1) + '</td><td>' + l[1] + '</td><td>' + pc(l[2]) + '</td><td>' + (0.612 + i * .041).toFixed(3) + '</td></tr>').join('') + '</tbody></table>'); };
      const bxPVend = () => { const k = K(), M = [['10/2026', 0, 0, 0, 0, 38, 38, 512.4, .621], ['08/2026', 112, 112, 541.2, .702, 24, 24, 468.0, .588], ['05/2026', 64, 64, 528.7, .689, 0, 0, 0, 0], ['03/2026', 0, 0, 0, 0, 2, 0, 0, 0], ['01/2026', 0, 0, 0, 0, 104, 104, 144.2, -.096]];
        return box('pvend', 'wb-box--2', 'Vendas (Mês a Mês)', 'De 01/01/2026 até 31/12/2026', '70 d', ['ref', 'fil', 'zoom', 'men'],
          '<table class="wb-tab wb-tab--linhas wb-tab--grade"><thead><tr><th rowspan="2">Meses</th><th colspan="4">Machos</th><th colspan="4">Fêmeas</th><th colspan="4">Total</th></tr><tr class="wb-sub2">'
          + [0, 1, 2].map(() => '<th>Quantidade</th><th>Com peso</th><th>Peso médio ' + I('pm') + '</th><th>GMD ' + I('gmd') + '</th>').join('') + '</tr></thead><tbody>'
          + M.map(m => { const mq = Math.round(m[1] * k), mc = Math.round(m[2] * k), fq = Math.round(m[5] * k), fc = Math.round(m[6] * k);
            return '<tr><td>' + m[0] + '</td><td>' + lk(mq, 'venda', 0, mq) + '</td><td>' + lk(mc, 'venda', 0, mc) + '</td><td>' + pc(m[3]) + '</td><td>' + m[4].toFixed(4).replace('.', ',') + '</td><td>' + lk(fq, 'venda', 0, fq) + '</td><td>' + lk(fc, 'venda', 0, fc) + '</td><td>' + pc(m[7]) + '</td><td>' + m[8].toFixed(4).replace('.', ',') + '</td><td>' + lk(mq + fq, 'venda', 0, mq + fq) + '</td><td>' + lk(mc + fc, 'venda', 0, mc + fc) + '</td><td>' + pc(mq + fq ? (m[3] * mq + m[7] * fq) / (mq + fq) : 0) + '</td><td>' + ((m[4] + m[8]) / 2).toFixed(4).replace('.', ',') + '</td></tr>'; }).join('') + '</tbody></table>'); };

      /* ---------------- páginas internas ---------------- */
      const pgResumoEM = () => '<span class="wb-form-aba">Informações Gerais</span><div class="wb-form">'
        + '<label>Estação de Monta * ' + I('estacao') + '</label><div class="wb-campo" style="justify-content:space-between">' + st.em.replace('EM ', 'EM - ').replace('/', '/') + '<span>▾</span></div>'
        + '<label>Propriedades *</label><div class="wb-campo wb-campo--alto"><span class="wb-tag">' + FAZ[st.faz].n + ' ×</span></div>'
        + '<label>Lote Estação de Monta IA (Atual) ' + I('lote') + '</label><div class="wb-campo" style="justify-content:flex-end">▾</div>'
        + '<label>Raça Matriz</label><div class="wb-campo"></div><label>Raça Touro</label><div class="wb-campo"></div><label>Inseminador</label><div class="wb-campo"></div>'
        + '<label>Layout ' + I('layout') + '</label><div class="wb-radios" data-grupo="layout"><button type="button" class="is-sel" data-wb="radio"><i></i>Sem o Lote IA</button><button type="button" data-wb="radio"><i></i>Com o Lote IA</button><button type="button" data-wb="radio"><i></i>Somente o Lote IA</button></div>'
        + '<label style="display:flex;align-items:center;gap:.5cqw;margin-top:1cqw"><input type="checkbox" checked style="accent-color:#2e7d32;width:.8cqw;height:.8cqw"> Exibir legendas ' + I('legendas') + '</label><hr style="border:0;border-top:1px solid #e6e6e6;margin:1cqw 0">'
        + '<label>Formato do envio do relatório ' + I('formato') + '</label><div class="wb-radios"><button type="button" class="is-sel"><i></i>Arquivo PDF</button></div>'
        + '<button type="button" class="wb-gerar" data-wb="toast" data-msg="Relatório «Resumo Estação de Monta» enviado para processamento (PDF)">Gerar Relatório</button></div>';
      const graf = (titulo, series, cats, cores, alto) => { const W = 900, H = alto || 210, mx = Math.max(1, ...series.flatMap(s => s.v)), gw = (W - 70) / cats.length, bw = Math.min(30, (gw - 16) / series.length);
        let s = '<svg class="wb-graf" viewBox="0 0 ' + W + ' ' + (H + 34) + '">';
        for(let g = 0; g <= 4; g++){ const y = 12 + (H - 24) * g / 4; s += '<line x1="50" x2="' + (W - 10) + '" y1="' + y + '" y2="' + y + '" stroke="#e6e6e6"/><text x="44" y="' + (y + 3) + '" font-size="10" text-anchor="end" fill="#666">' + Math.round(mx * (1 - g / 4)) + '</text>'; }
        cats.forEach((cat, i) => { const x0 = 60 + i * gw + (gw - bw * series.length) / 2;
          series.forEach((se, j) => { const v = se.v[i], h = (H - 24) * v / mx; s += '<rect x="' + (x0 + j * bw) + '" y="' + (H - 12 - h) + '" width="' + (bw - 3) + '" height="' + h + '" fill="' + cores[j] + '"/>' + (v ? '<text x="' + (x0 + j * bw + bw / 2 - 1.5) + '" y="' + (H - 15 - h) + '" font-size="9" text-anchor="middle" fill="#333">' + v + '</text>' : ''); });
          s += '<text x="' + (60 + i * gw + gw / 2) + '" y="' + (H + 6) + '" font-size="10" text-anchor="middle" fill="#444">' + cat + '</text>'; });
        return s + '</svg><div class="wb-leg">' + series.map((se, j) => '<span><i style="background:' + cores[j] + '"></i>' + se.n + '</span>').join('') + '</div>'; };
      const pgPartos = () => { const k = K(), meses = ['08/2024', '09/2024', '10/2024', '11/2024', '12/2024', '01/2025', '02/2025', '03/2025', '04/2025', '05/2025'], r = a => a.map(x => Math.round(x * k));
        const prev = r([42, 186, 512, 921, 1104, 688, 312, 96, 41, 19]), real = r([38, 179, 498, 902, 1089, 671, 301, 88, 38, 17]);
        const racas = ['NELORE', 'ANGUS', 'BRANGUS', 'TABAPUÃ', 'SENEPOL'], pr = r([2410, 612, 498, 288, 113]), rr = r([2366, 598, 487, 279, 107]);
        const cx = t => '<div class="wb-caixa" style="margin-bottom:1.2cqw"><div class="wb-ferr"><button type="button" data-wb="toast" data-msg="Atualizado">' + IC.ref + '</button><button type="button" data-wb="toast" data-msg="Filtro aplicado">' + IC.fil + '</button></div>' + t + '</div>';
        return cx('<h5>Nascimentos - Previstos e Realizados ' + I('partos') + '</h5>' + graf('', [{n: 'Previstos', v: prev}, {n: 'Realizados', v: real}], meses, ['#a5d6a7', '#1b5e20']))
          + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.2cqw">' + cx('<h5>Partos Previstos por Raça ' + I('partos') + '</h5>' + graf('', [{n: 'Previstos', v: pr}], racas, ['#66bb6a'], 180))
          + cx('<h5>Partos Realizados por Raça ' + I('partos') + '</h5>' + graf('', [{n: 'Realizados', v: rr}], racas, ['#2e7d32'], 180)) + '</div>'
          + cx('<h5>Resultado da Parição ' + I('partos') + '</h5><table class="wb-tab wb-tab--linhas wb-tab--grade"><thead><tr><th>Categoria</th><th>Prenhes</th><th>Partos</th><th>Perdas</th><th>Taxa de Parição</th><th>Machos</th><th>Fêmeas</th></tr></thead><tbody>'
            + [['Novilha', 1180, 1094], ['Primípara', 932, 871], ['Secundípara', 598, 561], ['Multípara', 1366, 1348]].map(l => { const a = Math.round(l[1] * k), b = Math.round(l[2] * k); return '<tr><td>' + l[0] + '</td><td>' + a + '</td><td>' + b + '</td><td>' + (a - b) + '</td><td>' + pc(100 * b / Math.max(1, a)) + '%</td><td>' + Math.round(b * .51) + '</td><td>' + (b - Math.round(b * .51)) + '</td></tr>'; }).join('') + '</tbody></table>'); };

      /* ---------------- render ---------------- */
      const ABAS_DASH = {reprodutivo: () => bxResumo() + bxAptas() + bxDias() + bxIA() + bxPartos() + bxEstoque() + bxDescarte() + bxDesmame() + bxMonit() + bxAtiv(),
                         producao: () => bxPEst() + bxPLot() + bxPCons() + bxPFaixa() + bxPFaixaG() + bxPPes() + bxPVend()};
      const MIG = {resumoEM: 'Resumo Estação de Monta', partos: 'Partos'};
      const render = () => {
        $$('[data-wb-aba]').forEach(b => b.classList.toggle('is-ativa', b.dataset.wbAba === st.aba));
        $$('[data-wb-escopo]').forEach(b => b.classList.toggle('is-ativa', b.dataset.wbEscopo === st.escopo));
        $('[data-wb-faz]').textContent = FAZ[st.faz].n;
        tela.classList.toggle('is-pagina', st.pag !== 'dash');
        if(st.pag !== 'dash'){ $('[data-wb-mig]').textContent = MIG[st.pag];
          corpo.innerHTML = st.carregando ? '<div class="wb-car" style="height:30cqw"><i></i><i></i><i></i></div>' : (st.pag === 'resumoEM' ? pgResumoEM() : pgPartos()); return; }
        const f = ABAS_DASH[st.aba];
        if(!f){ const nome = $('[data-wb-aba="' + st.aba + '"]').textContent;
          corpo.innerHTML = st.carregando ? '<div class="wb-car" style="height:30cqw"><i></i><i></i><i></i></div>' : '<div class="wb-grade">' + ['Indicadores', 'Resumo', 'Movimentação'].map((t, i) => '<div class="wb-box' + (i === 2 ? ' wb-box--3' : '') + '"><div class="wb-ferr">' + IC.ref.replace('<svg', '<svg style="width:.8cqw;height:.8cqw"') + '</div><h4>' + nome + ' — ' + t + '</h4><p class="wb-sub">&nbsp;</p><div class="wb-vazio">Sem dados para exibir</div></div>').join('') + '</div>'; return; }
        corpo.innerHTML = '<div class="wb-grade">' + f() + '</div>';
      };
      const carrega = (fn, alvo) => { fecharTudo(); if(fn) fn(); if(alvo) st.boxCarregando = alvo; else st.carregando = true; render();
        setTimeout(() => { st.carregando = false; st.boxCarregando = ''; render(); }, alvo ? 450 : 650); };

      /* ---------------- popovers, modais, toast ---------------- */
      const toast = msg => { const t = $('[data-wb-toast]'); t.textContent = msg; t.classList.add('is-visivel'); clearTimeout(t._t); t._t = setTimeout(() => t.classList.remove('is-visivel'), 2200); };
      const fecharPops = () => $$('.wb-pop').forEach(p => p.remove());
      const fecharTudo = () => { fecharPops(); $$('.wb-menu, .wb-drop').forEach(x => x.classList.remove('is-aberto')); $$('.wb-top > button').forEach(x => x.classList.remove('is-aberto')); };
      const posPop = (pop, ref, alinha) => { tela.appendChild(pop); const T = tela.getBoundingClientRect(), R = ref.getBoundingClientRect(), w = pop.offsetWidth, h = pop.offsetHeight;
        let x = alinha === 'esq' ? R.left - T.left : R.right - T.left - w, y = R.bottom - T.top + 4;
        x = Math.max(6, Math.min(x, T.width - w - 6)); if(y + h > T.height - 6) y = Math.max(6, R.top - T.top - h - 4);
        pop.style.left = x + 'px'; pop.style.top = y + 'px'; pop.classList.add('is-aberto'); };
      const sel = (nome, ops, v) => '<select data-f="' + nome + '">' + ops.map(o => '<option' + (o === v ? ' selected' : '') + '>' + o + '</option>').join('') + '</select>';
      const dat = (rot, v) => '<div><label>' + rot + '</label><div style="display:flex;align-items:center;gap:.3cqw"><input type="text" value="' + (v || '') + '" style="flex:1">' + IC.cal.replace('<svg', '<svg style="width:.9cqw;height:.9cqw"') + '</div></div>';
      const FILTROS = {
        resumo: f => '<label>Estação de Monta *</label>' + sel('em', Object.keys(EMS), st.em) + '<label>Propriedades</label>' + sel('prop', ['Desta fazenda', 'Todas as fazendas'], st.escopo === 'todas' ? 'Todas as fazendas' : 'Desta fazenda'),
        ia: f => '<label>Estação de Monta *</label>' + sel('em', Object.keys(EMS), st.em) + '<label>Raça</label>' + sel('raca', ['Todas', 'NELORE', 'ANGUS', 'BRANGUS'], f.raca),
        aptas: f => '<label>Dias de descanso pós-parto</label><input type="text" value="' + (f.descanso || 40) + '" data-f="descanso">' + '<label>Estação de Monta</label>' + sel('em', Object.keys(EMS), st.em),
        partos: f => '<div class="wb-duas">' + dat('Período (De)', '08/2024') + dat('Período (Até)', '05/2025') + '</div><label class="wb-ck"><input type="checkbox" checked style="accent-color:#2e7d32"> Considerar Matrizes de Compra</label>',
        estoque: f => '<label>Propriedades</label><input type="text" value="' + FAZ[st.faz].n + '"><label>Raça</label>' + sel('raca', ['Todas', 'NELORE', 'ANGUS', 'BRANGUS'], f.raca) + '<label>Tipo</label>' + sel('tipo', ['Todos', 'Reprodução', 'Receptora', 'Doadora'], f.tipo)
          + '<label>Novilhas com Idade superior a (meses)</label><input type="text" value="16"><div style="font-weight:700;font-size:.72cqw;margin-top:.6cqw">Novilha precoce</div><div class="wb-duas">' + dat('Nascimento (De)') + dat('Nascimento (Até)') + '</div>'
          + '<label class="wb-ck"><input type="checkbox" checked style="accent-color:#2e7d32"> Considerar Matrizes de Compra</label><div class="wb-duas">' + dat('Compra (De)') + dat('Compra (Até)') + '</div>',
        desmame: f => '<div class="wb-duas">' + dat('Desmame (De)', '02/2025') + dat('Desmame (Até)', '10/2025') + '</div>' + '<label>Raça</label>' + sel('raca', ['Todas', 'NELORE', 'ANGUS', 'BRANGUS'], f.raca),
        ativ: f => '<div class="wb-rapido"><button type="button" data-wb="rapido" data-mult=".004" data-per="Hoje">Hoje</button><button type="button" data-wb="rapido" data-mult=".03" data-per="Últimos 7 dias">7 Dias</button><button type="button" data-wb="rapido" data-mult=".11" data-per="Últimos 30 dias">Mês</button></div><div class="wb-duas">' + dat('Período (De)', '07/03/2025') + dat('Período (Até)', '28/11/2026') + '</div>',
        pest: f => '<div class="wb-duas">' + dat('Período (De)', '28/10/2026') + dat('Período (Até)', '28/11/2026') + '</div>', pcons: f => '<div class="wb-duas">' + dat('Período (De)', '17/04/2025') + dat('Período (Até)', '28/11/2026') + '</div>',
        pfaixa: f => '<label>Data</label><input type="text" value="31/12/2025"><label>Tipo</label>' + sel('tipo', ['Engorda e reprodução', 'Engorda', 'Reprodução'], f.tipo), ppes: f => '<div class="wb-duas">' + dat('Período (De)', '28/11/2026') + dat('Período (Até)', '28/11/2026') + '</div>',
        pvend: f => '<div class="wb-duas">' + dat('Período (De)', '01/01/2026') + dat('Período (Até)', '31/12/2026') + '</div>'};
      const abreFiltro = (bt, key) => { fecharPops(); const f = st.fil[key] || {}, pop = document.createElement('div'); pop.className = 'wb-pop wb-pop--filtro'; pop.dataset.box = key;
        pop.innerHTML = '<header>Filtro</header><div class="wb-pc">' + (FILTROS[key] || (() => '<label>Período</label><input type="text" value="Últimos 12 meses">'))(f) + '</div><footer><button type="button" class="wb-bt wb-bt--cheio" data-wb="aplicar">Aplicar</button><button type="button" class="wb-bt" data-wb="limpar">Limpar</button><button type="button" class="wb-bt" data-wb="fpop">Fechar</button></footer>';
        posPop(pop, bt); };
      const MENUS = {resumo: ['Lotes E.M', 'Cronograma IATF', 'Manejo de IATF', 'Planejamento da E.M', 'Estoque Sêmen', 'Resumo Produção', 'Configura E.M. – IA', 'Exportar Dados Reprodutivos (View)', 'Estação Monta MC'],
        desmame: ['Lançamento de Desmame', 'Relatório de Desmame', 'Bezerros por Lote', 'Exportar Desmame (View)'], pest: ['Demonstrativo de Movimentação', 'Estoque por Categoria', 'Estoque por Localidade', 'Exportar Estoque (View)'],
        pcons: ['Consumo por Retiro', 'Oferta Nutricional', 'Configurar Retiros'], ppes: ['Lançar Pesagem', 'Relatório de Pesagens', 'Curva de Crescimento'], pvend: ['Vendas Realizadas', 'Previsão de Vendas', 'Exportar Vendas (View)']};
      const abreMenuBox = (bt, key) => { fecharPops(); const pop = document.createElement('div'); pop.className = 'wb-pop wb-pop--menu';
        pop.innerHTML = (MENUS[key] || ['Exportar']).map(m => '<button type="button" data-wb="toast" data-msg="Abrindo «' + m + '»">' + m + '</button>').join(''); posPop(pop, bt); };
      const POPS = {
        femeas: n => [['IATF', .78], ['IA Convencional', .17], ['Repasse', .05]], prenhez: n => [['Prenhez IA', .86], ['Prenhez Repasse', .14]], taxaprenhez: n => [['Novilhas', .29], ['Primíparas', .23], ['Multíparas', .48]],
        insem: n => [['Novilhas', .31], ['Primíparas', .22], ['Secundíparas', .14], ['Multíparas', .33]], diag: n => [['DG Positivo', .86], ['DG Negativo', .14]], descarte: n => [['Descarte por idade', .5], ['Descarte por falha reprodutiva', .5]],
        perdas: n => [['DG+ | DG-', .4], ['Morte Embrionária', .3], ['Aborto', .2], ['Morte de Gestante', .1]], perdasdg: n => [['DG+ | DG-', .4], ['Morte Embrionária', .3], ['Aborto', .2], ['Morte de Gestante', .1]],
        conceppop: n => [['DG+ | DG-', 0], ['Morte Embrionária', 0], ['Aborto', 0], ['Morte de Gestante', 0]], partospop: n => [['Parto Normal', .93], ['Parto Puxado', .05], ['Cesariana', .02]], nascidospop: n => [['Machos', .51], ['Fêmeas', .49]],
        desmamepop: n => [['Machos', .12], ['Fêmeas', .88]], cobpop: n => [['IA', .84], ['Repasse', .16]], nascpop: n => [['Partos', 1]], regpop: n => [['Cadastros incompletos', .5], ['Pesagens pendentes', .5]],
        entradapop: n => [['Compra', .62], ['Nascimento', .38]], saidapop: n => [['Venda', .9], ['Transferência', .1]]};
      const abreDrillPop = (bt, chave) => { fecharPops(); const n = +bt.dataset.n || 0, L = (POPS[chave] || POPS.insem)(n), pop = document.createElement('div'); pop.className = 'wb-pop wb-pop--drill';
        let resto = n; pop.innerHTML = L.map((l, i) => { const v = i === L.length - 1 ? resto : Math.round(n * l[1]); resto -= v; return '<div>' + lk(l[0], 'lista' + chave, 0, Math.max(0, v)).replace('data-wb="lista"', 'data-wb="lista"') + '<b>' + Math.max(0, v) + '</b></div>'; }).join('');
        posPop(pop, bt, 'esq'); };
      const modal = (cls, html) => { const m = $('[data-wb-modal]'); m.innerHTML = '<div class="wb-dlg ' + cls + '">' + html + '</div>'; m.classList.add('is-aberto'); return m; };
      const fecharModal = () => $('[data-wb-modal]').classList.remove('is-aberto');
      /* listas de animais (drill) */
      const RES = ['GESTANTE', 'VAZIA', 'GESTANTE', 'SERVIDA', 'SERVIDA', 'GESTANTE'], OCO = ['REPASSADA - 03/12/2025', 'DG- DE REPASSE', 'DG+ DE REPASSE', '', '', ''];
      const COLS = {
        insem: ['ID Usual ⇅', 'Raça', 'Tipo', 'Data cobertura ⇅', 'Lote E.M.', 'Touro', 'DG Inicial ⓘ', 'DG Final ⓘ', 'Último DG ⓘ', 'Resultado ⓘ', 'Ocorrência ⓘ'],
        partos: ['Id. usual', 'Raça', 'Data da Cob', 'Tipo Cob', 'Touro', 'Data DG', 'Data Prevista', 'Data Parto', 'Gestação', 'Cria', 'Sexo', 'Peso Nasc', 'Sit no Parto', 'Sit da Cria'],
        descanso: ['ID Usual', 'Raça', 'Ordem', 'Último Parto', 'Dias em Descanso', 'Lote', 'Pasto'],
        estoque: ['ID Usual', 'Raça', 'Categoria', 'Situação', 'Estado', 'Nascimento', 'Pasto'], venda: ['ID Usual', 'Sexo', 'Peso (Kg)', 'Data Venda', 'Destino']};
      const TIPO = d => /parto|nascido|anascer|aparir|morte|nasc/.test(d) ? 'partos' : /descanso|dg30|ainseminar/.test(d) ? 'descanso' : /estoque|descarte|pesagem/.test(d) ? 'estoque' : /venda/.test(d) ? 'venda' : 'insem';
      const TITULOS = {femeas: 'Inseminações', insem: 'Inseminações', prenhez: 'Fêmeas Prenhes', semres: 'Sem Resultados', perdas: 'Perdas Gestacionais', descanso: 'Fêmeas Descanso', descanso40: 'Descanso > 40 dias', dg30: 'Diagnósticos > 30 dias',
        ainseminar: 'Fêmeas a Inseminar', anascer: 'Bezerros a Nascer', nascidos: 'Previsão Total Nascimentos', aparir: 'Fêmeas a Parir', morte: 'Morte de Gestante', estoque: 'Estoque de Reprodutores', descarte: 'Estoque de Descartadas',
        adesmamar: 'Bezerros a Desmamar', desmame: 'Desmame', concepcao: 'Concepção IA', taxaprenhez: 'Taxa de Prenhez', venda: 'Vendas', pesagem: 'Pesagens', diag: 'Diagnósticos', descarte2: 'Descartes'};
      const linha = (tp, i) => { const id = (tp === 'partos' ? 'MB' : 'BF') + String(101 + i).padStart(3, '0'), r = ['NE', 'NE', 'AN', 'NE', 'BR'][i % 5], d2 = String(1 + (i * 7) % 28).padStart(2, '0');
        if(tp === 'insem') return [id, r, 'REPR', '03/' + '11/2025', LOTES[i % 4], TOUROS[i % 5], i % 6 === 0 ? '05/01/2026 - POSITIVO' : i % 6 === 1 ? '-' : '', '', i % 6 === 0 ? '05/01/2026 - POSITIVO' : '', RES[i % 6], OCO[i % 6]];
        if(tp === 'partos') return [id, r, d2 + '/11/2025', i % 4 ? 'IA' : 'MC', TOUROS[i % 5], '05/01/2026', d2 + '/08/2026', '', '', '', '', '', '', ''];
        if(tp === 'descanso') return [id, r, ['Primípara', 'Multípara', 'Secundípara'][i % 3], d2 + '/09/2025', 40 + (i * 13) % 90, LOTES[i % 4], PASTOS[i % 6]];
        if(tp === 'venda') return [id, i % 2 ? 'Fêmea' : 'Macho', pc(480 + (i * 37) % 90), d2 + '/08/2026', 'FRIGORÍFICO MODELO'];
        return [id, r, ['Novilha', 'Primípara', 'Multípara'][i % 3], ['Prenha', 'Servida', 'Vazia'][i % 3], ['Parida', 'Solteira'][i % 2], d2 + '/0' + (1 + i % 9) + '/2022', PASTOS[i % 6]]; };
      const abreLista = (chave, n) => { const base = chave.replace(/^lista/, ''), tp = TIPO(base), cols = COLS[tp], total = Math.max(0, Math.min(n == null || isNaN(n) ? 30 : n, 300)), linhas = [...Array(total)].map((_, i) => linha(tp, i));
        const tit = TITULOS[base] || 'Detalhamento', exp = tp === 'partos' ? '<button type="button" class="wb-exp" data-wb="toast" data-msg="Arquivo Excel gerado">' + IC.dl + ' Exportar Excel</button>' : '';
        const m = modal('', '<header>' + tit + exp + '<button type="button" class="wb-x" data-wb="fmodal" aria-label="Fechar">×</button></header><div class="wb-dlg-corpo"><div class="wb-busca"><input type="text" placeholder="Pesquisa rápida em: ' + (tp === 'partos' ? 'Id. usual' : 'ID Usual') + '" data-wb-busca>' + IC.lupa + '</div><div data-wb-lista></div></div><footer><button type="button" class="wb-fechar" data-wb="fmodal">FECHAR</button></footer>');
        m._dados = {cols, linhas, pag: 1, q: ''}; desenhaLista(m); };
      const desenhaLista = m => { const D = m._dados, L = D.linhas.filter(l => !D.q || l[0].toLowerCase().includes(D.q)), np = Math.max(1, Math.ceil(L.length / 10)); D.pag = Math.min(D.pag, np);
        const pg = L.slice((D.pag - 1) * 10, D.pag * 10);
        m.querySelector('[data-wb-lista]').innerHTML = '<table class="wb-tab wb-tab--lista"><thead><tr>' + D.cols.map(c => '<th>' + c + '</th>').join('') + '</tr></thead><tbody>'
          + (pg.length ? pg.map(l => '<tr>' + l.map(v => '<td>' + v + '</td>').join('') + '</tr>').join('') : '<tr><td colspan="' + D.cols.length + '" style="background:#fff;padding-left:6.5cqw">Não existem dados a serem exibidos</td></tr>') + '</tbody></table>'
          + (L.length ? '<div class="wb-pag"><button type="button" class="wb-seta-pag" data-wb="pg" data-p="1">«</button><button type="button" class="wb-seta-pag" data-wb="pg" data-p="' + Math.max(1, D.pag - 1) + '">‹</button>'
            + [...Array(np)].map((_, i) => i + 1).filter(p => Math.abs(p - D.pag) <= 2).map(p => '<button type="button" data-wb="pg" data-p="' + p + '"' + (p === D.pag ? ' class="is-sel"' : '') + '>' + p + '</button>').join('')
            + '<button type="button" class="wb-seta-pag" data-wb="pg" data-p="' + Math.min(np, D.pag + 1) + '">›</button><button type="button" class="wb-seta-pag" data-wb="pg" data-p="' + np + '">»</button></div><p class="wb-pag-n">' + L.length + ' registros</p>' : ''); };
      const abrePrenhez60 = () => { const k = K(), L = [['Novilha Precoce', 1053, 1051, 703, 1916, 1588], ['Novilha', 553, 542, 254, 970, 868], ['Primipara', 1025, 926, 688, 1549, 1252], ['Secundipara', 280, 256, 176, 410, 337], ['Multipara', 3163, 2934, 2122, 4684, 3801]]
          .map(l => [l[0], ...l.slice(1).map(x => Math.round(x * k * .96))]);
        const T = [1, 2, 3, 4, 5].map(j => L.reduce((a, l) => a + l[j], 0)), row = (l, tot) => '<tr' + (tot ? ' class="wb-total"' : '') + '><td>' + l[0] + '</td><td>' + l[1] + '</td><td>' + l[2] + '</td><td>' + l[3] + '</td><td>' + pc(100 * l[3] / Math.max(1, l[2])) + '</td><td>' + l[4] + '</td><td>' + l[5] + '</td><td>' + pc(100 * l[3] / Math.max(1, l[5])) + '</td></tr>';
        modal('wb-dlg--medio', '<header>Prenhez 60 Dias<button type="button" class="wb-x" data-wb="fmodal" aria-label="Fechar">×</button></header><div class="wb-dlg-corpo"><div class="wb-caixa"><div class="wb-ferr"><span>1605 d</span>' + IC.ref.replace('<svg', '<svg style="width:.8cqw;height:.8cqw"') + IC.fil.replace('<svg', '<svg style="width:.8cqw;height:.8cqw"') + '</div><h5>Prenhas Primeiros Dias por Categoria ' + I('prenhez60') + '</h5>'
          + '<table class="wb-tab wb-tab--cat"><thead><tr><th>Categorias</th><th>Quantidade Fêmeas ' + I('q') + '</th><th>Fêmeas Diagnosticadas ' + I('q') + '</th><th>Prenhas ' + I('q') + '</th><th>Taxa de Prenhez ' + I('q') + '</th><th>Serviços ' + I('q') + '</th><th>Serviços com DG ' + I('q') + '</th><th>Taxa de Concepção IA ' + I('q') + '</th></tr></thead><tbody>'
          + L.map(l => row(l)).join('') + row(['Total', ...T], 1) + '</tbody></table></div></div><footer><button type="button" class="wb-fechar" data-wb="fmodal">FECHAR</button></footer>'); };
      const abreFazendas = () => { const m = modal('wb-dlg--faz', '<header>Escolha uma fazenda para administrar<button type="button" class="wb-x" data-wb="fmodal" aria-label="Fechar">×</button></header><div class="wb-dlg-corpo" style="background:#fff">'
          + '<div style="display:flex;gap:1.2cqw;align-items:center"><div class="wb-busca" style="flex:1;margin:0"><input type="text" placeholder="Pesquisa rápida em Nome, Razão social, Abreviatura e Exploradores" data-wb-buscafaz>' + IC.lupa + '</div><div style="text-align:center;color:#3e5d36;font-size:.66cqw">' + IC.fil.replace('<svg', '<svg style="width:.6cqw;height:.6cqw"') + ' Filtros avançados<br><small>+ Exibir</small></div></div>'
          + '<table class="wb-tab wb-tab--lista" style="margin-top:.6cqw"><thead><tr><th>Nome</th><th>Razão social</th><th>INCRA / NIRF / CNPJ</th><th>Proprietário/Cliente</th></tr></thead><tbody data-wb-fazlista>'
          + FAZ.map((f, i) => '<tr class="is-clicavel" data-wb="escolhefaz" data-i="' + i + '"><td>' + f.n + '</td><td>' + f.rs + '</td><td>' + f.doc + '</td><td>' + f.dono + '</td></tr>').join('') + '</tbody></table>'
          + '<div class="wb-pag"><button type="button" class="wb-seta-pag">«</button><button type="button" class="wb-seta-pag">‹</button><button type="button" class="is-sel">1</button><button type="button" class="wb-seta-pag">›</button><button type="button" class="wb-seta-pag">»</button></div><p class="wb-pag-n">' + FAZ.length + ' registros</p></div>'); };
      const abreBusca = () => { abreLista('estoque', 30); const m = $('[data-wb-modal]'); m.querySelector('header').firstChild.textContent = 'Busca de Animais'; };
      /* ajuda */
      const AJ = {
        perdas: '<h6>Perdas Gestacionais:</h6>Consideramos como Perdas de IA, Repasse ou MC com “Touro Desconhecido”, as Perdas que ocorreram até a data final do período do DG Final, são elas:<ul><li>DG+ | DG-</li><li>Morte Embrionária</li><li>Aborto</li><li>Morte de Gestante</li></ul><b>• Quantidade:</b> consideramos as situações listadas acima.<br><b>• Previsão:</b> considerando as diversas situações de perdas, % prevista de perdas que podem ocorrer. Valor informado nas configurações da Estação de Monta, aba Projeção.<br><br><b>• Como comparar com o MB Desktop:</b> não comparável com o Desktop. Na Web, M. Emb., Aborto e Morte de Gestante só são contabilizados como Perdas Gestacionais caso ocorram antes da Data Final do período do DG Final.',
        femeas: '<h6>Fêmeas Inseminadas:</h6><b>• Previsão:</b> quantidade de fêmeas previstas para inseminar na estação de monta. Valor informado nas configurações da Estação de Monta, aba Projeção.<br><b>• Quantidade:</b> quantidade de fêmeas que foram inseminadas no período.<br><br><b>• Como comparar com o MB Desktop:</b> selecione o menu Reprodução / Coberturas / Fêmeas Servidas e informe o mesmo período do Dashboard.',
        estacao: '<h6>Estação Monta:</h6>Informações de inseminações e diagnósticos de gestação da estação de monta selecionada, separadas por serviço (1ª a 5ª IA).<br><br><b>DG Inicial:</b> primeiro diagnóstico após o serviço.<br><b>DG Final:</b> diagnóstico realizado no período configurado para o DG final.',
        partos: '<h6>Partos:</h6><b>• Partos:</b> quantidade de fêmeas paridas no período.<br><b>• Bezerros Nascidos:</b> quantidade de crias nascidas, considerando gêmeos.<br><b>• Previsão Total Nascimentos:</b> nascidos + a nascer.<br><br><b>• Como comparar com o MB Desktop:</b> selecione o menu Reprodução / Partos e informe o mesmo período.'};
      const abreAjuda = k => { k = String(k || '').replace(/pop$/, ''); k = {nascidos: 'partos', anascer: 'partos', morte: 'partos', insem: 'femeas', estoque: 'femeas', semres: 'perdas', ia: 'estacao', servicos: 'estacao', dgini: 'estacao', dgfim: 'estacao'}[k] || k; const a = $('[data-wb-ajuda]'), txt = AJ[k] || AJ[k === 'taxaprenhez' || k === 'prenhez' ? 'femeas' : k === 'partosper' ? 'partos' : ''] || '<h6>Ajuda do indicador</h6>Este indicador considera os registros da fazenda selecionada no período exibido no box. Use o filtro para alterar o período e a lupa para ver os animais.';
        a.querySelector('.wb-ajc').innerHTML = '<p><b>Comparação com o MB Desktop</b><br>Este indicador <b>não é comparável</b> com o MB Desktop.</p><p><b>Motivo:</b></p><ul><li><b>Web:</b> considera apenas os serviços de <b>fêmeas ativas na fazenda</b>.</li><li><b>Desktop:</b> considera os serviços de <b>fêmeas ativas e inativas</b>.</li></ul><hr><div class="is-destaque">' + txt + '</div><hr><p class="wb-cp">MultSoft © 2026</p>';
        a.classList.add('is-aberta'); };
      /* menu principal */
      const MENU = {'Gerenciamento de Tarefas': {Principal: ['Tarefas', 'Agenda de Manejos', 'Responsáveis']}, 'Estoque de Animais': {Principal: ['Entrada de Animais', 'Saída de Animais', 'Transferências', 'Inventário'], 'Relatórios e Consultas': ['Estoque Atual', 'Movimentação de Gado', 'Estoque por Localidade']},
        'Reprodução': {Principal: ['Estação de Monta', 'Coberturas', 'Diagnóstico de Gestação', 'Partos', 'Desmame'], 'Relatórios e Consultas': ['Fêmeas Servidas', 'Previsão de Partos', 'Resumo Estação de Monta']},
        'Reprodutivo IATF': {Principal: ['Protocolos', 'Lotes de IATF', 'Cronograma IATF', 'Manejo de IATF'], 'Relatórios e Consultas': ['Resultado por Protocolo', 'Resultado por Inseminador']},
        'Controle Ponderal': {Principal: ['Pesagens', 'Curva de Crescimento'], 'Relatórios e Consultas': ['Ganho de Peso', 'Pesagens por Período']}, 'Zoossanitário': {Principal: ['Vacinações', 'Tratamentos', 'Ocorrências'], 'Relatórios e Consultas': ['Calendário Sanitário']},
        'Taxa de Lotação e Tratos': {Principal: ['Lotação por Pasto', 'Tratos'], 'Relatórios e Consultas': ['Consumo por Retiro']},
        'Melhoramento Genético': {Principal: ['Importação de DEPs', 'Catálogo Animal', 'Selecionar Programa', 'Avaliação', 'Safras'], 'Importações': ['Biblioteca de touros', 'Biblioteca de avaliadores', 'Biblioteca de acasalamentos', 'Animais escolhidos para genotipagem', 'Medições'],
          'Relatórios e Consultas': ['Certificado CEIP', 'Exportação PMG', 'Exportação de Avaliações Genéticas', 'Avaliações Morfológicas - Geral', 'Precocidade de Novilhas - ANCP', 'Avaliações Genéticas'], Outros: ['Ajuste de RGN / RGD']},
        'Lab FIV': {Principal: ['Aspirações', 'Produção de Embriões']}, 'FIV': {Principal: ['OPU', 'Transferências', 'Estoque de Embriões']}, 'Confinamento': {Principal: ['Lotes de Confinamento', 'Fabricação de Ração', 'Fornecimento de Tratos', 'Leitura de Cocho'], 'Relatórios e Consultas': ['Consumo por Lote', 'Desempenho do Lote', 'Custo da Diária']},
        'Planejamento de Vendas': {Principal: ['Previsão de Vendas', 'Escalas de Abate']}, 'Gestão de Vendas': {Principal: ['Vendas', 'Romaneios']}, 'Gerenciamento de Contratos': {Principal: ['Contratos', 'Aditivos']}, 'CRM': {Principal: ['Clientes', 'Oportunidades']},
        'Financeiro': {Principal: ['Contas a Pagar', 'Contas a Receber', 'Fluxo de Caixa', 'Conciliação Bancária'], 'Relatórios e Consultas': ['DRE', 'Extrato por Conta']}, 'Estoque de Materiais': {Principal: ['Entradas', 'Saídas', 'Inventário']}, 'Contabilidade Rural': {Principal: ['Lançamentos', 'LCDPR']},
        'Custos Pecuários': {Principal: ['Rateios', 'Custo por Animal']}, 'Agrícola': {Principal: ['Safras', 'Talhões', 'Aplicações']}, 'Ativo Fixo / Maquinários': {Principal: ['Bens', 'Depreciação']}, 'Manutenção Preventiva': {Principal: ['Ordens de Serviço', 'Planos de Manutenção']},
        'Integração ERP': {Principal: ['Configuração', 'Monitor de Integração']}, 'Tabelas Básicas': {Principal: ['Raças', 'Pelagens', 'Localidades', 'Lotes', 'Responsáveis']}, 'Administração': {Principal: ['Usuários', 'Perfis de Acesso', 'Fazendas']}, 'Curral': {Principal: ['Rotinas de Manejo', 'Sincronização do App']},
        'Gestão por Mapas': {Principal: ['Mapas da Fazenda', 'Pastos']}, 'Comunicação Online ABCZ': {Principal: ['Comunicações', 'Pendências']}, 'Multdados': {Principal: ['Painéis', 'Exportações']}, 'SISBOV': {Principal: ['Identificações', 'Movimentações SISBOV', 'Vistorias']}};
      const desenhaSub = cat => { const s = $('.wb-menu section'), M = MENU[cat] || {};
        s.innerHTML = Object.entries(M).map(([t, its]) => '<div><h6>' + t + '</h6>' + its.map(x => '<button type="button" data-wb="toast" data-msg="Abrindo «' + x + '»">' + x + '</button>').join('') + '</div>').join('');
        $$('.wb-menu nav button').forEach(b => b.classList.toggle('is-sel', b.dataset.cat === cat)); };
      const montaMenu = () => { const m = $('.wb-menu'); m.querySelector('nav').innerHTML = '<input type="text" placeholder="Digite uma funcionalidade" data-wb-menubusca>' + Object.keys(MENU).map(c => '<button type="button" data-cat="' + c + '">' + c + '</button>').join(''); desenhaSub('Melhoramento Genético'); };

      /* ---------------- eventos ---------------- */
      tela.addEventListener('mouseover', e => { const b = e.target.closest('.wb-menu nav button'); if(b) desenhaSub(b.dataset.cat); });
      tela.addEventListener('input', e => {
        if(e.target.matches('[data-wb-busca]')){ const m = $('[data-wb-modal]'); m._dados.q = e.target.value.trim().toLowerCase(); m._dados.pag = 1; desenhaLista(m); }
        if(e.target.matches('[data-wb-buscafaz]')){ const q = e.target.value.trim().toLowerCase(); $$('[data-wb-fazlista] tr').forEach(r => r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none'); }
        if(e.target.matches('[data-wb-menubusca]')){ const q = e.target.value.trim().toLowerCase(); $$('.wb-menu nav button').forEach(b => { const ok = !q || b.dataset.cat.toLowerCase().includes(q) || JSON.stringify(MENU[b.dataset.cat]).toLowerCase().includes(q); b.classList.toggle('is-oculto', !ok); }); }
      });
      tela.addEventListener('keydown', e => e.stopPropagation());
      corpo.addEventListener('scroll', fecharPops);
      tela.addEventListener('click', e => {
        const ab = e.target.closest('[data-wb-aba]'); if(ab){ carrega(() => { st.aba = ab.dataset.wbAba; st.pag = 'dash'; }); return; }
        const es = e.target.closest('[data-wb-escopo]'); if(es){ carrega(() => { st.escopo = es.dataset.wbEscopo; }); return; }
        const b = e.target.closest('[data-wb]');
        if(!e.target.closest('.wb-pop') && !(b && ['fil', 'men', 'pop'].includes(b.dataset.wb))) fecharPops();
        if(!e.target.closest('.wb-menu') && !(b && b.dataset.wb === 'menu')) { $('.wb-menu').classList.remove('is-aberto'); $('[data-wb="menu"]').classList.remove('is-aberto'); }
        if(!e.target.closest('.wb-drop') && !(b && ['user', 'sino'].includes(b.dataset.wb))) $$('.wb-drop').forEach(d => d.classList.remove('is-aberto'));
        if(e.target === $('[data-wb-modal]')){ fecharModal(); return; }
        if(!b) return; const a = b.dataset.wb, key = b.dataset.box;
        if(a === 'ref'){ b.classList.remove('is-girando'); void b.offsetWidth; b.classList.add('is-girando'); carrega(null, key); return; }
        if(a === 'fil'){ const ab2 = $('.wb-pop--filtro'); if(ab2 && ab2.dataset.box === key){ fecharPops(); return; } abreFiltro(b, key); return; }
        if(a === 'men'){ abreMenuBox(b, key); return; }
        if(a === 'zoom'){ abreLista({aptas: 'femeas', ia: 'insem', partos: 'nascidos', estoque: 'estoque', desmame: 'desmame', pest: 'estoque', pfaixa: 'estoque', ppes: 'pesagem', pvend: 'venda'}[key] || 'insem', 30); if(key === 'partos'){ fecharModal(); carrega(() => { st.pag = 'partos'; }); } return; }
        if(a === 'pop'){ abreDrillPop(b, b.dataset.drill); return; }
        if(a === 'lista'){ fecharPops(); abreLista(b.dataset.drill, b.dataset.n != null ? +b.dataset.n : 30); return; }
        if(a === 'pg'){ const m = $('[data-wb-modal]'); m._dados.pag = +b.dataset.p; desenhaLista(m); return; }
        if(a === 'fmodal'){ fecharModal(); return; }
        if(a === 'prenhez60'){ abrePrenhez60(); return; }
        if(a === 'pagina'){ carrega(() => { st.pag = b.dataset.pg; }); return; }
        if(a === 'dash'){ carrega(() => { st.pag = 'dash'; }); return; }
        if(a === 'ajuda'){ abreAjuda(b.dataset.aj); return; }
        if(a === 'fajuda'){ $('[data-wb-ajuda]').classList.remove('is-aberta'); return; }
        if(a === 'rapido'){ b.parentElement.querySelectorAll('button').forEach(x => x.classList.toggle('is-sel', x === b)); b.closest('.wb-pop')._rapido = {mult: +b.dataset.mult, per: b.dataset.per}; return; }
        if(a === 'aplicar'){ const pop = b.closest('.wb-pop'), k2 = pop.dataset.box, f = st.fil[k2] = st.fil[k2] || {};
          pop.querySelectorAll('[data-f]').forEach(x => { if(x.dataset.f === 'em') st.em = x.value; else if(x.dataset.f === 'prop') st.escopo = x.value === 'Todas as fazendas' ? 'todas' : 'esta'; else f[x.dataset.f] = x.value; });
          if(pop._rapido){ f.mult = pop._rapido.mult; f.per = pop._rapido.per; }
          carrega(null, ['resumo', 'ia', 'aptas'].includes(k2) && pop.querySelector('[data-f="em"]') ? '' : k2); if(pop.querySelector('[data-f="em"]') || pop.querySelector('[data-f="prop"]')) carrega(); return; }
        if(a === 'limpar'){ const k2 = b.closest('.wb-pop').dataset.box; delete st.fil[k2]; carrega(null, k2); return; }
        if(a === 'fpop'){ fecharPops(); return; }
        if(a === 'menu'){ const m = $('.wb-menu'), ab3 = !m.classList.contains('is-aberto'); fecharTudo(); if(ab3){ m.classList.add('is-aberto'); b.classList.add('is-aberto'); m.querySelector('input').value = ''; $$('.wb-menu nav button').forEach(x => x.classList.remove('is-oculto')); } return; }
        if(a === 'faz'){ fecharTudo(); abreFazendas(); return; }
        if(a === 'escolhefaz'){ fecharModal(); carrega(() => { st.faz = +b.dataset.i; st.escopo = 'esta'; st.pag = 'dash'; }); return; }
        if(a === 'user' || a === 'sino'){ const d = $('[data-wb-drop="' + a + '"]'), ab4 = !d.classList.contains('is-aberto'); $$('.wb-drop').forEach(x => x.classList.remove('is-aberto')); if(ab4) d.classList.add('is-aberto'); return; }
        if(a === 'busca'){ fecharTudo(); abreBusca(); return; }
        if(a === 'radio'){ b.parentElement.querySelectorAll('button').forEach(x => x.classList.toggle('is-sel', x === b)); return; }
        if(a === 'toast'){ fecharPops(); $$('.wb-menu, .wb-drop').forEach(x => x.classList.remove('is-aberto')); toast(b.dataset.msg); return; }
      });
      window.abreWebMB = aba => { st.aba = aba; st.pag = 'dash'; fecharTudo(); fecharModal(); $('[data-wb-ajuda]').classList.remove('is-aberta'); st.carregando = true; render(); goToSlide(125);
        setTimeout(() => { st.carregando = false; render(); }, 700); };
      montaMenu(); render();
    })();
