# Base de Conhecimento

## Dados Utilizados

Utilizei os seguintes arquivos da pasta `data`:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `Caderno de Educação Financeira - Banco Central do Brasil.pdf` | PDF | Trazer Educação Financeira no contexto brasileiro |
| `TOP Planejamento financeiro pessoal - Comissão de Valores Mobiliários.pdf` | PDF | Ajudar no Planejamento Financeiro pessoal no contexto brasileiro |
| `Transcrição do vídeo Como começar a investir.txt` | TXT | Trazer ideias de investimentos para iniciantes |
| `Transcrição do vídeo Como planejar a vida financeira.txt` | TXT | Ajudar no Planejamento Financeiro |
| `Transcrição do vídeo Nath Ensina.txt` | TXT | Ajudar a otimizar o uso de um orçamento curto |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.
Sim, meu objetivo era diferente do que os dados da pasta original forneciam, então trouxe as fontes listadas acima.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os PDFs e arquivos de texto são carregados no início da sessão e incluídos no contexto do prompt

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
Vão no system prompt, a partir da leitura dos arquivos no início, pois não é uma base muito grande.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
