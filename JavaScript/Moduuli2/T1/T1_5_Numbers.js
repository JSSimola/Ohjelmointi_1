'use strict';

const num1 = prompt('Give number 1: ');
const num2 = prompt('Give number 2: ');
const num3 = prompt('Give number 3: ');
const num4 = prompt('Give number 4: ');
const num5 = prompt('Give number 5: ');

const arr = [num1, num2, num3, num4, num5];

for (let i = arr.length - 1; i >= 0; i--) {
        console.log(arr[i]);
  }
