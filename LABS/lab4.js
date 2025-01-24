//JS-Authentication System


function authenticateUser(username, callback, users) {
    const userExists = users.includes(username);
    callback(userExists);
}

function accessCallback(isAuthorized) {
    if (isAuthorized) {
        console.log("Access granted");
    } else {
        console.log("Access denied");
    }
}

//Museum Ticket Booking

function calculateTicketPrice(age, isWeekend, hasStudentCard) {
    let price = 12;

    if (age < 12) {
        price -= 5;
    }
    if (isWeekend) {
        price += 3;
    }
    if (hasStudentCard) {
        price -= 2;
    }

    return price;
}

//Calculator Operation

function doubleResult(func) {
    return function(x) {
      return 2 * func(x);
    };
  }
  
  function addFive(x) {
    return x + 5;
  }

//Debugging Multiplication 

function calculateProduct(...numbers) {
    let product = Number(1); 
    let count =0
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i]!=0){
        product *= (numbers[i]);
        }
        else{
            count +=1
        }
    }
    if (count>0){
        return product;}
    else{
        return 1
    }
}
function greet(name = "Vishal Sir") {  
    return `Good Morning, ${name}!`;  
  }  
  
  console.log(greet(undefined));

var calculate = function(x, y, z = 8) {
    return x * y / z + z;
};

let ans = calculate(2, 6, 3);
console.log(ans);


console.log(`You can vote in ${18-age} years.`)