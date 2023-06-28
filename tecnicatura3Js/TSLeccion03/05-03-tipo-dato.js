function miFuncion(a, b) {
    return a + b
}
  
console.log(typeof miFuncion)

// Una función puede ser definida como un objeto
function miFuncion2(a, b) {
    console.log(arguments)
    console.log(`arguments.length: ${arguments.length}`)
}
miFuncion2(5, 7)

// toString
const miFuncionTexto = miFuncion2.toString()
console.log(miFuncionTexto)
