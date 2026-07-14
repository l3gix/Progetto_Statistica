import pandas as pd
import streamlit as st

from funzioni_dashboard import (
    calcola_statistiche,
    configura_stile,
    mostra_boxplot,
    mostra_grafico_donut,
    mostra_istogrammi,
    mostra_kpi_cards,
    mostra_scatterplot,
    mostra_sidebar,
    mostra_tab_statistiche,
    mostra_tabella_frequenze,
    mostra_tabella_riassuntiva,
)


# Deve essere la prima istruzione Streamlit della pagina.
st.set_page_config(
    page_title="StatLab - Dashboard statistica",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

configura_stile()

st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">STATLAB DASHBOARD</div>
        <h1>Analisi statistica interattiva</h1>
        <p>
            Esplora il dataset, confronta le variabili e interpreta gli indici
            statistici attraverso una dashboard ordinata e interattiva.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

try:
    # sep=None + engine="python" riconosce automaticamente
    # separatori come virgola, punto e virgola e tabulazione.
    df = pd.read_csv(
        "winequality-white.csv",
        sep=None,
        engine="python",
    )
except FileNotFoundError:
    st.error(
        "Il file winequality-white.csv non è stato trovato. "
        "Inseriscilo nella stessa cartella di app.py."
    )
    st.stop()
except pd.errors.ParserError as errore:
    st.error(f"Errore durante la lettura del file CSV: {errore}")
    st.stop()

st.markdown(
    '<div class="section-heading">1. Dataset e modifica dei dati</div>',
    unsafe_allow_html=True,
)

with st.expander("Apri la tabella per visualizzare o modificare i dati", expanded=False):
    st.caption(
        "Le modifiche effettuate nella tabella vengono applicate immediatamente "
        "a tutti i calcoli e ai grafici."
    )
    edited_df = st.data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic",
        key="editor_dati",
        height=390,
    )

col, col_x, col_y, num_bins = mostra_sidebar(edited_df)

statistiche = calcola_statistiche(
    df=edited_df,
    col=col,
    col_x=col_x,
    col_y=col_y,
)

st.markdown(
    '<div class="section-heading">2. Indicatori principali</div>',
    unsafe_allow_html=True,
)
mostra_kpi_cards(statistiche)

st.markdown(
    '<div class="section-heading">3. Esplorazione dell’analisi</div>',
    unsafe_allow_html=True,
)

pagina_tabelle, pagina_distribuzione, pagina_relazioni, pagina_calcoli = st.tabs(
    [
        "📋 Tabelle",
        "📊 Distribuzione",
        "🔗 Relazioni",
        "🧮 Formule e indici",
    ]
)

with pagina_tabelle:
    tab_frequenze, tab_riepilogo = st.tabs(
        ["Tabella delle frequenze", "Riepilogo statistico"]
    )

    with tab_frequenze:
        mostra_tabella_frequenze(
            df=edited_df,
            col=col,
            num_bins=num_bins,
        )

    with tab_riepilogo:
        mostra_tabella_riassuntiva(statistiche)

with pagina_distribuzione:
    st.markdown(
        "#### Distribuzione della variabile selezionata"
    )
    st.caption(
        f"I grafici di questa sezione analizzano la colonna **{col}**."
    )

    mostra_istogrammi(edited_df, col, num_bins)
    mostra_boxplot(edited_df, col)
    mostra_grafico_donut(edited_df, col, num_bins)

with pagina_relazioni:
    st.markdown("#### Confronto tra due variabili")
    st.caption(
        f"Asse X: **{col_x}** · Asse Y: **{col_y}**"
    )

    mostra_scatterplot(edited_df, col_x, col_y)

with pagina_calcoli:
    mostra_tab_statistiche(statistiche)

st.markdown(
    """
    <div class="footer-note">
        Dashboard realizzata con Streamlit, Pandas, Matplotlib e Seaborn.
    </div>
    """,
    unsafe_allow_html=True,
)
