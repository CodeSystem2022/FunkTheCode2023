//los arreglos en js son tipo objects

//declarar un array:
//let autos = new Array("ferrari", "audi", 'fiat'); //sintaxis vieja, discontinuada!
const autos = ["ferrari", "audi", "fiat", "ford", "alfa romeo", "chevrolet"];
const motos = ["yamaha", "motomel", "zanella", "gilera", "dukati", "suzuki"];

console.log(autos);
console.log(motos);

console.log(autos[4]);
console.log(motos[5]);

//para recorrer:

for (let i = 0; i < autos.length; i++) {
  console.log(i + "=" + autos, [i]);
}

for (let i = 0; i < motos.length; i++) {
  console.log(i + "=" + motos, [i]);
}
// Codigo de Matias
//para modificar un elemento de un array:

autos[2] = "volvo";
console.log(autos[2]);
console.log(autos);

//agregar nuevos elementos:
autos.push("Toyota");
console.log(autos);

//otra manera de agregar elementos;

autos[autos.length] = "porsche";
console.log(autos);

//otra manera pero que hay que tener cuidado al emplearla: no es una buena practica.

autos[8] = "mercedez benz";
console.log(autos);

//como preguntar si es un array:
console.log(Array.isArray(autos));
console.log(Array.isArray(motos));
//otra manera para preguntar si es un array:
console.log(autos instanceof Array);
/*//para modificar un elemento de un array:

autos[2] = "volvo";
console.log(autos[2]);
console.log(autos);

//agregar nuevos elementos:
autos.push("Toyota");
console.log(autos);

//otra manera de agregar elementos;

autos[autos.length] = "porsche";
console.log(autos);

//otra manera pero que hay que tener cuidado al emplearla: no es una buena practica.

autos[8] = "mercedez benz";
console.log(autos);

//como preguntar si es un array:
console.log(Array.isArray(autos));
console.log(Array.isArray(motos));
//otra manera para preguntar si es un array:
console.log(autos instanceof Array);
*/
