# Proyecto API - PAGOS

## Registro de cuenta
   http://127.0.0.1:8000/users/signup/
   
<div align="center">
<img aling="center" width="600" height="200" src="1.png" />
<img aling="center" width="350" height="150" src="2.png" />
</div>

## Postman
## Creacion de token para poder usar la API
### Ingresar el email,username, password y copiar el token
   http://127.0.0.1:8000/users/jwt/create/
   
<div align="center">
<img aling="center" width="800" height="300" src="3.png" />
</div>
   
## En HEADERS

    En la columna KEY escribir Authorization y en VALUE escribir Bearer y poner el token para poder usar la api
<div align="center">
<img aling="center" width="800" height="400" src="4.png" />
</div>

## En este caso solo si el usuario esta autenticado podra listar todas las vistas y solo crear datos en la vista Payment
   http://127.0.0.1:8000/api/v2/payment/

## Si el usuario es admin tiene acceso a todo (CRUD)
      users: http://127.0.0.1:8000/api/v2/users/
      servicios: http://127.0.0.1:8000/api/v2/servicios/
      payment: http://127.0.0.1:8000/api/v2/payment/
      expired: http://127.0.0.1:8000/api/v2/expired/


## Versionamiento
    http://127.0.0.1:8000/api/v1/
    http://127.0.0.1:8000/api/v2/
