'use strict';

const a = document.getElementById('target');
const txt =
    '<li>First item</li>\n<li>Second item</li>\n<li>Third item</li>';

a.innerHTML = txt;
a.setAttribute('class', 'my-list')
