#ApiChech de Verificação de Disponibilidade de Sites
Descrição
Esta API verifica a acessibilidade de qualquer site fornecido por meio de sua URL. Ela realiza uma requisição HTTP para o endereço informado e retorna informações sobre o status do site, indicando se ele está funcionando ou se houve algum problema ao acessá-lo.

A API foi construída usando FastAPI, garantindo alta performance e facilidade de uso, sendo ideal para monitoramento simples de sites ou integração em sistemas maiores.

Recursos
Verificação de Disponibilidade: Realiza uma consulta a um site para determinar se ele está acessível.
Mensagens Detalhadas: Retorna informações sobre o status do site ou o motivo de falha.
Rápida Configuração: Fácil de instalar e configurar, pronta para uso local ou em servidores.
Como Usar
Requisição
Método: GET
Endpoint: /check-site
Parâmetros de consulta:
url (obrigatório): A URL do site a ser verificado. Deve incluir o protocolo (http ou https).
Exemplo de Requisição
bash
Copiar
Editar
curl -X GET "http://127.0.0.1:8000/check-site?url=https://www.google.com"
Exemplo de Respostas
Sucesso (200):

json
Copiar
Editar
{
    "status": "Site está funcionando!",
    "url": "https://www.google.com"
}
Erro (400):

json
Copiar
Editar
{
    "detail": "Erro ao acessar o site: HTTPSConnectionPool(host='invalid-url', port=443): Max retries exceeded with url: /"
}
Instalação
Certifique-se de ter o Python 3.7+ instalado.
Clone este repositório:
bash
Copiar
Editar
git clone <url-do-repositorio>
cd <nome-do-repositorio>
Instale as dependências:
bash
Copiar
Editar
pip install -r requirements.txt
Inicie o servidor:
bash
Copiar
Editar
uvicorn main:app --reload
Acesse a API no navegador: http://127.0.0.1:8000.
Documentação Interativa
A API inclui uma interface Swagger para facilitar a exploração:

Documentação interativa: http://127.0.0.1:8000/docs
Especificações OpenAPI: http://127.0.0.1:8000/openapi.json
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para adicionar funcionalidades, corrigir bugs ou melhorar a documentação.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
