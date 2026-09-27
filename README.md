# 🙋‍♀️ AmícIA - Sua IA Amiga para Planejamento Financeiro

A **AmícIA** é uma agente virtual especializada em planejamento financeiro individual e familiar. O projeto foi criado para oferecer orientação e auxílio gratuito, direcionado para as necessidades de quem não pode buscar um profissional especializado.

---

## 🎯 O Problema e a Solução

* **O Problema:** É comum que as pessoas tenham sonhos e metas, mas não consigam traduzi-los em objetivos claros e alcançáveis porque não sabem lidar bem com suas finanças ou têm dificuldade em organizá-las.


* **A Solução:** A AmícIA resolve esse problema de forma proativa, trazendo orientações financeiras para a organização do salário, mesmo que seja pouco. O agente explica, dá dicas e exemplos de como organizar a vida financeira para atingir objetivos pessoais.


* **Público-Alvo:** Pessoas e famílias que desejam organizar melhor sua vida financeira, principalmente jovens que estão iniciando sua vida profissional.



---

## 🎭 Persona e Tom de Voz

A AmícIA foi construída com diretrizes de comportamento muito claras:

* **Personalidade:** Ela atua de forma amigável, com explicações didáticas e propondo sempre aplicações práticas para o dia a dia.


* **Abordagem:** Conversa como uma amiga especialista em finanças.


* **Saudação Padrão:** "Olá! Sou AmícIA, sua amiga inteligente. Quero te ajudar a alcançar as suas metas!".


* **Introdução de Soluções:** "Vou te explicar e te dar exemplos e propostas pra você colocar em prática...".



---

## ⚙️ Arquitetura e Tecnologias

O projeto foi desenvolvido para ser executado localmente, focado em privacidade e leveza.

* **Interface:** Streamlit.


* **LLM:** Ollama rodando localmente. Foi escolhido o modelo `llama3.2:1b`, que é um modelo ultraleve focado em computadores com pouca RAM.


* **Base de Conhecimento:** Arquivo TXT (`Transcrição do vídeo Nath Ensina.txt`) injetado diretamente no contexto do prompt.


* **Estratégia de Integração:** Os dados da base de conhecimento são carregados no início da sessão do aplicativo e inseridos no *System Prompt* (junto às diretrizes) antes do envio da mensagem para a IA. O modelo no Ollama também foi configurado com `num_ctx: 4096` (bloqueio de memória) para manter o computador rápido.



---

## 📚 Base de Dados: Desafios e Decisões

A ideia original para a Base de Conhecimento contemplava 5 arquivos diferentes, incluindo materiais do Banco Central, da Comissão de Valores Mobiliários (CVM) e transcrições de diversos vídeos de educação financeira.

**Ajuste de Rota:**

* A tentativa de usar 5 arquivos não funcionou bem na prática local.


* O computador não estava dando conta da quantidade de dados, sofrendo com superaquecimento e utilizando toda a memória RAM disponível.


* Como solução, a base foi reduzida para apenas 1 arquivo TXT ("Transcrição do vídeo Nath Ensina") para não sobrecarregar o sistema.


* Houve o sacrifício de uma base de dados maior em prol da acessibilidade e viabilidade de rodar localmente e de forma gratuita em computadores comuns.



---

## 🛡️ Segurança e Anti-Alucinação

Para garantir que a AmícIA seja uma conselheira responsável, foram implementadas regras estritas no *System Prompt* com a técnica de *Few-Shot Prompting* (fornecendo exemplos de interação).

**O que o agente NÃO faz:**

* O agente só responde com base nos dados fornecidos.


* Nunca acessa ou solicita dados sensíveis do usuário.


* Não faz promessas nem garantias de resultados financeiros, limitando-se a recomendar boas práticas.


* Não inventa estatísticas.


* Evita nomes de instituições reais e pessoas famosas.



**Redirecionamento:**
Quando não sabe a resposta ou quando o assunto foge do escopo financeiro, a IA é instruída a admitir o desconhecimento usando o padrão: *"Isso aí eu não sei te dizer agora, mas amiga aqui pode te ajudar com:..."*, listando em seguida suas reais capacidades.

---

## 📈 Avaliação e Resultados

A AmícIA foi submetida a cenários de teste reais focados em **Assertividade**, **Segurança** e **Coerência**. Durante as validações, registramos os seguintes aprendizados e resultados:

* **Oportunidade de Melhoria na Segurança:** O teste de perguntas fora do escopo (ex: "Que modelo de tênis você recomenda para correr?") teve um resultado incorreto. O agente tentou ensinar o usuário a escolher o tênis, ignorando a diretriz de não responder sobre outros assuntos. Isso mostra que a AmícIA precisa de refinamentos para não tentar responder a perguntas que fogem do escopo financeiro.

* **Desafio Técnico e Acessibilidade:** A ideia inicial de utilizar 5 fontes diferentes de dados exigiria uma IA muito pesada para processamento. Na prática, isso sobrecarregou o computador, causando superaquecimento e utilizando toda a memória RAM disponível.

* **Decisão Arquitetural:** Para manter a solução acessível e capaz de rodar localmente em computadores comuns, a base de dados precisou ser sacrificada, sendo reduzida para apenas um arquivo TXT. Concluímos que um modelo online (via compra de *tokens*) seria a arquitetura ideal para suportar um conhecimento mais robusto, embora a solução deixasse de ser 100% gratuita.

---

## 🚀 Como Executar o Projeto

**1. Configuração do Ollama:**
Instale o Ollama e baixe o modelo leve necessário para o projeto.

```bash
# Baixar o modelo
ollama pull llama3.2:1b

```

**2. Execução da Aplicação:**
Com o modelo baixado e as dependências instaladas, rode a aplicação utilizando o Streamlit.

```bash
python -m streamlit run src/app.py

```

---

## 🎥 Pitch e Demonstração

Para conferir a proposta de valor e a solução em funcionamento prático, assista ao nosso pitch:

🔗 **[AmícIA, sua Amiga Inteligente | Uma Especialista em Finanças](https://youtu.be/YTjavvynpEY)**.
