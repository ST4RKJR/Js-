let  arr = [ 10, 20, 30, 40, 50, 60, "char",{}]
// console.log(arr.isArray())
// arr.push("20")
// console.log("push",arr)

// arr.pop()
// console.log(arr)

// arr.shift(11)
// console.log(arr)

// arr.unshift("11")
// console.log(arr)

// let arr2 = ["my","name","is","sahil"]
// console.log(arr2.join(" "))
// console.log(arr2.join(arr))

let ans2 = [7 , 8, 9, 10 ]
let ans3 = [1000 , 10000, 100]
// let answ = arr.concat(ans2)
// console.log(answ)

let array = [...arr,...ans2,...ans3]
array.sort()
console.log(array)

