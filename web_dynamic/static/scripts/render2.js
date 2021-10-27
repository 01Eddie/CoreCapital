// import { createElement, Render, appendRender } from '../scripts/libreria.js';

const url = 'http://localhost:5001/api/v1/surveys/1/sections/1/questions/1';

/* console.log(url); */
const questions_url = 'http://localhost:5001/api/v1/questions';
// console.log("API QUESTIONS");
// console.log(questions_url);

const answers = [];
let questions = [];
let currentIndex = 0;

function render_question (res) {
  const name_section = res.section_name;
  const nameQuestion = res.name_question;
  const options = res.answer_options;
  $('#title').text(name_section);
  $('#p_question').text(nameQuestion);
  $('#text-buttons').html('');
  options.forEach((el) => {
    const id = el.id;
    $('#text-buttons')
      .append(
    `<button
      id='${id}'
      type="button"
      class="botones btn-light">
      ${el.name_option}
    </button>`);
  });
  $('#text-buttons button').click(function (arg) {
    if (currentIndex == questions.length - 1) {
      console.log('final');
      return;
    }
    currentIndex++;

    render_question(questions[currentIndex]);
  });
}

setTimeout(
  function () {
    $.get(questions_url, function (res) {
      console.log(res[currentIndex]);
      questions = res;
      render_question(res[currentIndex]);
    });
  }, 0);
