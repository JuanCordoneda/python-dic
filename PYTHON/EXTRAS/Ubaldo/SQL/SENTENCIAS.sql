--'SE ESCRIBE UN CODIGO A LA VEZ'
SELECT * FROM persona    --muestra todo el contenido de la tabla ersonas
SELECT * FROM persona ORDER BY id_persona  --muestra segun el orden de id_persona
select * from persona where id_persona = 1     --muestra las personas con id 
select * from persona where id_persona IN (1,2,3)   --mustra los ids de la tupla

INSERT INTO persona(nombre, apellido, email) VALUES('Susana', 'Esparza','sesparza@mail.com')   --agrega

UPDATE persona SET nombre = 'Ivonne', email='iesparza@mail.com' WHERE id_persona = 3 --modifica, si no especificamos que registro mod, se modifican todos

DELETE FROM persona WHERE id_persona = 3   --elimina el registro de id 3

