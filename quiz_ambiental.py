import streamlit as st

st.set_page_config(page_title="Quiz de Educação Ambiental", layout="centered")
st.title("🌱 Quiz: Educação Ambiental")

# Dados do quiz com explicações
quiz = [
    {
        "pergunta": "1. O que é reciclagem?",
        "opcoes": [
            "Uso de combustíveis fósseis",
            "Processo de reaproveitar materiais",
            "Queima de lixo",
            "Desmatamento"
        ],
        "resposta": "Processo de reaproveitar materiais",
        "explicacao": "Reciclagem é o processo de reaproveitar materiais para reduzir o consumo de recursos naturais."
    },
    {
        "pergunta": "2. Qual destes materiais é reciclável?",
        "opcoes": ["Vidro", "Comida", "Tecido sujo", "Papel higiênico usado"],
        "resposta": "Vidro",
        "explicacao": "Vidro é 100% reciclável e pode ser reutilizado infinitamente."
    },
    {
        "pergunta": "3. O que contribui para o efeito estufa?",
        "opcoes": [
            "Plantar árvores",
            "Emissão de gases de carros",
            "Coletar lixo reciclável",
            "Economizar energia"
        ],
        "resposta": "Emissão de gases de carros",
        "explicacao": "A emissão de CO₂ e outros gases dos carros aumenta o efeito estufa."
    },
    {
        "pergunta": "4. Qual é a fonte de energia renovável?",
        "opcoes": ["Carvão", "Petróleo", "Energia solar", "Gás natural"],
        "resposta": "Energia solar",
        "explicacao": "A energia solar é limpa, renovável e sustentável."
    },
    {
        "pergunta": "5. Qual ação ajuda a economizar água?",
        "opcoes": [
            "Lavar calçada com mangueira",
            "Deixar torneira aberta",
            "Fechar torneira ao escovar os dentes",
            "Tomar banhos longos"
        ],
        "resposta": "Fechar torneira ao escovar os dentes",
        "explicacao": "Essa prática simples pode economizar litros de água por dia."
    },
    {
        "pergunta": "6. O que significa biodiversidade?",
        "opcoes": [
            "Variedade de lixo",
            "Conjunto de espécies vivas",
            "Quantidade de poluição",
            "Tipos de gases poluentes"
        ],
        "resposta": "Conjunto de espécies vivas",
        "explicacao": "Biodiversidade é a variedade de formas de vida em um ecossistema."
    },
    {
        "pergunta": "7. Como o plástico afeta os oceanos?",
        "opcoes": [
            "Ajuda os peixes",
            "Purifica a água",
            "Polui e prejudica os animais marinhos",
            "Aumenta oxigênio na água"
        ],
        "resposta": "Polui e prejudica os animais marinhos",
        "explicacao": "O plástico pode ser ingerido por animais, causando morte e contaminação."
    },
    {
        "pergunta": "8. O que podemos fazer com pilhas usadas?",
        "opcoes": ["Jogar no lixo comum", "Queimar", "Enterrar", "Levar a ponto de coleta"],
        "resposta": "Levar a ponto de coleta",
        "explicacao": "Pilhas contêm metais pesados e devem ser descartadas em locais apropriados."
    },
    {
        "pergunta": "9. Qual destas atitudes NÃO é sustentável?",
        "opcoes": [
            "Reutilizar materiais",
            "Usar sacolas reutilizáveis",
            "Desperdiçar alimentos",
            "Reciclar embalagens"
        ],
        "resposta": "Desperdiçar alimentos",
        "explicacao": "Desperdício de alimentos gera impactos sociais, econômicos e ambientais."
    },
    {
        "pergunta": "10. Por que é importante preservar florestas?",
        "opcoes": [
            "Para aumentar o lixo",
            "Para gerar mais fumaça",
            "Porque ajudam a equilibrar o clima",
            "Para ter mais espaço para lixo"
        ],
        "resposta": "Porque ajudam a equilibrar o clima",
        "explicacao": "Florestas regulam o clima, protegem solos e abrigam biodiversidade."
    }
]

respostas_usuario = []
pontuacao = 0
mostrar_resultado = False

st.write("Responda todas as perguntas e clique no botão abaixo para ver seu resultado.")

with st.form("quiz_form"):
    for i, q in enumerate(quiz):
        resposta = st.radio(q["pergunta"], q["opcoes"], index=None, key=f"q{i}")
        respostas_usuario.append(resposta)

    submit = st.form_submit_button("Ver resultado")

if submit:
    st.markdown("---")
    for i, q in enumerate(quiz):
        resposta = respostas_usuario[i]
        correta = q["resposta"]
        if resposta == correta:
            pontuacao += 1
            st.success(f"✅ {q['pergunta']}\n\nVocê acertou! 🎉\n\n🟢 Explicação: {q['explicacao']}")
        elif resposta is None:
            st.warning(f"⚠️ {q['pergunta']}\n\nVocê não respondeu essa pergunta.")
        else:
            st.error(f"❌ {q['pergunta']}\n\nResposta correta: **{correta}**\n\n🔵 Explicação: {q['explicacao']}")

    st.markdown("## 🧾 Resultado final:")

    st.info(f"Você acertou **{pontuacao} de {len(quiz)}** perguntas.")

    if pontuacao == len(quiz):
        st.balloons()
        st.success("Parabéns! Você acertou tudo! 🌎💚")
    elif pontuacao >= 7:
        st.balloons()
        st.success("Muito bem! Você tem bom conhecimento ambiental!")
    else:
        st.warning("Você pode melhorar! Continue estudando sobre o meio ambiente. 💡")

