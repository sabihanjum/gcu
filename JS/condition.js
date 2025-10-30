//if condition example
//if value of x is more than 10 then display "Hello"
x=15;
if (x > 10) {
    console.log("Hello");
}

//if-else condition example
//if value of x is less than 10 display "Hello", otherwise display "Bye"
// x=5; o/p: Hello
x=15;   //o/p: Bye
if (x < 10) {
    console.log("Hello");
} else {
    console.log("Bye");
}

//display whether nums is a "even numver" or "odd number"
num=7;
if (num % 2 == 0) {
    console.log("even number");
} else {
    console.log("odd number");
}

//if-else-if or ladder if condition example
//if char is a print apple or if char is b bat or if char is c cat or if char d doll otherwise print mango
char='d';
if (char == 'a') {
    console.log("apple");
} else if (char == 'b') {
    console.log("bat");
} else if (char == 'c') {
    console.log("cat");
} else if (char == 'd') {
    console.log("doll");
} else {
    console.log("mango");
}

//if person grade is >90 grade S, >80 grade A+, >70 grade A, >60 grade B+, >50 grade B, >40 grade C or else fail
grade = 85;
if (grade > 90) {
    console.log("grade S");
} else if (grade > 80) {
    console.log("grade A+");
} else if (grade > 70) {
    console.log("grade A");
} else if (grade > 60) {
    console.log("grade B+");
} else if (grade > 50) {
    console.log("grade B");
} else if (grade > 40) {
    console.log("grade C");
} else {
    console.log("fail");
}

// if ladder day example
function withIF(){
    // debugger;
    let dayno = 5;
    if (dayno == 1) {
        console.log("Monday");
    }
    else if (dayno == 2) {
        console.log("Tuesday");
    } else if (dayno == 3) {
        console.log("Wednesday");
    } else if (dayno == 4) {
        console.log("Thursday");
    } else if (dayno == 5) {
        console.log("Friday");
    } else if (dayno == 6) {
        console.log("Saturday");
    } else if (dayno == 7) {
        console.log("Sunday");
    }
    else {
        console.log("Invalid day");
    }
}

//switch case day example
function withSwitchCase(){
    debugger;
    let dayno = 5;
    switch (dayno) {
        case 1:
            console.log("Monday");
            break;
        case 2:
            console.log("Tuesday");
            break;
        case 3:
            console.log("Wednesday");
            break;
        case 4:
            console.log("Thursday");
            break;
        case 5:
            console.log("Friday");
            break;
        case 6:
            console.log("Saturday");
            break;
        case 7:
            console.log("Sunday");
            break;
        default:
            console.log("Invalid day");
    }
    withSwitchCase();

}


//ternary operator example
num = 5;
console.log((num % 2 == 0) ? "even number" : "odd number");

//take 3 variable and find out smallest of 3
a = 10;
b = 20;
c = 5;
smallest = (a < b) ? ((a < c) ? a : c) : ((b < c) ? b : c);
console.log("smallest is " + smallest);

//other way to find smallest of 3
if (a < b && a < c) {
    console.log("smallest is " + a);
} else if (b < a && b < c) {
    console.log("smallest is " + b);
} else {
    console.log("smallest is " + c);
}

