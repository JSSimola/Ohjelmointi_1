'use strict';

const theForm = document.querySelector('#tv-form');
const search = document.querySelector('#query');
const results_div = document.querySelector('#results');

async function getInfo(query) {
  const url = `https://api.tvmaze.com/search/shows?q=${query}`;
  const response = await fetch(url);
  return response.json();
}

function printer(info) {
  for (let item of info) {
    //creating the elements for the article
    const article = document.createElement('article');
    const image = document.createElement('img');
    const header = document.createElement('h2');
    const link = document.createElement('a');
    const summary = document.createElement('div');
    //adding the header
    header.append(document.createTextNode(item.show.name));
    //adding the image
    image.src = 'https://via.placeholder.com/210x295?text=Not%20Found';
    image.src = item.show.image ? item.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
    image.alt = item.show.name;
    //adding the link
    link.href = item.show.url;
    link.textContent = item.show.name;
    link.target = `_blank`;
    //adding the summary
    summary.innerHTML = item.show.summary;
    //all the appends
    article.append(header, link, image, summary);
    results_div.append(article);
  }
}

theForm.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const query = search.value;
  const info = await getInfo(query);
  //nollaa artikkelit
  results_div.innerHTML = '';
  printer(info);
});
