"""Aplica o submenu do Monitoramento (slide 10) e o Sistema Web MultBovinos (slide 125) no deck de Confinamento.
Blocos entre marcadores WEB-MB:* são substituídos a cada execução. Uso: python3 ferramentas/aplica_web.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import web_mb as W
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
arq = os.path.join(RAIZ, 'presentation/confinamento-multbovinos.html'); t = open(arq).read()
def bloco(t, nome, novo, antes):
    ini, fim = f'<!-- WEB-MB:{nome}:INICIO -->\n' if nome == 'HTML' else f'/* WEB-MB:{nome}:INICIO */\n', f'<!-- WEB-MB:{nome}:FIM -->\n' if nome == 'HTML' else f'/* WEB-MB:{nome}:FIM */\n'
    if ini in t:
        a = t.index(ini); b = t.index(fim) + len(fim); return t[:a] + ini + novo + fim + t[b:]
    i = t.index(antes); return t[:i] + ini + novo + fim + t[i:]
t = bloco(t, 'CSS', W.CSS, '  /* TABLET-EVENTOS:CSS:INICIO */')
t = bloco(t, 'HTML', W.html_submenu() + W.html_web(), '      <!-- TABLET-EVENTOS:HTML:INICIO -->')
t = bloco(t, 'JS', W.JS, '    /* ---- Restaura último slide visto ---- */')
m = re.search(r'const TOTAL = (\d+);', t); t = t.replace(m.group(0), f'const TOTAL = {max(125, int(m.group(1)))};', 1)
m = re.search(r'const BUILT = \[([^\]]*)\];', t); built = sorted(set(int(x) for x in re.findall(r'\d+', m.group(1))) | {10, 125})
t = t.replace(m.group(0), 'const BUILT = [' + ', '.join(map(str, built)) + '];', 1)
if 'Roboto+Condensed' not in t: t = t.replace('&display=swap', '&family=Roboto+Condensed:wght@400;700&display=swap', 1)
open(arq, 'w').write(t); print('ok')
