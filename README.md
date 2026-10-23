# REWIND® v2.0 — GOOD GAMES NEVER DIE.

**Loja virtual demonstrativa de Retro Gaming e Colecionáveis**, refeita com a estética VHS analógica cinematográfica, direção editorial inspirada nas referências do usuário e componentes 3D reusados/adaptados do arquivo de referência original.

> IMPORTANTE: esta é uma experiência de portfólio. Produtos, preços, estoques, frete e pedidos são fictícios. **Não existe cobrança, pagamento, autenticação ou envio de informações do checkout para servidores.** Não use dados pessoais reais no checkout.

## Tecnologias

- React 19 + TypeScript + Vite 7
- Tailwind CSS v4 (`@tailwindcss/vite`)
- Three.js + React Three Fiber 9
- Framer Motion (`motion`, `AnimatePresence`, springs, scroll-linked animations)
- Lucide React
- SVGs locais sem links externos quebráveis

## Executar no Windows

1. Instale Node.js 22 ou superior compatível com Vite 7.
2. Extraia o ZIP e abra a pasta `REWIND_2_0` no VS Code.
3. Abra o Terminal na pasta que contém `package.json`.
4. Execute:

```powershell
npm install
npm run dev
```

Abra o endereço informado no terminal (em geral `http://localhost:5173`).

## Publicar na Vercel

1. Faça upload de todos os arquivos da pasta `REWIND_2_0` para a raiz de um repositório no GitHub (não carregue `node_modules`).
2. Importe o repositório em Vercel > Add New > Project.
3. Framework: **Vite**; Install: `npm install`; Build: `npm run build`; Output: `dist`.
4. Clique em Deploy. O `vercel.json` inclui rewrite para SPA.

Opcionalmente, rode `npm run build` na sua máquina para verificar a compilação antes de publicar.

## O que mudou na v2.0

**A página anterior foi reconstruída** com uma linguagem editorial mais próxima das referências AMP e VHS, com:

- Intro tape overlay REWIND com barra de progresso, saída animada e cena em camadas;
- Hero cinematográfico com skyline, pôr do sol, perspectiva grid, halos, produtos com animações independentes, microefeitos no hover e parallax no mouse/scroll;
- Efeitos VHS ao longo de **toda a página**, com scanlines, ruído, tracking, vinheta e botão FX ON/OFF;
- Marquee animado em loop, manchetes editoriais com revelação, cartões de curadoria em peach/white, cards com zoom, tilt e interação;
- **Estante 3D completa baseada diretamente no componente fornecido**: geometria `RoundedBoxGeometry`, texturas geradas em Canvas, variações de cor e motif, lombada e páginas, foco com trajetórias suaves, órbita por arraste, seleção por teclado, tooltip de hover e controle de câmera. Clique uma vez para ampliar; clique outra para ver detalhes. Navegue arrastando e com as setas;
- Fallback de vitrine 2D quando não há WebGL;
- Catálogo com 12 artigos fictícios, busca, seleção de categoria, favoritos, filtro de estoque, preço máximo e múltiplas ordenações;
- 12 artes de produtos em SVG, mais 12 versões transparentes para composição;
- Quick view completo, adicionar à sacola, editar quantidades e remover itens;
- Sacola e favoritos persistidos em localStorage;
- Cupom `REWIND10` (simulado), frete ilustrativo de R$ 29,90 ou grátis a partir de R$ 399;
- Checkout fictício em etapas, validação de campos, revisão e recibo demonstrativo (sem número de cartão ou chamadas de pagamento);
- Layout adaptado para desktop, tablet e celular; preferência de movimento reduzido respeitada na camada CSS e dentro da estante 3D;
- Tokens, espaçamentos, raios e cores de `@theme` e `:root` das referências preservados. A variável descritiva `--element-gap` (faixa 5–8px) foi normalizada para 8px.

## Onde editar

| Arquivo | Finalidade |
| --- | --- |
| `src/App.tsx` | Toda a experiência visual, filtros, estados, carrinho, favoritos e checkout |
| `src/components/ArchiveShelf.tsx` | Implementação adaptada integral da estante 3D de referência |
| `src/styles.css` | AMP tokens Tailwind v4 + CSS editorial + VHS + responsividade |
| `src/data/products.ts` | Catálogo, preços, estoque demonstrativo |
| `public/assets/` | 24 imagens locais, incluindo versões com transparência |
| `reference/` | Cópias dos **três arquivos originais do usuário**, para consulta e auditoria da fidelidade |
| `vercel.json` | Fallback SPA para Vercel |

## Check de qualidade

- TypeScript/TSX analisado para **sintaxe** com compilador TypeScript.
- CSS analisado com parser PostCSS: sem erros de parsing.
- 12 produtos / IDs únicos / imagens de catálogo e cutouts verificadas.
- Tokens de design do arquivo de referência conferidos com o CSS.
- Pacote ZIP inspecionado após a montagem.
- **Limitação desta sessão:** o domínio do npm não resolveu no ambiente de criação. Portanto `npm install`, `npm run build` e o teste visual no navegador real **não puderam ser concluídos**. Para validar a instalação e o layout final, siga os comandos acima em ambiente com acesso ao npm/Vercel. Não há declaração de build/teste de navegador aprovado.

## Avisos de segurança

Os pedidos e favoritos só existem localmente no navegador, sem backend. O formulário de checkout existe exclusivamente para exemplificar o fluxo e descarta seus valores após a confirmação. Não permite compras reais nem substitui integração de pagamentos, estoque real, autenticação, políticas de privacidade, frete, antifraude ou administração.

## Referências

- Arquivos do usuário preservados em `reference/`: estilo AMP, tokens JSON e componente `NewsletterBookshelf` baseado em React Three Fiber.
- Referência externa de linguagem editorial: https://amp.ai/.
- Identidade visual REWIND é uma interpretação original; não reutiliza marcas, logos, personagens ou materiais protegidos de GTA.
