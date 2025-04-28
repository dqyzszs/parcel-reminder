function generateParcelUpdate() {
  const statuses = ['Shipped', 'In Transit', 'Out for Delivery', 'Delivered'];
  const parcelId = `PRCL${Math.floor(Math.random() * 100000)}`;
  const status = statuses[Math.floor(Math.random() * statuses.length)];
  const location = ['New York', 'Los Angeles', 'Chicago', 'Houston'][Math.floor(Math.random() * 4)];
  const time = new Date().toISOString();

  console.log(`[${time}] Parcel ${parcelId} is currently "${status}" at ${location}.`);
}

function main() {
  generateParcelUpdate();
}

main();
