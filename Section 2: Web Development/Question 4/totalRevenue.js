// Dataset
const sales = [
  { item: "Pen", price: 20, quantity: 3 },
  { item: "Book", price: 200, quantity: 2 },
  { item: "Bag", price: 800, quantity: 1 }
];

// Function to calculate total revenue
// This function multiplies the price and quantity of each sale item and sums them up to get the total revenue.
function calculateTotalRevenue(data) {
  let total = 0;
  for (let sale of data) {
    total += sale.price * sale.quantity;
  }
  return total;
}

// Run the function
const totalRevenue = calculateTotalRevenue(sales);
console.log("Total Revenue:", totalRevenue);
