Feature: Cadastro de animais perdidos

  Scenario: Cadastrar um animal perdido com sucesso
    Given que o sistema HelpPet está disponível
    When eu cadastro um animal chamado "Bolt" na cidade "Maricá"
    Then o animal deve ser salvo com status "Perdido"