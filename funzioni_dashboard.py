from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st


# Palette diversa dal progetto originale rosa/viola.
BLU_NOTTE = "#0B132B"
PETROLIO = "#147D82"
PETROLIO_CHIARO = "#63B7AF"
ARANCIO = "#F4A261"
CORALLO = "#E76F51"
AZZURRO = "#4EA8DE"
SFONDO_CHIARO = "#F4F7FB"


def configura_stile() -> None:
    """Imposta lo stile generale dell'applicazione e dei grafici."""
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        font_scale=1.05,
    )

    st.markdown(
        f"""
        <style>
        /* Sfondo generale */
        [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(circle at top right, rgba(78, 168, 222, 0.13), transparent 28%),
                linear-gradient(180deg, #F8FAFD 0%, {SFONDO_CHIARO} 100%);
        }}

        [data-testid="stHeader"] {{
            background: rgba(248, 250, 253, 0.82);
        }}

        .block-container {{
            max-width: 1450px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }}


        /* Testi principali: evita testo bianco sugli sfondi chiari */
        [data-testid="stMain"] {{
            color: #0B132B !important;
        }}

        [data-testid="stMain"] p,
        [data-testid="stMain"] label,
        [data-testid="stMain"] li,
        [data-testid="stMain"] h1,
        [data-testid="stMain"] h2,
        [data-testid="stMain"] h3,
        [data-testid="stMain"] h4,
        [data-testid="stMain"] h5,
        [data-testid="stMain"] h6 {{
            color: #0B132B !important;
        }}

        [data-testid="stMain"] [data-testid="stCaptionContainer"],
        [data-testid="stMain"] [data-testid="stCaptionContainer"] p {{
            color: #607085 !important;
        }}

        /* La testata mantiene il testo chiaro */
        [data-testid="stMain"] .hero,
        [data-testid="stMain"] .hero h1 {{
            color: white !important;
        }}

        [data-testid="stMain"] .hero p {{
            color: rgba(255, 255, 255, 0.84) !important;
        }}

        [data-testid="stMain"] .hero-badge {{
            color: #F4A261 !important;
        }}

        /* Tab ed expander */
        button[data-baseweb="tab"] {{
            color: #0B132B !important;
        }}

        button[data-baseweb="tab"][aria-selected="true"] {{
            color: #147D82 !important;
        }}

        [data-testid="stExpander"] summary,
        [data-testid="stExpander"] summary p {{
            color: #0B132B !important;
        }}

        /* Campi dell'area principale */
        [data-testid="stMain"] input,
        [data-testid="stMain"] textarea,
        [data-testid="stMain"] [role="combobox"] {{
            color: #0B132B !important;
            -webkit-text-fill-color: #0B132B !important;
        }}

        /* Hero iniziale */
        .hero {{
            padding: 2rem 2.2rem;
            margin-bottom: 1.4rem;
            border-radius: 24px;
            color: white;
            background:
                linear-gradient(120deg, {BLU_NOTTE} 0%, #123A4A 55%, {PETROLIO} 100%);
            box-shadow: 0 18px 45px rgba(11, 19, 43, 0.18);
            position: relative;
            overflow: hidden;
        }}

        .hero::after {{
            content: "";
            position: absolute;
            width: 230px;
            height: 230px;
            border-radius: 50%;
            right: -70px;
            top: -95px;
            background: rgba(244, 162, 97, 0.22);
        }}

        .hero h1 {{
            color: white;
            margin: 0.45rem 0 0.45rem 0;
            font-size: clamp(2rem, 4vw, 3.25rem);
            line-height: 1.05;
        }}

        .hero p {{
            color: rgba(255, 255, 255, 0.84);
            max-width: 800px;
            margin: 0;
            font-size: 1.03rem;
        }}

        .hero-badge {{
            display: inline-block;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.22);
            color: {ARANCIO};
            font-size: 0.75rem;
            letter-spacing: 0.13rem;
            font-weight: 800;
        }}

        /* Titoli delle sezioni */
        .section-heading {{
            margin: 1.25rem 0 0.75rem 0;
            padding-left: 0.85rem;
            border-left: 5px solid {CORALLO};
            color: {BLU_NOTTE};
            font-size: 1.28rem;
            font-weight: 800;
        }}

        /* Sidebar */
        [data-testid="stSidebar"] {{
            background:
                linear-gradient(180deg, {BLU_NOTTE} 0%, #102D3C 62%, {PETROLIO} 145%);
            border-right: 0;
        }}

        /* Testi della sidebar, esclusi i campi bianchi */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] h4,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label {{
            color: #F7FAFC !important;
        }}

        [data-testid="stSidebar"] [data-baseweb="select"] > div,
        [data-testid="stSidebar"] [data-baseweb="input"] > div {{
            background-color: rgba(255, 255, 255, 0.96);
            border-color: rgba(99, 183, 175, 0.7);
            border-radius: 11px;
        }}

        [data-testid="stSidebar"] [data-baseweb="select"] * {{
            color: {BLU_NOTTE};
        }}


        [data-testid="stSidebar"] [data-baseweb="select"] *,
        [data-testid="stSidebar"] [data-baseweb="input"] *,
        [data-testid="stSidebar"] input,
        [data-testid="stSidebar"] [role="combobox"] {{
            color: #0B132B !important;
            -webkit-text-fill-color: #0B132B !important;
        }}

        /* Menu delle selectbox */
        [data-baseweb="popover"],
        [data-baseweb="popover"] *,
        [role="listbox"],
        [role="listbox"] * {{
            color: #0B132B !important;
        }}

        [role="option"] {{
            background-color: #FFFFFF !important;
            color: #0B132B !important;
        }}

        [role="option"]:hover,
        [role="option"][aria-selected="true"] {{
            background-color: #EAF5F4 !important;
            color: #0B132B !important;
        }}

        [data-testid="stSidebar"] hr {{
            border-color: rgba(255,255,255,0.16);
        }}

        .sidebar-brand {{
            margin: 0.3rem 0 1rem 0;
            padding: 1rem;
            border: 1px solid rgba(255,255,255,0.14);
            border-radius: 16px;
            background: rgba(255,255,255,0.07);
        }}

        .sidebar-brand strong {{
            display: block;
            color: {ARANCIO};
            font-size: 1.15rem;
            margin-bottom: 0.25rem;
        }}

        .sidebar-brand span {{
            color: rgba(255,255,255,0.72);
            font-size: 0.84rem;
        }}

        /* Card KPI */
        .kpi-card {{
            min-height: 126px;
            padding: 1.1rem 1.15rem;
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(20, 125, 130, 0.13);
            box-shadow: 0 10px 28px rgba(11, 19, 43, 0.07);
            position: relative;
            overflow: hidden;
        }}

        .kpi-card::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, {PETROLIO}, {ARANCIO});
        }}

        .kpi-label {{
            color: #607085;
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.045rem;
        }}

        .kpi-value {{
            color: {BLU_NOTTE};
            margin-top: 0.45rem;
            font-size: 1.75rem;
            line-height: 1;
            font-weight: 850;
        }}

        .kpi-note {{
            margin-top: 0.55rem;
            color: #738196;
            font-size: 0.78rem;
        }}

        /* Tab principali */
        button[data-baseweb="tab"] {{
            border-radius: 12px 12px 0 0;
            padding-left: 1.05rem;
            padding-right: 1.05rem;
            font-weight: 700;
        }}

        button[data-baseweb="tab"][aria-selected="true"] {{
            color: {PETROLIO};
            background: rgba(20, 125, 130, 0.09);
        }}

        [data-testid="stTabs"] [data-baseweb="tab-highlight"] {{
            background-color: {CORALLO};
        }}

        /* Contenitori e tabelle */
        [data-testid="stExpander"],
        [data-testid="stDataFrame"] {{
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid rgba(11, 19, 43, 0.09);
            box-shadow: 0 8px 22px rgba(11, 19, 43, 0.045);
        }}

        [data-testid="stDataFrame"] [role="columnheader"] {{
            background-color: {PETROLIO} !important;
            color: white !important;
            font-weight: 800 !important;
        }}

        [data-testid="stPlotlyChart"],
        [data-testid="stImage"] {{
            border-radius: 16px;
        }}

        .chart-title {{
            color: {BLU_NOTTE};
            font-weight: 800;
            font-size: 1rem;
            margin-bottom: 0.35rem;
        }}


        .explanation-box {{
            margin-top: 0.8rem;
            margin-bottom: 1rem;
            padding: 0.95rem 1.05rem;
            border-radius: 14px;
            background: linear-gradient(135deg, #EAF5F4 0%, #F7FBFC 100%);
            border: 1px solid rgba(20, 125, 130, 0.18);
            box-shadow: 0 5px 15px rgba(11, 19, 43, 0.04);
            color: #0B132B;
            font-size: 0.92rem;
            line-height: 1.55;
        }}

        .explanation-box strong {{
            color: {PETROLIO};
        }}

        .explanation-box ul {{
            margin-top: 0.45rem;
            margin-bottom: 0.1rem;
            padding-left: 1.25rem;
        }}

        .explanation-box li {{
            margin-bottom: 0.3rem;
        }}

        .formula-card {{
            border-left: 4px solid {PETROLIO};
            background: white;
            border-radius: 12px;
            padding: 0.8rem 1rem;
            margin-bottom: 0.7rem;
            box-shadow: 0 5px 16px rgba(11, 19, 43, 0.045);
        }}

        .footer-note {{
            margin-top: 2rem;
            text-align: center;
            color: #7A8799;
            font-size: 0.82rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def mostra_sidebar(df: pd.DataFrame) -> tuple[str, str, str, int]:
    """Mostra i controlli nella sidebar e restituisce le scelte dell'utente."""
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if not numeric_cols:
        st.error("Il file non contiene colonne numeriche da analizzare.")
        st.stop()

    indice_y = 1 if len(numeric_cols) > 1 else 0

    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
                <strong>📊 StatLab</strong>
                <span>Configura qui le variabili della tua analisi.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Analisi singola")
        col = st.selectbox(
            "Variabile da analizzare",
            numeric_cols,
        )

        st.divider()
        st.markdown("### Confronto tra variabili")
        col_x = st.selectbox(
            "Variabile asse X",
            numeric_cols,
            index=0,
        )
        col_y = st.selectbox(
            "Variabile asse Y",
            numeric_cols,
            index=indice_y,
        )

        st.divider()
        st.markdown("### Raggruppamento")
        num_bins = st.slider(
            "Numero di classi",
            min_value=3,
            max_value=12,
            value=6,
            help="Determina il numero di intervalli usati nelle frequenze e negli istogrammi.",
        )

        st.info(
            f"Analisi attiva: **{col}**\n\n"
            f"Confronto: **{col_x}** → **{col_y}**"
        )

    return col, col_x, col_y, num_bins


def scarto_medio_assoluto(serie: pd.Series) -> float:
    """Calcola lo scarto medio assoluto rispetto alla media."""
    serie = serie.dropna()
    if serie.empty:
        return float("nan")
    return float((serie - serie.mean()).abs().mean())


def interpreta_coefficiente_variazione(coefficiente: float) -> str:
    if pd.isna(coefficiente):
        return "Non calcolabile: la media è uguale o molto vicina a zero"
    if abs(coefficiente) <= 0.2:
        return "Bassa variabilità relativa"
    if abs(coefficiente) <= 0.5:
        return "Variabilità relativa moderata"
    return "Alta variabilità relativa"


def interpreta_asimmetria(skewness: float) -> str:
    if pd.isna(skewness):
        return "Asimmetria non calcolabile"
    if np.isclose(skewness, 0, atol=0.05):
        return "Distribuzione approssimativamente simmetrica"
    if skewness > 0:
        return "Asimmetria positiva: coda più lunga verso destra"
    return "Asimmetria negativa: coda più lunga verso sinistra"


def interpreta_curtosi(curtosi: float) -> str:
    if pd.isna(curtosi):
        return "Curtosi non calcolabile"
    if np.isclose(curtosi, 0, atol=0.05):
        return "Distribuzione normocurtica"
    if curtosi > 0:
        return "Distribuzione leptocurtica: code più pesanti e più valori estremi"
    return "Distribuzione platicurtica: forma più piatta e code più leggere"


def interpreta_correlazione(correlazione: float) -> str:
    if pd.isna(correlazione):
        return "Correlazione non calcolabile"

    valore_assoluto = abs(correlazione)
    if valore_assoluto <= 0.3:
        intensita = "Bassa"
    elif valore_assoluto <= 0.8:
        intensita = "Moderata"
    else:
        intensita = "Alta"

    if correlazione > 0:
        return f"{intensita}, diretta e positiva"
    if correlazione < 0:
        return f"{intensita}, inversa e negativa"
    return "Nulla"


def calcola_statistiche(
    df: pd.DataFrame,
    col: str,
    col_x: str,
    col_y: str,
) -> dict[str, Any]:
    """Calcola esclusivamente gli indici richiesti dalla traccia."""
    serie = df[col].dropna()

    if serie.empty:
        st.error(f"La colonna {col} non contiene valori numerici validi.")
        st.stop()

    coppie = pd.DataFrame({"x": df[col_x], "y": df[col_y]}).dropna()

    media = serie.mean()
    mediana = serie.median()
    moda = serie.mode().tolist()
    deviazione_standard = serie.std()
    varianza = serie.var()
    ampiezza = serie.max() - serie.min()

    coefficiente_variazione = (
        deviazione_standard / media
        if pd.notna(media) and not np.isclose(media, 0)
        else float("nan")
    )

    skewness = serie.skew()
    curtosi = serie.kurt()
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3 - q1

    correlazione = (
        coppie["x"].corr(coppie["y"])
        if len(coppie) >= 2
        else float("nan")
    )

    return {
        "col": col,
        "col_x": col_x,
        "col_y": col_y,
        "numero_osservazioni": int(serie.count()),
        "media": media,
        "mediana": mediana,
        "moda": moda,
        "deviazione_standard": deviazione_standard,
        "varianza": varianza,
        "scarto_medio_assoluto": scarto_medio_assoluto(serie),
        "ampiezza": ampiezza,
        "coefficiente_variazione": coefficiente_variazione,
        "interpretazione_cv": interpreta_coefficiente_variazione(
            coefficiente_variazione
        ),
        "skewness": skewness,
        "interpretazione_skewness": interpreta_asimmetria(skewness),
        "curtosi": curtosi,
        "interpretazione_curtosi": interpreta_curtosi(curtosi),
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "correlazione": correlazione,
        "interpretazione_correlazione": interpreta_correlazione(correlazione),
    }

def _formatta_numero(valore: Any, cifre: int = 3) -> str:
    if pd.isna(valore):
        return "N/D"
    return f"{valore:.{cifre}f}"


def mostra_kpi_cards(statistiche: dict[str, Any]) -> None:
    """Mostra quattro indicatori principali e spiega come interpretarli."""
    correlazione = statistiche["correlazione"]
    cards = [
        (
            "Media",
            _formatta_numero(statistiche["media"]),
            f"Valore medio di {statistiche['col']}",
        ),
        (
            "Mediana",
            _formatta_numero(statistiche["mediana"]),
            f"Valore centrale su {statistiche['numero_osservazioni']} osservazioni",
        ),
        (
            "Deviazione standard",
            _formatta_numero(statistiche["deviazione_standard"]),
            "Dispersione dei dati attorno alla media",
        ),
        (
            "Correlazione",
            _formatta_numero(correlazione),
            statistiche["interpretazione_correlazione"],
        ),
    ]

    colonne = st.columns(4)
    for colonna, (titolo, valore, nota) in zip(colonne, cards):
        with colonna:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-label">{titolo}</div>
                    <div class="kpi-value">{valore}</div>
                    <div class="kpi-note">{nota}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    _riquadro_spiegazione(
        "Come leggere le card riepilogative",
        """
        <ul>
            <li><b>Media:</b> rappresenta il valore medio della variabile selezionata.</li>
            <li><b>Mediana:</b> è il valore centrale dei dati ordinati ed è meno influenzata dagli outlier.</li>
            <li><b>Deviazione standard:</b> indica quanto i valori sono dispersi attorno alla media.</li>
            <li><b>Correlazione:</b> misura intensità e direzione della relazione lineare tra X e Y.</li>
        </ul>
        Le card non introducono nuovi calcoli: riassumono gli indicatori più importanti
        per permettere una lettura immediata dell'analisi.
        """,
    )

def crea_tabella_frequenze(
    df: pd.DataFrame,
    col: str,
    num_bins: int,
) -> pd.DataFrame:
    """Crea la tabella delle frequenze assolute, relative e cumulative."""
    intervalli = pd.cut(df[col].dropna(), bins=num_bins)
    frequenza_assoluta = intervalli.value_counts().sort_index()
    frequenza_relativa = frequenza_assoluta / frequenza_assoluta.sum()

    tabella = pd.DataFrame(
        {
            "Classe": frequenza_assoluta.index.astype(str),
            "Frequenza assoluta": frequenza_assoluta.values,
            "Frequenza relativa": frequenza_relativa.values,
            "Frequenza assoluta cumulativa": frequenza_assoluta.cumsum().values,
            "Frequenza relativa cumulativa": frequenza_relativa.cumsum().values,
        }
    )
    return tabella


def _stile_tabella(
    tabella: pd.DataFrame,
    formati: dict[str, str] | None = None,
) -> Any:
    """Applica intestazione petrolio e righe alternate alle tabelle."""
    styler = tabella.style.set_table_styles(
        [
            {
                "selector": "thead th",
                "props": [
                    ("background-color", PETROLIO),
                    ("color", "white"),
                    ("font-weight", "800"),
                    ("border", "0"),
                    ("padding", "11px"),
                    ("text-align", "center"),
                ],
            },
            {
                "selector": "tbody td",
                "props": [
                    ("border-bottom", "1px solid #DCE7EC"),
                    ("padding", "9px"),
                    ("color", BLU_NOTTE),
                ],
            },
        ]
    )

    styler = styler.apply(
        lambda riga: [
            "background-color: #FFFFFF" if riga.name % 2 == 0
            else "background-color: #EAF5F4"
        ] * len(riga),
        axis=1,
    )

    if formati:
        styler = styler.format(formati)

    return styler


def mostra_tabella_frequenze(
    df: pd.DataFrame,
    col: str,
    num_bins: int,
) -> None:
    """Visualizza la tabella delle frequenze con intestazioni colorate."""
    st.markdown("#### Frequenze per classe")
    st.caption(
        f"La variabile **{col}** è stata suddivisa in **{num_bins} classi**."
    )

    tabella = crea_tabella_frequenze(df, col, num_bins)
    tabella_stilizzata = _stile_tabella(
        tabella,
        {
            "Frequenza relativa": "{:.3f}",
            "Frequenza relativa cumulativa": "{:.3f}",
        },
    )
    st.dataframe(
        tabella_stilizzata,
        use_container_width=True,
        hide_index=True,
        height=min(465, 82 + len(tabella) * 36),
    )

    _riquadro_spiegazione(
        "Interpretazione della tabella delle frequenze",
        """
        La <b>frequenza assoluta</b> conta quante osservazioni appartengono a ogni classe.
        La <b>frequenza relativa</b> esprime lo stesso conteggio come proporzione del totale.
        Le frequenze <b>cumulative</b> sommano progressivamente i valori fino alla classe considerata.
        L'ultima frequenza relativa cumulativa deve essere uguale a 1, cioè al 100%.
        """,
    )


# -----------------------------------------------------------------------------
# GRAFICI
# -----------------------------------------------------------------------------


def _rifinisci_assi(ax: plt.Axes) -> None:
    """Uniforma lo stile degli assi dei grafici."""
    ax.set_facecolor("#FBFCFE")
    ax.grid(axis="y", alpha=0.22, linestyle="--")
    ax.grid(axis="x", alpha=0.08)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#CBD5E1")
    ax.spines["bottom"].set_color("#CBD5E1")


def mostra_istogrammi(df: pd.DataFrame, col: str, num_bins: int) -> None:
    """Mostra gli istogrammi in tab, evitando quattro grafici tutti in fila."""
    serie = df[col].dropna()
    st.markdown("### Frequenze e andamento cumulativo")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Assoluta",
            "Relativa",
            "Assoluta cumulativa",
            "Relativa cumulativa",
        ]
    )

    configurazioni = [
        (tab1, None, False, "Numero di osservazioni", "Frequenza assoluta"),
        (tab2, "probability", False, "Proporzione", "Frequenza relativa"),
        (tab3, None, True, "Osservazioni cumulate", "Frequenza assoluta cumulativa"),
        (tab4, "probability", True, "Proporzione cumulata", "Frequenza relativa cumulativa"),
    ]

    for contenitore, statistica, cumulativa, etichetta_y, titolo in configurazioni:
        with contenitore:
            fig, ax = plt.subplots(figsize=(10.5, 4.2))

            # I grafici normali sono composti da barre, mentre quelli cumulativi
            # vengono disegnati come linee a gradini. I due tipi non accettano
            # esattamente gli stessi parametri grafici.
            parametri_istogramma = {
                "data": serie,
                "bins": num_bins,
                "stat": statistica or "count",
                "cumulative": cumulativa,
                "color": PETROLIO if not cumulativa else CORALLO,
                "ax": ax,
            }

            if cumulativa:
                parametri_istogramma.update(
                    {
                        "element": "step",
                        "fill": False,
                        "linewidth": 2.4,
                        "alpha": 0.95,
                    }
                )
            else:
                parametri_istogramma.update(
                    {
                        "element": "bars",
                        "fill": True,
                        "edgecolor": "white",
                        "linewidth": 1.2,
                        "alpha": 0.88,
                    }
                )

            sns.histplot(**parametri_istogramma)

            ax.set_title(titolo, loc="left", fontsize=13, fontweight="bold", color=BLU_NOTTE)
            ax.set_xlabel(col)
            ax.set_ylabel(etichetta_y)
            _rifinisci_assi(ax)
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)


def mostra_boxplot(df: pd.DataFrame, col: str) -> None:
    """Mostra il box plot richiesto dalla traccia."""
    serie = df[col].dropna()

    st.markdown("### Box plot")
    fig, ax = plt.subplots(figsize=(10.5, 4.2))

    sns.boxplot(
        x=serie,
        color=PETROLIO_CHIARO,
        width=0.42,
        showmeans=True,
        meanprops={
            "marker": "D",
            "markerfacecolor": ARANCIO,
            "markeredgecolor": BLU_NOTTE,
            "markersize": 7,
        },
        flierprops={
            "marker": "o",
            "markerfacecolor": CORALLO,
            "markeredgecolor": "white",
            "markersize": 6,
            "alpha": 0.85,
        },
        ax=ax,
    )

    ax.set_xlabel(col)
    ax.set_ylabel("")
    ax.set_title(
        f"Distribuzione di {col}",
        loc="left",
        fontsize=13,
        fontweight="bold",
        color=BLU_NOTTE,
    )
    _rifinisci_assi(ax)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    _riquadro_spiegazione(
        "Come leggere il box plot",
        """
        La scatola è compresa tra il primo quartile Q1 e il terzo quartile Q3
        e contiene il 50% centrale delle osservazioni. La linea interna indica
        la mediana, mentre il rombo rappresenta la media. Gli eventuali punti
        isolati oltre i baffi rappresentano valori particolarmente lontani
        dal resto della distribuzione.
        """,
    )

def mostra_grafico_donut(df: pd.DataFrame, col: str, num_bins: int) -> None:
    """Mostra un grafico a ciambella della composizione per classi."""
    st.markdown("### Composizione percentuale delle classi")
    classi = pd.cut(df[col].dropna(), bins=num_bins)
    conteggi = classi.value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    colori = sns.color_palette(
        [PETROLIO, AZZURRO, ARANCIO, CORALLO, PETROLIO_CHIARO],
        n_colors=len(conteggi),
    )
    wedges, _, percentuali = ax.pie(
        conteggi,
        labels=None,
        autopct=lambda p: f"{p:.1f}%" if p >= 4 else "",
        startangle=90,
        colors=colori,
        pctdistance=0.79,
        wedgeprops={"width": 0.38, "edgecolor": "white", "linewidth": 2},
    )
    ax.text(
        0,
        0.06,
        f"{int(conteggi.sum())}",
        ha="center",
        va="center",
        fontsize=24,
        fontweight="bold",
        color=BLU_NOTTE,
    )
    ax.text(
        0,
        -0.12,
        "osservazioni",
        ha="center",
        va="center",
        fontsize=10,
        color="#6B7280",
    )
    ax.legend(
        wedges,
        conteggi.index.astype(str),
        title="Intervalli",
        loc="center left",
        bbox_to_anchor=(1.0, 0.5),
        frameon=False,
        fontsize=9,
    )
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


def mostra_scatterplot(
    df: pd.DataFrame,
    col_x: str,
    col_y: str,
) -> None:
    """Mostra il diagramma a dispersione richiesto dalla traccia."""
    dati = pd.DataFrame({"x": df[col_x], "y": df[col_y]}).dropna()

    st.markdown("### Diagramma a dispersione")

    if dati.empty:
        st.warning("Non ci sono coppie di valori valide per costruire il grafico.")
        return

    fig, ax = plt.subplots(figsize=(10.5, 5.2))
    ax.scatter(
        dati["x"],
        dati["y"],
        s=52,
        color=AZZURRO,
        edgecolor="white",
        linewidth=0.7,
        alpha=0.72,
    )
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    ax.set_title(
        f"{col_y} rispetto a {col_x}",
        loc="left",
        fontsize=13,
        fontweight="bold",
        color=BLU_NOTTE,
    )
    _rifinisci_assi(ax)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    _riquadro_spiegazione(
        "Come leggere il diagramma a dispersione",
        f"""
        Ogni punto rappresenta una riga del dataset con coordinate
        <b>({col_x}, {col_y})</b>. Una disposizione crescente suggerisce
        una relazione positiva; una disposizione decrescente suggerisce
        una relazione negativa. Se i punti non mostrano una direzione evidente,
        la relazione lineare può essere debole o nulla.
        """,
    )

def _riquadro_spiegazione(titolo: str, contenuto_html: str) -> None:
    """Mostra un riquadro descrittivo coerente con lo stile della dashboard."""
    st.markdown(
        f"""
        <div class="explanation-box">
            <strong>{titolo}</strong><br>
            {contenuto_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _formula_card(titolo: str, descrizione: str) -> None:
    st.markdown(
        f"""
        <div class="formula-card">
            <strong>{titolo}</strong><br>
            <span style="color:#64748B; font-size:0.9rem;">{descrizione}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def mostra_tab_indici_posizione(statistiche: dict[str, Any]) -> None:
    st.markdown("#### Centro della distribuzione")
    col1, col2, col3 = st.columns(3)
    col1.metric("Media", _formatta_numero(statistiche["media"], 4))
    col2.metric("Mediana", _formatta_numero(statistiche["mediana"], 4))
    col3.metric("Moda", str(statistiche["moda"]))

    _formula_card(
        "Media campionaria",
        "Somma dei valori divisa per il numero di osservazioni; è sensibile ai valori estremi.",
    )
    st.latex(
        rf"\overline{{x}} = \frac{{1}}{{n}} \sum_{{i=1}}^{{n}} x_i "
        rf"= {statistiche['media']:.4f}"
    )

    _formula_card(
        "Mediana campionaria",
        f"Valore centrale dei dati ordinati = {statistiche['mediana']:.4f}. "
        "È più robusta della media in presenza di outlier.",
    )

    _formula_card(
        "Moda campionaria",
        f"Valore o valori che compaiono più frequentemente = {statistiche['moda']}.",
    )

    _riquadro_spiegazione(
        "Confronto tra media, mediana e moda",
        """
        Se media e mediana sono molto vicine, la distribuzione può essere abbastanza
        simmetrica. Una forte differenza tra i due valori può segnalare asimmetria
        oppure la presenza di valori estremi. La moda evidenzia invece il valore più comune.
        """,
    )

def mostra_tab_indici_variabilita(statistiche: dict[str, Any]) -> None:
    st.markdown("#### Dispersione dei dati")
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Deviazione standard",
        _formatta_numero(statistiche["deviazione_standard"], 4),
    )
    col2.metric("Varianza", _formatta_numero(statistiche["varianza"], 4))
    col3.metric("Ampiezza", _formatta_numero(statistiche["ampiezza"], 4))

    _formula_card(
        "Deviazione standard campionaria",
        "Misura la dispersione nella stessa unità di misura della variabile.",
    )
    st.latex(
        rf"s = \sqrt{{\frac{{1}}{{n-1}} \sum_{{i=1}}^{{n}} "
        rf"(x_i - \overline{{x}})^2}} = {statistiche['deviazione_standard']:.4f}"
    )

    _formula_card(
        "Varianza campionaria",
        "È il quadrato della deviazione standard e misura la dispersione tramite gli scarti quadratici.",
    )
    st.latex(rf"s^2 = {statistiche['varianza']:.4f}")

    _formula_card(
        "Scarto medio assoluto",
        "Distanza media assoluta dei valori dalla media.",
    )
    st.latex(
        rf"\frac{{1}}{{n}} \sum_{{i=1}}^{{n}} |x_i - \overline{{x}}| "
        rf"= {statistiche['scarto_medio_assoluto']:.4f}"
    )

    _formula_card(
        "Ampiezza del campo di variazione",
        "Differenza tra il valore massimo e il valore minimo; è molto sensibile agli outlier.",
    )
    st.latex(rf"\max(x)-\min(x) = {statistiche['ampiezza']:.4f}")

    coefficiente = statistiche["coefficiente_variazione"]
    _formula_card(
        "Coefficiente di variazione",
        statistiche["interpretazione_cv"],
    )
    if pd.notna(coefficiente):
        st.latex(rf"CV = \frac{{s}}{{\overline{{x}}}} = {coefficiente:.4f}")
    else:
        st.warning("Il coefficiente di variazione non è calcolabile.")

    _riquadro_spiegazione(
        "Interpretazione della variabilità",
        """
        Valori elevati di varianza, deviazione standard e scarto medio indicano
        osservazioni più disperse. Il coefficiente di variazione mette la dispersione
        in rapporto con la media e permette confronti tra variabili con scale differenti.
        """,
    )

def mostra_tab_indici_forma(statistiche: dict[str, Any]) -> None:
    st.markdown("#### Forma della distribuzione")
    col1, col2 = st.columns(2)
    col1.metric("Skewness", _formatta_numero(statistiche["skewness"], 4))
    col2.metric("Curtosi", _formatta_numero(statistiche["curtosi"], 4))

    _formula_card(
        "Indice di asimmetria",
        statistiche["interpretazione_skewness"],
    )
    _formula_card(
        "Indice di curtosi",
        statistiche["interpretazione_curtosi"],
    )

    _riquadro_spiegazione(
        "Come interpretare gli indici di forma",
        """
        La <b>skewness</b> indica verso quale lato si allunga la coda della distribuzione:
        positiva verso destra, negativa verso sinistra. La <b>curtosi</b> descrive
        soprattutto il peso delle code e la presenza di valori estremi rispetto
        a una distribuzione normale.
        """,
    )

def mostra_tab_quartili(statistiche: dict[str, Any]) -> None:
    """Mostra esclusivamente quartili e scarto interquartile."""
    st.markdown("#### Quartili e scarto interquartile")

    col1, col2, col3 = st.columns(3)
    col1.metric("Primo quartile Q1", _formatta_numero(statistiche["q1"], 4))
    col2.metric("Terzo quartile Q3", _formatta_numero(statistiche["q3"], 4))
    col3.metric("IQR", _formatta_numero(statistiche["iqr"], 4))

    _formula_card(
        "Primo quartile Q1",
        "È il valore sotto il quale si trova circa il 25% delle osservazioni.",
    )
    st.latex(rf"Q_1 = {statistiche['q1']:.4f}")

    _formula_card(
        "Terzo quartile Q3",
        "È il valore sotto il quale si trova circa il 75% delle osservazioni.",
    )
    st.latex(rf"Q_3 = {statistiche['q3']:.4f}")

    _formula_card(
        "Scarto interquartile",
        "Misura l'ampiezza del 50% centrale della distribuzione.",
    )
    st.latex(
        rf"IQR = Q_3-Q_1 = {statistiche['q3']:.4f}-"
        rf"{statistiche['q1']:.4f} = {statistiche['iqr']:.4f}"
    )

    _riquadro_spiegazione(
        "Interpretazione dei quartili",
        """
        Tra Q1 e Q3 si trova il 50% centrale dei dati. Un IQR piccolo indica
        che questa parte della distribuzione è concentrata; un IQR più grande
        indica invece una maggiore dispersione centrale. Gli stessi valori
        sono rappresentati graficamente nel box plot.
        """,
    )

def mostra_tab_dati_bivariati(statistiche: dict[str, Any]) -> None:
    st.markdown("#### Relazione tra le variabili")
    correlazione = statistiche["correlazione"]
    st.metric("Coefficiente di correlazione", _formatta_numero(correlazione, 4))
    _formula_card(
        "Interpretazione",
        statistiche["interpretazione_correlazione"],
    )
    if pd.notna(correlazione):
        st.latex(rf"r = {correlazione:.4f}")

    _riquadro_spiegazione(
        "Come leggere il coefficiente di correlazione",
        """
        Il coefficiente r varia tra −1 e +1. Il segno indica la direzione della
        relazione, mentre il valore assoluto ne indica l'intensità.
        Un valore vicino a zero segnala una relazione lineare debole.
        La correlazione non implica necessariamente causalità.
        """,
    )

def mostra_tab_statistiche(statistiche: dict[str, Any]) -> None:
    """Crea i tab e richiama una funzione dedicata per ciascun gruppo."""
    st.markdown("#### Dettaglio dei calcoli")
    st.caption(
        "Ogni scheda raccoglie gli indici appartenenti alla stessa area statistica."
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📍 Posizione",
            "↔️ Variabilità",
            "〰️ Forma",
            "📐 Quartili",
            "🔗 Bivariati",
        ]
    )

    with tab1:
        mostra_tab_indici_posizione(statistiche)
    with tab2:
        mostra_tab_indici_variabilita(statistiche)
    with tab3:
        mostra_tab_indici_forma(statistiche)
    with tab4:
        mostra_tab_quartili(statistiche)
    with tab5:
        mostra_tab_dati_bivariati(statistiche)


def mostra_tabella_riassuntiva(statistiche: dict[str, Any]) -> None:
    """Visualizza la tabella finale con intestazione colorata e categorie."""
    coefficiente_cv = statistiche["coefficiente_variazione"]

    descrittivi = pd.DataFrame(
        {
            "Categoria": [
                "Posizione",
                "Posizione",
                "Posizione",
                "Variabilità",
                "Variabilità",
                "Variabilità",
                "Variabilità",
                "Variabilità",
                "Forma",
                "Forma",
                "Quartili",
                "Quartili",
                "Quartili",
            ],
            "Indice": [
                "Media",
                "Mediana",
                "Moda",
                "Deviazione standard",
                "Varianza",
                "Scarto medio assoluto",
                "Ampiezza del campo",
                "Coefficiente di variazione",
                "Asimmetria (skewness)",
                "Curtosi",
                "Q1",
                "Q3",
                "IQR",
            ],
            "Valore": [
                _formatta_numero(statistiche["media"], 4),
                _formatta_numero(statistiche["mediana"], 4),
                str(statistiche["moda"]),
                _formatta_numero(statistiche["deviazione_standard"], 4),
                _formatta_numero(statistiche["varianza"], 4),
                _formatta_numero(statistiche["scarto_medio_assoluto"], 4),
                _formatta_numero(statistiche["ampiezza"], 4),
                _formatta_numero(coefficiente_cv, 4),
                _formatta_numero(statistiche["skewness"], 4),
                _formatta_numero(statistiche["curtosi"], 4),
                _formatta_numero(statistiche["q1"], 4),
                _formatta_numero(statistiche["q3"], 4),
                _formatta_numero(statistiche["iqr"], 4),
            ],
        }
    )

    st.markdown("#### Tutti gli indici in un’unica tabella")
    st.caption(f"Riepilogo calcolato sulla variabile **{statistiche['col']}**.")
    st.dataframe(
        _stile_tabella(descrittivi),
        use_container_width=True,
        hide_index=True,
        height=500,
    )


# Funzione mantenuta per compatibilità con eventuali vecchie chiamate.
def mostra_sezione_grafici(
    df: pd.DataFrame,
    col: str,
    col_x: str,
    col_y: str,
    num_bins: int,
) -> None:
    """Mostra soltanto i grafici coerenti con la traccia del progetto."""
    mostra_istogrammi(df, col, num_bins)
    mostra_boxplot(df, col)
    mostra_grafico_donut(df, col, num_bins)
    mostra_scatterplot(df, col_x, col_y)

