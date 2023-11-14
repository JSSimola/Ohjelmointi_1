'use strict';

const numbers = [];

let num = 1;

while (num !== 0) {
  num = parseInt(prompt('Anna luku: '));
  numbers.push(num);
}

numbers.pop();
numbers.sort((a, b)=>a - b);
numbers.reverse();


for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
