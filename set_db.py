|#/usr/bin/python3
from models.question import Question
from models.survey import Survey


survey = `Surveys` (`id`,`name_survey`,`description`,`nro_questions`,`active`,`created_at`,`created_by`)
VALUES (1,'Encuesta Perfil de Riesgo','Cuestionario Integrado Perfil de riesgo y Evaluacion de Producto',39,1,'2021-10-18 02:17:07',1);


Question(
    # id_survey_section = Column(Integer, ForeignKey('Survey_Sections.id'))
    # id_survey = Column(String(128), nullable=False)
    # name_question = Column(String(255), nullable=False)
    # description = Column(String(255))
    # answer_required = Column(Integer, nullable=False)
    # calculated = Column(Integer, nullable=False)
    # order = Column(Integer, nullable=False)
)
