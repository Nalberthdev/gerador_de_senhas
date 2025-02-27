import random  #importar a função random para gerar números aleatórios
import string #importar a biblioteca string com caracteres especiais


def gerar_senha(tamanho=8): #cria a função gerar_senha que recebe um argumento de tamanho padrão de 8 caracteres
    caracteres = string.ascii_letters + string.digits + string.punctuation #combina caracteres alfabéticos, dígitos e caracteres especiais
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) #gera uma senha com o tamanho especificado, escolhendo um caractere aleatório de cada tipo de caractere com o range especificado.
    return senha

#perguntar o usuário para digitar o tamanho da senha
tamanho_senha = int(input("Digite o tamanho da senha: ")) 
senha_gerada = gerar_senha(tamanho_senha)
print(f"Senha gerada: {senha_gerada}")
