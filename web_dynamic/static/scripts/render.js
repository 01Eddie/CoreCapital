import { createElement, Render, appendRender } from '../scripts/libreria.js';

// imgSrc="{{url_for('static', filename='scripts/render.js')}}"

const url = 'http://localhost:5001/api/v1/surveys/1/sections/1/questions/1';

$.get(url, function (res) {
  const nameQuestion = res.name_question;
  console.log(nameQuestion);
});

const question = createElement('p', {
  class: 'question'
  // alt: 'Logo',
  // src: '../images/CorePartners_LogoRGB_positivo.png'
});

// const Nav = createElement('nav', { class: 'main-nav' });

// const Header = createElement('header', { class: 'main-header' }, [Logo, Nav]);

Render(question, document.getElementById('question'));
