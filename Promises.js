let vara = 5;
let newPromise = new Promise((resolve,reject)=>{
    if (vara % 2 == 0){
        resolve(vara);
    }else{
        reject("Number is odd");
    }
})
newPromise
.then((value)=>{console.log(value*value)})
.catch((err)=>{console.log(err)})
.finally(()=>{console.log("Finally Ended!")})
