# 🦁 Sistema de Gerenciamento de Zoológico

## 👩‍💻 Desenvolvido por

Karina Gabriela Ferreira de Oliveira

## 📖 Descrição

Projeto Final da disciplina de Programação Orientada a Objetos (POO).

O sistema simula o gerenciamento de um zoológico, permitindo o controle de animais, tratadores, recintos e atividades diárias, como alimentação, tratamento, limpeza e banho de sol. Além disso, o administrador pode acompanhar e registrar todas as atividades realizadas.

---

## 🚀 Funcionalidades

- Alimentar animais
- Tratar animais
- Limpar recintos
- Registrar banho de sol
- Registrar atividades realizadas
- Exibir relatório de atividades
- Salvar atividades em arquivo
- Ler histórico de atividades armazenadas

---

## 🧩 Conceitos de POO Utilizados

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
O sistema utiliza blocos `try/except` para validar entradas do usuário e evitar falhas durante a execução.

### Manipulação de Arquivos
As atividades realizadas são armazenadas no banco de dados `zoo.db` e podem ser consultadas posteriormente.

---

## 📂 Estrutura do Projeto

```text
zoo-management-system/

src/

├── models/
│   ├── animal.py
│   ├── recinto.py
│   └── tratador.py
│
├── services/
│   └── administrador.py
│
├── repository/
│   └── arquivos.py
│
└── main.py

docs/
images/
README.md
```

---

## Diagrama do Sistema
├── Animal
│   ├── Leao
│   ├── Macaco
│   └── Elefantet
│
├── Tratador
├── Administrador
├── Recinto


## ▶️ Como Executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

```bash
python main.py
```

3. Escolha uma das opções do menu para interagir com o sistema.

---

## 🖥️ Exemplo de Uso

```text
===== ZOOLÓGICO =====
1 - Alimentar animal
2 - Tratar animal
3 - Limpar recinto
4 - Banho de sol
5 - Relatório
6 - Ler arquivo
0 - Sair
```

Exemplo:

```text
Escolha o animal:
1 - Simba (Leão)
2 - Caco (Macaco)
3 - Dumbo (Elefante)
4 - Melman (Girafa)

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
- Manipulação de Arquivos
- Listas
- Menu Interativo
- Controle de Animais
- Controle de Tratadores
- Controle de Recintos
- Relatório Administrativo

---

## 📌 Conclusão

O projeto permitiu aplicar os principais conceitos de Programação Orientada a Objetos em Python por meio da simulação do gerenciamento de um zoológico. Foram implementadas funcionalidades de controle de animais, tratadores e recintos, além do registro e acompanhamento das atividades realizadas diariamente.