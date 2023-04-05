// Team Peanut Butter :: Prattay Dey, Brian Yang
// SoftDev pd07
// K27 -- Basic functions in JavaScript
// 2023-04-03t


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

function fact(n){
    if (n < 2){
        return 1;
    }
    else { 
        return n * fact(n-1); 
    }
}

console.log(fact(5)); // should be 120

function fib(n){
    if (n < 2){
        return n;
    }
    else {
        return fib(n-2) + fib(n-1);
    }
}

console.log(fib(5));  // should be 5