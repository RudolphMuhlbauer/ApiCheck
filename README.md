# ApiCheck
API de Verificação de Disponibilidade de Sites
Descrição
Esta API permite verificar a acessibilidade de um site fornecido por meio de sua URL. Ao realizar uma requisição HTTP, a API retorna informações sobre o status do site, indicando se ele está acessível ou não.

Funcionalidades Principais
Verificar disponibilidade: Confirma se o site está funcionando e acessível, retornando o status HTTP.
Erro detalhado: Em caso de falha na verificação, fornece uma mensagem explicativa sobre o erro encontrado.
Resposta rápida: Limita o tempo de espera para evitar travamentos em caso de sites lentos.
Rotas Disponíveis
GET /check-site
Verifica o status de um site.

Parâmetro de consulta:

url (obrigatório): A URL do site a ser verificado. Exemplo: https://www.example.com
Resposta de Sucesso (200):

Retorna uma mensagem indicando que o site está funcionando.
Estrutura:
json
Copiar
Editar
{
    "status": "Site está funcionando!",
    "url": "https://www.example.com"
}
Resposta de Erro (400):

Retorna uma mensagem indicando que houve um problema ao acessar o site.
Estrutura:
json
Copiar
Editar
{
    "detail": "Erro ao acessar o site: <detalhes do erro>"
}
Exemplo de Uso
Realizar uma requisição GET para a URL:

bash
Copiar
Editar
http://127.0.0.1:8000/check-site?url=https://www.google.com
Resposta de Sucesso:

json
Copiar
Editar
{
    "status": "Site está funcionando!",
    "url": "https://www.google.com"
}
Resposta de Erro (exemplo de site inacessível):

json
Copiar
Editar
{
    "detail": "Erro ao acessar o site: HTTPSConnectionPool(host='invalid-url', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x...>: Failed to establish a new connection: [Errno -2] Name or service not known'))"
}
Benefícios
Simples e intuitiva: Pode ser usada por desenvolvedores, sistemas automatizados ou ferramentas de monitoramento.
Personalizável: Fácil de ajustar para incluir métricas adicionais, como tempo de resposta ou cabeçalhos HTTP.
Documentação integrada: Acesse a interface Swagger em http://127.0.0.1:8000/docs para explorar a API.
Essa API é ideal para monitorar sites, verificar problemas de conectividade ou ser usada como base para soluções mais complexas de monitoramento.
