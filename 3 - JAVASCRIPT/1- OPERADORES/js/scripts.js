// 1 - Tipo Number
console.log(typeof 2)
console.log(typeof 1.52)
console.log(typeof -5)

// 2 - Operadores aritméticos
console.log(4 + 5)
console.log(4 - 5)
console.log(4 * 5)
console.log(4 / 5)

// 3 - Special  Numbers
console.log(typeof Infinity)
console.log(typeof -Infinity)
console.log(12 * "dois")
console.log(typeof NaN)


// 4 - strings
console("Alexandre")
console("Um texto")
console("Bom dia")

// 5 -  Mais sobre Strings
console.log('Testando a \n quebra de linha')
console.log("Espaçamento \t de tab")

// 6 - Concatenação
console.log("Oi, ", + "tudo bem?")

// 7 - Interpolação(Template Strings)
console.log(`Soma de 2 + 2 = {2 + 2}`)
console.log(`Podemos executar qauqler coisa aqui${console.log("teste")}`)

// 8 - Booleans
console.log(true)
console.log(false)
console.log(5 > 20)
console.log(30 > 10)

// 9 -  Comparações
console.log(5 > 20)
console.log(30 > 10)
console.log(30 == 30)
console.log(30 == 29)
console.log(30 != 29)

// 10 Comparação de idêntico
console.log(30 == "30") 
console.log(30 === "30") 
console.log(30 + "29")
console.log(30 != "29")
console.log(30 !== "29")


// 11 - Operadores Lógicos
console.log(true && true)
console.log(true && false)

console.log (5 > 2 && 2 < 10)
console.log (5 > 2 || 2 < 10)
console.log (5 > 2 && 2 < 10)

console.log(!true)
console.log(!false)

console.log(!5 > 2)

// 12 - Empty Values

console.log(typeof null, typeof undefined)
console.log(null == undefined)
console.log(null === undefined)
console.log(null == false)
console.log(undefined == false)

// 13 - mudança de tipos
console.lgo(5 * null)
console.lgo("teste" * "opa")
console.lgo("10" + 1)
console.lgo("10 "- 1)