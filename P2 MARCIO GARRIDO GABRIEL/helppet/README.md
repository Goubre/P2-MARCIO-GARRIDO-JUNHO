# HelpPet API

Sistema para cadastro e gerenciamento de animais perdidos desenvolvido com FastAPI.

## Tecnologias Utilizadas

- Python 3
- FastAPI
- Pytest
- Behave
- Docker

## Arquitetura

O projeto segue os princípios da Arquitetura Limpa:

```
app/
├── domain
├── application
├── infrastructure
├── presentation
```

## Design Patterns

### Repository Pattern

Responsável pela persistência dos dados dos animais.

Arquivo:

```
app/infrastructure/animal_repository.py
```

### Factory Pattern

Responsável pela criação dos objetos Animal.

Arquivo:

```
app/domain/animal_factory.py
```

### DTO Pattern

Responsável pela transferência de dados entre camadas.

Arquivo:

```
app/domain/animal_dto.py
```

### Strategy Pattern

Responsável pela estratégia de envio de notificações.

Arquivo:

```
app/strategies/notification_strategy.py
```

## Funcionalidades

### Listar animais

GET

```
/animals
```

### Cadastrar animal

POST

```
/animals
```

### Marcar animal como encontrado

PUT

```
/animals/{animal_id}/found
```

## Testes

### Executar testes unitários

```bash
python -m pytest
```

### Executar testes BDD

```bash
python -m behave
```

## Docker

Build da imagem:

```bash
docker build -t helppet .
```

Executar container:

```bash
docker run -p 8000:8000 helppet
```

## Autor

Gabriel Velasco Leonel

Universidade de Vassouras

Engenharia de Software