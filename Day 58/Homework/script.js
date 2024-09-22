const car = {
    model: 'M piat(5)',
    brand: 'Luka',
    year: 2024,
}

console.log(car.brand);
console.log(car.year);

car.color = 'white-black';
console.log(car.color);

car.year = '2025';
console.log(car.year);

delete car.model;

car.StartEnigne = 'Engine started!';
console.log(car.StartEnigne);

car.owner = 'Luka';
console.log(car.owner);