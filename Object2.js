obj = {
    name:"raghav",
    sub:"WAP",
    year:2025
}
const keys = Object.keys(obj);
console.log(keys)

const values = Object.values(obj)
console.log(values)

const entries = Object.entries(obj)
console.log(entries)

entries[1][1] = "DSA"
const newobj = Object.fromEntries(entries)
console.log(newobj)


function doubleValues(inputObject) {
    const entries = Object.entries(inputObject)
    // entries[0][1] *= 2
    // entries[1][1] *= 2
    // entries[2][1] *= 2
    for (let i = 0;i<entries.length;i++){
        entries[i][1] *= 2
    }
    const news = Object.fromEntries(entries)
    return news

}


function getHighestEnrolled(obj) {
    let max = Math.max(...Object.values(obj))
    let result = Object.keys(obj).filter((el)=>obj[el]===max)
    return result
}


const obj1 = { Alice: 85, Bob: 92, Charlie: 88 };
const obj2 = { David: 90, Eve: 95, Frank: 80 };

const merged = { ...obj1, ...obj2 };

const sorted = Object.fromEntries(
    Object.entries(merged).sort((a, b) => b[1] - a[1])
);

console.log(sorted);