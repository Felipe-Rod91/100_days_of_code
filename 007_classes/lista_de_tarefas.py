# Desenvolva um programa simples em Python para gerenciar tarefas diárias. Crie uma classe chamada GerenciadorTarefas 
# que permita adicionar tarefas, marcar tarefas como concluídas e exibir todas as tarefas pendentes.
# A classe deve ter métodos como adicionar_tarefa, marcar_concluida e exibir_tarefas_pendentes.

# Desafio extra: Implemente um método para exibir todas as tarefas concluídas.

class taskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f'A tarefa"{task}" foi adicionada com sucesso.')
    
    def show_tasks(self):
        print(f'Tarefas pendentes:')
        for item in self.tasks:
            print(f'- {item}')

manager = taskManager()
manager.add_task('Limpar o banheiro')
manager.add_task('Fechar a janela')
manager.add_task('Fazer a comida')
manager.show_tasks()
