// let array = [1,2,3,4,5]
// // let x = 4
// // for (let i = 0;i < array.length; i++){
// //     if (array[i] == x){
// //         console.log(array[i]**3)
// //     }else{
// //         console.log("NOT FOUND")
// //     }
// // }

// // for (let num of array){
// //     console.log(num**3)
// // }

// let printCube = (x) => (console.log(x**3))
// for (let i of array){
//     printCube(i)
// }

// array.forEach(printCube)

// array.forEach(function (x){
//     console.log(x**3)
// })

// array.forEach(num => {
//     console.log(num**3)
// })

// array.forEach(num => console.log(num**3))


// let hari = [2,3,4,5,6,7]

// let s = hari.map(marks => { //does not returns the value for each iteration when {} used or not return used
//      marks*2
// })
// let t = hari.map(marks => marks*2) //returns the square for every value and the map gives the array of those elements have the same length 

// console.log(s)
// console.log(t)


// let nums = [1,2,3,4]
// let evenNum = nums.filter(n => !(n%2))

// // write a fucntion that takes an array the fucntion returns the even squares doubles(twice) of the number


// // let evenSquareDouble = nums.filter(x => (evenNum(x))**2)


// let doubles = nums.map(n => 2*n)
// let squares = doubles.map(n => n * n)
// let filter = squares.filter(n => (n%2 == 0))

// console.log(doubles)
// console.log(squares)
// console.log(filter)

// // let result = nums.map(n => n*2).map(n => n*n).filter(n => (n*2 == 0))


var todoList = [
    "drink water",
    "meditate",
    "brush teeth",
    "exercise",
    "study javascript",
    "eat healthy meals"
]

for(var i = 0; i < todoList.length; i++){
    console.log(i);
}

todoList.forEach(function(i){
    console.log(i);
})
