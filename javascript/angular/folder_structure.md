# Estrutura de pastas do Angular

```tsx
src/app/
├── components/
│   ├── example/
│   │   ├── example.component.ts
│   │   ├── example.component.html
│   │   ├── example.component.css
│   │   └── example.component.spec.ts
├── shared/
│   ├── components/
│   │   ├── shared-button/
│   │   │   ├── shared-button.component.ts
│   │   │   ├── shared-button.component.html
│   │   │   ├── shared-button.component.css
│   │   │   └── shared-button.component.spec.ts
│   ├── directives/
│   │   ├── highlight.directive.ts
│   │   └── highlight.directive.spec.ts
│   ├── pipes/
│   │   ├── date-format.pipe.ts
│   │   └── date-format.pipe.spec.ts
│   ├── services/
│   │   ├── common.service.ts
│   │   └── common.service.spec.ts
│   ├── common/
│   │   ├── common-functions.ts
│   │   ├── constants.ts
│   │   └── validators.ts
├── services/
│   ├── api.service.ts
│   ├── auth.service.ts
│   └── user.service.ts
├── repositories/
│   ├── user.repository.ts
│   ├── product.repository.ts
│   └── order.repository.ts
```

## app

Contém a maior parte do código da aplicação.
Normalmente subdividido em pastas para organizar componentes, serviços, modelos, etc.

## components

Contém componentes específicos da aplicação.
Cada componente geralmente tem sua própria pasta, que inclui o arquivo .ts, .html, .css, e .spec.ts (para testes).

## shared

Contém código reutilizável que pode ser compartilhado por vários módulos ou componentes da aplicação.
Inclui diretivas, pipes, componentes pequenos (como botões ou formulários) e services que são usados globalmente.

Objetivo: Centralizar código reutilizável para evitar duplicação e promover a consistência.

Conteúdo: Componentes, diretivas, pipes, services globais, funções comuns.

## common

Subpasta dentro de shared ou utils que contém funções utilitárias ou constantes usadas em toda a aplicação.
Pode incluir helpers, funções de formatação, validadores, etc.

Objetivo: Agrupar funções utilitárias e constantes usadas globalmente.

Conteúdo: Helpers, validadores, constantes, formatadores de dados.

## services

Contém serviços específicos da aplicação que implementam lógica de negócio, comunicação com APIs, etc.
Serviços são injetáveis e fornecem uma maneira centralizada de acessar dados e realizar operações.

Objetivo: Implementar lógica de negócio e manipulação de dados, comunicação com APIs.

Conteúdo: Serviços específicos da aplicação, como autenticação, serviços de API, serviços de usuários.

## repositories

Contém classes ou serviços que tratam diretamente da manipulação de dados, muitas vezes interagindo com APIs ou bancos de dados.
Pode incluir lógica para acessar e manipular dados específicos de uma entidade ou recurso.

Objetivo: Centralizar a lógica de acesso a dados, proporcionando uma interface para manipulação de dados de entidades específicas.

Conteúdo: Serviços ou classes que interagem com APIs ou bancos de dados, realizando operações de CRUD.