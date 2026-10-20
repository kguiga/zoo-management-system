# 🦁 Zoo Management System

## 📖 Descrição

Sistema de gerenciamento de zoológico desenvolvido em Python para aplicação prática de conceitos de Programação Orientada a Objetos (POO), persistência de dados com SQLite, testes automatizados utilizando Pytest e versionamento utilizando Git e GitHub.

O sistema simula o gerenciamento de um zoológico, permitindo o controle de animais, tratadores, recintos e atividades diárias, como alimentação, tratamento veterinário, limpeza de recintos e banho de sol. Além disso, o administrador pode acompanhar e registrar todas as atividades realizadas.

---

## 🚀 Funcionalidades

- Alimentar animais
- Tratar animais
- Limpar recintos
- Registrar banho de sol
- Registrar atividades realizadas
- Exibir relatório de atividades
- Persistir atividades em banco de dados SQLite
- Consultar histórico de atividades registradas

---

## 🛠️ Tecnologias

- Python
- SQLite
- Pytest
- Git
- GitHub

---

## 🧩 Conceitos Aplicados

### Programação Orientada a Objetos

- Classes e Objetos
- Herança
- Polimorfismo
- Encapsulamento
- Separação de Responsabilidades

### Banco de Dados

- SQLite
- Persistência de Dados
- Operações de Inserção (INSERT)
- Operações de Consulta (SELECT)

### Qualidade de Software

- Testes Automatizados
- Pytest
- Versionamento com Git
- Desenvolvimento baseado em Branches
- Pull Requests

---

## 🧬 Conceitos de POO Utilizados

### Classes

- Animal
- Leao
- Macaco
- Elefante
- Tratador
- Recinto
- Administrador

### Herança

As classes `Leao`, `Macaco` e `Elefante` herdam da classe `Animal`.

### Polimorfismo

Cada animal possui sua própria implementação do método `tratar()`, permitindo comportamentos diferentes para cada espécie.

### Encapsulamento

Os atributos e métodos foram organizados dentro de classes responsáveis por cada entidade do sistema.

### Tratamento de Exceções

O sistema utiliza blocos `try/except` para evitar falhas durante a execução e lidar com cenários inesperados.

### Persistência de Dados

As atividades realizadas são armazenadas em um banco de dados SQLite (`zoo.db`) e podem ser consultadas posteriormente.

---

## 📂 Estrutura do Projeto

```text
zoo-management-system/

├── database/
│   └── database.py
│
├── src/
│   ├── animal.py
│   ├── tratador.py
│   ├── recinto.py
│   ├── administrador.py
│   ├── arquivos.py
│   └── main.py
│
├── tests/
│   ├── test_animal.py
│   ├── test_tratador.py
│   └── test_recinto.py
│
├── docs/
├── images/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Diagrama do Sistema

```text
Administrador
│
├── Animal
│   ├── Leao
│   ├── Macaco
│   └── Elefante
│
├── Tratador
└── Recinto
```

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/kguiga/zoo-management-system.git
```

Acesse a pasta do projeto:

```bash
cd zoo-management-system
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

### Windows (PowerShell)

```bash
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o sistema:

```bash
python src/main.py
```

---

## 🧪 Executando os Testes

Execute:

```bash
python -m pytest
```

Resultado atual:

```text
16 testes automatizados executados com sucesso
```

Cobertura atual:

- Animal
- Leão
- Macaco
- Elefante
- Tratador
- Recinto

---

## 🖥️ Exemplo de Uso

```text
===== ZOOLÓGICO =====

1 - Alimentar animal
2 - Tratar animal
3 - Limpar recinto
4 - Banho de sol
5 - Relatório
6 - Ler histórico
0 - Sair
```

Exemplo:

```text
Escolha o animal:

1 - Simba (Leão)
2 - Caco (Macaco)
3 - Dumbo (Elefante)

Animal: 1

Simba foi alimentado com Carne
```

---

## ✅ Requisitos Atendidos

- Programação Orientada a Objetos
- Classes e Objetos
- Construtores
- Herança
- Polimorfismo
- Encapsulamento
- Tratamento de Exceções
- SQLite
- Persistência de Dados
- Listas
- Menu Interativo
- Controle de Animais
- Controle de Tratadores
- Controle de Recintos
- Relatório Administrativo
- Testes Automatizados
- Versionamento com Git

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

- Programação Orientada a Objetos
- Modelagem de Domínio
- Herança e Polimorfismo
- Persistência de Dados
- SQLite
- Testes Automatizados com Pytest
- Controle de Versão com Git
- Fluxo de desenvolvimento utilizando Branches e Pull Requests
- Organização de projetos Python

---

## 🚀 Próximas Evoluções

- Adição de Type Hints
- Ampliação da cobertura de testes
- Refatoração utilizando SQLAlchemy
- Migração para FastAPI
- Criação de API REST
- Containerização com Docker

---

## 📌 Conclusão

O projeto foi inicialmente desenvolvido como trabalho final da disciplina de Programação Orientada a Objetos e posteriormente evoluído com banco de dados, testes automatizados e boas práticas de versionamento.
