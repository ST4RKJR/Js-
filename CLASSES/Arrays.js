// // let arr = [10,2,3,4,5]
// // let isOdd = (x) => !!(x%2)


// // //f(23)
// // console.log(isOdd(23))

// // let firstOdd = arr.find(isOdd)
// // console.log(firstOdd)

// // function AscendingCompareFunction(a,b){
// //     return a - b
// // }
// // function DescendingCompareFunction(a,b){
// //     return b - a
// // }
// // let array = [1,2,15,22,3]
// // // console.log(array.sort((a,b)=>(parseInt(a)-parseInt(b))))
// // console.log(array.sort(AscendingCompareFunction(a,b)))


// //write a program to reverse a array using only push pop unshift shift

// let arr = [1,2,3,4,5]
// let rev = []
// // for (let i = 0 ; i < arr.length ; i++){
// //     // let x = arr.pop(arr[i])
// //     // console.log(x)
// //     arr.shift(arr[i])
// //     // console.log(y)
// //     arr.unshift(arr[i])

// // }
// // console.log(arr)

// // while (arr.length){
// //     rev.push(arr.pop())
// // }
// // console.log(rev)

// while (arr.length){
//     rev.unshift(arr.shift())
// }
// console.log(rev)

// let a = [1,2,3]
// let b = a
// b[1] = 45
// console.log(a)
// console.log(b)
// a = 23
// b = 45
// a = 5
// console.log(a)
// console.log(b)


// function sum(a, b, ...args) {
//     console.log(a, b, args); 
//   }
//   sum(1, 2, 3, 4, 5);
  
  
//   const nums = [1, 2, 3];
//   console.log(Math.max(...nums)); 


// const arr1 = [1, 2, { name: 'Nishchal' }];
// const arr2 = arr1;

// arr2[2].name = 'Ajay';
// arr2[0] = 100;

// console.log('Array 1:', arr1);
// console.log('Array 2:', arr2);


// function modify() {
//     let arr1 = [10, 20, 30];
//     const arr2 = [40, 50, 60];

//     arr1.push(arr2);
//     arr1.pop();
//     arr2[0] = 99;

//     console.log("Array 1:", arr1);
//     console.log("Array 2:", arr2);
// }

// function updateCart() {
//     let cart = [5, 10, 15, 20];

//     cart.shift();

//     console.log("Updated Cart:", cart);
// }

// updateCart();

// const numbers = [40, 10, 100, 25, 50];
// numbers.sort((a, b) => a - b);
// console.log(numbers);

const mixedArray = ["Hello", 1, "world", 2, "JavaScript"]; 
const result = mixedArray.join(" "); console.log(result);
 