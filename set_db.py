#!/usr/bin/python3
from models import session
from models import Base, engine
from models.survey import Survey
from models.question import Question
from models.survey_section import Survey_Section
from models.question_option import Question_Option
from models.type_document import Type_Document
from models.measure import Measure
from models.risk_profile import Risk_Profile

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

typeDNI = Type_Document(
    name = 'DNI'
)
session.add(typeDNI)
session.commit()

typePass = Type_Document(
    name = 'Pasaporte'
)
session.add(typePass)
session.commit()

typeCarnet = Type_Document(
    name = 'Carnet de Extranjería'
)
session.add(typeCarnet)
session.commit()


survey=Survey(
    name_survey='Encuesta Perfil de Riesgo',
    description='Cuestionario Integrado Perfil de riesgo y Evaluacion de Producto',
    nro_questions=15
#   nro_questions=39
    )
session.add(survey)
session.commit()
# VALUES (1,'Encuesta Perfil de Riesgo','Cuestionario Integrado Perfil de riesgo y Evaluacion de Producto',39,1,'2021-10-18 02:17:07',1);


surv_sec = Survey_Section(
    id_survey=survey.id,
    name_section='Cuestionario',
    description=''
)
session.add(surv_sec)
session.commit()

surv_sec_2 = Survey_Section(
    id_survey=survey.id,
    name_section='Perfil de Riesgo',
    description=''
)
session.add(surv_sec_2)
session.commit()
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


# INSERT INTO `Questions` (`id`,`id_survey_section`,`id_survey`,`name_question`,`answer_required`,`active`,`calculated`,`order`)
# VALUES ,,(4,1,1,'F2. ¿Tienes recursos invertidos en algún tipo de producto financiero actualmente (por ejemplo: inmuebles, fondos de inversión, acciones en la bolsa, bonos)?',1,1,0,4),(5,2,1,'P1. En comparación con otras personas, ¿Cómo calificas tu disposición a asumir riesgos financieros?',1,1,1,1),(6,2,1,'P2. Cuando piensas en la palabra \'riesgo\' en un contexto financiero, ¿Cuál de las siguientes palabras viene a tu mente primero?',1,1,1,2),
# (7,2,1,'P3. ¿Alguna vez has invertido una gran suma en una inversión arriesgada principalmente por la adrenalina de ver si su valor subía o bajaba?',1,1,1,3),(8,2,1,'P4. Si tuvieras que elegir entre más seguridad laboral con un pequeño aumento salarial y menos seguridad laboral con un gran aumento salarial, ¿Cuál elegirías?',1,1,1,4),(9,2,1,'P5. Imagina que tienes un trabajo en el que puedes elegir que te paguen un salario, una comisión o una combinación de ambos. ¿Cuál elegirías?',1,1,1,5),(10,2,1,'P6. ¿Qué grado de riesgo has asumido con tus decisiones financieras en el pasado?',1,1,1,6),(11,2,1,'P7. ¿Qué grado de riesgo estás actualmente dispuesto(a) a asumir con tus decisiones financieras?',1,1,1,7),(12,2,1,'P8. Las inversiones pueden subir y bajar de valor y los expertos a menudo dicen que debes estar preparado para sobrellevar una recesión. ¿Cuánto podría bajar el valor total de todas tus inversiones antes de que comiences a sentirte incómodo(a)?',1,1,1,8),(13,2,1,'P9. La mayoría de las carteras de inversión presenta una variedad de productos en cuanto al riesgo y al rendimiento. Por favor, indique cuál de las siguientes opciones de cartera representa mejor la combinación de inversiones que te resulta más atractiva.',1,1,1,9),(14,2,1,'P10. Imagina que estás considerando colocar una cuarta parte de tus inversiones en una sola inversión. Se espera que esta inversión genere aproximadamente el doble de la tasa de un depósito a plazo. Sin embargo, a diferencia de un depósito a plazo, esta inversión no está protegida contra la pérdida del recurso invertido.<BR />¿Qué tan baja debería ser la posibilidad de una pérdida para que tú puedas realizar la inversión?',1,1,1,10),(15,2,1,'P11. En los últimos años, ¿Cómo ha cambiado el riesgo de tus inversiones personales?',1,1,1,11),(16,3,1,'P12. Desde tu perspectiva, consideras que el nivel de riesgo de este producto es:',1,1,0,1),(17,3,1,'P13. Asumiendo que dispones de los recursos necesarios ¿Cuál es la probabilidad que tú inviertas en este producto?',1,1,0,2),(18,3,1,'P14. ¿Cuál es la probabilidad que tú recomiendes este producto a un amigo o familiar?',1,1,0,3),(19,3,1,'P15. Asumiendo que dispones de los recursos necesarios ¿Cuál es la probabilidad que la siguiente inversión que hagas sea en este producto?',1,1,0,4),(20,3,1,'P16. Desde tu perspectiva, ¿En qué medida consideras que los profesionales financieros pueden predecir el desempeño futuro de este producto de inversión?',1,1,0,5),(21,3,1,'P17. Desde tu perspectiva, ¿Qué posibilidades hay de perder dinero al invertir en este producto de inversión?',1,1,0,6),(22,3,1,'P18. Si tuvieras recursos invertidos en este producto, ¿Cuánto te preocuparías por ellos?',1,1,0,7),(23,3,1,'P19. Desde tu perspectiva, ¿Cuánta atención debe prestar un inversionista al rendimiento de su dinero al invertir en este producto?',1,1,0,8),(24,3,1,'P20. ¿Qué tan fácil seria para un inversionista disponer del dinero invertido en este producto al momento que lo quiera hacer es decir antes de que termine el periodo de la inversión?',1,1,0,9),(25,3,1,'P21. Desde tu perspectiva, ¿Cuánta variabilidad consideras que tendrá el rendimiento de este producto con el tiempo?',1,1,0,10),(26,4,1,'P22. ¿Cuál es tu moneda preferida para invertir?',1,1,0,1),(27,4,1,'P23. ¿Qué tipo de inversión prefieres?',1,1,0,2),(28,4,1,'P24. ¿Tienes alguna preferencia por productos de inversión determinados (inmuebles, fondos de inversión, acciones de bolsa, bonos)?',1,1,0,3),(29,4,1,'P25.  ¿Qué tipo de producto de inversión prefieres? RANKEAR por orden de preferencia (1 más preferido – 4 menos preferido)',1,1,0,4),(30,4,1,'P26. ¿Cuál horizonte de tiempo de inversión prefieres?',1,1,0,5),(31,4,1,'P27. Dentro del contexto actual, ¿cuál es tu posición frente a las inversiones en el país?',1,1,0,6),(32,4,1,'P28. ¿Qué porcentaje de tus inversiones tienes en el país?',1,1,0,7),(33,5,1,'D3. Por favor indica tu grado de instrucción',1,1,0,1),(34,5,1,'D4. Considerando todos tus ingresos brutos (trabajo, inversión, familia y pensión) por favor indica el rango de tu ingreso personal antes de impuestos.',1,1,0,2),(35,5,1,'D5. ¿Estás casado (o tienes una pareja de hecho /conviviente)?',1,1,0,3),(36,5,1,'D6. ¿En qué categoría de ingresos brutos se ubican tus ingresos combinados con los de tu pareja antes de impuestos?',1,1,0,4),(37,5,1,'D7. Por favor, indica ¿A cuántas personas de tu familia, además de ti, apoyas total o parcialmente financieramente?',1,1,0,5),(38,5,1,'D8. Piensa en tu patrimonio neto como lo que posees, incluida la casa familiar, el valor de la empresa, tus ahorros y otros activos de uso personal, restando las deudas que tengas. ¿En qué grupo se encuentra el valor de tu patrimonio neto? (Si estás casado o tienes una pareja de hecho, incluye solo tu parte de los activos de propiedad conjunta).',1,1,0,6),(39,5,1,'D9. ¿Aproximadamente, cuánto de tu patrimonio está destinado a productos de inversión financiera?',1,1,0,7);

#PREGUNTA 1 - D1
# (1,1,1,'D1. Por favor indica tu género',1,1,0,1)
q1 = Question(
    id_survey_section=surv_sec.id,
    id_survey=survey.id,
    name_question='D1. Por favor indica tu género',
    description='',
    answer_required=1,
    calculated=0,
    order=1
)
session.add(q1)
session.commit()
# (1,1,1,1,'1. Masculino',1,1,1)
session.add(Question_Option(
    id_question=q1.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='1. Masculino',
    value=0,
    order=1
))
# (2,1,1,1,'2. Femenino',2,1,2),
session.add(Question_Option(
    id_question=q1.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='2. Femenino',
    value=0,
    order=2
))
session.commit()

#PREGUNTA 2 - D2
# (2,1,1,'D2. Por favor indica tu edad en años cumplidos',1,1,0,2)
q2 = Question(
    id_survey_section=surv_sec.id,
    id_survey=survey.id,
    name_question='D2. Por favor indica tu edad en años cumplidos',
    description='',
    answer_required=1,
    calculated=0,
    order=2
)
session.add(q2)
session.commit()

session.add(Question_Option(
    id_question=q2.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='Placeholder',
    value=0,
    order=1
))
session.commit()


#PREGUNTA 1 - F1
# (3,1,1,'F1. ¿Alguna vez has invertido en productos financieros?',1,1,0,3)
q3 = Question(
    id_survey_section=surv_sec.id,
    id_survey=survey.id,
    name_question='F1. ¿Alguna vez has invertido en productos financieros?',
    description='',
    answer_required=1,
    calculated=0,
    order=3
)
session.add(q3)
session.commit()
# (5,4,1,1,'1. Sí.',5,1,5)
session.add(Question_Option(
    id_question=q3.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='1. Sí.',
    value=0,
    order=1
))
# (6,4,1,1,'2. No.',6,1,6)
session.add(Question_Option(
    id_question=q3.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='2. No.',
    value=0,
    order=2,
    survey_is_over=1
))
session.commit()

#PREGUNTA 2 - F2
# (4,1,1,'F2. ¿Tienes recursos invertidos en algún tipo de producto financiero actualmente (por ejemplo: inmuebles, fondos de inversión, acciones en la bolsa, bonos)?',1,1,0,4)
# (`id`,`id_survey_section`,`id_survey`,`name_question`,`answer_required`,`active`,`calculated`,`order`)
q4 = Question(
    id_survey_section=surv_sec.id,
    id_survey=survey.id,
    name_question='F2. ¿Tienes recursos invertidos en algún tipo de producto financiero actualmente (por ejemplo: inmuebles, fondos de inversión, acciones en la bolsa, bonos)?',
    description='',
    answer_required=1,
    calculated=0,
    order=4
)
session.add(q4)
session.commit()
# (5,4,1,1,'1. Sí.',5,1,5)
session.add(Question_Option(
    id_question=q4.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='1. Si.',
    value=0,
    order=1
))
# (6,4,1,1,'2. No.',6,1,6)
session.add(Question_Option(
    id_question=q4.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='2. No.',
    value=0,
    order=2,
    survey_is_over=1
))

session.commit()

#PREGUNTA 1
# (5,2,1,'P1. En comparación con otras personas, ¿Cómo calificas tu disposición a asumir riesgos financieros?',1,1,1,1)
q5 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P1. En comparación con otras personas, ¿Cómo calificas tu disposición a asumir riesgos financieros?',
    description='',
    answer_required=1,
    calculated=1,
    order=1
)
session.add(q5)
session.commit()

# (7,5,1,2,'1. Extremadamente bajo.',1,1,1)
session.add(Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='1. Extremadamente bajo.',
    value=1,
    order=1
))
# (8,5,1,2,'2. Muy bajo.',2,1,2)
session.add(Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='2. Muy bajo.',
    value=2,
    order=2
))
# (9,5,1,2,'3. Bajo.',3,1,3)
# (`id`,`id_question`,`id_survey`,`id_survey_section`,`name_option`,`value`,`active`,`order`)
session.add(Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='3. Bajo.',
    value=3,
    order=3
))
# (10,5,1,2,'4. Promedio.',4,1,4)
session.add(Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='4. Promedio.',
    value=4,
    order=4
))
# (11,5,1,2,'5. Alto.',5,1,5)
session.add(Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='5. Alto.',
    value=5,
    order=5
))
# (12,5,1,2,'6. Muy alto.',6,1,6)
session.add(Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='6. Muy alto.',
    value=6,
    order=6
))
# (13,5,1,2,'7. Extremadamente alto.',7,1,7)
session.add(Question_Option(
    id_question=q5.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='7. Extremadamente alto.',
    value=7,
    order=7
))
session.commit()

#PREGUNTA 2
# (6,2,1,'P2. Cuando piensas en la palabra \'riesgo\' en un contexto financiero, ¿Cuál de las siguientes palabras viene a tu mente primero?',1,1,1,2)
q6 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P2. Cuando piensas en la palabra \'riesgo\' en un contexto financiero, ¿Cuál de las siguientes palabras viene a tu mente primero?',
    description='',
    answer_required=1,
    calculated=1,
    order=2
)
session.add(q6)
session.commit()
# (14,6,1,2,'1. Peligro.',1,1,1)
session.add(Question_Option(
    id_question=q6.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='1. Peligro.',
    value=1,
    order=1
))
# (15,6,1,2,'2. Incertidumbre.',2,1,2)
session.add(Question_Option(
    id_question=q6.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='2. Incertidumbre.',
    value=2,
    order=2
))
# (16,6,1,2,'3. Oportunidad.',3,1,3)
session.add(Question_Option(
    id_question=q6.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='3. Oportunidad.',
    value=3,
    order=3
))
# (17,6,1,2,'4. Adrenalina.',4,1,4)
session.add(Question_Option(
    id_question=q6.id,
    id_survey=survey.id,
    id_survey_section=surv_sec.id,
    name_option='4. Adrenalina.',
    value=4,
    order=4
))
session.commit()

#PREGUNTA 3
# (7,2,1,'P3. ¿Alguna vez has invertido una gran suma en una inversión arriesgada principalmente por la adrenalina de ver si su valor subía o bajaba?',1,1,1,3)
q7 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P3. ¿Alguna vez has invertido una gran suma en una inversión arriesgada principalmente por la adrenalina de ver si su valor subía o bajaba?',
    description='',
    answer_required=1,
    calculated=1,
    order=3
)
session.add(q7)
session.commit()
# (18,7,1,2,'1. No, nunca.',1,1,1)
session.add(Question_Option(
    id_question=q7.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1. No, nunca.',
    value=1,
    order=1
))
# (19,7,1,2,'2. Sí, aunque muy raramente.',2,1,2)
session.add(Question_Option(
    id_question=q7.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2. Sí, aunque muy raramente.',
    value=2,
    order=2
))
# (20,7,1,2,'3. Sí, aunque con poca frecuencia.',3,1,3)
session.add(Question_Option(
    id_question=q7.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3. Sí, aunque con poca frecuencia.',
    value=3,
    order=3
))
# (21,7,1,2,'4. Sí, con cierta frecuencia.',4,1,4)
session.add(Question_Option(
    id_question=q7.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4. Sí, con cierta frecuencia.',
    value=4,
    order=4
))
# (22,7,1,2,'5. Sí, con mucha frecuencia.',5,1,5)
session.add(Question_Option(
    id_question=q7.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='5. Sí, con mucha frecuencia.',
    value=5,
    order=5
))
session.commit()


#PREGUNTA 4
# (8,2,1,'P4. Si tuvieras que elegir entre más seguridad laboral con un pequeño aumento salarial y menos seguridad laboral con un gran aumento salarial, ¿Cuál elegirías?',1,1,1,4)
# (`id`,`id_survey_section`,`id_survey`,`name_question`,`answer_required`,`active`,`calculated`,`order`)
q8 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P4. Si tuvieras que elegir entre más seguridad laboral con un pequeño aumento salarial y menos seguridad laboral con un gran aumento salarial, ¿Cuál elegirías?',
    description='',
    answer_required=1,
    calculated=1,
    order=4
)
session.add(q8)
session.commit()
# (23,8,1,2,'1. Definitivamente más seguridad laboral con un pequeño aumento salarial.',1,1,1)
session.add(Question_Option(
    id_question=q8.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1. Definitivamente más seguridad laboral con un pequeño aumento salarial.',
    value=1,
    order=1
))
# (24,8,1,2,'2. Probablemente más seguridad laboral con un pequeño aumento salarial.',2,1,2)
session.add(Question_Option(
    id_question=q8.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2. Probablemente más seguridad laboral con un pequeño aumento salarial.',
    value=2,
    order=2
))
# (25,8,1,2,'3. No estoy seguro.',3,1,3)
session.add(Question_Option(
    id_question=q8.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3. No estoy seguro.',
    value=3,
    order=3
))
# (26,8,1,2,'4. Probablemente menos seguridad laboral con un gran aumento salarial.',4,1,4)
session.add(Question_Option(
    id_question=q8.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4. Probablemente menos seguridad laboral con un gran aumento salarial.',
    value=4,
    order=4
))
# (27,8,1,2,'5. Definitivamente menos seguridad laboral con un gran aumento salarial.',5,1,5)
# (`id`,`id_question`,`id_survey`,`id_survey_section`,`name_option`,`value`,`active`,`order`)
session.add(Question_Option(
    id_question=q8.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='5. Definitivamente menos seguridad laboral con un gran aumento salarial.',
    value=5,
    order=5
))
session.commit()

#PREGUNTA 5
q9 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P5. Imagina que tienes un trabajo en el que puedes elegir que te paguen un salario, una comisión o una combinación de ambos. ¿Cuál elegirías?',
    description='',
    answer_required=1,
    calculated=1,
    order=5
)
session.add(q9)
session.commit()
session.add(Question_Option(
    id_question=q9.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1. Todo salario.',
    value=1,
    order=1
))
session.add(Question_Option(
    id_question=q9.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2. Principalmente salario.',
    value=2,
    order=2
))
session.add(Question_Option(
    id_question=q9.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3. Combinación equitativa de salario y comisión.',
    value=3,
    order=3
))
session.add(Question_Option(
    id_question=q9.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4. Principalmente comisión.',
    value=4,
    order=4
))
session.add(Question_Option(
    id_question=q9.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='5. Todo comisión.',
    value=5,
    order=5
))
session.commit()

#PREGUNTA 6
q10 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P6. ¿Qué grado de riesgo has asumido con tus decisiones financieras en el pasado?',
    description='',
    answer_required=1,
    calculated=1,
    order=6
)
session.add(q10)
session.commit()
session.add(Question_Option(
    id_question=q10.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1. Muy pequeño.',
    value=1,
    order=1
))
session.add(Question_Option(
    id_question=q10.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2. Pequeño.',
    value=2,
    order=2
))
session.add(Question_Option(
    id_question=q10.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3. Medio.',
    value=3,
    order=3
))
session.add(Question_Option(
    id_question=q10.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4. Alto.',
    value=4,
    order=4
))
session.add(Question_Option(
    id_question=q10.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='5. Muy alto.',
    value=5,
    order=5
))
session.commit()

#PREGUNTA 7
q11 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P7. ¿Qué grado de riesgo estás actualmente dispuesto(a) a asumir con tus decisiones financieras?',
    description='',
    answer_required=1,
    calculated=1,
    order=7
)
session.add(q11)
session.commit()
session.add(Question_Option(
    id_question=q11.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1. Muy pequeño.',
    value=1,
    order=1
))
session.add(Question_Option(
    id_question=q11.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2. Pequeño.',
    value=2,
    order=2
))
session.add(Question_Option(
    id_question=q11.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3. Medio.',
    value=3,
    order=3
))
session.add(Question_Option(
    id_question=q11.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4. Alto.',
    value=4,
    order=4
))
session.add(Question_Option(
    id_question=q11.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='5. Muy alto.',
    value=5,
    order=5
))
session.commit()

#PREGUNTA 8
q12 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P8. Las inversiones pueden subir y bajar de valor y los expertos a menudo dicen que debes estar preparado para sobrellevar una recesión. ¿Cuánto podría bajar el valor total de todas tus inversiones antes de que comiences a sentirte incómodo(a)?',
    description='',
    answer_required=1,
    calculated=1,
    order=8
)
session.add(q12)
session.commit()
session.add(Question_Option(
    id_question=q12.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1. Cualquier caída en el valor me haría sentir incómodo(a).',
    value=1,
    order=1
))
session.add(Question_Option(
    id_question=q12.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2. Máximo 5%',
    value=2,
    order=2
))
session.add(Question_Option(
    id_question=q12.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3. Máximo 10%.',
    value=3,
    order=3
))
session.add(Question_Option(
    id_question=q12.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4. Máximo 15%.',
    value=4,
    order=4
))
session.add(Question_Option(
    id_question=q12.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='5. Máximo 20%.',
    value=5,
    order=5
))
session.add(Question_Option(
    id_question=q12.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='6. Máximo 25%',
    value=6,
    order=6
))
session.add(Question_Option(
    id_question=q12.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='7. Máximo 30%',
    value=7,
    order=7
))
session.add(Question_Option(
    id_question=q12.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='8. Más del 30%.',
    value=8,
    order=8
))
session.commit()

#PREGUNTA 9
q13 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P9. La mayoría de las carteras de inversión presenta una variedad de productos en cuanto al riesgo y al rendimiento. Por favor, indique cuál de las siguientes opciones de cartera representa mejor la combinación de inversiones que te resulta más atractiva.',
    description='',
    answer_required=1,
    calculated=1,
    order=9
)
session.add(q13)
session.commit()
session.add(Question_Option(
    id_question=q13.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1',
    value=1,
    order=1
))
session.add(Question_Option(
    id_question=q13.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2',
    value=2,
    order=2
))
session.add(Question_Option(
    id_question=q13.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3',
    value=3,
    order=3
))
session.add(Question_Option(
    id_question=q13.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4',
    value=4,
    order=4
))
session.add(Question_Option(
    id_question=q13.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='5',
    value=5,
    order=5
))
session.add(Question_Option(
    id_question=q13.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='6',
    value=6,
    order=6
))
session.add(Question_Option(
    id_question=q13.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='7',
    value=7,
    order=7
))
session.commit()

#PREGUNTA 10
q14 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P10. Imagina que estás considerando colocar una cuarta parte de tus inversiones en una sola inversión. Se espera que esta inversión genere aproximadamente el doble de la tasa de un depósito a plazo. Sin embargo, a diferencia de un depósito a plazo, esta inversión no está protegida contra la pérdida del recurso invertido.',
    description='',
    answer_required=1,
    calculated=1,
    order=10
)
session.add(q14)
session.commit()
session.add(Question_Option(
    id_question=q14.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1. Cero, es decir, sin posibilidad de pérdida.',
    value=1,
    order=1
))
session.add(Question_Option(
    id_question=q14.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2. Posibilidad de pérdida muy baja.',
    value=2,
    order=2
))
session.add(Question_Option(
    id_question=q14.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3. Posibilidad de pérdida moderadamente baja.',
    value=3,
    order=3
))
session.add(Question_Option(
    id_question=q14.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4. 50% de probabilidad de pérdida.',
    value=4,
    order=4
))
session.commit()

#PREGUNTA 11
q15 = Question(
    id_survey_section=surv_sec_2.id,
    id_survey=survey.id,
    name_question='P11. En los últimos años, ¿Cómo ha cambiado el riesgo de tus inversiones personales?',
    description='',
    answer_required=1,
    calculated=1,
    order=11
)
session.add(q15)
session.commit()
session.add(Question_Option(
    id_question=q15.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='1. Siempre hacia un riesgo menor.',
    value=1,
    order=1,
    survey_is_over=1
))
session.add(Question_Option(
    id_question=q15.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='2. Principalmente hacia un riesgo menor.',
    value=2,
    order=2,
    survey_is_over=1
))
session.add(Question_Option(
    id_question=q15.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='3. Sin cambios o cambios sin una dirección clara.',
    value=3,
    order=3,
    survey_is_over=1
))
session.add(Question_Option(
    id_question=q15.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='4. Principalmente hacia un mayor riesgo.',
    value=4,
    order=4,
    survey_is_over=1
))
session.add(Question_Option(
    id_question=q15.id,
    id_survey=survey.id,
    id_survey_section=surv_sec_2.id,
    name_option='5. Siempre hacia mayor riesgo.',
    value=5,
    order=5,
    survey_is_over=1
))
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

measure1 = Measure(
    id_question = 5,
    media = 3.86046511627907,
    desv_std = 0.965633158898179,
    score = 0.178672731177203
)
session.add(measure1)
session.commit()
measure2 = Measure(
    id_question = 6,
    media = 2.23255813953488,
    desv_std = 0.781854002396306,
    score = 0.119474535976691
)
session.add(measure2)
session.commit()
measure3 = Measure(
    id_question = 7,
    media = 1.72093023255814,
    desv_std = 0.983811378440982,
    score = 0.133514493245987
)
session.add(measure3)
session.commit()
measure4 = Measure(
    id_question = 8,
    media = 3.18604651162791,
    desv_std = 1.4352005659321,
    score = 0.125482172553175
)
session.add(measure4)
session.commit()
measure5 = Measure(
    id_question = 9,
    media = 2.65116279069767,
    desv_std = 0.719911400971793,
    score = 0.137375956440199
)
session.add(measure5)
session.commit()
measure6 = Measure(
    id_question = 10,
    media = 2.95348837209302,
    desv_std = 0.75446254513026,
    score = 0.173573261499592
)
session.add(measure6)
session.commit()
measure7 = Measure(
    id_question = 11,
    media = 2.48837209302326,
    desv_std = 0.960458546817633,
    score = 0.1470436485641
)
session.add(measure7)
session.commit()
measure8 = Measure(
    id_question = 12,
    media = 3.44186046511628,
    desv_std = 1.84264723623631,
    score = 0.121211309672033
)
session.add(measure8)
session.commit()
measure9 = Measure(
    id_question = 13,
    media = 3.81395348837209,
    desv_std = 1.20031372790792,
    score = 0.16417204198077
)
session.add(measure9)
session.commit()
measure10 = Measure(
    id_question = 14,
    media = 2.13953488372093,
    desv_std = 0.74262710468397,
    score = 0.099489154305808
)
session.add(measure10)
session.commit()
measure11 = Measure(
    id_question = 15,
    media = 2.67441860465116,
    desv_std = 1.10670962838063,
    score = 0.132667813313866
)
session.add(measure11)
session.commit()

risk_profile1 = Risk_Profile(
    name = 'Adverso',
    operator = '<',
    value = -1
)
session.add(risk_profile1)
session.commit()

risk_profile2 = Risk_Profile(
    name = 'Mod. Adverso',
    operator = '<=',
    value = 0
)
session.add(risk_profile2)
session.commit()

risk_profile3 = Risk_Profile(
    name = 'Mod. Agresivo',
    operator = '>',
    value = 0
)
session.add(risk_profile3)
session.commit()
risk_profile4 = Risk_Profile(
    name = 'Agresivo',
    operator = '>',
    value = 0.75
)
session.add(risk_profile4)
session.commit()