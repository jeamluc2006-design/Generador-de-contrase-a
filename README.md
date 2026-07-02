# Generador Seguro de Contraseñas

## Descripción

Este proyecto consiste en el desarrollo de un generador seguro de contraseñas realizado en Python como parte de la asignatura de Programación.

El programa permite al usuario generar contraseñas personalizadas seleccionando la longitud y los tipos de caracteres que desea incluir.

---

## Objetivo

Desarrollar una aplicación que permita generar contraseñas seguras de forma sencilla, aplicando conceptos básicos de programación como funciones, condicionales, bucles y validación de datos.

---

## Funcionalidades

- Ingresar la longitud de la contraseña.
- Seleccionar si se desean incluir:
  - Letras mayúsculas.
  - Letras minúsculas.
  - Números.
  - Símbolos (# _ - @).
- Generar una contraseña aleatoria.
- Validar que el usuario seleccione al menos un tipo de carácter.
- Permitir generar varias contraseñas sin cerrar el programa.

---

## Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

---

## Estructura del proyecto

```
Generador-Password/
│
├── diagramas/
│   ├── imagen1.png
│   └── imagen2.png
    └── imagen3.png
│
├── src/
│   └── Passgenerator
│
└── README.md
```

---

## Diagrama de flujo

El programa sigue el siguiente proceso:

1. Inicio.
2. Ingresar la longitud de la contraseña.
3. Seleccionar los tipos de caracteres.
4. Generar la contraseña.
5. Mostrar el resultado.
6. Preguntar si se desea generar otra contraseña.
7. Finalizar el programa.

---

## Arquitectura del sistema

El programa está organizado en los siguientes componentes:

- Usuario
- Interfaz de entrada
- Validación de datos
- Generador de contraseñas
- Presentación del resultado

---

## Cómo ejecutar el programa

1. Tener instalado Python 3.
2. Descargar o clonar este repositorio.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar el siguiente comando:

```bash
python Passgenerator.py
```

---

## Ejemplo de uso

```
===================================
 GENERADOR SEGURO DE CONTRASEÑAS
===================================

Ingrese la longitud de la contraseña: 12

¿Incluir mayúsculas? (s/n): s
¿Incluir minúsculas? (s/n): s
¿Incluir números? (s/n): s
¿Incluir símbolos? (s/n): s

Contraseña generada:
Ab3@jP_7Lm#Q
```

---

## Autor

Proyecto desarrollado con fines académicos para la asignatura de Programación.
