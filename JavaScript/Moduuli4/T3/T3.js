'use strict';

const theForm = document.querySelector('#tv-form');
const search = document.querySelector('#query');
const results_article = document.querySelector('#results');

async function getInfo(query) {
  const url = `https://api.tvmaze.com/search/shows?q=${query}`;
  const response = await fetch(url);
  return response.json();
}

function printer(info) {
  for (let item of info) {
    console.log(item);
    //creating the elements for the article
    const image = document.createElement('img');
    const header = document.createElement('h2');
    const link = document.createElement('a');
    const summary = document.createElement('div');
    //adding the header
    header.append(document.createTextNode(item.show.name));
    //adding the image
    image.src = item.show.image?.medium;
    image.alt = item.show.name;
    //adding the link
    link.href = item.show.url;
    link.textContent = item.show.name;
    link.target = `_blank`;
    //all the appends
    results_article.append(header, image, link, summary);
  }
}

theForm.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const query = search.value;
  const info = await getInfo(query);
  //nollaa artikkelin
  results_article.innerHTML = '';
  printer(info);
});
