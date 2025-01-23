//create a function makeItWalk() that takes an animal as an input then calls the method walk of that animal and then prints name of the animal has walked some distance every animal should have a name walk and walk 


// let dog = {
//   name : "bruno",
//   walk : function(x){
//     return "20";
//   }
// }
// let cat = {
//   name : "Srhi",
//   walk(){
//     return "15"
//   }
// }
// let rabbit = {
//   name : "anshi",
//   walk: "20",
// }
// function makeItWalk(animal){
//   // console.log(`${animal.ani} has walked ${walk}`)
//   let distance = animal.walk
//   console.log(`${animal.name} has walked ${distance}m`)
// }

// makeItWalk(dog)
// makeItWalk(cat)
// makeItWalk(rabbit)

// let animals = [dog,cat,rabbit]

// for (let i= 0 ;i < animals.length ; i++){
//   makeItWalk(animals[i])
// }


//functions that takes function as an input
// function first(age){
//   function person(x){

//   } 
// }

function mul(a,b){
  return a*b
}
function add(a,b){
  return a+b
}
function domath(x,y,z){
  if ( z == "mul"){
    return `multiplication of ${a} and ${b} is ${mul(x,y)}.`
  }
  else if (z == "add"){
    return `addition of ${a} and ${b} is ${add(x,y)}.`
  }
  
}
let a = 10
let b = 20
let c = "mul"
console.log(add(a,b))
console.log(mul(a,b))
console.log(domath(a,b,c))

function greet(x){
  console.log(`Hello ${x}`)
}
function createAwisher(xname){
  greet(xname)
}

let y = "Sahil"
createAwisher(y)

// function makeItWalk(animal){
//   dis = walk(animal)
// }
// function walk(){
//   return `the ${animal} `
// }

// function obj(animal) {
//     distance = walk(y)
//     return function animal() {
//         distance_walked = animal()
//       return walk(x);
//     };
//   }


// function doubleResult(func) {
//   return function(x) {
//     return 2 * func(x);
//   };
// }

// function addFive(x) {
//   return x + 5;
// }