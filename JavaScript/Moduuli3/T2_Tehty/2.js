'use strict';

const list = document.getElementById('target');
const li1 = document.createElement('li');
const li2 = document.createElement('li');
const li3 = document.createElement('li');

li1.appendChild(document.createTextNode('First item'));
li2.appendChild(document.createTextNode('Second item'));
li3.appendChild(document.createTextNode('Third item'));

li2.setAttribute('class', 'my-item')

list.appendChild(li1)
list.appendChild(li2)
list.appendChild(li3)


