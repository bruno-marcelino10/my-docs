# Angular

## Introdução

O Angular é uma plataforma e framework de desenvolvimento web mantido pelo Google, e utilizado para a criação de aplicações web responsivas de uma única página (SPA - Single Page Applications). Isso permite que a página seja renderizada diretamente em uma requisição, e as partes (componentes) do template são mostradas de acordo com a interação do usuário. 

O Angular é escrito em TypeScript, que é uma versão fortemente tipada do JavaScript. Isso significa que todas as declarações de variáveis devem sinalizar o tipo de dado que está sendo atribuído ou retornado, adicionando muito mais dicas e ferramentas de correção de código que permitem visualizar e corrigir bugs antes que ocorram. O TS também introduz o conceito de Interface, que são dicionários que contém todas as chaves tipadas.

São alguns dos conceitos introduzidos pelo Angular:

* **Módulos:** Os módulos (NgModule) são usados para organizar a aplicação em blocos funcionais. Eles agrupam componentes, diretivas, pipes e outros elementos relacionados.

Por combinar todos esses conceitos e ferramentas, o Angular permite o desenvolvimento de aplicações web robustas, escaláveis e de fácil manutenção, proporcionando uma experiência de desenvolvimento estruturada e poderosa. 

## Angular CLI

A Angular CLI (Command Line Interface) automatiza diversos processos de criação e testagem da aplicação. 

| COMANDO | DESCRIÇÃO |
| --- | --- |
| ng new <nome-do-projeto> | Permite criar um projeto Angular, com todos os arquivos necessários para configuração da aplicação. |
| ng g c <nome-do-componente> | Cria um componente dentro do projeto |
| ng version | Mostra a versão do Angular |
| npm install @angular/cli | Instala o Angular na máquina do usuário |
| ng serve ou npm start | Renderiza a aplicação na máquina do usuário |
| ng build |  |
| ng test |  |
| ng add |  |
| ng update |  |

## Componentes

São a base do Angular, e representam diferentes partes da interface do usuário. A aplicação pode ser segregada em diversos componentes, que permitem subdividir o template para facilitar a organização e manutenção do código.

Os componentes são organizados por meio da arquitetura de pirâmide (componente pai chama seus filhos). O arquivo `index.html` apresenta o template principal que chama todos os outros.

Para criar um componente, basta utilizar o comando `ng generate component <nome-do-component>`.

### Elementos

Cada componente é uma pasta que possui:

- `<component-name>.component.ts`: comportamento e lógica (TS)
- `<component-name>.component.html`: seu próprio template (HTML)
- `<component-name>.component.css`: seus próprios estilos (CSS)
- `<component-name>.component.spec.ts`: arquivo que especifica os testes unitários daquele componente.

### Estrutura

```tsx
import { Component } from '@angular/core';

@Component({
	selector: 'app-component', // tag que instancia o componente no HTML da página
  templateUrl: './app-component.component.html', // template relacionado
  styleUrls: ['./app-component.component.css'] // estilização do template
})
export class AppComponent {
	// lógica
}
```

Para renderizar o componente na aplicação, devemos instanciá-lo no HTML da página por meio do seu seletor CSS (selector). Para isso, faremos uma alteração no template principal.

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Super Açaí</title>
	  <base href="/">
		<link rel="icon" type="image/x-icon" href="favicon.png"/>
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
	</head>
	<body>
	  <app-component></app-component> <!-- instancia o componente criado -->
	</body>
</html>
```

### Ciclo de Vida

O componente é ativado quando o Angular instancia sua classe e renderiza o seu template associado. O ciclo continua enquanto não são detectadas alterações (eventos) nas propriedades-chave às quais o componente é vinculado no template. Nesse caso, ele é renderizado novamente após aplicar a lógica de negócio com os dados vinculados, e retorna o template atualizado.  

#### Lifecycle Hook Interfaces (Ganchos)

São métodos contidos no módulo `@angular/core`que agem durante o ciclo de vida do componente. Não são obrigatórios. São eles:

| MÉTODO | DESCRIÇÃO |
| --- | --- |
| ngOnInit() | É chamado quando o componente é instanciado pela primeira vez. |
| ngOnChanges() | Chamado toda vez que as propriedades-chave são alteradas. |
| ngOnDestroy() | Chamado quando o Angular destrói um componente. |

Exemplos:

```tsx
let nextId = 1;

// Spy on any element to which it is applied.
// Usage: <div appSpy>...</div>
@Directive({selector: '[appSpy]'})
export class SpyDirective implements OnInit, OnChanges, OnDestroy {
  private id = nextId++;

  constructor(
		private logger: LoggerService // somente instancia as variáveis locais
	) { } 
	
  ngOnInit() { // inicia na primeira vez que o componente é renderizado
    this.logger.log(`Spy #${this.id} onInit`);
  }

  ngOnChanges() { // inicia toda vez em que o estado do componente é alterado
    this.logger.log(`Spy #${this.id} onChanges`);
  }

  ngOnDestroy() { // inicia quanto o componente é destruído
    this.logger.log(`Spy #${this.id} onDestroy`);
  }
}
```

## Templates

São um fragmento da interface do usuário (UI), que compõe o HTML da página.

O Angular oferece diversas opções de comunicação entre o template e os componentes, conhecidas como *data-binding*, para fazer com que o template responda às interações do usuário*.* Isso permite estender a funcionalidade do HTML. 

### Interpolação (`{{ }}`)

Incorpora variáveis atribuídas no componente ao template.

```tsx
currentCustomer = 'Maria';
```

```html
<h3>Current customer: {{ currentCustomer }}</h3>
```

### Property Binding (`[ ]`)

Define valores dinâmicos vindos do componente para as propriedades dos elementos do HTML. 

```html
<img alt="item" [src]="itemImageUrl"> 
<!-- Define o valor da propriedade "src" com base em um trecho de código TS-->
```

### Event Binding (`( evento )`)

Chama um método contido no componente quando ocorre um evento específico. 

```html
<!-- Executa o método deleteHero() quando o botão é clicado -->
<button type="button" (click)="deleteHero()">Delete hero</button>

<!-- Executa o método onSave passando o nome do evento como parâmetro -->
<button type="button" (click)="onSave($event)">Save</button>

<input #phone placeholder="phone number" />
<button type="button" (click)="callPhone(phone.value)">Call</button>
<!-- #phone é o nome desse elemento "input" no DOM. Seu atributo "valor"
é passado como input para o método acionado pelo clique do botão -->
```

### Two-way Data Binding (`[( )]`)

Permite a comunicação entre componentes, combinando property e event binding. No processo, o template do componente pai recebe um atributo do componente filho como input e retorna um output para o componente pai. 

```html
<app-sizer [(size)]="fontSizePx"></app-sizer>
<div [style.font-size.px]="fontSizePx">Resizable Text</div>
```

```tsx
export class SizerComponent {
  @Input() size!: number | string;
  @Output() sizeChange = new EventEmitter<number>();

  dec() {
    this.resize(-1);
  }

  inc() {
    this.resize(+1);
  }

  resize(delta: number) {
    this.size = Math.min(40, Math.max(8, +this.size + delta));
    this.sizeChange.emit(this.size);
  }
}
```

### Pipes

São funções simples que permitem formatar os dados antes que sejam mostrados no template, e podem ter parâmetros opcionais. Existem diversos pipes previamente definidos no Angular. São alguns exemplos:

- [`DatePipe`](https://angular.io/api/common/DatePipe): Formata valores de data
- [`UpperCasePipe`](https://angular.io/api/common/UpperCasePipe): Formata texto em somente letras maiúsculas;
- [`LowerCasePipe`](https://angular.io/api/common/LowerCasePipe): Formata texto em somente letras minúsculas;
- [`CurrencyPipe`](https://angular.io/api/common/CurrencyPipe): Formata número em valores monetários;
- [`DecimalPipe`](https://angular.io/api/common/DecimalPipe): Formata número em valores decimais;
- [`PercentPipe`](https://angular.io/api/common/PercentPipe): Formata número em valores percentuais;
- [`AsyncPipe`](https://angular.io/api/common/AsyncPipe): Permite inscrever e desinscrever a um Observable;
- [`JsonPipe`](https://angular.io/api/common/JsonPipe): Mostra objetos (dicionários) em formato JSON.

Exemplo:

```html
<!-- Passa "birthday" como parâmetro no formato de data -->
<p>The hero's birthday is {{ birthday | date }}</p>

<!-- Passa "amount" como parâmetro no formato de moeda do tipo Euro -->
{{ amount | currency:'EUR' }}

<!-- Passa "texto" como parâmetro e mostra em formato de data maiúscula,
 encadeando os operadores -->
{{ texto | date | uppercase}}

```

## Diretivas

As diretivas permitem estender o HTML com funcionalidades customizadas.

#### Diretivas Estruturais

Adicionam ou removem elementos do DOM.

`*ngIf` :  Permite esconder componentes do template com base em determinado critério

```tsx
<app-component *ngIf="component.atributo"></app-component>
```

`*ngFor` : Permite repetir certos elementos do template

```tsx
<app-component *ngFor="let var in lista"></app-component>
	<p>Estou repetindo!</p> 
```

`*ngSwitch` : Funciona da mesma maneira que o *ngIf, permitindo adicionar condições do tipo if-else. Acompanha as diretivas *ngSwitchCase e *ngSwitchDefault para o último caso. 

```html
<div [ngSwitch]="currentItem.feature">
  <app-stout-item *ngSwitchCase="'stout'" [item]="currentItem"></app-stout-item>
  <app-device-item *ngSwitchCase="'slim'" [item]="currentItem"></app-device-item>
  <app-lost-item *ngSwitchCase="'vintage'" [item]="currentItem"></app-lost-item>
  <app-best-item *ngSwitchCase="'bright'" [item]="currentItem"></app-best-item>
  <app-unknown-item  *ngSwitchDefault [item]="currentItem"></app-unknown-item>
</div>
```

#### Diretivas de Atributos

Modificam o comportamento de elementos HTML, propriedades, atributos e componentes.

`ngClass` : Adicionam ou removem múltiplas classes simultaneamente (semelhante ao class binding).

```tsx
currentClasses: Record<string, boolean> = {};

setCurrentClasses() {
  // CSS classes: added/removed per current state of component properties
  this.currentClasses = {
    saveable: this.canSave,
    modified: !this.isUnchanged,
    special: this.isSpecial,
  };
}
```

```html
<div [ngClass]="currentClasses">
	This div is initially saveable, unchanged, and special.
</div>
```

`ngStyle` : Adicionam ou removem múltiplos atributos CSS simultaneamente. 

```tsx
currentStyles: Record<string, string> = {};
/* . . . */
setCurrentStyles() {
  // CSS styles: set per current state of component properties
  this.currentStyles = {
    'font-style': this.canSave ? 'italic' : 'normal',
    'font-weight': !this.isUnchanged ? 'bold' : 'normal',
    'font-size': this.isSpecial ? '24px' : '12px',
  };
}
```

```html
<div [ngStyle]="currentStyles">
  This div is initially italic, normal weight, and extra large (24px).
</div>
```

`ngModel` : 

```tsx

```

## Injeção de Dependências

É um design pattern oferecido pelo Angular, que permite importar e instanciar classes de outros arquivos, de uma maneira mais elegante e flexível. 

Os agentes do processo podem ser definidos como provedores e consumidores de dependência. Quando uma classe provedora é requisitada, o Angular verifica se já existe uma instância dessa classe para ser utilizada (Singleton). 

### Services

São módulos usados para compartilhar regras de negócio, dados ou funcionalidades entre diferentes partes da aplicação, que não são funções delegadas aos componente (que geralmente trabalham as noções de experiência do usuário e manipulação do DOM. Os services fazem o papel de *providers* para os componentes.

```tsx
@Injectable()
class HeroService {}
```

```tsx
@Component({
  standalone: true,
  selector: 'hero-list',
  template: '...',
  providers: [HeroService] // permite acessar a classe no contexto do componente.
})
class HeroListComponent {
	
	// o construtor sinaliza quais dependências o componente precisa.
	constructor(private service: HeroService) {} 
}
```

Para tornar uma classe provedora disponível para toda a aplicação, podemos declará-la como *provider* no arquivo principal `app.config.ts` ou utilizando o argumento “providedIn”.

```tsx
export const appConfig: ApplicationConfig = {
    providers: [
      { provide: HeroService },
    ]
};
```

```tsx
@Injectable({
  providedIn: 'root'
})
class HeroService {}
```

## Roteamento

### RouterModule

O Angular possui um sistema de roteamento que permite a navegação entre diferentes componentes sem recarregar a página inteira, a fim de manter a experiência de SPA. O objeto `Router` funciona como um interpretador, que ao receber uma URL nova, permite visualizar o tipo de componente vinculado àquela rota URL.

A principal maneira de definir o roteamento dentro do template é por meio da diretiva `<router-outlet>` , que vai agir como elemento “coringa”. Precisamos também definir quais links estão associados a quais componentes, no arquivo `app.routes.ts`. 

```tsx

```

## Comunicação com o Servidor

O Angular inclui ferramentas para fazer requisições HTTP a servidores remotos, como APIs, para buscar ou enviar dados de um servidor que lida com regras de negócio, conhecido como back-end.

Os módulos `HttpClient` e `RxJS` permitem realizar tais requisições de maneira assíncrona, a fim de:

- obter respostas já tipadas;
- realizar o tratamento de erros;
- oferecer ferramentas de teste;
- possibilitar a interceptação de requisições/respostas.

### HttpClient

O módulo `HttpClient` permite realizar tais requisições de forma assíncrona para obter respostas já tipadas, tratamento de erros, ferramentas de teste, interceptação de requisições/respostas.

### RxJS

O módulo RxJS (Reactive eXtensions for JavaScript) é usado no Angular para trabalhar com programação reativa. Ela facilita o gerenciamento de fluxos de dados assíncronos, permitindo o uso de *observables* para lidar com eventos, promessas, streams e muito mais. Os *observables* facilitam a manipulação, transformação e combinação de dados em tempo real. 

**Documentação:** [https://rxjs.dev/guide/overview](https://rxjs.dev/guide/overview)

### Requisições HTTP

Para utilizar o módulo `HttpClient`, é necessário importá-lo no arquivo `main.ts`, permitindo que esse módulo seja injetável em qualquer parte da aplicação. 

```tsx
import { bootstrapApplication } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { importProvidersFrom } from '@angular/core';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(HttpClientModule),
  ]
});
```

O primeiro passo é criar um arquivo `app.models.ts` , onde podemos definir os tipos esperados para as chaves da resposta JSON. Utilizamos a estruturas de dados *interface*, que funciona como um dicionário (objeto) tipado.

```tsx
export interface Hero {
  heroesUrl: string;
  textfile: string;
  date: any;
}
```

Podemos criar um “serviço”, que pode ser consumido por outras partes da aplicação. Esse serviço será responsável pela realização da requisição HTTP.

```tsx
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from '@angular/rxjs'
import { Hero } from './app.models.ts'

@Injectable()
export class ConfigService {
  url: string = 'http://localhost:4200';
	constructor(
		private http: HttpClient // injeta a biblioteca HttpClient
	) { }

	getConfig() {
	  return this.http.get Observable<Hero>(this.url);
	}
}
```

`httpClient.get()` : Realiza a consulta a um servidor por meio do protocolo HTTP.

- url: URL do serviço requisitado
- options: permite passar os headers, bem como o tamanho da resposta e os parâmetros da URL

As requisições HTTP retornam objetos do tipo *Observable*, oriundos da biblioteca RxJS, que faz a requisição “preguiçosa” de um evento. Enquanto não há retorno do servidor, os observables permitem que a aplicação continue rodando de forma assíncrona, e “notificam” o sistema quando o evento é finalizado (no caso, o quando o cliente obtêm uma resposta). Para que um método ou função seja notificada quando o evento ocorre, devemos utilizar o método `subscribe()` dentro de um Observable. 

Os Observables esperam funções como argumentos, que serão executadas com base na resposta obtida. Assim, podemos realizar o tratamento de erros (caso ocorram) ou continuar a execução da aplicação, realizando algum tipo de manipulação com os dados quando forem obtidos.

```tsx
import { Observable } from '@angular/rxjs'
import { Hero } from './app.models.ts'

@Component({
  standalone: true,
  selector: 'hero-list',
  template: '...',
  providers: [HeroService] // permite acessar a classe no contexto do componente.
})
class HeroListComponent implements OnInit {
	
	// o construtor sinaliza quais dependências o componente precisa.
	constructor(
		private heroService: HeroService
	) {} 

	heroesUrl: any
	textfile: any
	date: any

	ngOnInit() {
		this.getConfig()
	}

	getConfig() {
	  this.heroService.getConfig().subscribe({
			
			// roda essa função caso receba uma resposta, e retorna a resposta
			next: data => this.config = { 
        heroesUrl: data.heroesUrl,
        textfile:  data.textfile,
        date: data.date
			},

			// roda essa função caso não receba uma resposta, e retorna um objeto do tipo HttpErrorResponse
			error: errors => this.error = { 
			},
			
			// roda essa função assim que finaliza o processo
			complete: data => this.completed = {
			},
    });
	}
}
```

## Validação de Formulários

### FormsModule

```tsx

```

## 