# gerador_de_senhas 
intuito de usar em ambientes de NOC, gerando senhas complexas para não correr risco de invsão no Data Center.



# Explicação do código:

string.ascii_letters → Contém todas as letras maiúsculas e minúsculas.
string.digits → Contém os números de 0 a 9.
string.punctuation → Contém símbolos como !@#$%^&*().
random.choice(caracteres) → Escolhe aleatoriamente um caractere.
Loop (for _ in range(tamanho)) → Repete até formar a senha com o tamanho desejado.