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
        print()

# Método de mostrar a lista com as tarefas pendentes
    def tasks_list(self):
        print(f'Tarefas pendentes:')
        for number, item in enumerate(self.tasks):
            print(f'{number+1}- {item}')
        print()

# Método para marcar uma tarefa como concluída
    def concluded_task(self, concluded):
        print(f'A tarefa "{concluded}" foi concluída com sucesso')
        self.tasks.remove(concluded)
        self.concluded.append(concluded)
        print()

 # Método para mostrar a lista de tarefas concluídas   
    def concluded_tasks_list(self):
        print('Tarefas concluídas:')
        for item in self.concluded:
            print(f'- {item}')
        print()
        

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
manager.concluded_tasks_list()
