// import { createElement, Render, appendRender } from '../scripts/libreria.js';

const url = 'http://localhost:5001/api/v1/surveys/1/sections/2/questions/4';
const questions_url = 'http://localhost:5001/api/v1/questions';

$.get(url, function (res) {
  const nameQuestion = res.name_question;
  const options = res.answer_options;
  $('#p_question').text(nameQuestion);
  $('#text-buttons').html('');
  options.forEach((el) => {
    $('#text-buttons').append(`<button type="button" class="botones btn-light">${el.name_option}</button>`);
  });
});

$.get(questions_url, function (res) {
  console.log(res.name_option);
});
