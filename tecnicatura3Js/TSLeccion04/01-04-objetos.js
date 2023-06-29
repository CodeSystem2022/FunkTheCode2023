//Distintas formas de crear objetos - Bárbara
let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log("tipos primitivos");
//objeto
let persona = {
    nombre: 'carlos',
    apellido: 'gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); // convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ // metodo a funcion en JavaScript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){
        return 'el nombre es: '+this.nombre+', Edad: '+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

console.log("ejecutando con un objeto");
let persona2 = new Object(); // debe crear un nuevo objeto en memoria
persona2.nombre = 'juan';
persona2.direccion = 'salada 13';
persona2.telefono = '549248756'
console.log(persona2.telefono);

console.log("creamos un nuevo objeto");
console.log(persona['apellido']); // Accedemos como si fuera un arreglo 

console.log("usamos el ciclo for in")
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad)
    console.log(persona[propiedad]);
}

console.log("cambiamos y eliminamos un error");
persona.apellida = 'Betancud'; //cambiamos dinamicamente el valor de un objeto
delete persona.apellida; // eliminamos el error
console.log(persona);

//distintas formas de imprimir un objeto
//numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log("distintas formas de imprimir un objeto: forma 1")
console.log(persona.nombre+', '+persona.apellido);

//numero 2: a travez del ciclo for in
console.log("distintas formas de imprimir un objeto: forma 2")
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad])
}

//numero 3: la funcion object.values()
console.log("distintas formas de imprimir un objeto: forma 3")
let personaArray = Object.values(persona);
console.log(personaArray);

//numero 4: tilizaremos el metodo JSON.stringify
console.log("distintas formas de imprimir un objeto: forma 4")
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idioma');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){ // constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre = new Persona3("Leo","Lopez","lopezl@mail.com");
padre.nombre = "Luis"; // modificamos el nombre
padre.telefono = "54865432516";
console.log(padre);
console.log(padre.nombreCompleto())//utilizamos la funcion
let madre = new Persona3("Laura", "Contrera","contreraL@gmail.com");
console.log(madre);
console.log(madre.telefono); // la propiedad no esta definida
console.log(madre.nombreCompleto());

//diferentes foras de crear objetos
//caso numero 1
let miObjeto = new Object(); // esta es un opcion formal
//caso numero 2
let miObjeto2 = {}; // esta opcion es breve y recomendada

//caso String 1
let miCadena1 = new string("HOLA"); // sintaxis formal
//caso String 2
let miCadena2= "hola"; // esta es la sintaxis simplificada y recomedada

//caso con numeros 1
let miNumero = new Number(1); // es formal no recomendable
//caso con numeros 2 
let miNumero2 = 1; //sitaxis recomendada

//caso boolean 1 
let miBoolean1 = new Boolean(false); // formal
//caso boolean 2 
let miBoolean2 = false; // recomendada

//caso arreglos 1
let miArreglo1 = new Array(); //formal
//caso arreglos 2 
let miArreglo2 =[]; //recomendada

//caso function 1 
let miFuncion1 = new function(){}; // todo despues de new es considerado objeto
//caso function 2 
let miFunction2 = function(){}; // notacion simplificada y recomendada

//uso de prototype
Persona3.prototype.telefono = "156879865";
console.log(padre);
console.log(madre.telefono);
console.log (madre.telefono);'2604591803';

//Uso de call
let persona4 = {
    nombre: 'Ricardo',
    apellido: 'lopez',
    nombreCompleto2: function(titulo, telefono){
        return this.nombre+' '+this.apellido+ ''+telefono;
      // return this.nombre+' '+this.apellido;

    }
}
let persona5 = {
    nombre: 'Ruben',
    apellido: 'Lara',
}

console.log(persona4.nombreCompleto2('Lic.','5401457852132'));
console.log(persona4.nombreCompleto2.call(persona5,'Ing.', '542677424855'));


//Metodo Apply
let arreglo = ['Ing.', '54267851231'];
console.log(persona4.nombreCompleto2.apply(persona5,arreglo));

/*
let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log("tipos primitivos");
//objeto
let persona = {
    nombre: 'carlos',
    apellido: 'gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); // convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ // metodo a funcion en JavaScript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){
        return 'el nombre es: '+this.nombre+', Edad: '+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

console.log("ejecutando con un objeto");
let persona2 = new Object(); // debe crear un nuevo objeto en memoria
persona2.nombre = 'juan';
persona2.direccion = 'salada 13';
persona2.telefono = '549248756'
console.log(persona2.telefono);

console.log("creamos un nuevo objeto");
console.log(persona['apellido']); // Accedemos como si fuera un arreglo 

console.log("usamos el ciclo for in")
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad)
    console.log(persona[propiedad]);
}

console.log("cambiamos y eliminamos un error");
persona.apellida = 'Betancud'; //cambiamos dinamicamente el valor de un objeto
delete persona.apellida; // eliminamos el error
console.log(persona);

//distintas formas de imprimir un objeto
//numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log("distintas formas de imprimir un objeto: forma 1")
console.log(persona.nombre+', '+persona.apellido);

//numero 2: a travez del ciclo for in
console.log("distintas formas de imprimir un objeto: forma 2")
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad])
}

//numero 3: la funcion object.values()
console.log("distintas formas de imprimir un objeto: forma 3")
let personaArray = Object.values(persona);
console.log(personaArray);

//numero 4: tilizaremos el metodo JSON.stringify
console.log("distintas formas de imprimir un objeto: forma 4")
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idioma');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){ // constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre = new Persona3("Leo","Lopez","lopezl@mail.com");
padre.nombre = "Luis"; // modificamos el nombre
padre.telefono = "54865432516";
console.log(padre);
console.log(padre.nombreCompleto())//utilizamos la funcion
let madre = new Persona3("Laura", "Contrera","contreraL@gmail.com");
console.log(madre);
console.log(madre.telefono); // la propiedad no esta definida
console.log(madre.nombreCompleto());

//diferentes foras de crear objetos
//caso numero 1
let miObjeto = new Object(); // esta es un opcion formal
//caso numero 2
let miObjeto2 = {}; // esta opcion es breve y recomendada

//caso String 1
let miCadena1 = new string("HOLA"); // sintaxis formal
//caso String 2
let miCadena2= "hola"; // esta es la sintaxis simplificada y recomedada

//caso con numeros 1
let miNumero = new Number(1); // es formal no recomendable
//caso con numeros 2 
let miNumero2 = 1; //sitaxis recomendada

//caso boolean 1 
let miBoolean1 = new Boolean(false); // formal
//caso boolean 2 
let miBoolean2 = false; // recomendada

//caso arreglos 1
let miArreglo1 = new Array(); //formal
//caso arreglos 2 
let miArreglo2 =[]; //recomendada

//caso function 1 
let miFuncion1 = new function(){}; // todo despues de new es considerado objeto
//caso function 2 
let miFunction2 = function(){}; // notacion simplificada y recomendada

//uso de prototype
Persona3.prototype.telefono = "156879865";
console.log(padre);
console.log(madre.telefono);
console.log (madre.telefono);'2604591803';

//Uso de call
let persona4 = {
    nombre: 'Ricardo',
    apellido: 'lopez',
    nombreCompleto2: function(titulo, telefono){
        return this.nombre+' '+this.apellido+ ''+telefono;
      // return this.nombre+' '+this.apellido;

    }
}
let persona5 = {
    nombre: 'Ruben',
    apellido: 'Lara',
}

console.log(persona4.nombreCompleto2('Lic.','5401457852132'));
console.log(persona4.nombreCompleto2.call(persona5,'Ing.', '542677424855'));


//Metodo Apply
let arreglo = ['Ing.', '54267851231'];
console.log(persona4.nombreCompleto2.apply(persona5,arreglo));
*/
