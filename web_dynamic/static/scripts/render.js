// import { createElement, Render, appendRender } from '../scripts/libreria.js';

const url = 'http://localhost:5001/api/v1/surveys/1/sections/1/questions/2';

$.get(url, function (res) {
  const nameQuestion = res.name_question;
  $('#p_question').text(nameQuestion);
});
