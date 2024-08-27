# CRUD_EXAMEN
Examen de habilidades.

## Descripción

Este proyecto es un sistema de reservas de salas de juntas que permite a los usuarios crear, actualizar, y eliminar reservas. Está construido con Django y utiliza vistas basadas en clases para manejar las operaciones CRUD.

![image](https://github.com/user-attachments/assets/444876e5-36bf-4cc9-a3fc-8bd481e490bb)
![image](https://github.com/user-attachments/assets/50561fe0-8370-4a71-82d3-1f2f74074b4a)
![image](https://github.com/user-attachments/assets/5222e3f8-9c2c-42c8-89f2-0cb242b14887)
![image](https://github.com/user-attachments/assets/066fd725-c187-4010-af9d-12c3fdb3c48c)
![image](https://github.com/user-attachments/assets/b8090e15-4fc0-46b8-991b-418709907c6c)


## Requisitos

- Python 3.8+
- Django 3.2+
- SQLite (o cualquier otra base de datos compatible con Django)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/Aruz13/CRUD_EXAMEN.git
   cd CRUD_EXAMEN
   ```
2. **Crea y activa un entorno virtual:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. **Instala las dependencias:**
Crea un archivo txt con lo siguiente:
Django>=3.2,<4.0
pytz>=2021.1
sqlparse>=0.4.1

   ```bash
   pip install -r requirements.txt
   ```


5. **Realiza las migraciones de la base de datos:**

```bash
python manage.py migrate
```
5. **Ejecuta el servidor de desarrollo:**

```bash
python manage.py runserver
```

Ahora puedes acceder a la aplicación en http://127.0.0.1:8000/.

## Uso
Funcionalidades Principales
Home Page: Muestra las próximas reuniones y futuras reservas.
CRUD para Salas: Permite crear, editar y eliminar salas de juntas.
CRUD para Reservas: Permite crear, editar y eliminar reservas de salas.
CRUD para Usuarios: Permite crear, editar y eliminar usuarios.
Finalizar Reuniones: Los usuarios pueden finalizar reuniones manualmente desde la Home Page.
Eliminación Automática de Reuniones Caducadas: Las reuniones pasadas se eliminan automáticamente cuando se actualiza o abre la página.


## Agregar Datos de Prueba
Un botón en la Home Page permite agregar automáticamente 10 registros en cada una de las tablas User y Room, debido a que no se sabe la fecha en la que se probara, no es posible crear valores aleatorios que vayan a ser utiles. 

##Aspectos Importantes
Verificación de Reuniones Caducadas: Cada vez que se carga o actualiza la página, se verifica si hay reuniones caducadas. Si se encuentran, se eliminan automáticamente.
Validación de Formularios: Si ocurre un error al enviar un formulario (como un correo electrónico duplicado), se muestra un mensaje de error al usuario.

