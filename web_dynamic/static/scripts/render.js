// import { createElement, Render, appendRender } from '../scripts/libreria.js';

// const url = 'http://localhost:5001/api/v1/surveys/1/sections/1/questions/1';
const questions_url = 'http://localhost:5001/api/v1/questions';
const answer_url = 'http://localhost:5001/api/v1/answers';
const profile_url = 'http://localhost:5001/api/v1/risk_profile';

const answers = [];
let questions = [];
let currentIndex = 0;
let count = 0;
let measureSum = 0;
let id_risk_profile = 0;
// let risk_profile = ''
let msg = '';
const user_id = $('#user_id').val();

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
  data.id_question_option = answer.id;
  data.answer_value = answer.value;
  data.active = 1;
  data.id_question = question.id;
  data.id_survey = question.id_survey;
  data.id_survey_section = question.id_survey_section;
  return data;
}

function sendAnswers (answers, msg = 'Gracia por completar la ecuesta.') {
  $.ajax({
    type: 'POST',
    data: JSON.stringify(answers),
    url: answer_url,
    contentType: 'application/json; charset=utf-8',
    success: function (json) {
      // alert('Gracias por completar la encuesta, muy pronto un asesor se comunicará con usted.');
      window.location = '/final?msg=' + msg;
      console.log('pop_up');
    },
    error: function (xhr, status) {
      alert('Disculpe, existió un problema');
    },
    complete: function (xhr, status) {
      // alert('Petición realizada');
    }
  });
  // console.log(answers);
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
    $('#text-buttons').append(`<button id="${id}" type="button" class="botones">${el.name_option}</button>`);
    document.getElementById(`${id}`).addEventListener('click', function (event) {
      const question = { ...questions[currentIndex++] };

      question.answer = { ...options.find(op => op.id == id) };
      const answer = filterAnswer(question);
      console.log(answer);
      answers.push(answer);
      console.log(question.answer.value);
      console.log(question.answer.media);
      console.log(question.answer.desv_std);
      console.log(question.answer.score);

      if (question.measure) {
        const measureOp = ((question.answer.value - question.measure.media) / question.measure.desv_std) * question.measure.score;
        measureSum = measureSum + measureOp;
      }
      count = count + question.answer.value;
      // console.log(measureSum);
      // console.log(`Resultado: ${count}`);

      // Verifica que la encuesta ha finalizado
      if (question.answer.survey_is_over == 1) {
        progress(1, 1);
        console.log('pop_up');
        if (question.id == 3 || question.id == 4) {
          id_risk_profile = null;
          msg = 'Usted por el momento no puede acceder a nuestros productos.';
        } else {
          if (measureSum < -1) {
            id_risk_profile = 1;
            msg = 'Usted tiene un perfil tipo: Adverso, un asesor se comunicará con usted próximamente.';
          } else if (measureSum <= 0) {
            id_risk_profile = 2;
            msg = 'Usted tiene un perfil tipo: Moderado Adverso, un asesor se comunicará con usted próximamente.';
          } else if (measureSum > 0.75) {
            id_risk_profile = 4;
            msg = 'Usted tiene un perfil tipo: Agresivo, un asesor se comunicará con usted próximamente.';
          } else {
            id_risk_profile = 3;
            msg = 'Usted tiene un perfil tipo: Moderado Agresivo, un asesor se comunicará con usted próximamente.';
          }
        }

        const data = { res: measureSum, answers: answers, id_survey: question.id_survey, id_user: user_id, id_risk_profile: id_risk_profile };
        sendAnswers(data, msg);
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
      questions = res;
      progress(0, questions.length);
      render_question(res[currentIndex]);
    });
  }, 0);
