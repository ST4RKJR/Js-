let orders = []; 

async function menu() {
    const url = "http://50.50.50.115:3000/api/menu";
    const response = await fetch(url);
    const data = await response.json();

    console.log("Welcome to our Restaurant!\n");
    console.log("Today's Menu:\n");

    data.forEach(({ id, itemName, availableQuantity, price }) => {
        console.log(`ID: ${id} | Name: ${itemName}`);
        console.log(`Available: ${availableQuantity} | Price: $${price}\n`);
    });

    const ordID = prompt("Enter the item ID you want to order:");
    const ordQty = prompt("Enter the quantity:");
    const customerName = prompt("Enter your name:");

    if (ordID && ordQty && customerName) {
        console.log("Placing your order...");

        setTimeout(() => {
            console.log("Order placed successfully!");
            orders.push({ ordID, ordQty, customerName });

            setTimeout(() => {
                console.log("Order is ready! Thank you for shopping with us!");
            }, 2000);
        }, 1000);
    } else {
        console.log("Order canceled or invalid input.");
    }
}

function displayOrders() {
    if (orders.length === 0) {
        console.log("No orders placed yet.");
    } else {
        console.log("\nOrder List:");
        orders.forEach(order => {
            console.log(`Customer: ${order.customerName} | Item ID: ${order.ordID}`);
            console.log(`Quantity: ${order.ordQty}\n`);
        });
    }
}



