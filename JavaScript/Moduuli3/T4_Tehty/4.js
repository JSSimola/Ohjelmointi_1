'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const list = document.querySelector('#target');


for (let i of students) {
  let new_element = document.createElement('option');
  new_element.setAttributeNode(document.createAttribute('value'));
  new_element.setAttribute('value', i.id);
  new_element.appendChild(document.createTextNode(i.name));
  list.appendChild(new_element);
}
