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