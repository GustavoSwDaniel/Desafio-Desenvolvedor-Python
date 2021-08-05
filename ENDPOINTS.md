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
    "birthDate": "2017"
}
```

**Response body 201**
```json
{
    "birth_date": "2017",
    "breed": "ciames",
    "name_pet": "Gustavo",
    "pet_owner_name": "Mel"
}
```
---


### GET .../pet/<pet_id:int>/
 Enpoint para pesquisar um pet pelo seu ID


**Response body 201**
```json
{
    "birth_date": "2017",
    "breed": "ciames",
    "name_pet": "Gustavo",
    "pet_owner_name": "Mel"
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
**Response body 201**
```json
{
    "birthDate": "2017",
    "breed": "ciames",
    "namepet": "Gustavo D",
    "petOwnerName": "Mel"
}
```
