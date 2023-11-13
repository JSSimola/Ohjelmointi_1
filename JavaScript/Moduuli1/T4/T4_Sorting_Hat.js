'use strict';

const name = prompt('Give you name: ');

let room = Math.floor(Math.random() * 4) + 1;
let room_str = room.toString()

switch (room_str) {
  case '1':
    document.querySelector('#result').innerHTML = name + ' you are Gryffindor.';
    break;
  case '2':
    document.querySelector('#result').innerHTML = name + ' you are Slytherin.';
    break;
  case '3':
    document.querySelector('#result').innerHTML = name + ' you are Hufflepuff.';
    break;
  case '4':
    document.querySelector('#result').innerHTML = name + ' you are Ravenclaw.';
    break;
}

