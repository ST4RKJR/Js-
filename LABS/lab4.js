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

