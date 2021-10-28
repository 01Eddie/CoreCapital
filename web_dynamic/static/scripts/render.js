// import { createElement, Render, appendRender } from '../scripts/libreria.js';

// const url = 'http://localhost:5001/api/v1/surveys/1/sections/1/questions/1';
const questions_url = 'http://localhost:5001/api/v1/questions';
const answer_url = 'http://localhost:5001/api/v1/answers';

const answers = [];
let questions = [];
let currentIndex = 0;
let count = 0;
const user_id = $('#user_id').val();

// let progress_index = (currentIndex + 1) / answers.length;
function progress (parcial, total) {
  const progress_index = parseInt((parcial / total) * 100);
  $('.circle .percent svg circle:nth-child(2)').css({
    'stroke-dashoffset': `calc(440 - (320 * ${progress_index}) / 100)`
  });
  $('#number').text(`${progress_index}%`);
}

function filterAnswer (question) {
  const data = {};
  const answer = question.answer;
  data.user_id = user_id;
  data.id_question_option = answer.id_question;
  data.answer_value = answer.value;
  data.active = 1;
  data.id_question = question.id;
  data.id_survey = question.id_survey;
  data.id_survey_section = question.id_survey_section;
  return data;
}

function sendAnswers (answers) {
  $.ajax({
    type: 'POST',
    data: JSON.stringify(answers),
    url: answer_url,
    contentType: 'application/json; charset=utf-8',
    success: function (json) {
      alert('Gracias por completar la encuesta, muy pronto un asesor se comunicará con usted.');
    },
    error: function (xhr, status) {
      alert('Disculpe, existió un problema');
    },
    complete: function (xhr, status) {
      // alert('Petición realizada');
    }
  });
  console.log(answers);
}

function render_question (res) {
  const name_section = res.section_name;
  const nameQuestion = res.name_question;
  const options = res.answer_options;

  $('#title').text(name_section);
  $('#p_question').text(nameQuestion);
  $('#text-buttons').html('');

  options.forEach((el) => {
    const id = el.id;
    $('#text-buttons').append(`<button id='${id}' type="button" class="botones">${el.name_option}</button>`);
    document.getElementById(`${id}`).addEventListener('click', function (event) {
      const question = { ...questions[currentIndex++] };

      question.answer = { ...options.find(op => op.id == id) };
      const answer = filterAnswer(question);
      answers.push(answer);
      count = count + question.answer.value;
      // console.log(`Resultado: ${count}`);

      // Verifica que la encuesta ha finalizado
      if (question.answer.survey_is_over == 1) {
        progress(1, 1);
        console.log('pop_up');
        // if (question.id == 11){
        // console.log('pop_up_final')
        // } else {
        // console.log('pop_up')
        // }
        sendAnswers(answers);
        return;
      }

      render_question(questions[currentIndex]);
      progress(currentIndex, questions.length);
    }, false);
  });
}

setTimeout(
  function () {
    $.get(questions_url, function (res) {
      console.log(res);
      questions = res;
      progress(0, questions.length);
      render_question(res[currentIndex]);
    });
  }, 0);
