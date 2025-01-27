let  arr = [ 10, 20, 30, 40, 50, 60, "char",{}]
// console.log(arr.isArray())
arr.push("20")
console.log("push",arr)

arr.pop()
console.log(arr)

arr.shift(11)
console.log(arr)

arr.unshift("11")
console.log(arr)

let arr2 = ["my","name","is","sahil"]
console.log(arr2.join(" "))
console.log(arr2.join(arr))