'use strict';
const int1 = parseInt(prompt('Type an integer'));
const int2 = parseInt(prompt('Type a second integer'));
const int3 = parseInt(prompt('Type a 3rd integer'));

const sum = int1 + int2 + int3;
const product = int1 * int2 * int3;
const average = (int1 + int2 + int3)/3;

document.querySelector('#sum')
    .innerHTML = 'Sum of integers: ' + sum;
document.querySelector('#product')
    .innerHTML = 'Product of integers: ' + product;
document.querySelector('#average')
    .innerHTML = 'Average of integers: ' + average;
