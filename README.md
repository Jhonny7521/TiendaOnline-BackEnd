## API-PRODUCTS-BSALE
### DESCRIPCIÓN

__API-PRODUCTS-BSALE__ en la versión actual es solo de consumo. Unicamente el método get esta disponible para su interacción.

### INFORMACIÓN DE USO

__API-PRODUCTS-BSALE__ es un producto gratuito y está abierto para su libre uso. Se le pide a los desarrolladores hacer el uso correcto en base a las indicaciones aqui mencionadas.

### REST

- __Base url:__  `"https://deploy-api-bsale.herokuapp.com/api/"`

Todas las solicitudes aceptadas por la api en versión actual son solicitudes GET. Todas las respuestas obtenidas estarán en formato Json

> __Nota:__ 
Llamar a base de la API no devolverá ningún retorno de datos, para ello utilice los endpoints que se mencionan líneas abajo.

### ENDPOINTS DE API

Para obtener todos los productos utilice:

- __GET__  `"https://deploy-api-bsale.herokuapp.com/api/products/"`
```sh
[
    {   "category":1,
        "discount":20,
        "id":5,
        "name":"ENERGETICA MRBIG",
        "price":1490.0,
        "url_image":"https://dojiw2m9tvv09.cloudfront.net/11132/product/misterbig3308256.jpg"
    },
    {   "category":1,
        "discount":0,
        "id":6,
        "name":"ENERGETICA REDBULL",
        "price":1490.0,
        "url_image":"https://dojiw2m9tvv09.cloudfront.net/11132/product/redbull8381.jpg"
        },
        {   "category":1,
            "discount":0,
            "id":7,
            "name":"ENERGETICA SCORE",
            "price":1290.0,
            "url_image":"https://dojiw2m9tvv09.cloudfront.net/11132/product/logo7698.png"
        },
        ...
]
```
Para obtener todos las categorias de productos utilice:

- __GET__ `"https://deploy-api-bsale.herokuapp.com/api/categories/"`
```sh
[ 
    {   "id":1,
        "name":"bebida energetica"
    },
    {   "id":2,
    "name":"pisco"
    },
    {   "id":3,
        "name":"ron"
    },
    {   "id":4,
    "name":"bebida"
    },
    ...
]
```

Para obtener todos los productos de una categoria utilice:

- __GET__  `"https://deploy-api-bsale.herokuapp.com/api/products/category/{id}"`

- __Parámetros:__
id: Identificador de categoria de producto.

__Ejemplo:__
- __GET__  `"https://deploy-api-bsale.herokuapp.com/api/products/category/4"`
```sh
[
    {   "category":4,
        "discount":0,
        "id":37,
        "name":"COCA COLA ZERO DESECHABLE",
        "price":1490.0,
        "url_image":"https://dojiw2m9tvv09.cloudfront.net/11132/product/cocazero9766.jpg"
        },
        {"category":4,
        "discount":0,
        "id":48,
        "name":"SPRITE 1 1/2 Lts",
        "price":1500.0,
        "url_image":"https://dojiw2m9tvv09.cloudfront.net/11132/product/sprite-lata-33cl5575.jpg"
        },
        ...
]
```

Para obtener todos los productos contengan en su nombre un texto utilice:

- __GET__ `"https://deploy-api-bsale.herokuapp.com/api/products/{text}"`

- __Parámetros:__ 
text: Cadena de texto que se buscará en los nombres de productos.

#### Ejemplo:
- __GET__  `"https://deploy-api-bsale.herokuapp.com/api/products/bebida"`
```sh
[
    {   "category":4,
        "discount":10,
        "id":68,
        "name":"Bebida Sprite 1 Lt",
        "price":1250.0,
        "url_image":null
    }
]
```

## CLONACIÓN DE PROYECTO

Para interatuar con el presente proyecto se debe tener en cuenta la versión de python instalada Python 3.7. Así tambien, deberá seguir las siguientes indicaciones:

- Clonar el repositorio:
```sh
$ git clone 
```

- Instalar un ambiente virtual
```sh
$ python -m venv venv
```

- Activar el ambiente virtual
```sh
$ source venv/Scripts/activate    --> Windows
$ source venv/bin/activate        --> Linux
```

I- nstalar requerimientos y ejecutar el servidor:
```sh
$ pip install -r requirements.txt
$ python server.py
```

### SOBRE EL PROYECTO:

- Lenguaje de programación: __Python__
- Versión de lenguaje: __Python 3.7__
- Framework utilizado: __Flask__
- Motor de base de datos: __MySQL__
