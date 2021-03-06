# Endpoints

---
## Pets
---
### POST .../pet
 Enpoint para o cadastro de novos Pets

**Request body**
```json
{
    "namePets": "Gustavo",
    "petOwnerName": "Mel",
    "breed": "ciames",
    "birthDate": "2017",
    "petPhoto": null
}
```

**Response body 201**
```json
{
    "birthDate": "2017",
    "breed": "ciames",
    "namePet": "Gustavo",
    "petOwnerName": "Mel",
    "petPhoto": null
}
```
---


### GET .../pet/<pet_id:int>/
 Enpoint para pesquisar um pet pelo seu ID


**Response body 201**
```json
{
    "birthDate": "2017",
    "breed": "ciames",
    "namePet": "Gustavo",
    "petOwnerName": "Mel",
    "petPhoto": null
}
```

---
### PUT .../pet/<pet_id:int>/
 Endpoint para atualizar as informações do pet

**Request body**
```json
{
    "namePets": "Gustavo D",
}
```
**Response body 200**
```json
{
    "birthDate": "2017",
    "breed": "ciames",
    "namepet": "Gustavo D",
    "petOwnerName": "Mel",
    "petPhoto": null
}
```

### DELETE .../pet/<pet_id:int>/
 Endpoint para a exclusão de um pet

 **Response body 200**
```json
{

}
```

### POST .../pet/photo/<pet_id:int>/
 Endpoint para adicionar foto ao pet

 **Extensões permitidas**

| Extensão|Descrição|
|----------|:------:|
| image/png | PNG  |
| image/jpeg  | JPG  |

**Content-Type**
```
   Content-Type: multipart/form-data; 
```

**Request file name**
```
   file
```

**Response body 200**
```json
{
    "birthDate": "2017",
    "breed": "ciames",
    "namepet": "Gustavo D",
    "petOwnerName": "Mel",
    "petPhoto": "amazon.s3/image.png"
}
```

### GET .../pet/image/<pet_id:int>/
 Endpoint para pegar a imagem do pet

**Response body 200**
```json
{
    "petPhoto": "amazon.s3/image.png"
}
