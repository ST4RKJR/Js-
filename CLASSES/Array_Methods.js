let array = [1,2,3,4,5]
// let x = 4
// for (let i = 0;i < array.length; i++){
//     if (array[i] == x){
//         console.log(array[i]**3)
//     }else{
//         console.log("NOT FOUND")
//     }
// }

// for (let num of array){
//     console.log(num**3)
// }

let printCube = (x) => (console.log(x**3))
for (let i of array){
    printCube(i)
}

array.forEach(printCube)

array.forEach(function (x){
    console.log(x**3)
})

array.forEach(num => {
    console.log(num**3)
})

array.forEach(num => console.log(num**3))


let hari = [2,3,4,5,6,7]

let s = hari.map(marks => { //does not returns the value for each iteration when {} used or not return used
     marks*2
})
let t = hari.map(marks => marks*2) //returns the square for every value and the map gives the array of those elements have the same length 

console.log(s)
console.log(t)




