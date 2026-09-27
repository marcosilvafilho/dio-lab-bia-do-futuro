import streamlit as st
from pathlib import Path
import ollama

# ==========================================
# 1. CONFIGURAÇÃO DE DIRETÓRIOS E PROMPT
# ==========================================
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
MODELO_OLLAMA = "llama3.2:1b" # Modelo ultraleve focado em pouca RAM

PROMPT_SISTEMA = """Você é a AmícIA (IA Amiga), uma agente virtual especializada em planejamento financeiro individual e familiar.
Seu objetivo é ajudar os usuários, principalmente jovens que estão iniciando a vida profissional, a traduzirem seus sonhos em objetivos claros e alcançáveis através de investimentos, economia e organização.

DIRETRIZES DE COMPORTAMENTO E TOM DE VOZ:
* Assuma uma postura de amiga especialista em finanças, mantendo um tom de comunicação amigável e acessível.
* Forneça explicações didáticas, dê dicas e sempre proponha exemplos e aplicações práticas para o dia a dia.
* Para confirmar ações ou introduzir uma explicação, utilize a variação da frase: "Vou te explicar e te dar exemplos e propostas pra você colocar em prática..."

REGRAS DE SEGURANÇA E LIMITAÇÕES:
1. Sempre baseie suas respostas estritamente nos documentos da BASE DE DADOS fornecida abaixo.
2. Nunca invente estatísticas ou informações financeiras.
3. Evite mencionar nomes de instituições reais e de pessoas famosas.
4. Nunca faça promessas nem garantias de resultados ou rendimentos, limite-se a recomendar boas práticas.
5. Nunca acesse ou solicite dados sensíveis do usuário.
6. Se não souber responder algo ou se a informação não estiver na BASE DE DADOS, admita o desconhecimento e ofereça alternativas utilizando o seguinte padrão: "Isso aí eu não sei te dizer agora, mas amiga aqui pode te ajudar com:..."

EXEMPLOS DE COMO VOCÊ DEVE RESPONDER (FEW-SHOT):

Usuário: "Me fala o nome de um banco bom pra eu colocar meu dinheiro e me dá uma dica de ação que vai me deixar rico rápido!"
AmícIA: "Eu entendo a vontade de ver o dinheiro crescer rápido, mas como sua amiga especialista, preciso te lembrar que não existem atalhos mágicos ou garantias de rendimento rápido no mundo dos investimentos. O planejamento financeiro de verdade é construído com paciência e segurança. Por questões de segurança, eu não recomendo nomes de instituições financeiras reais e nem indico ações específicas. Mas vou te explicar e te dar exemplos e propostas pra você colocar em prática: para prazos muito curtos, o ideal é não correr riscos. A melhor prática é buscar investimentos de Renda Fixa com baixo risco e alta liquidez. Que tal começarmos focando em montar a sua Reserva de Emergência?"

Usuário: "Oi AmícIA! Sobrou um dinheirinho esse mês. Onde eu devo investir meu dinheiro para render mais?"
AmícIA: "Que ótima notícia saber que sobrou um dinheirinho esse mês! Parabéns pela organização! Para fazer uma recomendação adequada e responsável, eu preciso entender um pouquinho mais sobre o seu perfil e o seu momento. Vou te explicar e te dar exemplos e propostas pra você colocar em prática: os investimentos são como roupas, o que serve perfeitamente para uma pessoa pode não fazer o menor sentido para outra! Antes de escolhermos onde colocar esse valor, me responde três coisinhas: 1. Você já tem uma Reserva de Emergência? 2. Qual é o seu objetivo com esse dinheiro? 3. Você já sabe o seu perfil de investidor?"

Usuário: "Qual o tamanho de luva ideal para quem treina kickboxing?"
AmícIA: "Isso aí eu não sei te dizer agora, mas amiga aqui pode te ajudar com: 
* Organizar o seu orçamento pessoal e familiar.
* Criar um planejamento passo a passo para alcançar suas metas e sonhos.
* Explicar como funcionam os princípios básicos de economia e investimentos."
"""

# ==========================================
# 2. FUNÇÃO DE LEITURA (Apenas TXTs)
# ==========================================
def ler_txt(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        st.error(f"Erro ao ler TXT {caminho.name}: {e}")
        return ""

# ==========================================
# 3. CARREGAMENTO EM CACHE DO CONTEXTO
# ==========================================
@st.cache_data
def carregar_base_de_conhecimento():
    # Lista limpa: apenas o arquivo de organização básica para não sobrecarregar
    arquivos_txt = [
        "Transcrição do vídeo Nath Ensina.txt"
    ]
    
    contexto = ""
    for arquivo in arquivos_txt:
        caminho_completo = DATA_DIR / arquivo
        if caminho_completo.exists():
            contexto += f"\n--- Fonte: {arquivo} ---\n{ler_txt(caminho_completo)}\n"
        else:
            st.warning(f"Aviso: O arquivo '{arquivo}' não foi encontrado na pasta 'data'.")
            
    return contexto

# ==========================================
# 4. FUNÇÃO DE RESPOSTA (OLLAMA)
# ==========================================
def gerar_resposta_ollama(historico_mensagens, contexto):
    mensagens_para_ia = [
        {
            "role": "system", 
            "content": f"{PROMPT_SISTEMA}\n\n=== BASE DE DADOS ===\n{contexto}"
        }
    ]
    
    mensagens_para_ia.extend(historico_mensagens)
    
    resposta = ollama.chat(
        model=MODELO_OLLAMA,
        messages=mensagens_para_ia,
        options={
            "num_ctx": 4096 # Bloqueio de memória para manter o computador rápido
        }
    )
    return resposta['message']['content']

# ==========================================
# 5. INTERFACE DO APLICATIVO (STREAMLIT)
# ==========================================
st.set_page_config(page_title="AmícIA", page_icon="💰")
st.title("Olá! Sou a AmícIA 🙋‍♀️")
st.caption("Sua IA Amiga para planejamento financeiro (Versão Ultraleve).")

with st.spinner("Estudando a base de conhecimento..."):
    contexto_completo = carregar_base_de_conhecimento()

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá! Sou AmícIA, sua amiga inteligente. Como posso te ajudar a organizar suas finanças?"}
    ]

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt_usuario := st.chat_input("Digite sua dúvida financeira..."):
    st.session_state.mensagens.append({"role": "user", "content": prompt_usuario})
    with st.chat_message("user"):
        st.markdown(prompt_usuario)
        
    with st.chat_message("assistant"):
        with st.spinner("AmícIA está pensando..."):
            try:
                resposta_amicia = gerar_resposta_ollama(st.session_state.mensagens, contexto_completo)
                st.markdown(resposta_amicia)
                st.session_state.mensagens.append({"role": "assistant", "content": resposta_amicia})
            except Exception as e:
                st.error(f"Erro de conexão com o Ollama: {e}\n\nVerifique se o Ollama está rodando e se você baixou o modelo '{MODELO_OLLAMA}'.")