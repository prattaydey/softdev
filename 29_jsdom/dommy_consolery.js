//Team Peanut Butter :: Prattay Dey, Brian Yang
//SoftDev pd07
//K29 -- DOMfoolery++
//2023-04-20


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};
//To call this in the console log use f(_)

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };
//Creates an object in the console log.
//What would this be used for?


var addItem = function(text) {
  var list = document.getElementById("thelist"); //Fetches the element with the id "thelist"
  var newitem = document.createElement("li"); //Adds a row to the list
  newitem.innerHTML = text; //innerHTML specifies whatever is enclosed in li
  list.appendChild(newitem); // Adds newitem to the list
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li'); //listitems is a list all all elements with a tag 'li'
  listitems[n].remove(); //removes the nth item on the list
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red'); //only addes red to the class if there isnt red in the class already
  }
};
//why do some not change even though the last class element is red? Does it have something to do with the order the colors were declared in <style>

var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red'); //if even add red to class name
    } else {
      items[i].classList.add('blue'); //if not even add blue to the class name
    }
  }
};

//How are these any different from just having a function(name?)

//insert your implementations here for...

var fib = function(n){
    if (n < 2){
        return n;
    }
    else {
        return fib(n-2) + fib(n-1);
    }
}

var fact = function(n){
    if (n < 2){
        return 1;
    }
    else {
        return n * fact(n-1);
    }
}

var gcd = function(a,b){
  if (a % b === 0){
     return b;
   }
   return gcd(b, a%b);
}

var addFib = function(number){
  addItem(fib(number))
}

var addFact = function(number){
  addItem(fact(number))
}

var addGcd = function(num1, num2){
  var ans = gcd(num1, num2)
  addItem(ans)
}

console.log(fib(5));
console.log(fact(5));
console.log(gcd(20, 5));

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return param1;
};
//function is called is myFxn
 //param1 and param2 are the params and the arrow points to the function
