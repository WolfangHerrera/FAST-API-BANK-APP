---

![](docs/Welcome-README.jpg)

---

[![](docs/BackEnd-README.jpg)](https://github.com/WolfangHerrera/FAST-API-BANK-APP)

---

![](docs/TextBackEnd-README.jpg)

---

![](docs/Docker-README.jpg)

---

![](docs/TextDocker-README.jpg)

---

![](docs/AboutApp-README.jpg)

---

![](docs/TextAboutApp-README.jpg)

---

![](docs/Endpoints-README.jpg)

---

![](docs/CreateAccount-README.jpg)

```sh
curl -X POST 'http://localhost:8000/accounts' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Wolfang",
    "last_name": "Herrera",
    "dni": 1025520565
}'
```

```sh
{
    "account_id": "1025452"
}
```

---

![](docs/GetAccounts-README.jpg)

```sh
curl -X GET 'http://localhost:8000/accounts'
```

```sh
[
    {
        "account_id": "1025452",
        "balance": 6000000.0
    },
    {
        "account_id": "1001274",
        "balance": 6600000.0
    }
]
```

---

![](docs/UpdateAccountBalance-README.jpg)

```sh
curl -X PATCH 'http://localhost:8000/accounts/{account_id}' \
--header 'Content-Type: application/json' \
--data '{
    "balance" : 500000
}'
```

```sh
{
    "message": "The account balance has been updated"
}
```

---

![](docs/ThankYou-README.jpg)
