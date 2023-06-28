-- Comenzamos con CRUD: Create(insertar), Read(leer), Update(actualizar), Delete(eliminar)
-- Listar los estudiantes (read)
use estudiantes;
SELECT * FROM estudiantes2022;
-- Insertar estudiante
INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES ("Juan", "Perez", "2312454", "juan@mail.com");
-- Update(actualizar)
UPDATE estudiantes2022 SET nombre="Juan Carlos", apellido="Garcia" where idestudiantes2022=1;
-- Delete(eliminar)
DELeTE FROM estudiantes2022 WHERE idestudiantes2022=3;
-- Para modificar el idestudiantes2022 y comience en 1
ALTER TABLE estudiantes2022 AUTO_INCREMENT = 1;