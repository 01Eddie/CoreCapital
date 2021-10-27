// import { createElement, Render, appendRender } from '../scripts/libreria.js';

const url = 'http://localhost:5001/api/v1/surveys/1/sections/1/questions/1';
const questions_url = 'http://localhost:5001/api/v1/questions';
const answer_url = 'http://localhost:5001/api/v1/answers';

const answers = [];
let questions = [];
let currentIndex = 0;
let count = 0;

function sendAnswer () {
  console.log('enviado');
  console.log(answers);
  $.ajax({
    type: 'POST',
    data: JSON.stringify(answers),
    url: answer_url,
    contentType: 'application/json; charset=utf-8',
    success: function (json) {
      console.log('enviado desde render');
      console.log(json);
    },
    error: function (xhr, status) {
      alert('Disculpe, existió un problema');
    },
    complete: function (xhr, status) {
      alert('Petición realizada');
    }
  });
}

function render_question (res) {
  const name_section = res.section_name;
  console.log(res);
  const nameQuestion = res.name_question;
  const options = res.answer_options;
  $('#title').text(name_section);
  $('#p_question').text(nameQuestion);
  $('#text-buttons').html('');
  options.forEach((el) => {
    const id = el.id;
    $('#text-buttons').append(`<button id='${id}' type="button" class="botones btn-light">${el.name_option}</button>`);
    // console.log(id);
    document.getElementById(`${id}`).addEventListener('click', function (event) {
      // console.log(event.detail);
      // console.log(id);
      const question = { ...questions[currentIndex++] };
      // let val = el.value;
      // let count = valArr[val.length];
      question.answer = { ...options.find(op => op.id == id) };
      delete question.answer_options;
      answers.push(question);
      count = count + question.answer.value;
      console.log(question.answer.value);
      console.log(`Resultado: ${count}`);
      if (question.answer.survey_is_over == 1) {
        console.log('pop_up');
        // if (question.id == 11){
        // console.log('pop_up_final')
        // } else {
        // console.log('pop_up')
        // }
        sendAnswer();
        return;
      }
      render_question(questions[currentIndex]);
    }, false);
  });
}

console.log('resultados');

setTimeout(
  function () {
    $.get(questions_url, function (res) {
      // console.log(res[0]);
      questions = res;
      render_question(res[currentIndex]);
    });
  }, 0);
