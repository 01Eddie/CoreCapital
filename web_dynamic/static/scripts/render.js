import { createElement, Render, appendRender } from '../scripts/libreria.js';

const url = 'http://localhost:5001/api/v1/surveys/1/sections/1/questions/1';

$.get(url, function (res) {
  const nameQuestion = res.name_question;
  // const update = $('DIV#p_question');
  // const question = $('p_question');
  // $(update).click(function () {
  // header.text('New Header!!!');
  // $(nameQuestion).appendTo('#p_question');
  $('text_placeholder').appendTo('#p_question');
});

// console.log(nameQuestion);
// });

// const question = createElement('p', {
//   class: 'question'
// alt: 'Logo',
// src: '../images/CorePartners_LogoRGB_positivo.png'
// });

// const Nav = createElement('nav', { class: 'main-nav' });

// const Header = createElement('header', { class: 'main-header' }, [Logo, Nav]);

// Render(question, document.getElementById('question'));
