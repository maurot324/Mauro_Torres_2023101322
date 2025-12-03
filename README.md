
Sistema web para gestión y venta de ganado bovino con Flask y MySQL.


### **Paso 1: Clonar el Repositorio**



### **Paso 2: Crear Contenedor MySQL**
```bash
docker run -d --name mysql_test2 -e MYSQL_ROOT_PASSWORD=root123 -e MYSQL_DATABASE=ganado_db -p 3306:3306 mysql:8.0
```

### **Paso 3: Crear la Tabla en la Base de Datos**
```bash
# Acceder a MySQL
docker exec -it mysql_test2 mysql -u root -proot123

# Dentro de MySQL, ejecutar:
USE ganado_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NULL,
    correo VARCHAR(100) NULL,
    celular VARCHAR(20) NOT NULL,
    horario_llamar VARCHAR(50) NOT NULL
);
```

### **Paso 4: Configurar Conexión a Base de Datos**
Crear archivo `db_connection.py`:
```python
import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root123',
        database='ganado_db',
        cursorclass=pymysql.cursors.DictCursor
    )
```

### **Paso 5: Verificar Estructura de Archivos**

### **Paso 6: Ejecutar la Aplicación (python app.py)**


### **Paso 7: Acceder desde el Navegador**
- **En tu PC:** http://localhost:5000
- **Desde otro dispositivo en tu red:**
  1. Obtener tu IP:
```bash
     ipconfig  # Windows
     ifconfig  # Linux/Mac
```
  2. Acceder desde otro dispositivo: http://TU_IP:5000
     - Ejemplo: http://192.168.1.100:5000

### **Paso 8: Subir Cambios a GitHub**
```bash
git add .
git commit -m "Descripción de cambios"
git push origin main
```

---

##  Información del Sistema(Examen_Final)

**Tecnologías:** Python, Flask, MySQL, Docker, HTML5, CSS3

**Categorías de Ganado:** Terneros, Novillito, Novillos, Vaquillonas, Vacas, Toros con imagenes cada categoriasimilar a un catalogo

**Autor:** Mauro Torres - UNIDA

---

## Comandos Útilizados
```bash
# Docker
docker start mysql_test2      # Iniciar contenedor
docker stop mysql_test2       # Detener contenedor
docker ps                     # Ver contenedores activos

# Git
git status                    # Ver estado
git add .                     # Agregar cambios
git commit -m "mensaje"       # Guardar cambios
git push                      # Subir a GitHub
```

---

⭐ **¡Proyecto listo para usar!** Si tienes problemas, abre un issue en GitHub.
