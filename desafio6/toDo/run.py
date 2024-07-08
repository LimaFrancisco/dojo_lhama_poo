from model import GerenciadorDeEmails


from model import Email

while True:
    gerenciador = GerenciadorDeEmails('Empresa', 'empresa@email.com')
    assunto = input('Defina o Titulo do Email: ')
    mensagem = input('Defina o assunto: ')
    email = gerenciador.enviar_email(assunto, mensagem)
    print(email.mostrar_email())
