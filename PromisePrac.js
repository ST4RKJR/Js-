let AgeValidator = new Promise((resolve,reject)=>{
    if(age>= 18){
        resolve("Eligible to Vote")
    }else{
        reject("Not Eligible to Vote")
    }

}).then()


async function getData(){
    const url = "https://fakestoreapi.com/products"
    try{
        const response = await fetch(url)
        const data = await response.json()
        console.log(data)
        let receiveData = data
    }catch(error){
        console.error(error.message)
    }
}

getData()

function getData() {
    const url = "https://fakestoreapi.com/products";
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            let receiveData = data;
        })
        .catch(error => console.error(error.message));
}
getData()