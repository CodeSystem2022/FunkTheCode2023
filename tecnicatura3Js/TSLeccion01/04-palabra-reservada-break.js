//Break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando); //Muestra todos los números pares
        break;//Muestra solo el 1er número par porque rompe la estructura del if y termina con la búsqueda
    }
}
console.log("Termina el ciclo al encontrar el primer número par");
