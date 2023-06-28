//La palabra continue: significa que se va a ejecutar la siguiente iteración del ciclo
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue; // Esto va a continuar a la siguiente iteración
    }
    console.log(contando);
}
console.log("Termina el ciclo");
