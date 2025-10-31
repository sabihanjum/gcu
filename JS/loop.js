//print 9 6 3 0 -3 -5 -9 -12 -15 using for loop

for(let i=9; i>=-15; i-=3){
    console.log(i);
}


//using loop print all the number between 1 and 50 that is multiple of 3 or 5
for(let i=1; i<=50; i++){
    if(i%3==0 || i%5==0){
        console.log(i);
    }
}


//print 1 3 5 7 9 using while loop
let i=1;
while(i<=9){
    console.log(i);
    i+=2;
}

//print 1 3 5 7 9 using  do while loop
let j=1;
do{
    console.log(j);
    j+=2;
}while(j<=9);

