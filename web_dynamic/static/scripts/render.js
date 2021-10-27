// import { createElement, Render, appendRender } from '../scripts/libreria.js';

const url = 'http://localhost:5001/api/v1/surveys/1/sections/1/questions/1';

// console.log(url);
const questions_url = 'http://localhost:5001/api/v1/questions';
// console.log("API QUESTIONS");
// console.log(questions_url);

const answers = [];
let questions = [];
let currentIndex = 0;
let count = 0;

function render_question (res) {
  const nameQuestion = res.name_question;
  const options = res.answer_options;
  $('#p_question').text(nameQuestion);
  $('#text-buttons').html('');
  options.forEach((el) => {
    const id = el.id;
    $('#text-buttons').append(`<button id='${id}' type="button" class="botones btn-light">${el.name_option}</button>`);
    // console.log(id);
    document.getElementById(`${id}`).addEventListener("click", function(event) {
      // console.log(event.detail);
      // console.log(id);
      let question = {...questions[currentIndex++]};
      // let val = el.value;
      // let count = valArr[val.length];
      question.answer = {...options.find(op => op.id == id)};
      delete question.answer_options;
      answers.push(question);
      count = count + question.answer.value;
      console.log(question.answer.value);
      console.log(`Resultado: ${count}`);
      render_question(questions[currentIndex]);
    }, false);
  });
}

setTimeout(
  function () {
    $.get(questions_url, function (res) {
      // console.log(res[0]);
      questions = res;
      render_question(res[currentIndex]);
    });
  }, 0);
