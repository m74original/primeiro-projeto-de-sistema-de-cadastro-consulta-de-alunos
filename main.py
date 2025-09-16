# primeiro-projeto-de-sistema-de-cadastro-consulta-de-alunos
Primeiro projeto baseado em PYTHON, no qual eu desenvolvi um projeto instruido do professor IRLAN FERREIRA, baseado em criar um sistema de cadastro para uma escola.


escolha = 0
alunos = []

def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    while True:
        nota = float(input('Digite a nota do aluno(0-10):'))
        if nota >0 and nota <=10:
            break
        else:
            (print('Nota inválida. (0 a 10)'))
    dados = {
            "nome":nome,
            "idade":idade,
            "nota":nota
    }
    alunos.append(dados)
    
def mostrar_alunos():
    if len(alunos) == 0:
        print(f'Sem alunos na lista.')
        return
    for aluno in alunos:
        print(f' Nome : {aluno['nome']}\n Idade : {aluno['idade']}\n Nota : {aluno['nota']}\n{'-'*15}')

def procurar_aluno(nome_do_aluno):
    if len (alunos) == 0:
        print('Sem alunos cadastrados:')
        return
    for aluno in alunos:
        if aluno ['nome'].lower() == nome_do_aluno.lower():
            print(f' Nome : {aluno['nome']}\n Idade : {aluno['idade']}\n Nota : {aluno['nota']}')
            break
    else:
        print('Aluno não encontrado.')

def deletar_aluno(nome_do_aluno):
    if len (alunos) == 0:
        print('Sem alunos cadastrados:')
        return
    for aluno in alunos:
        if aluno ['nome'].lower() == nome_do_aluno.lower():
            alunos.remove(aluno)
            print(f'Aluno {nome_aluno} foi deletado com sucesso!')
            break
    else:
        print('Aluno não encontrado.')
    
def media_notas():
    if len(alunos) == 0:
        print("Sem alunos cadastrados.")
        return
    soma = 0
    for aluno in alunos:
        soma += aluno['nota']
    media = soma / len(alunos)
    print(f'A média dos alunos é de {media:.2f}')

while True:
    print('\n1. ADICIONAR ALUNO.\n2. LISTAR TODOS ALUNOS.\n3. BUSCAR PELO NOME.\n4. REMOVER ALUNO.\n5. MOSTRAR MÉDIA GERAL DAS NOTAS.\n6. SAIR.\n')
    escolha = int(input('O que deseja fazer?\n'))
    match escolha:
        case 1:
            adicionar_aluno()
        case 2:
            mostrar_alunos()
        case 3:
            nome_aluno = input('Qual aluno deseja buscar? : ')
            procurar_aluno(nome_aluno)
        case 4:
            nome_aluno = input('Qual aluno deseja remover? : ')
            deletar_aluno(nome_aluno)
        case 5:
            media_notas()
        case 6:
            break
