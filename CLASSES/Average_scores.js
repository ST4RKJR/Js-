// function analyzeScores(scores){
//     let arr = scores.filter((ele)=>{if (ele>=  50){return ele}})
//     let sum = 0 
//     if  (arr.length === 0 )return 0
//     else return summ / arr.length
// }
function an(scores){
    // let sum = 0 
    // let count = 0
    // for (let i = 0; i < scores.length ; i ++){
    //     if (scores[i]>=50){
    //         sum += scores[i];
    //         count++;
    //     }
    // }
    let sum = scores.reduce((acc,curr)=>{
        if (curr>=50){
            acc += curr
            count ++;

        }
        return acc
    },0)
}