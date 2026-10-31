"""Slides de evento com tablet 3D navegável (App MB Curral) — compartilhados pelos decks de
Reprodução e Cria e de Confinamento. Layout do slide medido por pixel nos slides de referência
(1920x1080); a tela do app é HTML em fluxo, com medidas em cqw/cqh da própria tela (container).
css(prefixo), html(prefixo, n, evento, tela_html, voltar) e js(prefixo)."""
import re

def top(cap, fs, L=1.0):
    """top (% da altura) para que o topo das maiúsculas (Montserrat) fique em `cap`, com fonte fs (cqh) e line-height L."""
    return round(cap - fs*((L-1.219)/2 + .268), 2)

ICO = {
 'vaca': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5c-1.5 0-2.5 1-2.5 2.5S3 10 4.5 10M20 5c1.5 0 2.5 1 2.5 2.5S21 10 19.5 10"/><path d="M6 9.5 4.5 6.5h15L18 9.5M6 9.5c0 4 1.5 7 6 7s6-3 6-7M9 16.5v3h6v-3"/><circle cx="9.5" cy="11" r=".8" fill="currentColor"/><circle cx="14.5" cy="11" r=".8" fill="currentColor"/></svg>',
 'grafico': '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="3" y="12" width="4" height="9" rx=".8"/><rect x="10" y="4" width="4" height="17" rx=".8"/><rect x="17" y="9" width="4" height="12" rx=".8"/></svg>',
 'alerta': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="10"/><rect x="11" y="6" width="2" height="8" rx="1" fill="#285519"/><circle cx="12" cy="17" r="1.3" fill="#285519"/></svg>',
 'menu': '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="3" y="5" width="18" height="2.2" rx="1"/><rect x="3" y="10.9" width="18" height="2.2" rx="1"/><rect x="3" y="16.8" width="18" height="2.2" rx="1"/></svg>',
 'chevron': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
 'lixo': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 3h6l1 2h4v2H4V5h4l1-2zm-3 6h12l-1 12H7L6 9zm4 2v8h1.6v-8H10zm2.4 0v8H14v-8h-1.6z"/></svg>',
 'lupa': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/></svg>',
 'lapis': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 17.25V21h3.75L17.8 9.94l-3.75-3.75L3 17.25zm17.7-10.2a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>',
 'mais': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="11"/><path d="M11 6h2v5h5v2h-5v5h-2v-5H6v-2h5z" fill="#fff"/></svg>',
 'relogio': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 'link': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg>',
 'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5L20 7"/></svg>',
 'bandeira': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M5 3h2v18H5zM8 4h10l-2.5 4L18 12H8z"/></svg>',
 'seta-baixo': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m6 9 6 6 6-6z"/></svg>',
 'zoom': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5M8 10.5h5M10.5 8v5"/></svg>',
 'info': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="11"/><path d="M11 10h2v7h-2zM11 6.5h2v2h-2z" fill="#fff"/></svg>',
 'ficha': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 4h9l4 4v12H6z"/><path d="M15 4v4h4M9 12h6M9 16h6"/></svg>',
 'desfazer': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 14 4 9l5-5"/><path d="M4 9h9a6 6 0 0 1 0 12h-2"/></svg>',
 'ok-circulo': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m7.5 12.5 3 3 6-7"/></svg>',
 'play': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15l12-7.5z"/></svg>',
 'editar': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H5.5A1.5 1.5 0 0 0 4 5.5v13A1.5 1.5 0 0 0 5.5 20h13a1.5 1.5 0 0 0 1.5-1.5V13"/><path d="m17.5 3.5 3 3L12 15H9v-3z"/></svg>',
 'g-inicio': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3 2 12h3v8h5v-5h4v5h5v-8h3z"/></svg>',
 'g-lotes': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 3 3 5.8v5.4L8 14l5-2.8V5.8zM16 9l-5 2.8v5.4L16 20l5-2.8v-5.4z"/></svg>',
 'g-vaca': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 4c-1.5 0-2.5 1.2-2.5 2.6S2.6 9 4 9h1.2l1.3 4.5c.4 1.4 1.6 2.3 3 2.3h5c1.4 0 2.6-.9 3-2.3L18.8 9H20c1.4 0 2.5-1 2.5-2.4S21.5 4 20 4h-3l-1 2.5H8L7 4zm5.5 7.5a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm5 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2zM9 17h6v3H9z"/></svg>',
 'g-pastos': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 5h18v3H3zm0 5.5h11v3H3zm13 0h5v3h-5zM3 16h18v3H3z"/></svg>',
 'g-enviar': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 16V8m-3.5 3.5L12 8l3.5 3.5"/></svg>',
 'g-envios': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.7 2.7L16 9.5"/></svg>',
 'g-venda': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 6h20v12H2zm10 2.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7zM5 10.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3zm14 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3z"/></svg>',
 'g-carga': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="4.5" cy="6" r="1.8"/><circle cx="4.5" cy="12" r="1.8"/><circle cx="4.5" cy="18" r="1.8"/><path d="M8.5 4.8h12v2.4h-12zm0 6h12v2.4h-12zm0 6h12v2.4h-12z"/></svg>',
 'g-config': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m19.4 13 1.9 1.5-2 3.4-2.3-.9a7 7 0 0 1-1.8 1l-.4 2.5h-4l-.4-2.5a7 7 0 0 1-1.8-1l-2.3.9-2-3.4L6.2 13a7 7 0 0 1 0-2L4.3 9.5l2-3.4 2.3.9a7 7 0 0 1 1.8-1L10.8 3.5h4l.4 2.5a7 7 0 0 1 1.8 1l2.3-.9 2 3.4-1.9 1.5a7 7 0 0 1 0 2zM12.8 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/></svg>',
 'g-bluetooth': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7.5 17 16l-5 4.5V3.5l5 4.5L7 16.5"/></svg>',
 'g-erros': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.5 1.5 21h21zM11 9h2v6h-2zm0 7.5h2v2h-2z"/></svg>',
 'g-quebras': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1M4 4l16 16"/></svg>',
 'g-historico': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 12a8.5 8.5 0 1 0 2.5-6M3.5 4v4.5H8M12 8v4.5l3 2"/></svg>',
 'g-ajuda': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="10"/><path d="M11 10h2v7h-2zM11 6.5h2v2h-2z" fill="#4f7d3b"/></svg>',
 'casa': '<svg viewBox="0 0 24 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 10 12 2.8l8.5 7.2M6 8.6V17.5h4.3v-4.6h3.4v4.6H18V8.6"/></svg>',
 'alca': '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="4" y="9" width="16" height="2" rx="1"/><rect x="4" y="13" width="16" height="2" rx="1"/></svg>',
 'maisb': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M10 4h4v6h6v4h-6v6h-4v-6H4v-4h6z"/></svg>',
}

# ======================================================================= CSS
def css(p='tb'):
    return f'''  /* ================= EVENTOS COM TABLET 3D (App MB Curral) =================
     Texto à esquerda (medidas do slide de referência 1920x1080), faixa de foto à direita e tablet em
     perspectiva que acompanha o mouse. A tela do app é HTML dentro da moldura (container próprio).
     Gerado por ferramentas/aplica_eventos.py — não editar à mão. */
  .{p}{{background:#fff;}}
  .{p} *{{font-family:var(--ms-fonte);}}
  .{p}-foto{{position:absolute;left:74.84%;top:0;width:25.16%;height:100%;object-fit:cover;display:block;}}
  .{p}-barra-teal{{position:absolute;left:74.84%;top:0;width:12.43%;height:1.86%;background:#00a7b0;}}
  .{p}-eyebrow{{
    position:absolute;left:6.68%;top:{top(6.68,2.85,1)}%;margin:0;
    color:#9db8bc;font-size:2.85cqh;font-weight:600;line-height:1;letter-spacing:-.02em;white-space:nowrap;
  }}
  .{p}-titulo{{
    position:absolute;left:6.4%;top:{top(12.25,7.4,.9)}%;margin:0;
    color:#008593;font-size:7.4cqh;font-weight:800;line-height:.9;letter-spacing:-.04em;white-space:nowrap;
  }}
  .{p}-tag{{
    position:absolute;left:6.52%;top:21.2%;height:3.8%;margin:0;padding:0 1.6cqw 0 1.1cqw;
    display:flex;align-items:center;background:#8cc27c;color:#fff;
    font-size:2.45cqh;font-weight:700;letter-spacing:.02em;text-transform:uppercase;white-space:nowrap;
    clip-path:polygon(0 0,100% 0,calc(100% - 1.05cqw) 100%,0 100%);
  }}
  .{p}-pilula{{position:absolute;left:6.63%;top:35.3%;width:7.78%;height:2.69%;border-radius:999px;background:#00aebe;}}
  .{p}-texto{{
    position:absolute;left:18.06%;top:{top(34.4,4.25,1.25)}%;width:44%;margin:0;
    color:#435f47;font-size:4.25cqh;font-weight:500;line-height:1.25;letter-spacing:-.025em;
  }}
  /* título em duas linhas: o que vem abaixo desce 8,5% (medido nos slides de referência) */
  .{p}--2l .{p}-tag{{top:29.7%;}}
  .{p}--2l .{p}-pilula{{top:43.8%;}}
  .{p}--2l .{p}-texto{{top:{top(42.9,4.25,1.25)}%;}}
  .{p} .ms-nav{{z-index:4;}}

  /* ---- tablet: 3D com perspectiva; camadas atrás dão a espessura ---- */
  .{p}-palco{{position:absolute;left:63.36%;top:2.78%;width:34.76%;height:93.9%;perspective:170cqw;perspective-origin:50% 45%;z-index:2;}}
  /* palco, giro e tablet não recebem o mouse: como planos no espaço 3D, eles ficariam na frente da tela onde ela
     se inclina para trás e roubariam os cliques; só a tela do app (e seus botões) é alvo */
  .{p}-palco,.{p}-giro,.{p}-tablet,.{p}-camada,.{p}-moldura{{pointer-events:none;}}
  .{p}-tela{{pointer-events:auto;}}
  .{p}-giro{{position:absolute;inset:0;transform-style:preserve-3d;transition:transform 1s cubic-bezier(.22,.78,.28,1) var(--d,0s);}}
  .{p}:not(.is-active) .{p}-giro{{transform:rotateY(42deg);}}
  .{p}.is-active .{p}-giro{{transform:rotateY(0deg);}}
  .{p}-tablet{{
    position:absolute;inset:0;transform-style:preserve-3d;
    /* avança o tablet no eixo Z para que, mesmo inclinado, nenhuma parte da tela fique atrás do plano do slide
       (o Chrome não detecta cliques atrás desse plano); o scale compensa a aproximação da câmera */
    transform:translateZ(6cqw) scale(.965) rotateX(var(--rx,0deg)) rotateY(var(--ry,8deg));
  }}
  .{p}-camada{{position:absolute;inset:0;border-radius:7.9% / 5.2%;background:#101010;}}
  .{p}-camada:last-of-type{{background:#0a0a0a;box-shadow:0 2.5cqh 5cqh rgba(0,20,30,.45);}}
  .{p}-moldura{{position:absolute;inset:0;width:100%;height:100%;display:block;transform:translateZ(.02cqw);}}
  .{p}-tela{{
    position:absolute;left:2.70%;top:2.66%;width:94.69%;height:88.84%;
    border-radius:1.1cqw;overflow:hidden;background:#f7f7f7;transform:translateZ(.04cqw);
    container-type:size;
  }}

  /* ===== tela do app (unidades cqw/cqh = largura/altura da tela) ===== */
  .{p}-app{{position:absolute;inset:0;font-family:"Roboto","Segoe UI",Helvetica,Arial,sans-serif;color:#333;}}
  .{p}-app *{{font-family:inherit;box-sizing:border-box;}}
  .{p}-appbar{{position:absolute;left:0;top:0;width:100%;height:4.4cqh;background:#285519;display:flex;align-items:center;padding:0 2cqw;gap:1.6cqw;}}
  .{p}-applogo{{height:2.9cqh;width:auto;display:block;}}
  .{p}-appdiv{{width:1px;height:2.6cqh;background:#5a8a48;}}
  .{p}-appfaz{{color:#fff;font-size:2cqw;font-weight:700;letter-spacing:.01em;white-space:nowrap;}}
  .{p}-appicos{{margin-left:auto;display:flex;align-items:center;gap:1.7cqw;color:#fff;}}
  .{p}-appicos svg{{width:2.5cqw;height:2.5cqw;display:block;}}
  .{p}-subbar{{position:absolute;left:0;top:4.4cqh;width:100%;height:4.6cqh;background:#396e27;border-top:1px solid #4d8a37;display:flex;align-items:center;}}
  .{p}-volta{{width:6.5cqw;height:100%;border:0;margin:0;padding:0;background:#1b430e;color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;flex:0 0 auto;}}
  .{p}-volta svg{{width:2.6cqw;height:2.6cqw;}}
  .{p}-subtxt{{color:#fff;font-size:2cqw;font-weight:700;margin-left:2.5cqw;white-space:nowrap;}}
  .{p}-subacoes{{margin-left:auto;display:flex;height:100%;}}
  .{p}-subacoes button{{height:100%;border:0;margin:0;padding:0 2cqw;background:transparent;color:#fff;font-size:1.8cqw;display:flex;align-items:center;gap:.8cqw;cursor:pointer;white-space:nowrap;}}
  .{p}-subacoes button svg{{width:2cqw;height:2cqw;}}
  .{p}-subacoes button.is-escuro{{background:#2b5a1e;}}
  /* corpo: barra lateral opcional + formulário rolável */
  .{p}-corpo{{position:absolute;left:0;top:9cqh;width:100%;height:91cqh;display:flex;background:#f7f7f7;}}
  .{p}-lado{{width:27.3cqw;flex:0 0 auto;background:#347d27;padding:2.4cqh 1.9cqw 2cqh 2.2cqw;overflow-y:auto;overflow-x:hidden;scrollbar-width:none;}}
  .{p}-lado::-webkit-scrollbar{{display:none;}}
  .{p}-id{{color:#f3d53a;font-size:2.6cqw;font-weight:700;display:flex;align-items:center;gap:1.4cqw;margin:0 0 1.6cqh;white-space:nowrap;}}
  .{p}-id i{{width:2.7cqw;height:2.7cqw;border-radius:50%;background:#5f9450;display:inline-flex;align-items:center;justify-content:center;color:#fff;}}
  .{p}-id i svg{{width:1.5cqw;height:1.5cqw;}}
  .{p}-par{{margin:0 0 1.45cqh;}}
  .{p}-par small,.{p}-caixa small{{display:block;color:#a9cf9b;font-size:1.45cqw;line-height:1.2;margin-bottom:.35cqh;white-space:nowrap;}}
  .{p}-par b{{display:block;color:#fff;font-weight:400;font-size:2.05cqw;line-height:1.2;white-space:nowrap;}}
  .{p}-hr{{height:1px;background:#8fbf7f;margin:2.2cqh 0 2.6cqh;}}
  .{p}-caixa{{margin:0 0 1.7cqh;}}
  .{p}-caixa div{{background:#b9e3a4;color:#1f3d14;font-size:1.5cqw;line-height:1.35;padding:.9cqh 1.1cqw;border-radius:.45cqw;}}
  .{p}-caixa--amarela div{{background:#ffe24a;}}
  .{p}-caixa--alta div{{min-height:6.5cqh;}}
  .{p}-form{{flex:1;min-width:0;overflow-y:auto;scrollbar-width:none;padding:2.3cqh 3.6cqw 2cqh 4.2cqw;display:flex;flex-direction:column;}}
  .{p}-form::-webkit-scrollbar{{display:none;}}
  .{p}-form > *{{flex-shrink:0;}}   /* o conteúdo rola, não encolhe */
  .{p}-corpo--lado .{p}-form{{padding-left:3.8cqw;}}
  .{p}-tit{{margin:0;color:#3d7029;font-size:5cqw;font-weight:700;line-height:1.15;letter-spacing:-.01em;display:flex;align-items:center;flex-wrap:wrap;gap:1.2cqw;}}
  .{p}-corpo--lado .{p}-tit{{font-size:4.5cqw;}}
  .{p}-info{{width:2.4cqw;height:2.4cqw;border-radius:50%;background:#6e9a62;color:#fff;font:italic 700 1.6cqw/2.4cqw Georgia,serif;text-align:center;display:inline-block;flex:0 0 auto;}}
  .{p}-obs{{margin:.7cqh 0 2.2cqh;color:#9a9a9a;font-size:1.85cqw;font-style:italic;line-height:1;white-space:nowrap;}}
  .{p}-campo{{margin:0 0 2.7cqh;min-width:0;}}
  .{p}-campo label{{display:flex;align-items:center;gap:1cqw;color:#4a4a4a;font-size:2.35cqw;font-weight:500;line-height:1;margin-bottom:1cqh;white-space:nowrap;}}
  .{p}-campo label b{{color:#e53935;font-weight:500;}}
  .{p}-campo label .{p}-mais{{width:2.4cqw;height:2.4cqw;color:#8a8a8a;cursor:pointer;display:inline-flex;}}
  .{p}-campo label .{p}-mais svg{{width:100%;height:100%;}}
  .{p}-campo label .{p}-relogio{{margin-left:auto;width:2.6cqw;height:2.6cqw;color:#9a9a9a;}}
  .{p}-linha{{display:flex;gap:3.4cqw;}}
  .{p}-linha .{p}-campo{{flex:1;}}
  .{p}-input{{height:6cqh;display:flex;align-items:center;background:#fff;border:1px solid #c9c9c9;border-radius:.6cqw;overflow:hidden;}}
  .{p}-input span{{flex:1;min-width:0;padding-left:2.6cqw;color:#2b2b2b;font-size:3.2cqw;line-height:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}
  .{p}-input span.{p}-ph{{color:#b9b9b9;}}
  .{p}-input--off{{background:#e9e9ea;border-color:#d2d2d2;}}
  .{p}-bt{{width:5.86cqw;height:100%;border:0;margin:0;padding:0;background:#7aa070;color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;flex:0 0 auto;}}
  .{p}-bt:disabled{{color:#fff;}}
  .{p}-bt svg{{width:2.4cqw;height:2.4cqw;}}
  .{p}-input--off .{p}-bt{{background:#919392;cursor:default;}}
  .{p}-seg{{height:6.2cqh;display:flex;border:1px solid #c9c9c9;border-radius:.7cqw;overflow:hidden;background:#fff;}}
  .{p}-seg button{{flex:1;border:0;margin:0;padding:0;background:#fff;color:#555;font-size:2.7cqw;cursor:pointer;transition:background-color .2s ease,color .2s ease;}}
  .{p}-seg button+button{{border-left:1px solid #d6d6d6;}}
  .{p}-seg button.is-sel{{background:#7aa070;color:#fff;}}
  .{p}-passos{{display:flex;gap:1.3cqw;margin-top:1.2cqh;}}
  .{p}-passos button{{flex:1;height:6.2cqh;border:0;border-radius:.6cqw;background:#7aa070;color:#fff;font-size:3cqw;cursor:pointer;display:flex;align-items:center;justify-content:center;}}
  .{p}-passos button:active{{filter:brightness(.92);}}
  .{p}-passos button svg{{width:2.6cqw;height:2.6cqw;}}
  .{p}-area{{min-height:15cqh;background:#fff;border:1px solid #c9c9c9;border-radius:.6cqw;padding:1.6cqh 2.6cqw;color:#b9b9b9;font-size:3cqw;line-height:1.3;}}
  .{p}-lista{{margin:0;padding:0;list-style:none;}}
  .{p}-item{{height:6cqh;background:#ececec;border-radius:.6cqw;display:flex;align-items:center;padding:0 1.6cqw 0 2.6cqw;margin-bottom:1.3cqh;font-size:3cqw;color:#2b2b2b;white-space:nowrap;overflow:hidden;}}
  .{p}-item span{{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;}}
  .{p}-item--vazio{{height:4.6cqh;font-size:2.1cqw;color:#444;}}
  .{p}-item button{{border:0;background:transparent;color:#6e9a62;width:3cqw;height:3cqw;padding:0;cursor:pointer;display:flex;flex:0 0 auto;}}
  .{p}-item button svg{{width:100%;height:100%;}}
  .{p}-item button.is-escuro{{color:#222;}}
  .{p}-nota{{text-align:center;color:#5a9a4e;font-size:2cqw;line-height:1.9;margin:-1.2cqh 0 0;}}
  .{p}-nota u{{cursor:pointer;}}
  .{p}-avancar{{
    align-self:center;margin-top:auto;width:35cqw;height:6.3cqh;flex:0 0 auto;
    border:.25cqw solid #7d9a78;border-radius:999px;background:#40603b;color:#fff;
    font-size:2.85cqw;font-weight:700;letter-spacing:.02em;cursor:pointer;
    box-shadow:0 .5cqh 1.2cqh rgba(0,0,0,.28);transition:scale .15s ease,filter .15s ease;
  }}
  .{p}-avancar:not(:disabled):hover{{filter:brightness(1.12);}}
  .{p}-avancar:not(:disabled):active{{scale:.96;}}
  /* variantes de uma mesma tela (ex.: Entrada do Animal, fêmea/macho) */
  .{p}-var{{display:none;}}
  .{p}-app[data-sexo="f"] .{p}-var--f,.{p}-app[data-sexo="m"] .{p}-var--m{{display:contents;}}
  /* páginas internas da mesma tela (sequência de telas do app) */
  .{p}-pag{{position:absolute;inset:0;display:none;background:#f7f7f7;overflow:hidden;}}
  .{p}-pag.is-ativa{{display:block;}}
  /* navegação com deslize lateral, como no app: a nova tela entra pela direita e a atual sai pela esquerda
     (ao voltar, o contrário) */
  .{p}-pag--sai-esq,.{p}-pag--sai-dir{{display:block;z-index:1;pointer-events:none;}}
  .{p}-pag--entra-dir,.{p}-pag--entra-esq{{z-index:2;pointer-events:none;}}
  .{p}-pag--entra-dir{{animation:{p}pagEntraDir .38s cubic-bezier(.25,.7,.25,1) both;}}
  .{p}-pag--sai-esq{{animation:{p}pagSaiEsq .38s cubic-bezier(.25,.7,.25,1) both;}}
  .{p}-pag--entra-esq{{animation:{p}pagEntraEsq .38s cubic-bezier(.25,.7,.25,1) both;}}
  .{p}-pag--sai-dir{{animation:{p}pagSaiDir .38s cubic-bezier(.25,.7,.25,1) both;}}
  @keyframes {p}pagEntraDir{{from{{translate:100% 0;}}to{{translate:0 0;}}}}
  @keyframes {p}pagSaiEsq{{from{{translate:0 0;opacity:1;}}to{{translate:-28% 0;opacity:.5;}}}}
  @keyframes {p}pagEntraEsq{{from{{translate:-28% 0;opacity:.5;}}to{{translate:0 0;opacity:1;}}}}
  @keyframes {p}pagSaiDir{{from{{translate:0 0;}}to{{translate:100% 0;}}}}
  /* ---- protótipo do app: fazendas e rotinas ---- */
  .{p}-appdiv:has(+ .{p}-appfaz:empty){{display:none;}}
  .{p}-app[data-proto] .{p}-corpo{{background:#e9e9e9;}}
  .{p}-app[data-proto] .{p}-form{{padding:2.6cqh 3cqw 0;}}
  .{p}-pergunta{{margin:0 0 1.6cqh;color:#333;font-size:2.3cqw;}}
  .{p}-busca{{height:5.6cqh;display:flex;align-items:center;background:#fff;border:1px solid #cfcfcf;border-radius:.5cqw;padding:0 2cqw;margin-bottom:3cqh;}}
  .{p}-busca{{position:relative;}}
  .{p}-busca input{{flex:1;min-width:0;height:100%;border:0;background:transparent;padding:0;color:#2b2b2b;font-size:2.4cqw;outline:none;}}
  .{p}-busca input::placeholder{{color:#a3a3a3;}}
  .{p}-busca .{p}-toque{{border-radius:.5cqw;}}
  .{p}-busca:focus-within .{p}-toque{{display:none;}}
  .{p}-faz.is-oculta{{display:none;}}
  .{p}-vazio{{display:none;color:#777;font-size:2.2cqw;font-style:italic;margin:1cqh 0;}}
  .{p}-vazio.is-visivel{{display:block;}}
  .{p}-busca svg{{width:2.6cqw;height:2.6cqw;color:#9a9a9a;}}
  .{p}-rotulo-lista{{margin:0 0 1.4cqh;color:#333;font-size:2.1cqw;}}
  .{p}-faz{{width:100%;height:5.6cqh;display:flex;align-items:center;background:#fff;border:1px solid #cfcfcf;border-radius:.4cqw;padding:0 1.8cqw 0 2cqw;margin:0 0 1.4cqh;color:#222;font-size:2.4cqw;text-align:left;cursor:pointer;transition:background .15s ease;}}
  .{p}-faz:hover{{background:#f1f7ee;}}
  .{p}-faz span{{flex:1;}}
  .{p}-faz svg{{width:2.4cqw;height:2.4cqw;color:#6e9a62;}}
  .{p}-marca-agua{{margin-top:auto;padding:4cqh 0;text-align:center;color:#c4c4c4;font-size:3.2cqw;font-weight:800;letter-spacing:.02em;}}
  .{p}-marca-agua span{{font-weight:400;}}
  .{p}-rot{{margin:0 0 2.4cqh;border-radius:.5cqw;overflow:hidden;box-shadow:0 .2cqh .5cqh rgba(0,0,0,.08);}}
  .{p}-rot__cab{{height:7cqh;display:flex;align-items:stretch;background:#fff;}}
  .{p}-rot__cab span{{flex:1;min-width:0;display:flex;align-items:center;padding-left:2.6cqw;color:#222;font-size:3.1cqw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}
  .{p}-rot__ic{{width:11cqw;flex:0 0 auto;border:0;border-left:1px solid #dcdcdc;background:transparent;color:#6e9a62;display:flex;align-items:center;justify-content:center;padding:0;}}
  .{p}-rot__ic svg{{width:4.1cqw;height:4.1cqw;}}
  .{p}-rot__ic:not(:disabled){{cursor:pointer;transition:background .15s ease;}}
  .{p}-rot__ic:not(:disabled):hover{{background:#eef5ea;}}
  .{p}-rot__cad{{background:#d9d9d9;padding:.9cqh 2.6cqw;color:#333;font-size:1.85cqw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}
  .{p}-fab{{position:absolute;right:3cqw;bottom:2.4cqh;width:11cqw;height:11cqw;border-radius:50%;border:.35cqw solid #b7cfab;background:#5a7d4a;color:#fff;box-shadow:0 .6cqh 1.4cqh rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center;z-index:2;}}
  .{p}-fab svg{{width:5cqw;height:5cqw;}}
  .{p}-appmenu{{border:0;background:transparent;padding:0;margin:0;color:#fff;display:flex;cursor:pointer;position:relative;}}
  /* hover dos ícones da barra do app: bola verde-clara cresce por trás do ícone */
  .{p}-appmenu::before{{content:"";position:absolute;left:50%;top:50%;width:4.6cqw;height:4.6cqw;border-radius:50%;background:#8fc47a;translate:-50% -50%;scale:0;opacity:0;transition:scale .18s cubic-bezier(.3,1.4,.5,1),opacity .18s ease;z-index:0;}}
  .{p}-appmenu:not(:disabled):hover::before{{scale:1;opacity:1;}}
  .{p}-appmenu svg{{position:relative;z-index:1;}}
  /* gaveta do menu sanduíche: escurece a tela e as opções deslizam da direita */
  .{p}-gaveta{{position:absolute;inset:0;z-index:8;visibility:hidden;transition:visibility 0s .38s;font-family:"Roboto","Segoe UI",Helvetica,Arial,sans-serif;}}
  .{p}-gaveta *{{font-family:inherit;}}
  .{p}-gaveta.is-aberta{{visibility:visible;transition-delay:0s;}}
  .{p}-gaveta__fundo{{position:absolute;inset:0;border:0;padding:0;margin:0;background:rgba(0,0,0,.62);opacity:0;transition:opacity .38s ease;cursor:pointer;}}
  .{p}-gaveta.is-aberta .{p}-gaveta__fundo{{opacity:1;}}
  .{p}-gaveta__painel{{position:absolute;top:0;right:0;bottom:0;width:46cqw;background:#4f7d3b;box-shadow:-.6cqw 0 2cqw rgba(0,0,0,.35);translate:100% 0;transition:translate .38s cubic-bezier(.25,.7,.25,1);overflow-y:auto;scrollbar-width:none;}}
  .{p}-gaveta__painel::-webkit-scrollbar{{display:none;}}
  .{p}-gaveta.is-aberta .{p}-gaveta__painel{{translate:0 0;}}
  .{p}-gaveta__item{{width:100%;height:6.7cqh;border:0;border-bottom:1px solid #6b9a55;background:transparent;display:flex;align-items:center;gap:2.2cqw;padding:0 2.4cqw;color:#fff;font-size:2.15cqw;text-align:left;white-space:nowrap;cursor:pointer;}}
  .{p}-gaveta__item:not(:disabled):hover{{background:#5c8c47;}}
  .{p}-gaveta__item:disabled{{color:rgba(255,255,255,.38);cursor:not-allowed;}}
  .{p}-gaveta__item:disabled svg{{color:rgba(191,224,163,.35);}}
  .{p}-gaveta__item svg{{width:2.8cqw;height:2.8cqw;color:#bfe0a3;flex:0 0 auto;}}
  .{p}-app[data-proto]::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:9cqh;background:linear-gradient(180deg,rgba(233,233,233,0),#e9e9e9 85%);pointer-events:none;}}
  /* link "Ver Ficha Completa" na barra lateral */
  .{p}-ficha{{margin:1.6cqh -1.9cqw 2.4cqh -2.2cqw;padding:1.6cqh 2.2cqw;background:#2b6a1f;color:#fff;display:flex;align-items:center;gap:1.4cqw;font-size:1.9cqw;font-style:italic;text-decoration:underline;white-space:nowrap;}}
  .{p}-ficha svg{{width:2.2cqw;height:2.2cqw;flex:0 0 auto;}}
  /* diálogo de confirmação */
  .{p}-dialogo{{position:absolute;left:29cqw;top:40cqh;width:42cqw;background:#fff;border-radius:.5cqw;padding:2.4cqh 2.6cqw 1.6cqh;box-shadow:0 1cqh 3cqh rgba(0,0,0,.4);}}
  .{p}-dialogo h4{{margin:0 0 1.4cqh;font-size:2.6cqw;font-weight:400;color:#222;}}
  .{p}-dialogo p{{margin:0 0 2.2cqh;font-size:2.1cqw;color:#555;}}
  .{p}-dialogo div{{display:flex;justify-content:flex-end;gap:1cqw;}}
  .{p}-dialogo button{{border:0;background:transparent;color:#222;font-size:1.9cqw;letter-spacing:.04em;padding:.6cqh 1.4cqw;cursor:pointer;border-radius:.4cqw;}}
  .{p}-dialogo button:hover{{background:#eee;}}
  /* resumo da rotina */
  .{p}-res{{margin:2.2cqh 0 0;padding:0;list-style:none;}}
  .{p}-res li{{display:flex;align-items:center;gap:2.2cqw;font-size:2.6cqw;color:#333;margin-bottom:1.4cqh;}}
  .{p}-res li svg{{width:3cqw;height:3cqw;color:#7aa070;flex:0 0 auto;}}
  .{p}-res li.{p}-res--sub{{margin:-.4cqh 0 3cqh 5.4cqw;font-size:1.9cqw;color:#777;font-style:italic;gap:1cqw;}}
  .{p}-res li.{p}-res--sub svg{{width:1.8cqw;height:1.8cqw;color:#333;}}
  .{p}-avancar--largo{{width:50cqw;}}
  /* opções em rádio (ex.: avaliação ovariana) */
  .{p}-radios{{display:grid;grid-template-columns:1fr 1fr;gap:1.8cqh 2cqw;}}
  .{p}-radio{{display:flex;align-items:center;gap:1.6cqw;border:0;background:transparent;padding:0;color:#333;font-size:2.4cqw;cursor:pointer;text-align:left;white-space:nowrap;}}
  .{p}-radio i{{width:2.8cqw;height:2.8cqw;border-radius:50%;border:.22cqw solid #555;box-sizing:border-box;flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;}}
  .{p}-radio.is-sel i{{border-color:#5a8a48;}}
  .{p}-radio.is-sel i::after{{content:"";width:1.3cqw;height:1.3cqw;border-radius:50%;background:#5a8a48;}}
  /* variantes escolhidas por um seletor (data-escolha): só a ativa aparece */
  .{p}-var[data-var].is-ativa{{display:contents;}}
  /* link "Histórico" no fim da barra lateral */
  .{p}-historico{{margin-top:1cqh;color:#fff;display:flex;align-items:center;gap:1cqw;font-size:1.9cqw;font-style:italic;text-decoration:underline;white-space:nowrap;}}
  .{p}-historico svg{{width:2cqw;height:2cqw;}}
  /* campo editável (ex.: peso) e botões desativados nas telas de demonstração */
  .{p}-entrada{{flex:1;min-width:0;height:100%;border:0;background:transparent;padding-left:2.6cqw;color:#2b2b2b;font-size:3.2cqw;outline:none;}}
  .{p}-entrada::placeholder{{color:#b9b9b9;}}
  .{p}-entrada.cc-hint{{border-radius:.6cqw;}}
  /* botão transparente por cima do campo: recebe o clique em toda a área (o campo nativo falha no 3D) */
  .{p}-input--toque{{position:relative;}}
  .{p}-toque{{position:absolute;inset:0;border:0;margin:0;padding:0;background:transparent;cursor:pointer;border-radius:.6cqw;}}
  .{p}-app button:disabled{{cursor:default;}}
  .{p}-dialogo button:disabled{{color:#b5b5b5;}}
  .{p}-dialogo button:disabled:hover{{background:transparent;}}
  .{p}-subacoes button:disabled{{opacity:1;}}
  /* painel sobreposto (ex.: cadastro da cria) */
  .{p}-modal{{position:absolute;inset:0;background:rgba(0,0,0,.45);display:none;z-index:5;}}
  .{p}-modal.is-aberto{{display:block;}}
  .{p}-painel{{position:absolute;left:21cqw;top:1.6cqh;width:58cqw;height:96.6cqh;background:#f7f7f7;display:flex;flex-direction:column;box-shadow:0 1cqh 3cqh rgba(0,0,0,.4);}}
  .{p}-painel-topo{{height:4.4cqh;background:#2e6b1f;color:#fff;display:flex;align-items:center;font-size:1.9cqw;font-weight:700;flex:0 0 auto;}}
  .{p}-painel-topo .{p}-volta{{width:5.5cqw;}}
  .{p}-painel-topo span{{margin-left:1.6cqw;}}
  .{p}-painel-topo em{{margin-left:auto;margin-right:1.6cqw;font-style:normal;font-weight:400;font-size:1.3cqw;display:flex;align-items:center;gap:.6cqw;}}
  .{p}-painel-topo em svg{{width:1.5cqw;height:1.5cqw;}}
  .{p}-painel-corpo{{flex:1;overflow-y:auto;scrollbar-width:none;padding:1.6cqh 2cqw 1.6cqh;display:flex;flex-direction:column;}}
  .{p}-painel-corpo::-webkit-scrollbar{{display:none;}}
  .{p}-painel-corpo h4{{margin:0 0 .5cqh;font-size:1.6cqw;color:#333;}}
  .{p}-painel-corpo h4+p{{margin:0 0 1.4cqh;font-size:1.5cqw;font-weight:700;color:#333;}}
  .{p}-painel-corpo .{p}-seg{{height:4.6cqh;margin-bottom:1.6cqh;}}
  .{p}-painel-corpo .{p}-seg button{{font-size:2cqw;}}
  .{p}-painel-corpo .{p}-campo{{margin-bottom:1.6cqh;}}
  .{p}-painel-corpo .{p}-campo label{{font-size:1.8cqw;margin-bottom:.7cqh;}}
  .{p}-painel-corpo .{p}-input{{height:4.8cqh;}}
  .{p}-painel-corpo .{p}-input span{{font-size:2.4cqw;padding-left:1.6cqw;}}
  .{p}-painel-corpo .{p}-bt{{width:4.6cqw;}}
  .{p}-painel-corpo .{p}-avancar{{width:19cqw;height:4.6cqh;font-size:2cqw;margin-top:1cqh;}}
  /* edição de rotina (Venda de Animais) */
  .{p}-rot-label{{margin:0 0 .9cqh;color:#4a4a4a;font-size:2.35cqw;}}
  .{p}-rot-titulo{{height:6cqh;border:1px solid #9cc48f;border-radius:.6cqw;background:#fff;display:flex;align-items:center;padding-left:2.6cqw;font-size:3.2cqw;color:#2b2b2b;margin-bottom:2.2cqh;}}
  .{p}-rot-card{{background:#fff;border-radius:.8cqw;box-shadow:0 .3cqh 1cqh rgba(0,0,0,.14);display:flex;}}
  .{p}-rot-alca{{width:6cqw;flex:0 0 auto;background:#ececec;border-radius:.8cqw 0 0 .8cqw;display:flex;align-items:center;justify-content:center;color:#9a9a9a;}}
  .{p}-rot-alca svg{{width:3cqw;height:3cqw;}}
  .{p}-rot-conteudo{{flex:1;min-width:0;padding:1.8cqh 2.4cqw 2cqh;}}
  .{p}-rot-cab{{display:flex;align-items:center;font-size:2.1cqw;font-weight:700;color:#222;margin-bottom:1.6cqh;}}
  .{p}-rot-cab svg{{margin-left:auto;width:2.6cqw;height:2.6cqw;color:#222;}}
  .{p}-rot-grade{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6cqh 2.4cqw;}}
  .{p}-chip{{background:#dcefd3;border:1px solid #9cc48f;border-radius:.5cqw;padding:.9cqh 1.6cqw;min-height:5.9cqh;min-width:0;}}
  .{p}-chip small{{display:block;color:#3d7029;font-size:1.5cqw;margin-bottom:.4cqh;white-space:nowrap;}}
  .{p}-chip b{{display:block;color:#1f3d14;font-weight:400;font-size:2.3cqw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}
  .{p}-rot-botoes{{margin-top:auto;display:flex;justify-content:flex-end;gap:1.6cqw;padding-top:2cqh;}}
  .{p}-rot-botoes button{{height:6cqh;padding:0 3.4cqw;border:.25cqw solid #7d9a78;border-radius:999px;background:#40603b;color:#fff;font-size:2.8cqw;display:flex;align-items:center;gap:1cqw;cursor:pointer;box-shadow:0 .5cqh 1.2cqh rgba(0,0,0,.28);}}
  .{p}-rot-botoes button svg{{width:2.4cqw;height:2.4cqw;}}
  /* conferência de lote (resumo do dia) */
  .{p}-conf-cab{{display:flex;align-items:baseline;margin-bottom:1.6cqh;}}
  .{p}-conf-cab b{{font-size:2.6cqw;color:#222;font-weight:500;}}
  .{p}-conf-cab i{{margin-left:auto;font-size:1.7cqw;color:#555;}}
  .{p}-conf-resumo{{display:flex;border:1px solid #c9c9c9;border-radius:.6cqw;background:#fff;margin-bottom:2.6cqh;}}
  .{p}-conf-resumo div{{flex:1;display:flex;align-items:center;justify-content:space-between;padding:1.6cqh 1.8cqw;min-width:0;}}
  .{p}-conf-resumo div+div{{border-left:1px solid #d6d6d6;}}
  .{p}-conf-resumo small{{font-size:1.75cqw;color:#333;line-height:1.3;}}
  .{p}-conf-resumo b{{font-size:4.2cqw;color:#1f3d14;font-weight:500;}}
  .{p}-lote{{border-top:1px solid #dcdcdc;padding:1.8cqh 3.6cqw 0 4.2cqw;margin:0 -3.6cqw 1.6cqh -4.2cqw;}}
  .{p}-lote-cab{{display:flex;align-items:center;gap:1cqw;font-size:2.2cqw;color:#222;margin-bottom:1.4cqh;}}
  .{p}-lote-cab svg{{width:2.4cqw;height:2.4cqw;color:#7aa070;}}
  .{p}-lote-cab span{{margin-left:auto;display:flex;align-items:center;gap:.8cqw;}}
  .{p}-lote-cab span svg{{color:#6e9a62;}}
  .{p}-lote-tab{{border:1px solid #c9c9c9;border-radius:.6cqw;overflow:hidden;background:#fff;}}
  .{p}-lote-tab div{{display:grid;grid-template-columns:2.2fr 1fr 1fr 1fr;align-items:center;}}
  .{p}-lote-tab div:first-child{{background:#ececec;font-size:1.9cqw;font-weight:700;color:#333;padding:1.2cqh 1cqw;}}
  .{p}-lote-tab div:first-child span{{text-align:center;}}
  .{p}-lote-tab div:first-child span:first-child{{text-align:left;padding-left:3.6cqw;}}
  .{p}-lote-tab div:last-child{{font-size:3.4cqw;color:#1f3d14;padding:1.6cqh 1cqw;}}
  .{p}-lote-tab div:last-child span{{display:flex;align-items:center;justify-content:center;gap:.6cqw;}}
  .{p}-lote-tab div:last-child span:first-child{{justify-content:flex-start;padding-left:3.6cqw;}}
  .{p}-lote-tab div:last-child span svg{{width:3.3cqw;height:3.3cqw;color:#6e9a62;}}
  .{p}-lote-tab .{p}-vermelho{{color:#d32f2f;}}
  .{p}-lote-tab small{{font-size:2.3cqw;color:#333;margin-left:1cqw;}}
  .{p}-conf-rodape{{margin-top:auto;font-size:1.4cqw;color:#777;font-style:italic;}}

  /* ===== cena da Identificação Eletrônica: boi atrás do tablet e bastão leitor à esquerda ===== */
  .{p}-cena{{position:absolute;inset:0;pointer-events:none;}}
  .{p}-boi{{position:absolute;left:var(--boi-x,74%);top:var(--boi-y,37%);width:var(--boi-w,36%);z-index:3;transform-origin:70% 95%;}}
  .{p}-boi img{{display:block;width:100%;height:auto;}}
  .{p}-bastao{{position:absolute;left:var(--bas-x,49%);top:var(--bas-y,46%);height:var(--bas-h,50%);z-index:4;transform-origin:50% 90%;
    transition:translate 1.3s cubic-bezier(.4,0,.2,1),rotate 1.3s cubic-bezier(.4,0,.2,1);}}
  .{p}-bastao img{{display:block;height:100%;width:auto;filter:drop-shadow(0 .8cqh 1.4cqh rgba(0,0,0,.3));}}
  .{p}-led{{position:absolute;left:31.5%;top:68.5%;width:7%;aspect-ratio:1;border-radius:50%;background:#2a2a2a;box-shadow:inset 0 0 .2cqh #000;transition:background .25s ease,box-shadow .25s ease;}}
  .{p}-cena.is-ligado .{p}-led{{background:#5dff3a;box-shadow:0 0 .8cqh .3cqh rgba(93,255,58,.85),0 0 2cqh .6cqh rgba(93,255,58,.45);}}
  .{p}-cena.is-lendo .{p}-led{{animation:{p}ledPisca .18s steps(2) 4;}}
  @keyframes {p}ledPisca{{to{{background:#2a2a2a;box-shadow:none;}}}}
  .{p}-onda{{position:absolute;left:var(--onda-x,0);top:var(--onda-y,0);width:3cqw;aspect-ratio:1;border-radius:50%;border:.35cqw solid rgba(93,255,58,.9);translate:-50% -50%;opacity:0;z-index:5;}}
  .{p}-cena.is-lendo .{p}-onda{{animation:{p}onda .7s ease-out 2;}}
  @keyframes {p}onda{{0%{{opacity:.9;scale:.3;}}100%{{opacity:0;scale:2.2;}}}}
  /* entrada: depois que o tablet estaciona, o bastão desliza da esquerda e a vaca da direita, em fade, desacelerando */
  .{p}-boi,.{p}-bastao{{opacity:0;transition:translate 1.3s cubic-bezier(.4,0,.2,1),rotate 1.3s cubic-bezier(.4,0,.2,1);}}
  .{p}.is-active .{p}-bastao{{opacity:1;animation:{p}entraEsq 1.1s cubic-bezier(.22,.78,.28,1) 1.5s backwards;}}
  .{p}.is-active .{p}-boi{{opacity:1;animation:{p}entraDir 1.1s cubic-bezier(.22,.78,.28,1) 1.5s backwards;}}
  @keyframes {p}entraEsq{{from{{opacity:0;translate:-9cqw 0;}}to{{opacity:1;translate:0 0;}}}}
  @keyframes {p}entraDir{{from{{opacity:0;translate:9cqw 0;}}to{{opacity:1;translate:0 0;}}}}
  .{p}-cena.is-lendo .{p}-boi{{animation:{p}entraDir 1.1s cubic-bezier(.22,.78,.28,1) 1.5s backwards,{p}boiBalanca .7s ease-in-out;}}
  @keyframes {p}boiBalanca{{0%,100%{{rotate:0deg;}}25%{{rotate:-3deg;}}55%{{rotate:2.5deg;}}80%{{rotate:-1.2deg;}}}}
  .{p}-cena.is-no-boi .{p}-bastao{{translate:var(--bas-dx,0) var(--bas-dy,0);rotate:var(--bas-rot,0deg);}}
  /* estado do bastão na tela do app */
  .{p}-nota--erro{{color:#d32f2f;}}
  .{p}-nota--erro u{{color:#d32f2f;}}
  .{p}-nota button{{border:0;background:transparent;padding:0;font:inherit;color:inherit;text-decoration:underline;cursor:pointer;}}
  .{p}-ident span{{letter-spacing:.04em;}}

  /* ===== slide de protótipo: faixa verde do cabeçalho, título e texto à esquerda ===== */
  .{p}--proto{{background:#fff;}}
  .{p}-faixa{{position:absolute;left:0;top:0;width:100%;height:13.2%;display:block;z-index:2;pointer-events:none;}}
  .{p}-topo{{
    position:absolute;left:1.1%;top:0;height:10.21%;margin:0;z-index:3;
    display:flex;align-items:center;gap:1.5cqw;
    color:#fff;font-size:4.3cqh;font-weight:600;letter-spacing:-.03em;white-space:nowrap;
  }}
  .{p}-topo img{{height:7.4cqh;width:auto;display:block;filter:drop-shadow(0 .3cqh .5cqh rgba(0,0,0,.25));}}
  .{p}-ptit{{position:absolute;left:4.9%;top:{top(17.8,5.2,1.05)}%;margin:0;color:#3f5f40;font-size:5.2cqh;font-weight:800;line-height:1.05;letter-spacing:-.03em;white-space:nowrap;}}
  .{p}-ppil{{position:absolute;left:5.1%;top:36%;width:3.6%;height:2.9%;border-radius:999px;background:#2a8fa0;}}
  .{p}-ptexto{{position:absolute;left:11.6%;top:{top(36,3.7,1.5)}%;width:40%;margin:0;color:#435f47;font-size:3.7cqh;font-weight:500;line-height:1.5;letter-spacing:-.02em;}}
  /* blocos de texto à esquerda: cada tela do protótipo pode trocar o texto (data-texto); sem texto próprio, volta ao padrão */
  .{p}-pbloco{{position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .35s ease;}}
  .{p}-pbloco.is-ativo{{opacity:1;}}
  .{p}-pb-tit{{position:absolute;left:4.3%;top:{top(16.8,4.9,1)}%;margin:0;color:#3f5f40;font-size:4.9cqh;font-weight:800;line-height:1;letter-spacing:-.03em;white-space:nowrap;}}
  .{p}-pb-item{{position:absolute;margin:0;color:#435f47;font-weight:500;letter-spacing:-.02em;}}
  .{p}-pb-item--g{{left:13.2%;font-size:4.1cqh;line-height:1.35;}}
  .{p}-pb-item--p{{left:12.9%;font-size:3.7cqh;line-height:1.2;}}
  .{p}-pb-pil{{position:absolute;height:2.7%;border-radius:999px;}}
  .{p}-pb-pil--g{{left:4.4%;width:5.2%;}}
  .{p}-pb-pil--p{{left:7.5%;width:2.2%;}}
  .{p}-pb-caixa{{position:absolute;left:4.3%;top:88%;height:5.5%;margin:0;padding-right:1.6%;background:#c9edc0;color:#3f5f40;font-size:3.4cqh;font-weight:500;display:flex;align-items:center;padding-left:1.4%;letter-spacing:-.02em;white-space:nowrap;}}
  /* janela suspensa (detalhe do lote), ao lado do tablet */
  .{p}-popup{{position:absolute;left:44.2%;top:31%;width:18.2%;height:53%;z-index:5;display:flex;flex-direction:column;
    background:#f2f2f2;border-radius:1.2cqh;box-shadow:0 1.2cqh 3cqh rgba(0,0,0,.32);overflow:hidden;
    font-family:"Roboto","Segoe UI",Helvetica,Arial,sans-serif;color:#333;opacity:0;scale:.92;pointer-events:none;transform-origin:100% 25%;transition:opacity .3s ease,scale .3s ease;}}
  .{p}-popup *{{font-family:inherit;box-sizing:border-box;}}
  .{p}-popup.is-aberto{{opacity:1;scale:1;pointer-events:auto;}}
  .{p}-popup__seta{{position:absolute;right:-1.2cqh;top:24%;width:0;height:0;border:1.2cqh solid transparent;border-left-color:#dcdcdc;border-right:0;}}
  .{p}-popup__cab{{flex:0 0 auto;padding:2.2cqh 1.3cqw 1.6cqh;background:linear-gradient(180deg,#ececec,#d6d6d6);font-size:2.2cqh;color:#333;}}
  .{p}-popup__corpo{{flex:1;min-height:0;padding:1.8cqh 1cqw 1cqh;display:flex;flex-direction:column;}}
  .{p}-popup__n{{margin:0 0 1.6cqh;font-size:2.5cqh;}}
  .{p}-popup table{{width:100%;border-collapse:collapse;font-size:1.85cqh;}}
  .{p}-popup th{{font-weight:500;font-size:2cqh;padding:.5cqh 0 .7cqh;border-bottom:.15cqh solid #444;text-align:center;}}
  .{p}-popup td{{padding:.75cqh 0;text-align:center;color:#444;}}
  .{p}-popup tr:nth-child(even) td{{background:#e6e6e6;}}
  .{p}-popup__rod{{flex:0 0 auto;padding:1.4cqh 1cqw 1.6cqh;background:linear-gradient(180deg,#d8d8d8,#c8c8c8);}}
  .{p}-popup__rod label{{display:block;font-size:1.9cqh;margin-bottom:.8cqh;color:#333;}}
  .{p}-popup__rod label b{{color:#d32f2f;font-weight:400;}}
  .{p}-popup__linha{{display:flex;align-items:center;background:#fff;border-radius:.9cqh;padding:.5cqh .5cqh .5cqh 1.2cqh;}}
  .{p}-popup__linha span{{flex:1;color:#b5b5b5;font-size:2.3cqh;}}
  .{p}-popup__linha button{{border:0;border-radius:999px;background:#3f6b3a;color:#fff;font-size:1.9cqh;padding:1.1cqh 1.4cqw;cursor:default;}}
  /* janela modal dentro do app (ex.: detalhe dos faltantes): fundo escuro, barra de título e X */
  .{p}-janela{{position:absolute;left:11cqw;top:16cqh;width:78cqw;max-height:70cqh;background:#f2f2f2;border-radius:.6cqw;box-shadow:0 1cqh 3cqh rgba(0,0,0,.45);display:flex;flex-direction:column;overflow:hidden;}}
  .{p}-janela__topo{{flex:0 0 auto;height:4.6cqh;background:#2e6b1f;color:#fff;display:flex;align-items:center;padding-left:2.2cqw;font-size:2cqw;font-weight:700;}}
  .{p}-janela__x{{margin-left:auto;width:6.5cqw;height:100%;border:0;background:transparent;color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;}}
  .{p}-janela__x:hover{{background:rgba(255,255,255,.14);}}
  .{p}-janela__x svg{{width:2.4cqw;height:2.4cqw;}}
  .{p}-janela__corpo{{padding:1.8cqh 2.4cqw 1.2cqh;overflow-y:auto;scrollbar-width:none;}}
  .{p}-janela__corpo::-webkit-scrollbar{{display:none;}}
  .{p}-janela__lote{{margin:0 0 1.4cqh;font-size:2.4cqw;color:#333;}}
  .{p}-janela__n{{margin:0 0 1.2cqh;font-size:2.7cqw;color:#222;}}
  .{p}-janela table{{width:100%;border-collapse:collapse;font-size:2.1cqw;}}
  .{p}-janela th{{font-weight:500;font-size:2.2cqw;padding:.6cqh 0 .8cqh;border-bottom:.15cqh solid #444;text-align:center;}}
  .{p}-janela td{{padding:.9cqh 0;text-align:center;color:#444;}}
  .{p}-janela tr:nth-child(even) td{{background:#e4e4e4;}}
  .{p}-janela__rod{{flex:0 0 auto;padding:1.4cqh 2.4cqw 1.8cqh;background:linear-gradient(180deg,#dcdcdc,#cdcdcd);}}
  .{p}-janela__rod label{{display:block;font-size:2.1cqw;margin-bottom:.8cqh;color:#333;}}
  .{p}-janela__rod label b{{color:#d32f2f;font-weight:400;}}
  .{p}-janela__linha{{display:flex;align-items:center;background:#fff;border-radius:.9cqh;padding:.6cqh .6cqh .6cqh 1.6cqw;}}
  .{p}-janela__linha span{{flex:1;color:#b5b5b5;font-size:2.5cqw;}}
  .{p}-janela__linha button{{border:0;border-radius:999px;background:#3f6b3a;color:#fff;font-size:2.1cqw;padding:1.2cqh 2.6cqw;cursor:default;}}
  /* ---- seleção de eventos (nova rotina) ---- */
  .{p}-grupo{{margin:1.2cqh 0 0;}}
  .{p}-grupo.is-oculta{{display:none;}}
  .{p}-grupo__t{{margin:0;padding:1cqh 0 .8cqh;font-size:2.1cqw;color:#333;border-bottom:1px solid #c9c9c9;}}
  .{p}-evt{{width:100%;height:5.9cqh;border:0;border-bottom:1px solid #d0d0d0;background:transparent;display:flex;align-items:center;gap:2.2cqw;padding:0 .6cqw;color:#222;font-size:2.55cqw;text-align:left;white-space:nowrap;cursor:pointer;transition:background .15s ease;}}
  .{p}-evt.is-oculta{{display:none;}}
  .{p}-evt i{{width:3cqw;height:3cqw;border:.16cqw solid #8a8a8a;border-radius:.4cqw;background:#fff;flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;color:#fff;}}
  .{p}-evt i svg{{width:2cqw;height:2cqw;opacity:0;}}
  .{p}-evt.is-marcado{{background:#d8ecc6;}}
  .{p}-evt.is-marcado i{{background:#6e9a62;border-color:#6e9a62;}}
  .{p}-evt.is-marcado i svg{{opacity:1;}}
  .{p}-continuar{{font-weight:500;}}
  .{p}-continuar:disabled{{opacity:.45;}}
  .{p}-continuar:not(:disabled){{background:#2b5a1e;}}
  /* ---- edição da rotina: título e slots de eventos ---- */
  .{p}-busca input.{p}-titulo-input{{width:100%;height:6cqh;border:1px solid #9cc48f;border-radius:.6cqw;background:#fff;padding:0 2.6cqw;font-size:3.2cqw;color:#2b2b2b;outline:none;margin-bottom:2.2cqh;}}
  .{p}-busca input.{p}-titulo-input::placeholder{{color:#b9b9b9;}}
  .{p}-slot{{display:flex;background:#fff;border-radius:.6cqw;box-shadow:0 .3cqh 1cqh rgba(0,0,0,.14);margin-bottom:2.2cqh;position:relative;}}
  .{p}-slot.is-arrastando{{box-shadow:0 1.2cqh 2.6cqh rgba(0,0,0,.32);scale:1.02;z-index:3;}}
  .{p}-slot__alca{{width:7cqw;flex:0 0 auto;background:#efefef;border-radius:.6cqw 0 0 .6cqw;display:flex;align-items:center;justify-content:center;color:#9a9a9a;cursor:grab;touch-action:none;user-select:none;}}
  .{p}-slot__alca:active{{cursor:grabbing;}}
  .{p}-slot__alca svg{{width:3.2cqw;height:3.2cqw;}}
  .{p}-slot__conteudo{{flex:1;min-width:0;padding:1.8cqh 2.4cqw 2cqh;}}
  .{p}-slot__cab{{display:flex;align-items:center;gap:.8cqw;font-size:2.5cqw;font-weight:500;color:#222;margin-bottom:1.6cqh;}}
  .{p}-slot__lixo{{margin-left:auto;border:0;background:transparent;padding:0;color:#222;display:flex;cursor:pointer;}}
  .{p}-slot__lixo svg{{width:2.8cqw;height:2.8cqw;}}
  .{p}-info-v{{width:2.2cqw;height:2.2cqw;border-radius:50%;background:#6e9a62;color:#fff;font:italic 700 1.4cqw/2.2cqw Georgia,serif;text-align:center;display:inline-block;}}
  .{p}-slot__grade{{display:grid;grid-template-columns:1fr 1fr;gap:1.4cqh 2cqw;}}
  .{p}-slot__grade--4{{grid-template-columns:repeat(4,1fr);}}
  .{p}-slot__grade .{p}-chip--largo{{grid-column:1 / -1;}}
  .{p}-chip--amarelo{{background:#eeeab8;border-color:#d9d08a;}}
  .{p}-chip--vazio{{background:#fff;border:.16cqw dashed #bdbdbd;display:flex;align-items:center;}}
  .{p}-chip--vazio b{{color:#9a9a9a;font-size:2.3cqw;}}
  .{p}-chip b{{white-space:normal;}}
  .{p}-slot__sub{{margin:0 0 1.2cqh;font-size:2.3cqw;font-weight:500;color:#333;}}
  .{p}-slot__link{{display:inline-block;margin-top:1.6cqh;font-size:2.3cqw;color:#333;text-decoration:underline;}}
  .{p}-fixo{{position:absolute;left:0;right:0;bottom:0;padding:5cqh 3cqw 2cqh;display:flex;justify-content:flex-end;gap:1.6cqw;background:linear-gradient(180deg,rgba(247,247,247,0),#f7f7f7 45%);z-index:2;pointer-events:none;}}
  .{p}-fixo button{{pointer-events:auto;height:6cqh;padding:0 3.4cqw;border:.25cqw solid #7d9a78;border-radius:999px;background:#40603b;color:#fff;font-size:2.8cqw;display:flex;align-items:center;gap:1cqw;cursor:pointer;box-shadow:0 .5cqh 1.2cqh rgba(0,0,0,.28);}}
  .{p}-fixo button svg{{width:2.4cqw;height:2.4cqw;}}
  .{p}-fixo button:not(:disabled):hover{{filter:brightness(1.12);}}
  .{p}-fixo button:disabled{{background:#9a9a9a;border-color:#c4c4c4;color:#f0f0f0;cursor:default;box-shadow:none;}}
  /* ---- lotes de IATF: acordeão por propriedade com grade de lotes ---- */
  .{p}-acc{{border-bottom:1px solid #b7d4a6;margin:0 -3.6cqw 0 -4.2cqw;padding:0 3.6cqw 0 4.2cqw;}}
  .{p}-acc__cab{{width:100%;border:0;background:transparent;display:flex;align-items:center;gap:1.6cqw;padding:2cqh 0 1.8cqh .4cqw;color:#222;font-size:2.5cqw;text-align:left;cursor:pointer;white-space:nowrap;}}
  .{p}-acc__cab b{{font-weight:500;}}
  .{p}-acc__cab svg{{width:2.2cqw;height:2.2cqw;color:#6e9a62;flex:0 0 auto;rotate:-90deg;transition:rotate .25s ease;}}
  .{p}-acc.is-aberto .{p}-acc__cab svg{{rotate:0deg;}}
  .{p}-acc__corpo{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .32s ease;}}
  .{p}-acc__corpo > div{{overflow:hidden;}}
  .{p}-acc.is-aberto .{p}-acc__corpo{{grid-template-rows:1fr;}}
  .{p}-lotes{{border:1px solid #c9c9c9;border-radius:.5cqw;overflow:hidden;background:#fff;margin:0 0 2.4cqh;}}
  .{p}-lotes div{{display:grid;grid-template-columns:2.7fr 1.3fr 1fr .9fr .9fr 1.15fr .6fr;align-items:center;padding:0 1cqw 0 2.2cqw;height:5.6cqh;border-top:1px solid #e3e3e3;font-size:2.15cqw;color:#222;}}
  .{p}-lotes div:first-child{{background:#ececec;border-top:0;color:#333;}}
  .{p}-lotes span{{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}
  .{p}-lotes .{p}-lupa{{justify-self:end;}}
  .{p}-lotes .{p}-lupa svg{{width:2.8cqw;height:2.8cqw;}}
  .{p}-lupa{{border:0;background:transparent;padding:0;margin:0;color:#6e9a62;display:inline-flex;cursor:pointer;}}
  .{p}-lupa svg{{width:3.3cqw;height:3.3cqw;}}
  .{p}-lupa:hover svg{{color:#3d7029;scale:1.15;}}
  .{p}-topo,.{p}-ptit,.{p}-ppil,.{p}-ptexto{{transition:opacity .5s ease var(--d,0s),translate .58s cubic-bezier(.22,.78,.28,1) var(--d,0s);}}
  .{p}:not(.is-active) .{p}-topo{{opacity:0;translate:0 -40%;}}
  .{p}:not(.is-active) :is(.{p}-ptit,.{p}-ppil,.{p}-ptexto){{opacity:0;translate:-6% 0;}}
  .{p}.is-active :is(.{p}-topo,.{p}-ptit,.{p}-ppil,.{p}-ptexto){{opacity:1;translate:none;}}

  /* ---- Entrada: textos pela esquerda, foto pela direita, tablet em fade subindo com giro ---- */
  .{p}-eyebrow,.{p}-titulo,.{p}-tag,.{p}-pilula,.{p}-texto,.{p}-foto,.{p}-barra-teal,.{p}-palco{{
    transition:opacity .6s ease var(--d,0s),translate .65s cubic-bezier(.22,.78,.28,1) var(--d,0s);
  }}
  .{p}-palco{{transition-duration:.8s,1s;}}
  .{p}:not(.is-active) :is(.{p}-eyebrow,.{p}-titulo,.{p}-tag,.{p}-pilula,.{p}-texto){{opacity:0;translate:-6% 0;}}
  .{p}:not(.is-active) :is(.{p}-foto,.{p}-barra-teal){{opacity:0;translate:8% 0;}}
  .{p}:not(.is-active) .{p}-palco{{opacity:0;translate:0 10%;}}
  .{p}.is-active :is(.{p}-eyebrow,.{p}-titulo,.{p}-tag,.{p}-pilula,.{p}-texto,.{p}-foto,.{p}-barra-teal,.{p}-palco){{opacity:1;translate:none;}}
  @media (prefers-reduced-motion:reduce){{
    .{p} :is(.{p}-eyebrow,.{p}-titulo,.{p}-tag,.{p}-pilula,.{p}-texto,.{p}-foto,.{p}-barra-teal,.{p}-palco){{transition:none;opacity:1;translate:none;}}
    .{p} .{p}-giro{{transition:none;transform:none;}}
  }}

'''

# ======================================================================= componentes da tela
def campo(p, rotulo, valor, ativo=True, obrig=False, bt='lixo', ph=False, extra=''):
    """campo com rótulo e caixa; bt: 'lixo' | 'lupa' | 'link' | None; ph=True mostra o valor como placeholder."""
    ob = ' <b>*</b>' if obrig else ''
    cls = f'{p}-input' + ('' if ativo else f' {p}-input--off')
    rot_bt = 'Limpar' if bt == 'lixo' else 'Buscar'
    btn = f'<button class="{p}-bt" type="button" aria-label="{rot_bt}"{"" if ativo else " disabled"}>{ICO[bt]}</button>' if bt else ''
    sp = f'<span class="{p}-ph">{valor}</span>' if ph else f'<span>{valor}</span>'
    return f'<div class="{p}-campo"><label>{rotulo}{ob}{extra}</label><div class="{cls}">{sp}{btn}</div></div>'

def seg(p, rotulo, opcoes, sel, obrig=False, sexo=False, escolha=None):
    """escolha: lista de nomes de variante (um por opção); o botão clicado ativa .{p}-var[data-var=nome]."""
    SEL = ' class="is-sel"'
    VAR = lambda i: f' data-var="{escolha[i]}"' if escolha else ''
    bts = ''.join(f'<button type="button" data-opcao{SEL if i == sel else ""}{VAR(i)}>{o}</button>' for i, o in enumerate(opcoes))
    ob = ' <b>*</b>' if obrig else ''
    lab = f'<label>{rotulo}{ob}</label>' if rotulo else ''
    attr = ' data-sexo' if sexo else (' data-escolha' if escolha else '')
    return f'<div class="{p}-campo">{lab}<div class="{p}-seg" role="group"{attr}>{bts}</div></div>'

def radios(p, rotulo, opcoes, sel=0):
    SEL = ' is-sel'
    bts = ''.join(f'<button type="button" class="{p}-radio{SEL if i == sel else ""}" data-radio><i></i>{o}</button>' for i, o in enumerate(opcoes))
    return f'<div class="{p}-campo" data-radios><label>{rotulo}</label><div class="{p}-radios">{bts}</div></div>'

def variante(p, nome, html, ativa=False):
    return f'<div class="{p}-var" data-var="{nome}"{" class=is-ativa" if False else ""}>{html}</div>' if not ativa else f'<div class="{p}-var is-ativa" data-var="{nome}">{html}</div>'

def passos(p, rotulo, valor, obrig=True):
    ob = ' <b>*</b>' if obrig else ''
    return (f'<div class="{p}-campo" data-passos><label>{rotulo}{ob}</label>'
            f'<div class="{p}-input {p}-input--off"><span data-valor="{valor}">{valor}</span></div>'
            f'<div class="{p}-passos"><button type="button" data-passo="1">+1</button><button type="button" data-passo="0.5">+0,5</button>'
            f'<button type="button" data-passo="0.25">+0,25</button><button type="button" data-passo="0" aria-label="Zerar">{ICO["lixo"]}</button></div></div>')

def area(p, rotulo, ph='Digite'):
    return f'<div class="{p}-campo"><label>{rotulo}</label><div class="{p}-area">{ph}</div></div>'

def lista(p, rotulo, itens, obrig=False, mais=None, relogio=False, vazio=None, attr='', escuro=False):
    """itens: [(texto, lixo?)]; mais: data-acao do botão +; vazio: texto quando a lista está vazia."""
    ob = '<b>*</b>' if obrig else ''
    m = f'<i class="{p}-mais" role="button" data-acao="{mais}" aria-label="Adicionar">{ICO["mais"]}</i>' if mais else ''
    r = f'<i class="{p}-relogio" aria-hidden="true">{ICO["relogio"]}</i>' if relogio else ''
    cls_bt = ' class="is-escuro"' if escuro else ''
    li = ''.join(f'<li class="{p}-item"><span>{t}</span>' + (f'<button type="button"{cls_bt} data-acao="remover" aria-label="Remover">{ICO["lixo"]}</button>' if lx else '') + '</li>' for t, lx in itens)
    if not itens and vazio:
        li = f'<li class="{p}-item {p}-item--vazio" data-vazio>{vazio}</li>'
    vt = f' data-vazio-texto="{vazio}"' if vazio else ''
    return f'<div class="{p}-campo"{attr}><label>{rotulo}{ob}{m}{r}</label><ul class="{p}-lista"{vt}>{li}</ul></div>'

def linha(p, *campos):
    return f'<div class="{p}-linha">{"".join(campos)}</div>'

def lado(p, id_, pares, caixas, lapis=True, ficha=False, historico=False):
    """barra lateral do animal: id, pares (rótulo, valor), caixas (rótulo, texto, 'verde'|'amarela'[, alta])."""
    lp = f'<i>{ICO["lapis"]}</i>' if lapis else ''
    ps = ''.join(f'<p class="{p}-par"><small>{r}</small><b>{v}</b></p>' for r, v in pares)
    cs = ''
    for c in caixas:
        r, t, cor = c[0], c[1], c[2]; alta = len(c) > 3 and c[3]
        cls = f'{p}-caixa' + (f' {p}-caixa--amarela' if cor == 'amarela' else '') + (f' {p}-caixa--alta' if alta else '')
        cs += f'<div class="{cls}"><small>{r}</small><div>{t}</div></div>'
    sep = f'<div class="{p}-ficha">{ICO["ficha"]}Ver Ficha Completa</div>' if ficha else f'<div class="{p}-hr"></div>'
    hist = f'<div class="{p}-historico">{ICO["relogio"]}Histórico</div>' if historico else ''
    return f'<aside class="{p}-lado"><p class="{p}-id">{id_}{lp}</p>{ps}{sep}{cs}{hist}</aside>'

def tit(p, texto, info=True):
    i = f' <i class="{p}-info" aria-hidden="true">i</i>' if info else ''
    return f'<h3 class="{p}-tit">{texto}{i}</h3>'

def obs(p, t='Este evento é obrigatório.'):
    return f'<p class="{p}-obs">{t}</p>'

def avancar(p):
    return f'<button class="{p}-avancar" type="button" data-acao="avancar">AVANÇAR</button>'

def app(p, fazenda, sub, corpo, lado_html='', modal='', attrs='', gaveta=False, vaca=None):
    """monta a tela completa. sub: ('execucao', data) | ('titulo', texto, acoes_html)."""
    volta = f'<button class="{p}-volta" type="button" aria-label="Voltar">{ICO["chevron"]}</button>'
    if sub[0] == 'execucao':
        subbar = f'{volta}<span class="{p}-subtxt">Execução em {sub[1]}</span>'
    elif sub[0] == 'simples':
        subbar = f'<span class="{p}-subtxt">{sub[1]}</span>{sub[2]}'
    else:
        subbar = f'{volta}<span class="{p}-subtxt">{sub[1]}</span>{sub[2]}'
    cl = f'{p}-corpo' + (f' {p}-corpo--lado' if lado_html else '')
    return (f'<div class="{p}-app"{attrs}>'
            f'<header class="{p}-appbar"><img class="{p}-applogo" src="assets/confinamento/logo-mb-curral-h.webp?v=2" alt="MB Curral">'
            f'<span class="{p}-appdiv"></span><span class="{p}-appfaz">{fazenda}</span>'
            f'<span class="{p}-appicos">' + (f'<button class="{p}-appmenu" type="button" data-acao="{vaca}" aria-label="Animais Faltantes">{ICO["vaca"]}</button>' if vaca else ICO['vaca']) + f'{ICO["grafico"]}{ICO["alerta"]}'
            + (f'<button class="{p}-appmenu" type="button" data-acao="gaveta" aria-label="Menu">{ICO["menu"]}</button>' if gaveta else ICO['menu']) + '</span></header>'
            f'<div class="{p}-subbar">{subbar}</div>'
            f'<div class="{cl}">{lado_html}<div class="{p}-form">{corpo}</div></div>{modal}</div>')

# ======================================================================= slide
ACOES = ('ir:', 'nav:', 'nav-volta:', 'popup:', 'focar', 'evt-toggle', 'evt-continuar', 'slot-excluir', 'slot-excluir-sim', 'rotina-salvar', 'rotina-editar', 'rotina-nova', 'gaveta', 'gaveta-fechar', 'gaveta-inicio', 'gaveta-ir:', 'acordeao', 'fechar', 'remover', 'abrir-cria', 'fechar-cria', 'salvar-cria', 'tocar-peso', 'reconectar')

def desativa_sem_acao(tela_html):
    """Botões da tela do app sem comportamento programado ficam disabled: não piscam, não mostram a mãozinha
    e não enganam o usuário. Funcionais: seletores (data-opcao), passos, rádios e data-acao conhecidas."""
    def troca(m):
        tag = m.group(0)
        if ' disabled' in tag or 'data-opcao' in tag or 'data-passo' in tag or 'data-radio' in tag: return tag
        acao = re.search(r'data-acao="([^"]*)"', tag)
        if acao and acao.group(1).startswith(ACOES): return tag
        return tag.replace('<button ', '<button disabled ', 1)
    return re.sub(r'<button [^>]*>', troca, tela_html)

def html(p, n, ev, tela_html, voltar):
    """ev: titulo (com <br> se tiver 2 linhas), tag, texto (com <br>), aria, linhas (1|2)."""
    tela_html = desativa_sem_acao(tela_html)
    nn = str(n).zfill(2)
    camadas = ''.join(f'<div class="{p}-camada" style="transform:translateZ(-{k*0.14:.2f}cqw)"></div>' for k in range(1, 11))
    cls2 = f' {p}--2l' if ev.get('linhas', 1) == 2 else ''
    return f'''      <!-- ===================== SLIDE {n} — {ev['aria']} (tablet 3D navegável) ===================== -->
      <section class="slide {p}{cls2}" data-slide="{n}" data-screen-label="{nn}" aria-label="Slide {n} — Rotinas de Manejo Salvas: {ev['aria']}">
        <img class="{p}-foto" src="assets/confinamento/ev-fazendeiro.webp?v=1" alt="" aria-hidden="true" style="--d:.05s">
        <div class="{p}-barra-teal" style="--d:.05s"></div>
        <p class="{p}-eyebrow" style="--d:.06s">Rotinas de Manejo Salvas</p>
        <h2 class="{p}-titulo" style="--d:.12s">{ev['titulo']}</h2>
        <p class="{p}-tag" style="--d:.2s">Tipo: {ev['tag']}</p>
        <div class="{p}-pilula" style="--d:.3s"></div>
        <p class="{p}-texto" style="--d:.34s">{ev['texto']}</p>

        <div class="{p}-palco" style="--d:.18s">
          <div class="{p}-giro">
          <div class="{p}-tablet">
            {camadas}
            <img class="{p}-moldura" src="assets/confinamento/tablet-moldura.webp?v=1" alt="" aria-hidden="true">
            <div class="{p}-tela">
              {tela_html}
            </div>
          </div>
          </div>
        </div>

{ev.get('extra', '')}        <button class="ms-nav" type="button" style="top:83.9%;width:5.4%;height:6.4%;left:6.52%;--d:.44s" onclick="goToSlide({voltar})" aria-label="Voltar aos eventos" title="Voltar aos eventos">
          <svg viewBox="0 0 24 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 3 3 7l4 4M3 7h12.5a4.5 4.5 0 0 1 0 9H12"/></svg>
        </button>
      </section>

'''

def html_proto(p, n, d, tela_html, voltar, menu=2, casa=9):
    """Slide de protótipo: faixa verde com título, texto à esquerda e o tablet 3D; nav Voltar/Menu à esquerda do tablet."""
    tela_html = desativa_sem_acao(tela_html)
    nn = str(n).zfill(2)
    camadas = ''.join(f'<div class="{p}-camada" style="transform:translateZ(-{k*0.14:.2f}cqw)"></div>' for k in range(1, 11))
    return f'''      <!-- ===================== SLIDE {n} — {d['aria']} (protótipo, tablet 3D navegável) ===================== -->
      <section class="slide {p} {p}--proto" data-slide="{n}" data-screen-label="{nn}" aria-label="Slide {n} — {d['aria']}">
        <img class="slide__bg" src="assets/erp-senior/fundo-claro-topo.webp?v=1" alt="" aria-hidden="true">
        <img class="{p}-faixa" src="assets/erp-senior/faixa-topo.webp?v=1" alt="" aria-hidden="true">
        <h2 class="{p}-topo" style="--d:.04s"><img src="assets/erp-senior/icone-mb.webp?v=1" alt="" aria-hidden="true">{d['topo']}</h2>
        <div class="{p}-pbloco is-ativo" data-texto="padrao">
          <h3 class="{p}-ptit" style="--d:.12s">{d['titulo']}</h3>
          <div class="{p}-ppil" style="--d:.24s"></div>
          <p class="{p}-ptexto" style="--d:.28s">{d['texto']}</p>
        </div>
{d.get('blocos', '')}{d.get('popups', '')}

        <div class="{p}-palco" style="--d:.18s">
          <div class="{p}-giro">
          <div class="{p}-tablet">
            {camadas}
            <img class="{p}-moldura" src="assets/confinamento/tablet-moldura.webp?v=1" alt="" aria-hidden="true">
            <div class="{p}-tela">
              {tela_html}
            </div>
          </div>
          </div>
        </div>

        <button class="ms-nav" type="button" style="top:2%;width:5.2%;height:6.2%;left:44.3%;--d:.2s" onclick="goToSlide({voltar})" aria-label="Voltar" title="Voltar">
          <svg viewBox="0 0 24 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 3 3 7l4 4M3 7h12.5a4.5 4.5 0 0 1 0 9H12"/></svg>
        </button>
        <button class="ms-nav" type="button" style="top:2%;width:5.2%;height:6.2%;left:50.6%;--d:.23s" onclick="goToSlide({casa})" aria-label="Coleta de Dados" title="Coleta de Dados">
          {ICO['casa']}
        </button>
        <button class="ms-nav" type="button" style="top:2%;width:5.2%;height:6.2%;left:56.9%;--d:.26s" onclick="goToSlide({menu})" aria-label="Menu" title="Menu">
          <svg viewBox="0 0 24 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="10" r="8.2"/><path d="M8.8 6.9h6.4M8.8 10h6.4M8.8 13.1h6.4"/></svg>
        </button>
      </section>

'''

def js(p='tb'):
    import json as _j
    ALCA_JSON, LIXO_JSON, EDITAR_JSON, PLAY_JSON = (_j.dumps(ICO[k]) for k in ('alca', 'lixo', 'editar', 'play'))
    return f'''    /* ---- Tablet 3D: inclina seguindo o mouse (repouso: levemente virado para a esquerda) ----
       Gerado por ferramentas/aplica_eventos.py — não editar à mão. */
    document.querySelectorAll('.slide.{p}').forEach(sec => {{
      const tab = sec.querySelector('.{p}-tablet'); if(!tab) return;
      const REP = {{x:0, y:8}};
      let cx = REP.x, cy = REP.y, ax = REP.x, ay = REP.y, raf = null;
      const passo = () => {{
        cx += (ax-cx)*.1; cy += (ay-cy)*.1;
        tab.style.setProperty('--rx', cx.toFixed(2)+'deg'); tab.style.setProperty('--ry', cy.toFixed(2)+'deg');
        raf = (Math.abs(ax-cx)>.03 || Math.abs(ay-cy)>.03) ? requestAnimationFrame(passo) : null;
      }};
      const anima = () => {{ if(!raf) raf = requestAnimationFrame(passo); }};
      sec.addEventListener('pointermove', e => {{
        const r = sec.getBoundingClientRect();
        const px = Math.min(1, Math.max(0, (e.clientX - r.left)/r.width));
        const py = Math.min(1, Math.max(0, (e.clientY - r.top)/r.height));
        ay = 11 - px*22;             // mouse à esquerda: virado p/ esquerda (+11°) … à direita: p/ direita (-11°)
        ax = (0.5 - py)*7;           // em cima inclina um pouco para trás
        anima();
      }});
      sec.addEventListener('pointerleave', () => {{ ax = REP.x; ay = REP.y; anima(); }});
      /* teclas digitadas nos campos do app não navegam o deck */
      sec.querySelector('.{p}-tela').addEventListener('keydown', e => e.stopPropagation());

      /* ---- interações dentro do app ---- */
      const tela = sec.querySelector('.{p}-tela');
      /* título da rotina: Salvar só habilita com texto no campo */
      tela.querySelectorAll('[data-titulo-rotina]').forEach(inp => inp.addEventListener('input', () => tela.querySelectorAll('[data-acao="rotina-salvar"]').forEach(x => x.disabled = !inp.value.trim())));
      const mostraTexto = pg => sec.querySelectorAll('.{p}-pbloco').forEach(b => b.classList.toggle('is-ativo', b.dataset.texto === (pg.dataset.texto || 'padrao')));
      const fechaPopups = () => sec.querySelectorAll('.{p}-popup.is-aberto').forEach(x => x.classList.remove('is-aberto'));
      sec.addEventListener('click', e => {{ if(!e.target.closest('.{p}-popup, [data-acao^="popup:"]')) fechaPopups(); }});
      const ICONE_ALCA = {ALCA_JSON}, ICONE_LIXO = {LIXO_JSON}, ICONE_EDITAR = {EDITAR_JSON}, ICONE_PLAY = {PLAY_JSON};
      const irPara = (dest, volta, nome) => {{
        const hist = tela._hist = tela._hist || [];
        const atual = tela.querySelector('.{p}-pag.is-ativa');
        if(volta){{ if(!dest) dest = hist.pop() || '1'; else if(hist.length && hist[hist.length-1] === dest) hist.pop(); }}
        else if(atual && atual.dataset.pag !== dest) hist.push(atual.dataset.pag);
        const prox = tela.querySelector('.{p}-pag[data-pag="' + dest + '"]');
        if(!prox || prox === atual || tela.dataset.animando) return;
        if(nome) tela.querySelectorAll('[data-fazenda-nome]').forEach(x => x.textContent = nome);
        tela.dataset.animando = '1'; mostraTexto(prox); fechaPopups();
        prox.classList.add('is-ativa', volta ? '{p}-pag--entra-esq' : '{p}-pag--entra-dir');
        atual.classList.add(volta ? '{p}-pag--sai-dir' : '{p}-pag--sai-esq');
        setTimeout(() => {{
          atual.classList.remove('is-ativa', '{p}-pag--sai-dir', '{p}-pag--sai-esq');
          prox.classList.remove('{p}-pag--entra-esq', '{p}-pag--entra-dir');
          prox.querySelectorAll('.{p}-form').forEach(f => f.scrollTop = 0);
          delete tela.dataset.animando;
        }}, 400);
      }};
      /* ---- criação de rotina: seleção de eventos, slots ordenáveis, exclusão e salvamento ---- */
      const norm2 = s => s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase();
      const marcados = () => [...tela.querySelectorAll('.{p}-evt.is-marcado')].map(x => x.dataset.nome);
      const atualizaContinuar = () => tela.querySelectorAll('[data-acao="evt-continuar"]').forEach(x => x.disabled = marcados().length === 0);
      const renumera = () => tela.querySelectorAll('[data-slots]').forEach(l => [...l.querySelectorAll('.{p}-slot')].forEach((s, i) => s.querySelector('[data-ordem]').textContent = (i + 1) + '°'));
      const montaSlots = () => {{
        const lista = tela.querySelector('[data-slots]'); if(!lista) return;
        const campos = JSON.parse(tela.querySelector('[data-slot-campos]').textContent);
        const nomes = marcados();
        [...lista.querySelectorAll('.{p}-slot')].forEach(s => {{ if(!nomes.includes(s.dataset.nome) && tela.querySelector('.{p}-evt[data-nome="' + CSS.escape(s.dataset.nome) + '"]')) s.remove(); }});
        nomes.forEach(n => adicionaSlot(lista, campos, n));
        renumera();
      }};
      const adicionaSlot = (lista, campos, n) => {{
        if(lista.querySelector('.{p}-slot[data-nome="' + CSS.escape(n) + '"]')) return;
        const c = campos[n] || campos['*'];
        lista.insertAdjacentHTML('beforeend', '<div class="{p}-slot" data-nome="' + n + '"><div class="{p}-slot__alca">' + ICONE_ALCA + '</div><div class="{p}-slot__conteudo">'
          + '<div class="{p}-slot__cab"><span data-ordem>1°</span> ' + n + (c.info ? ' <i class="{p}-info-v">i</i>' : '') + '<button class="{p}-slot__lixo" type="button" data-acao="slot-excluir" aria-label="Excluir evento">' + ICONE_LIXO + '</button></div>'
          + c.html + '</div></div>');
      }};
      const limpaRotina = () => {{
        tela.querySelectorAll('.{p}-evt.is-marcado').forEach(x => x.classList.remove('is-marcado')); atualizaContinuar();
        tela.querySelectorAll('[data-slots] .{p}-slot').forEach(s => s.remove());
        const inp = tela.querySelector('[data-titulo-rotina]'); if(inp) inp.value = '';
        tela.querySelectorAll('[data-acao="rotina-salvar"]').forEach(x => x.disabled = true); tela._rotinaEditando = null;
      }};
      tela.querySelectorAll('[data-filtro-evt]').forEach(inp => inp.addEventListener('input', () => {{
        const q = norm2(inp.value.trim()); const pag = inp.closest('.{p}-pag');
        pag.querySelectorAll('.{p}-evt').forEach(f => f.classList.toggle('is-oculta', !!q && !norm2(f.textContent).includes(q)));
        pag.querySelectorAll('.{p}-grupo').forEach(g => {{ const vis = [...g.querySelectorAll('.{p}-evt')].some(f => !f.classList.contains('is-oculta')); g.classList.toggle('is-oculta', !vis); }});
      }}));
      /* arrastar pelo friso para reordenar os slots */
      tela.querySelectorAll('[data-slots]').forEach(lista => {{
        let drag = null;
        lista.addEventListener('pointerdown', e => {{
          const alca = e.target.closest('.{p}-slot__alca'); if(!alca) return;
          drag = alca.closest('.{p}-slot'); drag.classList.add('is-arrastando'); alca.setPointerCapture(e.pointerId); e.preventDefault(); e.stopPropagation();
        }});
        lista.addEventListener('pointermove', e => {{
          if(!drag) return; e.stopPropagation();
          for(const o of [...lista.querySelectorAll('.{p}-slot')].filter(s => s !== drag)){{
            const r = o.getBoundingClientRect(); if(e.clientY < r.top || e.clientY > r.bottom) continue;
            if(e.clientY < r.top + r.height/2){{ if(o.previousElementSibling !== drag) lista.insertBefore(drag, o); }}
            else if(o.nextElementSibling !== drag) lista.insertBefore(drag, o.nextElementSibling);
            break;
          }}
          renumera();
        }});
        const fim = e => {{ if(!drag) return; drag.classList.remove('is-arrastando'); drag = null; e.stopPropagation(); }};
        lista.addEventListener('pointerup', fim); lista.addEventListener('pointercancel', fim);
      }});
      /* busca de fazendas: filtra a lista enquanto digita (sem acentos, sem maiúsculas) */
      const norm = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
      tela.querySelectorAll('[data-filtro]').forEach(inp => inp.addEventListener('input', () => {{
        const q = norm(inp.value.trim()); const pag = inp.closest('.{p}-pag') || tela; let n = 0;
        pag.querySelectorAll('.{p}-faz').forEach(f => {{ const ok = !q || norm(f.textContent).includes(q); f.classList.toggle('is-oculta', !ok); if(ok) n++; }});
        pag.querySelectorAll('.{p}-vazio').forEach(v => v.classList.toggle('is-visivel', n === 0));
      }}));
      /* campo de peso: começa vazio e, ao receber o clique, preenche com o valor de demonstração */
      tela.querySelectorAll('[data-peso]').forEach(inp => {{
        const preenche = () => {{ if(!inp.value.trim()) inp.value = inp.dataset.sugestao || ''; }};
        ['pointerdown', 'focus', 'click'].forEach(ev => inp.addEventListener(ev, preenche));
        inp.parentElement.addEventListener('pointerdown', () => {{ preenche(); inp.focus(); }});   // clique na borda da caixa também
        inp.parentElement.querySelectorAll('.{p}-toque').forEach(bt => bt.addEventListener('click', () => {{ preenche(); inp.focus(); }}));
      }});
      tela.addEventListener('click', e => {{
        const b = e.target.closest('button, [data-acao]'); if(!b) return;
        const app = b.closest('.{p}-app');
        const segm = b.closest('.{p}-seg');
        if(segm){{   // seletor (Fêmea/Macho, Sim/Não, ...)
          segm.querySelectorAll('button').forEach(x => x.classList.toggle('is-sel', x === b));
          if(segm.hasAttribute('data-sexo')) app.dataset.sexo = [...segm.children].indexOf(b) === 0 ? 'f' : 'm';
          if(segm.hasAttribute('data-escolha')) app.querySelectorAll('.{p}-var[data-var]').forEach(x => x.classList.toggle('is-ativa', x.dataset.var === b.dataset.var));
          return;
        }}
        const grupo = b.closest('[data-radios]');
        if(grupo && b.hasAttribute('data-radio')){{ grupo.querySelectorAll('[data-radio]').forEach(x => x.classList.toggle('is-sel', x === b)); return; }}
        if(b.dataset.passo !== undefined){{   // quantidade com passos
          const sp = b.closest('[data-passos]').querySelector('[data-valor]');
          const v = b.dataset.passo === '0' ? 0 : parseFloat(sp.dataset.valor) + parseFloat(b.dataset.passo);
          sp.dataset.valor = v; sp.textContent = String(v).replace('.', ',');
          return;
        }}
        const acao = b.dataset.acao;
        if(acao && acao.startsWith('popup:')){{   // janela suspensa ao lado do tablet
          const jan = tela.querySelector('.{p}-modal[data-popup="' + acao.slice(6) + '"]');
          if(jan){{
            if(b.dataset.lupa){{   // cada lupa preenche a janela com o seu lote, título e lista de animais
              const d = JSON.parse(tela.querySelector('[data-lupas]').textContent)[b.dataset.lupa];
              jan.querySelector('[data-j-titulo]').textContent = d.titulo; jan.querySelector('[data-j-lote]').textContent = 'Lote: ' + d.lote;
              jan.querySelector('[data-j-n]').textContent = d.rotulo + ': ' + d.qtd;
              let linhas = ''; for(let i = 0; i < d.qtd; i++) linhas += '<tr><td>' + d.prefixo + (d.inicio + i) + '</td><td>' + d.sexo + '</td></tr>';
              jan.querySelector('[data-j-linhas]').innerHTML = linhas; jan.querySelector('.{p}-janela__corpo').scrollTop = 0;
            }}
            jan.classList.toggle('is-aberto'); return;
          }}
          const pp = sec.querySelector('.{p}-popup[data-popup="' + acao.slice(6) + '"]'); if(pp) pp.classList.toggle('is-aberto'); return;
        }}
        if(acao && (acao.startsWith('nav:') || acao.startsWith('nav-volta:'))){{   // troca de tela com deslize lateral
          irPara(acao.split(':')[1], acao.startsWith('nav-volta:'), b.dataset.nome); return;
        }}
        if(acao && acao.startsWith('ir:')){{   // troca de página dentro do tablet
          const dest = acao.slice(3);
          const peso = tela.querySelector('[data-peso]');
          if(peso){{   // leva o peso digitado (ou o sugerido, se vazio) para o resumo e para a ficha
            if(!peso.value.trim() && b.closest('.{p}-pag') === peso.closest('.{p}-pag')) peso.value = peso.dataset.sugestao || '';   // só ao avançar da pesagem
            const v = (peso.value || '0').trim().replace('.', ',');
            tela.querySelectorAll('[data-peso-resumo]').forEach(x => x.textContent = v);
            tela.querySelectorAll('[data-peso-kg]').forEach(x => x.textContent = v);
          }}
          if(b.dataset.proximo !== undefined){{   // próximo animal: troca a ficha, limpa o peso e reabre a confirmação
            const lista = JSON.parse(tela.querySelector('[data-animais]').textContent);
            const i = ((parseInt(tela.dataset.animal || '0', 10) + 1) % lista.length); tela.dataset.animal = i;
            Object.entries(lista[i]).forEach(([k, v]) => tela.querySelectorAll('[data-animal="' + k + '"]').forEach(x => x.innerHTML = v));
            if(peso){{ peso.value = ''; peso.dataset.sugestao = lista[i].pesokg || peso.dataset.sugestao; }}
            tela.querySelectorAll('.{p}-seg[data-escolha] button').forEach(x => x.classList.remove('is-sel'));   // volta ao estado inicial
            tela.querySelectorAll('.{p}-seg:not([data-escolha]):not([data-sexo])').forEach(s => [...s.children].forEach((x, k) => x.classList.toggle('is-sel', k === 0)));
            tela.querySelectorAll('.{p}-var[data-var]').forEach(x => x.classList.remove('is-ativa'));
            tela.querySelectorAll('[data-radios]').forEach(g => g.querySelectorAll('[data-radio]').forEach((x, k) => x.classList.toggle('is-sel', k === 0)));
            tela.querySelectorAll('.{p}-modal[data-inicial]').forEach(m => m.classList.add('is-aberto'));
          }}
          tela.querySelectorAll('.{p}-pag').forEach(pg => pg.classList.toggle('is-ativa', pg.dataset.pag === dest));
          return;
        }}
        if(acao === 'fechar'){{ b.closest('.{p}-modal').classList.remove('is-aberto'); return; }}
        if(acao === 'gaveta'){{ tela.querySelector('.{p}-gaveta').classList.add('is-aberta'); return; }}
        if(acao === 'gaveta-fechar'){{ tela.querySelector('.{p}-gaveta').classList.remove('is-aberta'); return; }}
        if(acao === 'acordeao'){{   // abre a propriedade clicada e fecha as outras
          const acc = b.closest('.{p}-acc'), abrir = !acc.classList.contains('is-aberto');
          acc.parentElement.querySelectorAll('.{p}-acc').forEach(x => x.classList.remove('is-aberto')); if(abrir) acc.classList.add('is-aberto'); return;
        }}
        if(acao && acao.startsWith('gaveta-ir:')){{ tela.querySelector('.{p}-gaveta').classList.remove('is-aberta'); irPara(acao.slice(10), false); return; }}
        if(acao === 'gaveta-inicio'){{   // Início: fecha o menu e volta à escolha da fazenda
          tela.querySelector('.{p}-gaveta').classList.remove('is-aberta');
          const atual = tela.querySelector('.{p}-pag.is-ativa'), ini = tela.querySelector('.{p}-pag[data-pag="1"]');
          tela._hist = []; fechaPopups();
          if(atual && ini && atual !== ini && !tela.dataset.animando){{
            tela.dataset.animando = '1'; mostraTexto(ini);
            ini.classList.add('is-ativa', '{p}-pag--entra-esq'); atual.classList.add('{p}-pag--sai-dir');
            setTimeout(() => {{ atual.classList.remove('is-ativa', '{p}-pag--sai-dir'); ini.classList.remove('{p}-pag--entra-esq'); delete tela.dataset.animando; }}, 400);
          }}
          return;
        }}
        if(acao === 'evt-toggle'){{ b.classList.toggle('is-marcado'); atualizaContinuar(); return; }}
        if(acao === 'evt-continuar'){{ montaSlots(); irPara('5', false); return; }}
        if(acao === 'slot-excluir'){{ tela._slotExcluir = b.closest('.{p}-slot'); app.querySelector('.{p}-modal[data-popup="excluir"]').classList.add('is-aberto'); return; }}
        if(acao === 'slot-excluir-sim'){{
          const s = tela._slotExcluir; if(s){{ const ev = tela.querySelector('.{p}-evt[data-nome="' + CSS.escape(s.dataset.nome) + '"]'); if(ev) ev.classList.remove('is-marcado'); s.remove(); renumera(); atualizaContinuar(); }}
          app.querySelector('.{p}-modal[data-popup="excluir"]').classList.remove('is-aberto'); return;
        }}
        if(acao === 'rotina-salvar'){{   // nova rotina entra no topo das Rotinas Salvas e volta para a lista
          const titulo = (tela.querySelector('[data-titulo-rotina]').value || '').trim() || 'Nova Rotina';
          const cadeia = [...tela.querySelectorAll('[data-slots] .{p}-slot')].map(s => s.dataset.nome).join(' &gt; ');
          const alvo = tela.querySelector('[data-rotinas]'), ed = tela._rotinaEditando;
          if(ed && ed.isConnected){{ ed.querySelector('.{p}-rot__cab span').textContent = titulo; ed.querySelector('.{p}-rot__cad').innerHTML = cadeia; }}
          else alvo.insertAdjacentHTML('afterbegin', '<div class="{p}-rot"><div class="{p}-rot__cab"><span>' + titulo + '</span><button class="{p}-rot__ic" type="button" data-acao="rotina-editar" aria-label="Editar">' + ICONE_EDITAR + '</button><button class="{p}-rot__ic" type="button" disabled>' + ICONE_PLAY + '</button></div><div class="{p}-rot__cad">' + cadeia + '</div></div>');
          limpaRotina(); tela._hist = []; irPara('2', true); return;
        }}
        if(acao === 'rotina-nova'){{ limpaRotina(); irPara('4', false); return; }}
        if(acao === 'rotina-editar'){{   // abre a edição com o título e os eventos da rotina escolhida
          limpaRotina(); const card = b.closest('.{p}-rot'); tela._rotinaEditando = card;
          const titulo = card.querySelector('.{p}-rot__cab span').textContent.trim();
          const nomes = card.querySelector('.{p}-rot__cad').textContent.split('>').map(s => s.trim()).filter(Boolean);
          tela.querySelectorAll('.{p}-evt').forEach(e => e.classList.toggle('is-marcado', nomes.includes(e.dataset.nome))); atualizaContinuar();
          tela.querySelector('[data-titulo-rotina]').value = titulo; tela.querySelectorAll('[data-acao="rotina-salvar"]').forEach(x => x.disabled = false);
          const lista = tela.querySelector('[data-slots]'), campos = JSON.parse(tela.querySelector('[data-slot-campos]').textContent);
          nomes.forEach(n => adicionaSlot(lista, campos, n)); renumera();
          irPara('5', false); return;
        }}
        if(acao === 'focar'){{ const inp = b.parentElement.querySelector('input'); if(inp) inp.focus(); return; }}
        if(acao === 'reconectar'){{   // Identificação Eletrônica: liga o LED, leva o bastão ao brinco, o boi estranha, lê e preenche o campo
          const cena = sec.querySelector('.{p}-cena'), nota = b.closest('.{p}-nota'), campo = app.querySelector('[data-ident]');
          if(!cena || cena.dataset.ocupado) return;
          cena.dataset.ocupado = '1';
          cena.classList.remove('is-lendo', 'is-no-boi'); campo.querySelector('span').textContent = ''; campo.classList.add('{p}-input--off');
          nota.classList.remove('{p}-nota--erro'); nota.innerHTML = 'Bastão conectado!<br><button type="button" data-acao="reconectar"><u>Clique aqui para ler o brinco</u></button>';
          cena.classList.add('is-ligado');
          // posiciona a ponta do bastão sobre o brinco (medido na tela, em pixels do slide)
          const r = sec.getBoundingClientRect(), bas = cena.querySelector('.{p}-bastao').getBoundingClientRect(), boi = cena.querySelector('.{p}-boi').getBoundingClientRect();
          const ponta = {{x: bas.left + bas.width*.86, y: bas.top + bas.height*.025}};
          const brinco = {{x: boi.left + boi.width*0.137, y: boi.top + boi.height*0.359}};
          cena.style.setProperty('--bas-dx', (brinco.x - ponta.x + r.width*.012) + 'px'); cena.style.setProperty('--bas-dy', (brinco.y - ponta.y + r.height*.03) + 'px'); cena.style.setProperty('--bas-rot', '-6deg');
          cena.style.setProperty('--onda-x', (brinco.x - r.left) + 'px'); cena.style.setProperty('--onda-y', (brinco.y - r.top) + 'px');
          setTimeout(() => cena.classList.add('is-no-boi'), 450);
          setTimeout(() => cena.classList.add('is-lendo'), 1850);
          setTimeout(() => {{ campo.classList.remove('{p}-input--off'); campo.querySelector('span').textContent = campo.dataset.ident; }}, 2650);
          setTimeout(() => {{ cena.classList.remove('is-lendo', 'is-no-boi'); }}, 4000);
          setTimeout(() => {{ delete cena.dataset.ocupado; }}, 5400);
          return;
        }}
        if(acao === 'remover'){{
          const li = b.closest('li'), ul = li.parentElement; li.remove();
          if(!ul.children.length && ul.dataset.vazioTexto) ul.innerHTML = '<li class="{p}-item {p}-item--vazio" data-vazio>' + ul.dataset.vazioTexto + '</li>';
        }} else if(acao === 'abrir-cria'){{
          app.querySelector('.{p}-modal').classList.add('is-aberto');
        }} else if(acao === 'fechar-cria'){{
          app.querySelector('.{p}-modal').classList.remove('is-aberto');
        }} else if(acao === 'salvar-cria'){{
          const ul = app.querySelector('[data-crias] ul'); const vz = ul.querySelector('[data-vazio]'); if(vz) vz.remove();
          const n = ul.children.length + 1;
          ul.insertAdjacentHTML('beforeend', '<li class="{p}-item"><span>Cria número ' + n + ' / Vivo / CRIA0' + n + '</span><button type="button" class="is-escuro" data-acao="remover" aria-label="Remover">{ICO["lixo"]}</button></li>');
          app.querySelector('.{p}-modal').classList.remove('is-aberto');
        }}
      }});
    }});

'''
