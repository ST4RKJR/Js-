let array = [1,2,3,4,5]
// let x = 4
for (let i = 0;i < array.length; i++){
    if (array[i] == x){
        console.log(array[i]**3)
    }else{
        console.log("NOT FOUND")
    }
}

for (let num of array){
    console.log(num**3)
}