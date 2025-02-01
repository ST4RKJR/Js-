let objectName={};
console.log(objectName)

let car={
    name:"Koenigsegg Jesko",
    brand:"Koenigsegg Automotive AB",
    category:"Hyper Car",
    priceRange: "1.8M - 10M",
    topSpeed: "450km/h",
    "tank capacity" : "72 Litres",
    start(){
        return "car started"
    },
    stop:function(){
        return "car stopped"
    },
    name:function(n){
        return `${n} is my name.`
    },
    horn: ()=>{
        return `car makes the horn`
    }
}
car.colour="Yellow"
car["no of seats"] = 2;
console.log(car)



//when we create a function outside a function 
car.accelerate=function accelerate(){
    return `car accelerated`;
}


//to delete
// delete car.[tank capacity]
// console.log(car)

//function
console.log(car.start())
console.log(car.stop())
console.log(car.name("SAHIL"))
console.log(car.horn())
console.log(car)
console.log(car.accelerate())