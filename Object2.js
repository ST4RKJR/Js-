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
