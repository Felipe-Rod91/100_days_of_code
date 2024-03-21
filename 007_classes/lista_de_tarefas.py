# Desenvolva um programa simples em Python para gerenciar tarefas diárias. Crie uma classe chamada GerenciadorTarefas 
# que permita adicionar tarefas, marcar tarefas como concluídas e exibir todas as tarefas pendentes.
# A classe deve ter métodos como adicionar_tarefa, marcar_concluida e exibir_tarefas_pendentes.

# Desafio extra: Implemente um método para exibir todas as tarefas concluídas.

class taskManager:
    def __init__(self):
        self.tasks = []
        self.concluded = []
    
# Método de adicionar tarefas à lista
    def add_task(self, task):
        self.tasks.append(task)
        print(f'A tarefa "{task}" foi adicionada com sucesso.')

# Método de mostrar a lista com as tarefas pendentes e concluídas
    def tasks_list(self):
        print('-=' * 30)
        print(f'Tarefas pendentes:'.upper())
        for number, item in enumerate(self.tasks):
            print(f'    {number+1}- {item}')
        print()
        print('Tarefas concluídas:'.upper())
        for item in self.concluded:
            print(f'    - {item}')
        print('-=' * 30)

# Método para marcar uma tarefa como concluída
    def concluded_task(self, concluded):
        try:
            self.tasks.remove(concluded)
            self.concluded.append(concluded)
            print(f'A tarefa "{concluded}" foi concluída com sucesso')
        except ValueError:
            print(f'A tarefa "{concluded}" não está na lista de tarefas.')
        

manager = taskManager()
manager.add_task('Limpar o banheiro')
manager.add_task('Fechar a janela')
manager.add_task('Fazer a comida')
manager.tasks_list()
manager.add_task('Ligar para a farmácia')
manager.tasks_list()
manager.concluded_task('Limpar o banheiro')
manager.tasks_list()
manager.add_task('Buscar o filho na escola')
manager.tasks_list()
manager.concluded_task('Buscar o filho na escola')
manager.tasks_list()
