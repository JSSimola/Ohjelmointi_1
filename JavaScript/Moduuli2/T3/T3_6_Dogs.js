'use strict';

const dogs = [];

for (let i = 0; i < 6; i++) {
  dogs[i] = prompt('Anna koiran nimi: ');
}

dogs.sort();
dogs.reverse();

for (let i = 0; i < dogs.length; i++) {
  let list_item = document.createElement('li');
  list_item.innerHTML = dogs[i];
  document.getElementById('lista').appendChild(list_item);
}
