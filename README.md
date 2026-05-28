# 🚀 CRUD com Python (Flask) + MySQL

Aplicação web com operações básicas de CRUD (Create, Read, Update, Delete), desenvolvida com **Python (Flask)** e banco de dados **MySQL**.

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Flask
* MySQL
* HTML + Jinja2

---

## ⚙️ Funcionalidades

✔ Criar usuários
✔ Listar usuários
✔ Editar usuários
✔ Deletar usuários
✔ Integração com banco de dados MySQL

---

## 🧱 Estrutura do projeto

```
crud-python-mysql/
│
├── app.py
├── db.py
├── models.py
├── templates/
│   ├── index.html
│   ├── criar.html
│   └── editar.html
└── README.md
```

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/crud-python-mysql.git
cd crud-python-mysql
```

---

### 2. Criar ambiente virtual

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependências

```
pip install flask mysql-connector-python
```

---

### 4. Configurar o banco de dados

No MySQL, execute:

```
CREATE DATABASE crud_db;
USE crud_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);
```

---

### 5. Configurar conexão

No arquivo `db.py`, altere:

```
password="SUA_SENHA"
```

---

### 6. Rodar aplicação

```
python app.py
```

---

### 7. Acessar no navegador

```
http://localhost:5000
```

---

## 💡 Melhorias futuras

* Interface com Bootstrap
* Sistema de login/autenticação
* API REST

---

## 📚 Aprendizados

Este projeto demonstra:

* Integração backend com banco de dados
* Estruturação de projeto Flask
* Operações CRUD completas
* Organização de código em camadas
