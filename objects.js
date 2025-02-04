// // let car = {
// //     brand :"Koegnissegg",
// //     model :"Jesko",
// //     color :"Red",
// //     speed(){
// //         "Runs on the Speed of 500Km/hr"
// //     },
// // }

// // console.log(Object.keys(car))


// // let car = {
// //     brand: "Koenigsegg",
// //     model: "Jesko",
// //     color: "Red",
// //     speed() {
// //         return "Runs on the Speed of 500Km/hr";
// //     },
// // };

// // for (let [key, value] of Object.entries(car)) {
// //     console.log(`${key}: ${typeof value}`);
// // }

// // let methods = Object.keys(car).filter(k =>{
// //     return typeof car[k] === "function"
// // })

// // console.methods


// //how to use object.entries and object.fromentries


// //ShallowCopy and DeepCopy
// const vamshi = {
//     age : 19,
//     lc : 850,
//     githubStreak: {
//         count : 21,
//         unit : "days"
//     },
//     githubHandle: "dingdong_vamshi",
//     voulnteer(){
//         return "Feeds street dogs"
//     },
//     play(){
//         console.log("Throws a volleyball at your face!")
//     },
//     dance(){
//         return "breaks the floor"
//     }
// }


// vamshi.lc = 1050

// const imposter = {...vamshi }

// imposter.lc = 1050



// //underscore library and lowdash library



// imposter.lc = 50

// console.log(vamshi)
// console.log(imposter)

// console.log(JSON.stringify(vamshi,null,2))


// let copyofVamshi 

function printKeys(obj){
    for (key in obj){
        console.log(key)
    }
    
}

function printValues(obj){
    for(key in obj){
        if (obj[key] > 50){
            console.log(obj[key])
        } 
    }
}