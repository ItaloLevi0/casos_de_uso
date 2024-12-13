from random import random

# Classe que representa um pacote de dados.
class Pacote:
    def __init__(self, id, dado):
        self.id = id  # Identificador único do pacote.
        self.dado = dado  # Dados ou conteúdo do pacote.
        self.confirmado = False  # Indica se o pacote foi confirmado.

# Classe que simula uma conexão TCP.
class conexaoTCP:
    def __init__(self):
        self.state = "FECHADO" 
        self.pacotes = []  # Lista para armazenar os pacotes criados.
        self.taxa_de_perda = 0.2  # Taxa simulada de perda de pacotes (20%).

    # Método para estabelecer uma conexão.
    def estabelecer_conexao(self):
        if self.state == "FECHADO":  # Verifica se a conexão está fechada.
            print("Estabelecendo conexão...") 
            self.state = "ESTABELECIDO"  # Altera o estado para estabelecido.
            print("Conexão estabelecida!") 
        else:
            print("Conexão já está aberta.")  

    # Método para criar pacotes a partir de uma mensagem.
    def criar_pacotes(self, mensagem):
        print(f"Criando pacotes para a mensagem: '{mensagem}'") 
        # Divide a mensagem em partes e cria uma lista de objetos da classe pacote.
        self.pacotes = [Pacote(i, pedaco) for i, pedaco in enumerate(mensagem.split())]
        print(f"{len(self.pacotes)} pacotes criados.")  # Exibe a quantidade de pacotes criados.

    # Método para enviar pacotes.
    def enviar_pacotes(self):
        if self.state != "ESTABELECIDO":  # Verifica se a conexão está ativa.
            print("Conexão não estabelecida. Não é possível enviar pacotes.") 
            return 

        for pacote in self.pacotes:  # Itera sobre os pacotes criados.
            if not pacote.confirmado:  # Verifica se o pacote ainda não foi confirmado.
                print(f"Enviando pacote {pacote.id}: '{pacote.dado}'")  
                if random() > self.taxa_de_perda:  # Simula a entrega com chance de perda.
                    print(f"Pacote {pacote.id} entregue com sucesso.")  
                    self.receber_ack(pacote.id)  # Recebe a confirmação do pacote.
                else:
                    print(f"Pacote {pacote.id} perdido no envio.")  # Indica que o pacote foi perdido.
            else:
                print(f"Pacote {pacote.id} já foi entregue e confirmado.")  # Indica que o pacote já foi processado.

    # Método para receber uma confirmação (ACK) de um pacote.
    def receber_ack(self, pacote_id):
        print(f"Recebendo confirmação (ACK) para o pacote {pacote_id}.") 
        for pacote in self.pacotes:  # Itera sobre os pacotes para encontrar o correspondente.
            if pacote.id == pacote_id:  # Verifica se o ID do pacote corresponde.
                pacote.confirmado = True  # Marca o pacote como confirmado.
                print(f"Pacote {pacote_id} confirmado.")  
                return

    # Método para reenviar pacotes que não foram confirmados.
    def reenviar_pacotes_desconhecidos(self):
        print("Verificando pacotes não confirmados para reenvio...")  
        for pacote in self.pacotes:  # Itera sobre os pacotes criados.
            if not pacote.confirmado:  # Verifica se o pacote não foi confirmado.
                print(f"Reenviando pacote {pacote.id}: '{pacote.dado}'") 
                self.enviar_pacotes()  # Chama o método de envio para reenviar.

    # Método para fechar a conexão.
    def fechar_conexao(self):
        if self.state == "ESTABELECIDO":  # Verifica se a conexão está ativa.
            print("Encerrando conexão...")  
            self.state = "FECHADO"  # Altera o estado para fechado.
            print("Conexão encerrada.")  
        else:
            print("Conexão já está fechada.")  


if __name__ == "__main__":
    conexao = conexaoTCP()  # Cria uma instância da classe conexaoTCP.

    # Estabelecendo conexão.
    conexao.estabelecer_conexao()

    # Criando e enviando pacotes.
    conexao.criar_pacotes("Exemplo simplificado do protocolo TCP")
    conexao.enviar_pacotes()

    # Tentativa de reenvio de pacotes não confirmados.
    conexao.reenviar_pacotes_desconhecidos()

    # Encerrando conexão.
    conexao.fechar_conexao()
