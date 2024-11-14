"""
CREATE TABLE IF NOT EXISTS Pregunta (
  idPregunta    INT NOT NULL AUTO_INCREMENT,
  pregunta      TEXT NOT NULL,
  respuesta     CHAR(1) NOT NULL,
);
"""

"""
CREATE TABLE IF NOT EXISTS Opcion (
  idOpcion      INT     NOT NULL AUTO_INCREMENT,
  idPregunta    INT     NOT NULL,
  opcion        TEXT    NOT NULL,
  letra         CHAR(1) NOT NULL,

    FOREIGN KEY (idPregunta)
    REFERENCES Pregunta (idPregunta)
"""
