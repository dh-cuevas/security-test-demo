# 🔒 Security Test Demo

Proyecto de demostración para pruebas de seguridad automatizadas en CI/CD.

## ⚠️ ADVERTENCIA
Este proyecto contiene código **intencionalmente vulnerable** con fines educativos.  
**NO USAR EN PRODUCCIÓN**

## 🎯 Objetivo
Implementar un pipeline CI/CD con Jenkins que ejecute pruebas de seguridad automatizadas usando:
- OWASP Dependency-Check
- SonarQube
- OWASP ZAP

## 🛠️ Tecnologías
- Python 3.x / Flask
- Jenkins
- Docker
- OWASP Dependency-Check
- SonarQube
- OWASP ZAP

## 📁 Estructura del Proyecto
```
security-test-demo/
├── .gitignore
├── README.md
├── app.py                      # Aplicación Flask vulnerable
├── requirements.txt            # Dependencias Python
├── sonar-project.properties    # Configuración SonarQube
└── Jenkinsfile                 # Pipeline CI/CD (próximamente)
```

## ⚠️ Vulnerabilidades Implementadas
Este código incluye intencionalmente:
- ❌ Inyección de comandos OS
- ❌ Uso de `eval()` con entrada del usuario
- ❌ Debug mode habilitado en producción
- ❌ Sin validación de entrada
- ❌ Sin sanitización de datos

## 🚀 Instalación Local (Opcional)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

## 📚 Proyecto Académico
**Curso:** OCY1102 - Ciberseguridad en Desarrollo  
**Institución:** Duoc UC  
**Actividad:** 3.2 - Automatización de Pruebas de Seguridad  
**Modalidad:** Trabajo en Parejas

## 👥 Autores
- David Cuevas Salgado

---
**Fecha:** Noviembre 2025
```

5. Commit message: `Update README with project details`
6. Click **"Commit changes"**

---

## ✅ **Checkpoint - Verificación de Archivos**

Tu repositorio **debe tener** estos archivos:
```
✅ .gitignore
✅ README.md
✅ app.py
✅ requirements.txt
✅ sonar-project.properties
