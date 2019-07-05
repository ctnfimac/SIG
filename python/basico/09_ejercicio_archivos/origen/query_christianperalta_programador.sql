"""
 query a realizar
 
"""

select id, nombre, edad 
from perdona
where nombre = 'christian' , apellido = 'peralta' , profesion = 'programador'
order by fecha asc;