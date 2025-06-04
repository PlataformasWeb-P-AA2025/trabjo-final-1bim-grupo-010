## Lo que se consultó en la IA generativa:

- Al momento de generar las tablas, estas se crearon mal y consultamos para entender cómo deben crearse, además de comprender la estructura de los archivos CSV.

- Al momento de llenar las tablas, solo se llenaba la tabla de usuario, mientras que las otras dos no. Consultamos por qué pasaba esto y descubrimos que estaban mal generadas.

- En tres consultas nos salían errores o los resultados eran incorrectos, por lo que consultamos qué estaba mal en nuestro código.

- En lo que tiene que ver con la instalacion de postgres en docker tambien se consulto a la IA.

## Base de datos Postgres a través de Docker

## 🐳 Instalación de Docker en Ubuntu 24

Ejecuta los siguientes comandos para instalar Docker:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
echo \"deb [signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \$(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

---

## 🗄️ Iniciar un contenedor de PostgreSQL

```bash
sudo docker run --name postgres_bd -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```
- **Nombre del contenedor**: \`postgres_bd\`
- **Contraseña**: \`1234\`

Verifica que el contenedor está corriendo:
```bash
sudo docker ps
```

---

## ⚙️ Configurar la conexión en \`configuracion_postgres.py\`

```python
cadena_base_datos = 'postgresql+psycopg2://postgres:1234@localhost:5432/postgres'
```

### 🔍 Desglose de la cadena de conexión:
| Elemento               | Descripción |
|------------------------|------------|
| \`postgresql+psycopg2\`  | Tipo de base de datos y controlador (\`psycopg2\`). |
| \`postgres\`            | Nombre del usuario de la base de datos. |
| \`1234\`                | Contraseña del usuario \`postgres\`. |
| \`localhost\`           | Dirección del servidor donde corre PostgreSQL. |
| \`5432\`                | Puerto de conexión predeterminado. |
| \`postgres\`            | Nombre de la base de datos. |

---

## 🔑 Acceder al contenedor para gestionar la base de datos

```bash
sudo docker exec -it postgres_bd psql -U postgres
```

---

## 🐍 Probar conexión desde Python

Antes de ejecutar los scripts, instala las dependencias necesarias:

```bash
sudo apt update
sudo apt install libpq-dev python3-dev
```

Instalar \`psycopg2-binary\`:
```bash
pip install psycopg2-binary
```

Ejecutar los scripts:
```bash
python genera_tablas_postgres.py
python csv_cargaDatos_postgres.py
```

---

## 📊 Verificar tablas y datos dentro de PostgreSQL

Accede al contenedor:
```bash
sudo docker exec -it postgres_bd psql -U postgres
```

Conéctate a la base de datos:
```sql
\c postgres;
```

Verificar tablas creadas:
```sql
\dt
```

Consultar los datos en las tablas:
```sql
SELECT * FROM usuario;
SELECT * FROM publicacion;
SELECT * FROM reaccion;
```

Contar registros por tabla:
```sql
SELECT COUNT(*) FROM usuario;
SELECT COUNT(*) FROM publicacion;
SELECT COUNT(*) FROM reaccion;
```

---


