/* 
---   RESUMO JAVASCRIPT VANILLA   ---
Autor: Bruno Marcelino
Data: 03/08

Criação de Script que resume os conceitos básicos da linguagem JavaScript, sob os moldes do conhecimento em Python.
*/

/*
    OBSERVAÇÕES

-- ';' nao é necessário para terminar as sentenças
--

*/

/* --- Criação de variáveis --- */

var a = 123; // modo antigo de declarar variáveis
const b = 123; // cria uma variável que só pode ser declarada uma vez, e não é alterada
let c = 123; // cria uma variável que só pode ser declarada uma vez, mas pode ser alterada ao longo do código.
console.log(a, b, c)

// - Hoisting (içar ou elevar): É o sistema de declaração de variáveis do JavaScript. O código executa primeiro as declarações de variáveis do tipo `const`
// O hoisting permite usar uma função antes de declará-la, por exemplo. Ele ocorre dentro do escopo das funções também.
// O JavaScript apenas eleva (hoists) as declarações, não as inicializações. Se uma variável for declarada e inicializada após usá-la, o valor será undefined
console.log(num); // Retorna undefined
var num;
num = 6;
console.log("---------------\n")


/* --- Estruturas de dados --- */

// - Objetos: são os tipos de dados que existem. Cada tipo permite realizar determinadas operações com os dados.
console.log(typeof a)

// Strings

const d = "123"
console.log(d*2) // converte em numero e faz a conta, se não consegue retorna NaN
console.log(`${d} é uma template string!`) // f-string do JavaScript
console.log("---------------\n")

// Number

const e = 1234
console.log(e/0) // Possui tipo "Infinito"
console.log(Math.PI, Math.pow(e, 2)) // Módulo que armazena constantes e realiza potenciação
console.log("---------------\n")

// Bool

let f = true
console.log(!f) // negação 
console.log(!!3, !!-1, !!" ", !![], !!{}, !!Infinity, ) // converte qualquer tipo para seu correspondente booleano
console.log(!!0, !!"", !!null, !!NaN, !!undefined, !!(f=false)) // converte qualquer tipo para seu correspondente booleano

console.log(true && true) // e
console.log(true || false) // ou
console.log("---------------\n")

// Array

let g = [1,2]
console.log(g, g[0], g[1], g[2]) // acessa os índices do array. Se não tem, retorna undefined
console.log(g.length) // tamanho do array

g.push(3, "a") // adiciona elementos ao array
console.log(g)

g.pop() // apaga o ultimo valor do array
console.log(g) 

delete g[0] // apaga um elemento do array, e deixa o campo vazio
console.log(g)
console.log("---------------\n")

// Object

let h = {"A": 1, "B": 2, "C": 3} // cria pares [key] = value (keys devem ser únicas)

h.D = 4 // adiciona chave-valor ao objeto
h["E"] = 5 // adiciona chave-valor ao objeto
console.log(h)
console.log("---------------\n")


/* --- Funções --- */