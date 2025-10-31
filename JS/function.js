//Create a fujction with 2 parameters and display their sum
function sum_of_two(num1, num2){
    console.log(num1 + num2)
    // document.write("The sum is: " + (num1 + num2));
}
sum_of_two(5, 10)

//write a function that takes 3 parameter and find largest of all
function largest_of_three(a, b, c){
    if(a>b && a>c){
        console.log(a + " is the largest number");
    }else if(b>a && b>c){
        console.log(b + " is the largest number");
    }else{
        console.log(c + " is the largest number");
    }
}
largest_of_three(5, 10, 15);

//function expression
let largest_of_three1 = function(a, b, c){
    if(a>b && a>c){
        console.log(a + " is the largest number");
    }else if(b>a && b>c){
        console.log(b + " is the largest number");
    }else{
        console.log(c + " is the largest number");
    }
}
largest_of_three1(5, 10, 15);

//arrow function
let sum_of_two1 = (num1, num2) => {
    console.log(num1 + num2)
}
sum_of_two1(20, 30);

//create a function to display factorial of any number
function factorial(n){
    let fact = 1;
    for(let i = 1; i <= n; i++){
        fact *= i;
    }
    console.log("The factorial of " + n + " is: " + fact);
}
factorial(5);

//create a function factorial of number between  1 to 10 by using higher order function(1 function output is input of another function)
function factorial1(n){
    let fact = 1;
    for(let i=n; i>=2; i--){
        fact *= i;
    }
    console.log(fact);
}
function display(fun){
    for(i=1; i<=10; i++){
        fun(i);
    }
}
display(factorial1)

//map function example to find double of each element in array
let arr = [1, 2, 3, 4, 5];
arr2 = arr.map((num) => num*2);
console.log(arr2);

//hosting example
console.log(a);
var a = 10;               //it work only for var keyword not for let and const
console.log(a);

