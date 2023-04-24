// Team Turing Testers :: Ayman Habib, Ryan Lau
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17
// --------------------------------------------------


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


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red'); // what is a classList??
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
function fact (n) {
    if (n < 2) {
        return 1
    }
    return n * fact(n - 1)
}

function fib (n) {
    if (n == 0) {
        return 0
    }
    if (n == 1) {
        return 1
    }
    return fib(n - 1) + fib(n - 2)
}

function gcd (a, b) {
    if (a % b === 0){
        return b;
      }
    return gcd(b, a%b);
}

var fib15 = function() {
  console.log(fib(15));
  var fibresult = document.getElementById("fib-result");
  fibresult.innerHTML = "the result of fib(15) is " + fib(15);
}

var fibbut = document.getElementById("fib-button");
fibbut.addEventListener('click', fib);

var fact15 = function() {
  console.log(fact(15));

  var factresult = document.getElementById("fact-result");
  factresult.innerHTML = "the result of fact(15) is " + fact(15);
}

var factbut = document.getElementById("fact-button");
factbut.addEventListener('click', fact15);


var gcd15and20 = function() {
  console.log(15, 20);

  var gcdresult = document.getElementById("gcd-result");
  gcdresult.innerHTML = "the result of gcd(15, 20) is " + gcd(15, 20);
}

var gcdbut = document.getElementById("gcd-button");
gcdbut.addEventListener('click', gcd15and20);



// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

