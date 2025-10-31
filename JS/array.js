//basics methods in array
let fruits = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruits);

console.log(fruits.length); //length of array
console.log(fruits[0]); //accessing element
console.log(fruits[fruits.length - 1]); //accessing last element

console.log(fruits.pop()); //removing last element

console.log(fruits.push("Pineapple")); //adding element at last

console.log(fruits.shift()); //removing first element
console.log(fruits.unshift("Strawberry")); //adding element at first

console.log(fruits.slice(1, 3)); //slicing array from index 1 to 2

//for each method
fruits.forEach(fruit =>{
    console.log(fruit);
});