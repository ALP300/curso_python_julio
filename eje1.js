/*
5. Suma condicional de múltiplos:
Pide un número N y suma solo los 
múltiplos de 3 o 5 hasta N.
Muestra la suma y los
múltiplos encontrados.
*/
let n= 30
suma=0
multiplos=[]
for(let i=0; i<=n;i++){
    if(i%3===0 || i%5===0){
        suma+=i
        multiplos.push(i)
    }
}
console.log(`Múltiplos de 3 y 5 de ${n}: ${multiplos.join(", ")}`)