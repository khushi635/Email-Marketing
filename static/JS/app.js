// document.getElementById("servicesOptionsID").addEventListener("change", calculateTotalPrice);
// document.getElementById("subscriptionPeriod").addEventListener("change", calculateTotalPrice);

function calculateTotalPrice() {

    let selectedService = document.getElementById("servicesOptionsID").value;
    let subscriptionPeriod = document.getElementById("subscriptionPeriod").value;
    let totalPriceLabel = document.getElementById("calculateparice");

    let pricePerMonth;

    // Determine price based on selected service
    switch (selectedService) {
        case "email-service":
            pricePerMonth = 499; // Price for email service (in Rupees)
            break;
        case "vip":
            pricePerMonth = 999; // Price for VIP service (in Rupees)
            break;
        case "prime":
            pricePerMonth = 1499; // Price for Prime service (in Rupees)
            break;
        case "exclusive":
            pricePerMonth = 1999; // Price for Exclusive service (in Rupees)
            break;
        case "prime-exclusive":
            pricePerMonth = 2499; // Price for Prime Exclusive service (in Rupees)
            break;
        // default:
        //     pricePerMonth = 0;
    }

    // Calculate total price based on subscription period
    let totalPrice;
    switch (subscriptionPeriod) {
        case "monthly":
            totalPrice = pricePerMonth;
            break;
        case "quarterly":
            totalPrice = pricePerMonth * 3; // Multiply monthly price by 3 for quarterly
            break;
        case "yearly":
            totalPrice = pricePerMonth * 12; // Multiply monthly price by 12 for yearly
            break;
        // default:
        //     totalPrice = 0;
    }
    console.log("Selected Service:", selectedService);
    console.log("Subscription Period:", subscriptionPeriod);
    console.log("Total Price:", totalPrice);
    // Display total price
    totalPriceLabel.textContent = "Total Price: " + totalPrice + " Rupees";
}

