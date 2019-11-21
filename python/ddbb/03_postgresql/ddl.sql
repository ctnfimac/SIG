CREATE TABLESPACE ctn_misdatos LOCATION '/var/ctndatos/miprimertablespace';

CREATE DATABASE empresa TABLESPACE = ctn_misdatos;

CREATE TABLE persona(
    codigo int,
    nombre varchar(50) NOT NULL,
    apellido varchar(50) NOT NULL,
    fecha_nacimiento Date NOT NULL,
    CONSTRAINT PK_persona PRIMARY KEY(codigo)
);