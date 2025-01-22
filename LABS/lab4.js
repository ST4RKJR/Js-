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

