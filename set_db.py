#!/usr/bin/python3
from models import session
from models.survey import Survey
from models.question import Question
from models.survey_section import Survey_Section
from models.question_option import Question_Option

survey=Survey(
    name_survey='Encuesta Perfil de Riesgo',
    description='Cuestionario Integrado Perfil de riesgo y Evaluacion de Producto',
    nro_questions=39
    )
session.add(survey)
# VALUES (1,'Encuesta Perfil de Riesgo','Cuestionario Integrado Perfil de riesgo y Evaluacion de Producto',39,1,'2021-10-18 02:17:07',1);


surv_sec = Survey_Section(
    id_survey=survey.id,
    name_section='Perfil de Riesgo',
    description=''
)
session.add(surv_sec)

surv_sec_2 = Survey_Section(
    id_survey=survey.id,
    name_section='Evaluación de Producto',
    description='Imagina que tu asesor financiero te ofrezca una oportunidad de invertir en Bonos de Financiamiento de Terrenos.<BR />Se trata de un bono a tasa fija que invierte en la compra de terrenos donde se desarrollarán proyectos inmobiliarios de empresas de prestigio.<BR />Estos bonos están respaldados con la garantía hipotecaria del terreno, la cual equivale entre el 100% y 125% de la inversión y se haría efectiva en caso de impago.<BR />El bono tiene un plazo promedio de 15 meses y el monto mínimo de inversión es de US$ 100,000.<BR />Se paga intereses trimestralmente calculados a una tasa anual de 6.5% en dólares para una inversión inferior a US$ 200,000 y de 7.5% para una inversión igual o superior a ese monto.'
)
# Survey_Section(
#     id_survey=survey.id,
#     name_section='Preferencias',
#     description=''
# )
# Survey_Section(
#     id_survey=survey.id,
#     name_section='Datos Demográficos',
#     description=''
# )
# INSERT INTO `Survey_Sections` (`id_survey`,`id`,`name_section`,`description`,`active`)
# VALUES (1,1,'Inicio','',1),(1,2,'Perfil de Riesgo','',1),(1,3,'Evaluación de Producto','Imagina que tu asesor financiero te ofrezca una oportunidad de invertir en Bonos de Financiamiento de Terrenos.<BR />Se trata de un bono a tasa fija que invierte en la compra de terrenos donde se desarrollarán proyectos inmobiliarios de empresas de prestigio.<BR />Estos bonos están respaldados con la garantía hipotecaria del terreno, la cual equivale entre el 100% y 125% de la inversión y se haría efectiva en caso de impago.<BR />El bono tiene un plazo promedio de 15 meses y el monto mínimo de inversión es de US$ 100,000.<BR />Se paga intereses trimestralmente calculados a una tasa anual de 6.5% en dólares para una inversión inferior a US$ 200,000 y de 7.5% para una inversión igual o superior a ese monto.',1),(1,4,'Preferencias','',1),(1,5,'Datos Demográficos','',1);

q1 = Question(
    id_survey_section=surv_sec.id,
    id_survey=survey.id,
    name_question='Question 1',
    description='Description for question 1',
    answer_required=1,
    calculated=12,
    order=1
)
Question_Option(
    id_question=q1.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='Respuesta 1',
    value=2,
    order=1
)
Question_Option(
    id_question=q1.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='Respuesta 2',
    value=2,
    order=2
)
Question_Option(
    id_question=q1.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='Respuesta 3',
    value=2,
    order=3
)
# INSERT INTO `Question_Options` (`id_question_option`,`id_question`,`id_survey`,`id_survey_section`,`name_option`,`value`,`active`,`order`)
# VALUES (1,1,1,1,'1. Masculino',1,1,1),(2,1,1,1,'2. Femenino',2,1,2),
# (3,2,1,1,'1. Sí.',3,1,3),(4,2,1,1,'2. No.',4,1,4),
# (5,3,1,1,'1. Sí.',5,1,5),(6,3,1,1,'2. No.',6,1,6),
# (7,4,1,2,'1. Extremadamente bajo.',1,1,1),(8,4,1,2,'2. Muy bajo.',2,1,2),(9,4,1,2,'3. Bajo.',3,1,3),(10,4,1,2,'4. Promedio.',4,1,4),(11,4,1,2,'5. Alto.',5,1,5),(12,4,1,2,'6. Muy alto.',6,1,6),(13,4,1,2,'7. Extremadamente alto.',7,1,7)
# ;

q2 = Question(
    id_survey_section=surv_sec.id,
    id_survey=survey.id,
    name_question='Question 2',
    description='Description for question 2',
    answer_required=1,
    calculated=4,
    order=2
)
Question_Option(
    id_question=q2.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='Respuesta 1',
    value=2,
    order=1
)
Question_Option(
    id_question=q2.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='Respuesta 2',
    value=2,
    order=2
)
Question_Option(
    id_question=q2.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='Respuesta 3',
    value=2,
    order=3
)

q3 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='Question 1',
    description='Description for question 1',
    answer_required=0,
    calculated=6,
    order=1
)
Question_Option(
    id_question=q3.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='Respuesta 1',
    value=2,
    order=1
)
Question_Option(
    id_question=q3.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='Respuesta 2',
    value=2,
    order=2
)
Question_Option(
    id_question=q3.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='Respuesta 3',
    value=2,
    order=3
)

q4 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='Question 2',
    description='Description for question 2',
    answer_required=1,
    calculated=8,
    order=2
)
Question_Option(
    id_question=q4.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='Respuesta 1',
    value=2,
    order=1
)
Question_Option(
    id_question=q4.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='Respuesta 2',
    value=2,
    order=2
)
Question_Option(
    id_question=q4.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='Respuesta 3',
    value=2,
    order=3
)

q5 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='Question 3',
    description='Description for question 3',
    answer_required=1,
    calculated=23,
    order=3
)
Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='Respuesta 1',
    value=2,
    order=1
)
Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='Respuesta 2',
    value=2,
    order=2
)

session.commit()

##############################################
# (1,1,1,'D1. Por favor indica tu género',1,1,0,1),(2,1,1,'D2. Por favor indica tu edad en años cumplidos',1,1,0,2),(3,1,1,'F1. ¿Alguna vez has invertido en productos financieros?',1,1,0,3),(4,1,1,'F2. ¿Tienes recursos invertidos(7,2,1,'P3. ¿Alguna vez has invertido una gran suma en una inversión arriesgada principalmente por la adrenalina de ver si su valor subía
########################################################################
# import xlrd

# wb=xlrd.open_workbook('work_questions-v2.xls')

# sheet=wb.sheet_by_index(0)
# for row in range(sheet.nrows):
#     row_txt=sheet.cell_value(row, 0)
#     cells=list(row_txt.split(','))
#     qname=''.join(cells[3:-5])
#     qname=qname[1:]
#     qname=qname[:-1]
#     # print(qname)
#     print(len(cells), end=', ')
#     # Question(
#     #     id_survey_section=,
#     #     id_survey=survey.id,
#     #     name_question=qname,
#     #     description=,
#     #     answer_required=,
#     #     calculated=,
#     #     order=
#     # )
#     # print(sheet.cell_value(row, 0))
#     # print()
#     # print(qname)
