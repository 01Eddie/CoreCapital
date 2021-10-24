CREATE DATABASE IF NOT EXISTS cp_survey_db;
CREATE USER IF NOT EXISTS 'usr_survey'@'localhost';
SET PASSWORD FOR 'usr_survey'@'localhost' = 'survey_pwd';
GRANT ALL PRIVILEGES ON cp_survey_db.* TO 'usr_survey'@'localhost';
GRANT SELECT ON performance_schema.* TO 'usr_survey'@'localhost';
FLUSH PRIVILEGES;

USE cp_survey_db;

CREATE TABLE `Type_Document` (
  `id_type_doc` int NOT NULL ,
  `name` varchar(45) NOT NULL ,
  `active` tinyint(1) NOT NULL ,
  PRIMARY KEY (`id_type_doc`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Type_Document` WRITE;
INSERT INTO `Type_Document` VALUES (1,'DNI',1),(2,'Pasaporte',1),(3,'Carnet de Extranjería',1);
UNLOCK TABLES;


CREATE TABLE `Users`
(
 `id_user`      int NOT NULL AUTO_INCREMENT ,
 `id_type_doc`  int NOT NULL ,
 `name`         varchar(100) NOT NULL ,
 `lastname`     varchar(255) NOT NULL ,
 `email`        varchar(100) NOT NULL ,
 `nro_document` varchar(15) NOT NULL ,
 `phone`        varchar(20) NOT NULL ,
 `active`       tinyint(1) NOT NULL ,
 `created_at`   datetime NOT NULL ,
 `updated_at`   datetime NULL ,
 `deleted_at`   datetime NULL ,
 `created_by`   int NOT NULL ,
 `updated_by`   int NULL ,
 `deleted_by`   int NULL ,

PRIMARY KEY (`id_user`),
KEY `id_type_doc` (`id_type_doc`),
CONSTRAINT `Users_FK_1` FOREIGN KEY (`id_type_doc`) REFERENCES `Type_Document` (`id_type_doc`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Users` WRITE;
INSERT INTO `Users` (`id_user`,`id_type_doc`,`name`,`lastname`,`email`,`nro_document`,`phone`,`active`,`created_at`,`created_by`) 
VALUES (1,1,'admin','admin','admin@gmail.com','11111111','999999999',1,'2021-10-18 02:17:06',1),(2,1,'Pablo','Perez','pablitop@gmail.com','12345678','999988888',1,'2021-10-18 02:17:07',1);
UNLOCK TABLES;


CREATE TABLE `Surveys`
(
 `id_survey`   int NOT NULL AUTO_INCREMENT ,
 `name_survey` varchar(100) NOT NULL ,
 `description` varchar(255) NOT NULL ,
 `nro_questions` int NOT NULL,
 `active`      tinyint(1) NOT NULL ,
 `created_at`  datetime NOT NULL ,
 `updated_at`  datetime NULL ,
 `deleted_at`  datetime NULL ,
 `created_by`  int NOT NULL ,
 `updated_by`  int NULL ,
 `deleted_by`  int NULL ,

PRIMARY KEY (`id_survey`)
); ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Surveys` WRITE;
INSERT INTO `Surveys` (`id_survey`,`name_survey`,`description`,`nro_questions`,`active`,`created_at`,`created_by`)
VALUES (1,'Encuesta Perfil de Riesgo','Cuestionario Integrado Perfil de riesgo y Evaluacion de Producto',38,1,'2021-10-18 02:17:07',1);
UNLOCK TABLES;

CREATE TABLE `Survey_Sections`
(
 `id_survey`         int NOT NULL ,
 `id_survey_section` int NOT NULL ,
 `name_section`      varchar(100) NOT NULL ,
 `description`       varchar(1024) NULL ,
 `active`            tinyint(1) NOT NULL ,

PRIMARY KEY (`id_survey`, `id_survey_section`),
KEY `id_survey` (`id_survey`),
CONSTRAINT `Survey_Sections_FK_2` FOREIGN KEY (`id_survey`) REFERENCES `Surveys` (`id_survey`)
); ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Survey_Sections` WRITE;
INSERT INTO `Survey_Sections` (`id_survey`,`id_survey_section`,`name_section`,`description`,`active`)
VALUES (1,1,'Inicio','',1),(1,2,'Perfil de Riesgo','',1),(1,3,'Evaluación de Producto','Imagina que tu asesor financiero te ofrezca una oportunidad de invertir en Bonos de Financiamiento de Terrenos.<BR />Se trata de un bono a tasa fija que invierte en la compra de terrenos donde se desarrollarán proyectos inmobiliarios de empresas de prestigio.<BR />Estos bonos están respaldados con la garantía hipotecaria del terreno, la cual equivale entre el 100% y 125% de la inversión y se haría efectiva en caso de impago.<BR />El bono tiene un plazo promedio de 15 meses y el monto mínimo de inversión es de US$ 100,000.<BR />Se paga intereses trimestralmente calculados a una tasa anual de 6.5% en dólares para una inversión inferior a US$ 200,000 y de 7.5% para una inversión igual o superior a ese monto.',1),(1,4,'Preferencias','',1),(1,5,'Datos Demográficos','',1);
UNLOCK TABLES;

CREATE TABLE `Questions`
(
 `id_question`       int NOT NULL ,
 `id_survey_section` int NOT NULL ,
 `id_survey`         int NOT NULL ,
 `name_question`     varchar(255) NOT NULL ,
 `description`       varchar(255) NULL ,
 `answer_required`   tinyint(1) NOT NULL ,
 `active`            tinyint(1) NOT NULL ,
 `calculated`        tinyint(1) NOT NULL ,
 `order`             int NOT NULL ,

PRIMARY KEY (`id_question`, `id_survey_section`, `id_survey`),
KEY `id_survey_section` (`id_survey_section`, `id_survey`),
CONSTRAINT `Question_FK_3` FOREIGN KEY (`id_survey_section`, `id_survey`) REFERENCES Survey_Sections (`id_survey_section`, `id_survey`)
); ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Questions` WRITE;
INSERT INTO `Questions` (`id_question`,`id_survey_section`,`id_survey`,`name_question`,`answer_required`,`active`,`calculated`,`order`)
VALUES (1,1,1,'D1. Por favor indica tu género',1,1,0,1),(2,1,1,'D2. Por favor indica tu edad en años cumplidos',1,1,0,2),(3,1,1,'F1. ¿Alguna vez has invertido en productos financieros?',1,1,0,3),(4,1,1,'F2. ¿Tienes recursos invertidos en algún tipo de producto financiero actualmente (por ejemplo: inmuebles, fondos de inversión, acciones en la bolsa, bonos)',1,1,0,4),(5,2,1,'P1. En comparación con otras personas, ¿Cómo calificas tu disposición a asumir riesgos financieros?',1,1,1,1)(6,2,1,'P2. Cuando piensas en la palabra "riesgo" en un contexto financiero, ¿Cuál de las siguientes palabras viene a tu mente primero?',1,1,1,2),(7,2,1,'P3. ¿Alguna vez has invertido una gran suma en una inversión arriesgada principalmente por la adrenalina de ver si su valor subía o bajaba?',1,1,1,3),(8,2,1,'P4. Si tuvieras que elegir entre más seguridad laboral con un pequeño aumento salarial y menos seguridad laboral con un gran aumento salarial, ¿Cuál elegirías?',1,1,1,4),(9,2,1,'P5. Imagina que tienes un trabajo en el que puedes elegir que te paguen un salario, una comisión o una combinación de ambos. ¿Cuál elegirías?',1,1,1,5),(10,2,1,'P6. ¿Qué grado de riesgo has asumido con tus decisiones financieras en el pasado?',1,1,1,6),(11,2,1,'P7. ¿Qué grado de riesgo estás actualmente dispuesto(a) a asumir con tus decisiones financieras?',1,1,1,7),(12,2,1,'P8. Las inversiones pueden subir y bajar de valor y los expertos a menudo dicen que debes estar preparado para sobrellevar una recesión. ¿Cuánto podría bajar el valor total de todas tus inversiones antes de que comiences a sentirte incómodo(a)?',1,1,1,8),(13,2,1,'P9. La mayoría de las carteras de inversión presenta una variedad de productos en cuanto al riesgo y al rendimiento. Por favor, indique cuál de las siguientes opciones de cartera representa mejor la combinación de inversiones que te resulta más atractiva.',1,1,1,9),(14,2,1,'P10. Imagina que estás considerando colocar una cuarta parte de tus inversiones en una sola inversión. Se espera que esta inversión genere aproximadamente el doble de la tasa de un depósito a plazo. Sin embargo, a diferencia de un depósito a plazo, esta inversión no está protegida contra la pérdida del recurso invertido.<BR />¿Qué tan baja debería ser la posibilidad de una pérdida para que tú puedas realizar la inversión?',1,1,1,10),(15,2,1,'P11. En los últimos años, ¿Cómo ha cambiado el riesgo de tus inversiones personales?',1,1,1,11),(16,3,1,'P12. Desde tu perspectiva, consideras que el nivel de riesgo de este producto es:',1,1,0,1),(17,3,1,'P13. Asumiendo que dispones de los recursos necesarios ¿Cuál es la probabilidad que tú inviertas en este producto?',1,1,0,2),(18,3,1,'P14. ¿Cuál es la probabilidad que tú recomiendes este producto a un amigo o familiar?',1,1,0,3),(19,3,1,'P15. Asumiendo que dispones de los recursos necesarios ¿Cuál es la probabilidad que la siguiente inversión que hagas sea en este producto?',1,1,0,4),(20,3,1,'P16. Desde tu perspectiva, ¿En qué medida consideras que los profesionales financieros pueden predecir el desempeño futuro de este producto de inversión?',1,1,0,5),(21,3,1,'P17. Desde tu perspectiva, ¿Qué posibilidades hay de perder dinero al invertir en este producto de inversión?',1,1,0,6),(22,3,1,'P18. Si tuvieras recursos invertidos en este producto, ¿Cuánto te preocuparías por ellos?',1,1,0,7),(23,3,1,'P19. Desde tu perspectiva, ¿Cuánta atención debe prestar un inversionista al rendimiento de su dinero al invertir en este producto?',1,1,0,8),(24,3,1,'P20. ¿Qué tan fácil seria para un inversionista disponer del dinero invertido en este producto al momento que lo quiera hacer es decir antes de que termine el periodo de la inversión?',1,1,0,9),(25,3,1,'P21. Desde tu perspectiva, ¿Cuánta variabilidad consideras que tendrá el rendimiento de este producto con el tiempo?',1,1,0,10),(26,4,1,'P22. ¿Cuál es tu moneda preferida para invertir?',1,1,0,1),(27,4,1,'P23. ¿Qué tipo de inversión prefieres?',1,1,0,2),(28,4,1,'P24. ¿Tienes alguna preferencia por productos de inversión determinados (inmuebles, fondos de inversión, acciones de bolsa, bonos)?',1,1,0,3),(29,4,1,'P25.  ¿Qué tipo de producto de inversión prefieres? RANKEAR por orden de preferencia (1 más preferido – 4 menos preferido)',1,1,0,4),(30,4,1,'P26. ¿Cuál horizonte de tiempo de inversión prefieres?',1,1,0,5),(31,4,1,'P27. Dentro del contexto actual, ¿cuál es tu posición frente a las inversiones en el país?',1,1,0,6),(32,4,1,'P28. ¿Qué porcentaje de tus inversiones tienes en el país?',1,1,0,7),(33,5,1,'D3. Por favor indica tu grado de instrucción',1,1,0,1),(34,5,1,'D4. Considerando todos tus ingresos brutos (trabajo, inversión, familia y pensión) por favor indica el rango de tu ingreso personal antes de impuestos.',1,1,0,2),(35,5,1,'D5. ¿Estás casado (o tienes una pareja de hecho /conviviente)?',1,1,0,3),(36,5,1,'D6. ¿En qué categoría de ingresos brutos se ubican tus ingresos combinados con los de tu pareja antes de impuestos?',1,1,0,4),(37,5,1,'D7. Por favor, indica ¿A cuántas personas de tu familia, además de ti, apoyas total o parcialmente financieramente?',1,1,0,5),(38,5,1,'D8. Piensa en tu patrimonio neto como lo que posees, incluida la casa familiar, el valor de la empresa, tus ahorros y otros activos de uso personal, restando las deudas que tengas. ¿En qué grupo se encuentra el valor de tu patrimonio neto? (Si estás casado o tienes una pareja de hecho, incluye solo tu parte de los activos de propiedad conjunta).',1,1,0,6),(39,5,1,'D9. ¿Aproximadamente, cuánto de tu patrimonio está destinado a productos de inversión financiera?',1,1,0,7);
UNLOCK TABLES;

CREATE TABLE `Question_Options`
(
 `id_question_option` int NOT NULL ,
 `id_question`        int NOT NULL ,
 `id_survey`          int NOT NULL ,
 `id_survey_section`  int NOT NULL ,
 `name_option`        varchar(200) NOT NULL ,
 `value`              int NULL ,
 `active`             tinyint(1) NOT NULL ,
 `order`              int NOT NULL ,

PRIMARY KEY (`id_question_option`, `id_question`, `id_survey`, `id_survey_section`),
KEY `id_question` (`id_question`, `id_survey`, `id_survey_section`),
CONSTRAINT `Question_Options_FK_4` FOREIGN KEY (`id_question`, `id_survey`, `id_survey_section`) REFERENCES Questions (`id_question`, `id_survey`, `id_survey_section`)
); ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Question_Options` WRITE;
INSERT INTO `Question_Options` (`id_question_option`,`id_question`,`id_survey`,`id_survey_section`,`name_option`,`value`,`active`,`order`)
VALUES (1,1,1,1,'1. Masculino',1,1,1),(2,1,1,1,'2. Femenino',2,1,2),
(3,2,1,1,'1. Sí.',3,1,3),(4,2,1,1,'2. No.',4,1,4),
(5,3,1,1,'1. Sí.',5,1,5),(6,3,1,1,'2. No.',6,1,6),
(7,4,1,2,'1. Extremadamente bajo.',1,1,1),(8,4,1,2,'2. Muy bajo.',2,1,2),(9,4,1,2,'3. Bajo.',3,1,3),(10,4,1,2,'4. Promedio.',4,1,4),(11,4,1,2,'5. Alto.',5,1,5),(12,4,1,2,'6. Muy alto.',6,1,6),(13,4,1,2,'7. Extremadamente alto.',7,1,7)
;
UNLOCK TABLES;


CREATE TABLE `Answers`
(
 `id_answer`          int NOT NULL AUTO_INCREMENT ,
 `id_user`            int NOT NULL ,
 `id_question_option` int NOT NULL ,
 `answer_value`       int NULL ,
 `active`             tinyint(1) NULL ,
 `id_question`        int NOT NULL ,
 `id_survey`          int NOT NULL ,
 `id_survey_section`  int NOT NULL ,
 `created_at`         datetime NOT NULL ,
 `updated_at`         datetime NULL ,
 `deleted_at`         datetime NULL ,
 `create_by`          int NOT NULL ,
 `updated_by`         int NULL ,
 `deleted_by`         int NULL ,

PRIMARY KEY (`id_answer`),
KEY fkIdx_140 (`id_question_option`, `id_question`, `id_survey`, `id_survey_section`),
CONSTRAINT FK_135 FOREIGN KEY fkIdx_140 (`id_question_option`, `id_question`, `id_survey`, `id_survey_section`) REFERENCES Question_Options (`id_question_option`, `id_question`, `id_survey`, `id_survey_section`),
KEY fkIdx_82 (`id_user`),
CONSTRAINT FK_80 FOREIGN KEY fkIdx_82 (`id_user`) REFERENCES Users (`id_user`)
); ENGINE=InnoDB DEFAULT CHARSET=latin1;






