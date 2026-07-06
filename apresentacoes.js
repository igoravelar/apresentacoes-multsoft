/* ============================================================
   REPOSITÓRIO DE APRESENTAÇÕES — MultSoft
   ------------------------------------------------------------
   Este é o "catálogo" lido pela página inicial (index.html).
   Para publicar uma nova apresentação, adicione um objeto ao
   array MULTSOFT_APRESENTACOES abaixo.

   RELAÇÃO POR TAGS
   Cada categoria tem uma TAG (identificador curto, sem espaços/
   acentos). Uma apresentação se relaciona a uma categoria quando
   inclui a TAG dela no campo "categorias". O texto exibido (label)
   pode mudar sem quebrar os vínculos — só a tag importa.

   Campos de cada apresentação:
     id          → identificador único da apresentação
     titulo      → nome exibido no card
     categorias  → uma ou mais TAGS de categoria (ver CATEGORIAS)
     descricao   → texto curto mostrado no balão do botão ⓘ
     atualizadoEm→ data "dd/mm/aaaa" (aparece no balão)
     arquivo     → caminho do HTML a abrir (null = "Em breve")
     thumb       → imagem de capa do card (opcional; null = placeholder)
   ============================================================ */

/* Categorias do filtro: { tag, label }. A ordem é a ordem exibida.
   tag = chave de relacionamento | label = texto mostrado na tela. */
const CATEGORIAS = [
  { tag: "institucional",              label: "Institucional" },
  { tag: "pecuaria-elite",             label: "Pecuária Elite" },
  { tag: "reproducao-cria-comercial",  label: "Reprodução e Cria Comercial" },
  { tag: "recria-engorda-pasto",       label: "Recria e Engorda a Pasto" },
  { tag: "recria-engorda-confinamento", label: "Recria e Engorda em Confinamento" },
  { tag: "labfiv",                     label: "LabFIV" },
  { tag: "integracao-erps",            label: "Integração ERPs" },
  { tag: "ciclo-completo",             label: "Ciclo Completo" },
  { tag: "representantes-comerciais",  label: "Representantes Comerciais" },
];

const MULTSOFT_APRESENTACOES = [
  {
    id: "solucoes-plataforma-multbovinos",
    titulo: "Soluções Plataforma MultBovinos",
    categorias: [
      "institucional",
      "pecuaria-elite",
      "reproducao-cria-comercial",
      "recria-engorda-pasto",
      "recria-engorda-confinamento",
      "ciclo-completo",
      "representantes-comerciais",
    ],
    descricao:
      "Visão geral da plataforma MultBovinos: coleta de dados, conectividade e gestão à vista no MB Web, cobrindo todo o ciclo da fazenda.",
    atualizadoEm: "22/06/2026",
    arquivo: "presentation/solucoes-plataforma-multbovinos.html",
    thumb: "presentation/assets/slide-01-bg.webp",
  },

  /* ----------------------------------------------------------
     PRÓXIMAS APRESENTAÇÕES (Em breve)
     Troque "arquivo: null" pelo caminho do HTML quando ficar
     pronta, ou remova o item se não for usar.
     ---------------------------------------------------------- */
  {
    id: "onboarding-colaboradores",
    titulo: "Onboarding para Novos Colaboradores",
    categorias: ["institucional"],
    descricao:
      "Trilha de boas-vindas e integração para novos colaboradores MultSoft.",
    atualizadoEm: "06/07/2026",
    arquivo: "presentation/onboarding-colaboradores.html",
    thumb: "presentation/assets/onboarding/slide-01-bg.webp",
  },
  {
    id: "reproducao-cria-comercial",
    titulo: "Reprodução e Cria Comercial",
    categorias: ["reproducao-cria-comercial"],
    descricao:
      "Aprofundamento no módulo reprodutivo: dashboards, coleta de dados e relatórios.",
    atualizadoEm: "06/07/2026",
    arquivo: "presentation/reproducao-cria-comercial.html",
    thumb: "presentation/assets/reproducao/thumb.webp?v=2",
  },
  {
    id: "representantes-comerciais",
    titulo: "Material para Representantes Comerciais",
    categorias: ["representantes-comerciais", "institucional"],
    descricao:
      "Apoio de vendas e argumentário comercial para a rede de representantes.",
    atualizadoEm: "—",
    // quando estiver pronta: arquivo: "presentation/representantes-comerciais.html"
    arquivo: null,
    thumb: null,
  },
  {
    id: "integracao-erps",
    titulo: "Integração com ERPs",
    categorias: ["integracao-erps"],
    descricao:
      "Como a plataforma MultBovinos se integra aos principais ERPs do mercado.",
    atualizadoEm: "—",
    // quando estiver pronta: arquivo: "presentation/integracao-erps.html"
    arquivo: null,
    thumb: null,
  },
];
