CREATE TABLESPACE ctn_misdatos LOCATION '/var/ctndatos/miprimertablespace';

DROP DATABASE empresa;

CREATE DATABASE empresa TABLESPACE = ctn_misdatos;

CREATE TABLE persona(
    codigo varchar UNIQUE,
    nombre varchar(50) NOT NULL,
    apellido varchar(50) NOT NULL,
    fecha_nacimiento Date NOT NULL,
    CONSTRAINT PK_persona PRIMARY KEY(codigo)
);


--CREATE SEQUENCE persona_codigo_seq;
--ALTER TABLE persona ALTER COLUMN codigo SET DEFAULT nextval('persona_codigo_seq');