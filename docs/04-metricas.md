# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Dicas de como organizar as finanças
- **Pergunta:** "Como posso organizar minhas finanças?"
- **Resposta esperada:** Valor baseado no texto da transcrição do vídeo de Nath Ensina
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Que modelo de tênis você recomenda para correr?"
- **Resposta esperada:** "Não sei te responder isso agora, mas posso te ajudar com..."
- **Resultado:** [ ] Correto  [X] Incorreto (Tentou me ensinar a escolher)


---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Minha ideia inicial de 5 arquivos não deu certo. Diminui para um .txt. Meu computador não estava dando conta da quantidade de dados e o computador estava muito quente, utilizando toda a memória RAM disponível

**O que pode melhorar:**
- A Amícia não tentar responder perguntas que estão fora de escopo.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
