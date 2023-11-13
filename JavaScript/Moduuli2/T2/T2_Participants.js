'use strict';

const num_ppl = parseInt(prompt('Anna osallistujien määrä: '));

const ppl = [];

for (let i = 0; i < num_ppl; i++) {
  ppl[i] = prompt('Anna osallistujan nimi: ');
}

for (let i = 0; i < ppl.length; i++) {
  let list_item = document.createElement('li');
  list_item.innerHTML = ppl[i];
  document.getElementById('lista').appendChild(list_item);
}
