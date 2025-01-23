//create a function makeItWalk() that takes an animal as an input then calls the method walk of that animal and then prints name of the animal has walked some distance every animal should have a name walk and walk 


let dog = {
  name : "bruno",
  walk : function(x){
    return 20;
  }
}
let cat = {
  name : "Srhi",
  walk(){
    return 15
  }
}
let rabbit = {
  name : "anshi",
  walk: ()=> 20
}
function makeItWalk(animal){
  // console.log(`${animal.ani} has walked ${walk}`)
  let distance = animal.walk
  console.log(`${animal.name} has walked ${distance}m`)
}

makeItWalk(dog)
makeItWalk(cat)
makeItWalk(rabbit)

let animals = [dog,cat,rabbit]

for (let i= 0 ;i < animals.length ; i++){
  makeItWalk(animals[i])
}

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