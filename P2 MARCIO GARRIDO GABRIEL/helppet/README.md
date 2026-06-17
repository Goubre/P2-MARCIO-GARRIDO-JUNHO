# HelpPet API

Sistema para cadastro e gerenciamento de animais perdidos, desenvolvido com FastAPI.

## Problema escolhido

Muitas pessoas perdem seus animais e não possuem uma forma simples de registrar, consultar e atualizar informações sobre animais desaparecidos. O HelpPet propõe uma solução para cadastrar animais perdidos, listar registros existentes e marcar animais como encontrados.

## Solução proposta

A aplicação permite cadastrar animais informando nome e cidade, listar todos os animais cadastrados e atualizar o status quando o animal for encontrado.

## Microsserviços

A solução foi dividida em microsserviços:

- animal-service: responsável pelo cadastro, listagem e atualização dos animais.
- notification-service: responsável pela simulação/envio de notificações.

## Arquitetura Limpa

O animal-service foi organizado em camadas:

- domain: entidades, DTOs e regras centrais.
- application: serviços e casos de uso.
- infrastructure: repositórios e persistência.
- presentation: controllers e rotas da API.
- strategies: estratégias de notificação.

## SOLID

O projeto aplica princípios SOLID ao separar responsabilidades entre entidades, serviços, repositórios, factories e controllers. Cada classe possui uma responsabilidade específica, facilitando manutenção e testes.

## Design Patterns

Foram utilizados os seguintes padrões:

- Repository Pattern: separa a persistência dos dados.
- Factory Pattern: centraliza a criação de objetos Animal.
- DTO Pattern: organiza a transferência de dados entre camadas.
- Strategy Pattern: permite variar a estratégia de notificação.

## Clean Code

O código foi organizado com nomes claros, funções pequenas, separação de responsabilidades e estrutura de pastas coerente com a Arquitetura Limpa.

## TDD

Foram criados testes unitários com Pytest para validar o comportamento do serviço de animais.

Para executar:

python -m pytest

## BDD

Foram criados cenários de comportamento usando Behave, descrevendo o fluxo de cadastro e gerenciamento de animais.

Para executar:

python -m behave

## Docker

O projeto possui Dockerfile e docker-compose.yml para execução em ambiente conteinerizado.

Para executar com Docker:

docker compose up --build

## Deploy

O sistema está publicado no Render.

Link do sistema:

https://p2-marcio-garrido-junho.onrender.com/

Documentação Swagger:

https://p2-marcio-garrido-junho.onrender.com/docs

## Funcionalidades

- Listar animais
- Cadastrar animal
- Marcar animal como encontrado
- Interface web integrada ao backend
- Documentação automática com Swagger

## Rotas principais

- GET /animals
- POST /animals
- PUT /animals/{animal_id}/found
- GET /docs

## Justificativa técnica

FastAPI foi escolhido por ser simples, rápido e adequado para criação de APIs REST. A Arquitetura Limpa foi utilizada para separar responsabilidades e facilitar manutenção. Os Design Patterns foram aplicados para melhorar organização e reutilização do código. Docker foi utilizado para garantir execução padronizada, e o Render foi escolhido por permitir publicação rápida da aplicação em ambiente cloud.

## Autor

Gabriel Velasco Leonel

Universidade de Vassouras

Engenharia de Software
