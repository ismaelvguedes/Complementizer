from complementizer import Complementizer
from complementizer.type import TypeField
from complementizer.form import Form

# Configuração da API genérica
comp = Complementizer(
    url_base='https://api.exemplo.com',  # Base URL da API
    username='seu_usuario',              # Nome de usuário para autenticação
    password='seu_password',             # Senha para autenticação
    has_token=True,                      # Se a API usa tokens de autenticação
    path_auth='/auth/token'              # Endpoint para autenticação e obtenção do token
)

# Gerando dados fictícios para interagir com a API
for n in range(0, 3):
    form = Form(table='usuarios')

    # Criando campos com dados fictícios
    nome_completo = form.createField('nome_completo', TypeField.NAME_FULL)
    email = form.createField('email', TypeField.EMAIL)
    username = form.createDefault('username', nome_completo.data.split(' ')[0].lower())
    senha = form.createField('senha', TypeField.PASSWORD)

    # Associando campos adicionais, se necessário
    endereco = form.createField('endereco', TypeField.ADDRESS)
    telefone = form.createField('telefone', TypeField.PHONE)

    # Populando o endpoint com os dados gerados
    comp.populate('/usuarios/criar', form)

    # Log de resposta para verificar se os dados foram inseridos corretamente
    print(f'Usuário {nome_completo.data} criado com sucesso!')
