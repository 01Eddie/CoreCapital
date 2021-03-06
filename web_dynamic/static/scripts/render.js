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
const id_risk_profile = 0;
const user_id = $('#user_id').val();
let user_age = null;

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

function sendAnswers (answers, msg = 'Gracias por completar la encuesta.') {
  $.ajax({
    type: 'POST',
    data: JSON.stringify(answers),
    url: answer_url,
    contentType: 'application/json; charset=utf-8',
    success: function (json) {
      window.location = '/final?msg=' + json.msg;
    },
    error: function (xhr, status) {
      alert('Disculpe, existió un problema');
    },
    complete: function (xhr, status) {
      // alert('Petición realizada');
    }
  });
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
      answers.push(answer);

      if (question.measure) {
        const measureOp = ((question.answer.value - question.measure.media) / question.measure.desv_std) * question.measure.score;
        measureSum = measureSum + measureOp;
      }
      count = count + question.answer.value;

      // Verifica que la encuesta ha finalizado
      if (question.answer.survey_is_over == 1) {
        progress(1, 1);
        console.log('pop_up');
        if (question.id == 3 || question.id == 4) {
          measureSum = null;
        }
        const data = { res: measureSum, answers: answers, id_survey: question.id_survey, id_user: user_id, id_risk_profile: id_risk_profile, user_age };
        sendAnswers(data);
        console.log(user_age);
        if (questions[currentIndex] === undefined) {
          // Ruta para enviar el msj
          $.ajax({
            type: 'POST',
            data: JSON.stringify({ user_id: user_id }),
            url: '/final',
            contentType: 'application/json; charset=utf-8',
            error: function (xhr, status) {
              alert('Disculpe, existió un problema');
            }
          });
        }
        return;
      }

      my_table = `
          <table border="1" align="center"></i>
            <tr>
              <th scope="col"><strong>Cartera</th>
              <th cope="col"><strong>Alto Riesgo &<br> Alto Retorno</th>
              <th cope="col"><strong>Medio Riesgo &<br> Medio Retorno</th>
              <th cope="col"><strong>Bajo Riesgo &<br> Bajo Retorno</th>
            </tr>

            <tr>
              <td>1</td>
              <td>0%</td>
              <td>0%</td>
              <td>100%</td>
            </tr>
            
            <tr>
              <td>2</td>
              <td>0%</td>
              <td>30%</td>
              <td>70%</td>
            </tr>
            
            <tr>
              <td>3</td>
              <td>10%</td>
              <td>40%</td>
              <td>50%</td>
            </tr>

            <tr>
              <td>4</td>
              <td>30%</td>
              <td>40%</td>
              <td>30%</td>
            </tr>

            <tr>
              <td>5</td>
              <td>50%</td>
              <td>40%</td>
              <td>10%</td>
            </tr>

            <tr>
              <td>6</td>
              <td>70%</td>
              <td>30%</td>
              <td>0%</td>
            </tr>

            <tr>
              <td>7</td>
              <td>100%</td>
              <td>0%</td>
              <td>0%</td>
            </tr>

          </table>
      `;

      my_list = `
        <label for="quantity"></label>
        <input class="input_age" type="number" id="quantity" name="quantity" min="18" max="100" placeholder="18" value="18">
      `;

      if (question.order == 2 && question.id_survey_section == 1) {
        const container = document.getElementById('p_question');
        user_age = $('#quantity').val();
      }

      render_question(questions[currentIndex]);

      if (question.order == 1 && question.id_survey_section == 1) {
        const container = document.getElementById('p_question');
        const list = createElement('div', { class: 'input_age_container' }, children = [], content = my_list);
        container.appendChild(list);
      }

      if (question.order == 8) {
        const container = document.getElementById('p_question');
        const table = createElement('div', { class: 'my_table' }, children = [], content = my_table);
        container.appendChild(table);
      }

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
