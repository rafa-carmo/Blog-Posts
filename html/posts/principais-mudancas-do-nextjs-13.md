2023-09-12 12:20
# Principais Mudanças do Nextjs 13
## Quais Mudanças que mudaram que vão afetar o uso do Nextjs 13?
nextjs
### Introdução

Primeiramente, o que é o [nextjs](https://nextjs.org/), é um Framework web construído em cima do Reactjs, porem, com o diferencial de ser SSR (server side rendering), ou seja, ele constrói a pagina em backend, cria um cache e serve esse cache para o frontend, deixando a aplicação muito mais rápida na utilização para o cliente.

E o Next 13, bom, ele deu um passo a mais nesse conceito, unindo o conceito de SSR com a funcionalidade do js mais ainda, deixando bem mais interativo e de forma mais amigável para os devs.

## Mãos na massa

Antes de mais nada, vamos criar nossa aplicação.

```bash
npx create-next-app@latest
```

Responda de acordo com seu projeto

```bash
 What is your project named? … new-app
✔ Would you like to use TypeScript? … No / *Yes*
✔ Would you like to use ESLint? … No / *Yes*
✔ Would you like to use Tailwind CSS? … No / *Yes*
✔ Would you like to use `src/` directory? … No / *Yes*
✔ Would you like to use App Router? (recommended) … No / *Yes*
✔ Would you like to customize the default import alias? … *No* / Yes
```

Após criado o projeto, temos a nova estrutura de pastas do next.

Agora o nextjs tem uma lista de nomes de arquivos para cada função, tanto em tsx ou jsx que são.

- page.tsx ( Serão as paginas da aplicação )
- layout.tsx ( É o layout que será aplicado para todas as pages deste diretório e os abaixo dele )
- loading.tsx ( Tela de loading para quando está gerando a pagina )
- route.tsx ( Para paginas de Rotas de api )

Agora seguindo da pasta app, cada subdiretório com um arquivo page.tsx, será uma rota nova, porem caso você não queria que a pasta apareça na url, basta envolver a pasta entre parêntesis, 

exemplo: app/(rota)/page.tsx, assim será ignorado o nome da rota na url.
