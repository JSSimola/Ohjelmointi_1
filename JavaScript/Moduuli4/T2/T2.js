'use strict';

const theForm = document.querySelector('#tv-form');

theForm.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const tv_show = document.querySelector('input[id=query]').value;
  try {
    const response = await fetch(
        `https://api.tvmaze.com/search/shows?q=${tv_show}`);
    const jsonData = await response.json();
    console.log(jsonData)
    return jsonData;
  } catch (error) {
    console.log(error.message);
  }
});


