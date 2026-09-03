import streamlit as st

def render_books():
    st.title("📚 Estruturação de Books de Projeto")
    st.markdown("#### Referência conforme Portaria SUROD nº 12/2025 - ANTT")
    st.markdown("Interface interativa para consulta dos volumes e documentos entregáveis por tipo de projeto rodoviário.")

    # Custom CSS for Books
    st.markdown('''
    <style>
    .sigla-box {
        background-color: #2c3e50;
        color: #ffffff;
        padding: 15px 20px;
        border-radius: 8px;
        font-size: 26px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stExpander {
        border-left: 4px solid #16a085 !important;
    }
    </style>
    ''', unsafe_allow_html=True)

    if 'proj_select' not in st.session_state:
        st.session_state.proj_select = "Selecione o tipo de projeto..."

    def reset_selection():
        st.session_state.proj_select = "Selecione o tipo de projeto..."

    col1, col2 = st.columns([4, 1])
    with col1:
        projetos = {
            "Selecione o tipo de projeto...": {"sigla": "", "vols": {}},
            "Estudo de Viabilidade Técnica, Econômica e Ambiental (EVTEA)": {
                "sigla": "EVT",
                "vols": {
                    "Volume 1 – Relatório do Estudo": ["Termo de Referência", "Estudos socioambientais", "Estudos de traçado", "Estudos de tráfego", "Estudos de soluções tecnológicas", "Estudos de engenharia (obras, serviços e operação)", "Estimativa de custos", "Análise de sensibilidade / multicritério / custo-benefício", "Cronograma físico-financeiro"],
                    "Volume 2 – Memorial Justificativo Descritivo": ["Contextualização da obra", "Dados da obra"],
                    "Volume 3 – Estimativa de Custos": ["Memória de cálculo", "Parâmetros adotados", "Referências utilizadas"]
                }
            },
            "Projeto Funcional (FUN)": {
                "sigla": "FUN",
                "vols": {
                    "Volume 1 – Desenhos Técnicos": ["Projeto geométrico sobre ortofoto ou imagem de satélite", "Planta de situação", "Planta de localização", "Seções tipo", "Seções transversais", "Traçado"],
                    "Volume 2 – Estimativa Paramétrica de Custos": ["Memória de cálculo (quando aplicável)", "Parâmetros e referências adotadas"]
                }
            },
            "Anteprojeto (ANT)": {
                "sigla": "ANT",
                "vols": {
                    "Volume 1 – Relatório de Estudos": ["Memorial descritivo e justificativo", "Estudo de tráfego", "Estudo de sinalização", "Estudo geométrico", "Estudo de pavimentação", "Estudo de drenagem", "Estudo de desapropriação", "Estudo de remoção de interferências", "Estudo de desvio de tráfego"],
                    "Volume 2 – Desenhos Técnicos": ["Projeto geométrico", "Projeto de sinalização", "Projeto de pavimentação"]
                }
            },
            "Projeto Executivo (EXE / EXO)": {
                "sigla": "EXE / EXO",
                "vols": {
                    "Volume 1 – Relatório Técnico": ["Todos os estudos exigidos pelos manuais do DNIT (Topografia, Tráfego, Geotecnia, Hidrologia, Terraplenagem, Pavimentação, Drenagem, Sinalização, Obras complementares, Interferências, Estruturas, Iluminação, Desapropriações, etc)."],
                    "Volume 2 – Projetos e Desenhos": ["Todos os projetos e desenhos exigidos pelos manuais do DNIT."],
                    "Volume 3 – Planejamento da Obra": ["EAP (Estrutura Analítica do Projeto)", "Método construtivo", "Plano de trabalho / plano de ataque", "Dimensionamento de equipes, materiais e equipamentos", "Cronograma físico-financeiro", "Histograma e Eventograma", "Diagrama Tempo-Caminho (obras lineares)", "Licenças ambientais, autorizações e alvarás"]
                }
            },
            "Projeto As Built (ASB)": {
                "sigla": "ASB",
                "vols": {
                    "Volume 1 – Registro da Obra Executada": ["Memorial descritivo demonstrando as alterações", "Relatório fotográfico da execução da obra"],
                    "Volume 2 – Projeto Atualizado": ["Desenhos ajustados da obra executada", "Projeto executivo parcial demonstrando as alterações"]
                }
            }
        }
        
        opcoes = list(projetos.keys())
        selected = st.selectbox("Selecione a fase / tipo do projeto:", opcoes, key="proj_select")
        
    with col2:
        st.write("")
        st.write("")
        st.button("🔄 Limpar Seleção", on_click=reset_selection, use_container_width=True)

    if selected != "Selecione o tipo de projeto...":
        dados = projetos[selected]
        st.markdown(f'<div class="sigla-box">SIGLA DO PROJETO: {dados["sigla"]}</div>', unsafe_allow_html=True)
        st.subheader("📋 Estrutura de Volumes (Books)")
        for vol, items in dados["vols"].items():
            with st.expander(vol, expanded=True):
                for item in items:
                    st.markdown(f"- {item}")
        st.divider()
        st.subheader("📎 Documentos Obrigatórios Transversais")
        st.info(
            "Em TODOS os protocolos, a ANTT determina que devem acompanhar o envio:\n\n"
            "1. **Declaração de veracidade** de informações e documentos\n"
            "2. **Guia de remessa** de documentos\n"
            "3. **Caderno de respostas** (em caso de reapresentações)\n"
            "4. **Check-list** de atendimento aos parâmetros técnicos do PER com indicação da página\n"
            "5. **Justificativa de alterações** do projeto (quando aplicável)\n"
            "6. **Tabela-resumo do orçamento** (para obras não previstas no PER)\n"
            "7. **ART** (Anotação de Responsabilidade Técnica) do engenheiro\n"
            "8. **Declaração de responsabilidade** sobre os serviços, quantitativos e custos"
        )
    else:
        st.info("👈 Selecione um tipo de projeto acima para visualizar os entregáveis detalhados.")

def render_renomeador():
    st.title("⚙️ Configurador de Nomenclatura - Padrão ANTT")
    st.markdown("#### Referência conforme Portaria SUROD nº 12/2025")
    st.markdown("Selecione os campos abaixo para gerar o nome do arquivo codificado.")

    st.markdown('''
    <style>
    .output-box {
        background-color: #2c3e50;
        color: #ffffff;
        padding: 25px;
        border-radius: 8px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    .output-title {
        margin: 0;
        color: #bdc3c7;
        font-family: sans-serif;
        font-size: 16px;
    }
    .output-name {
        margin: 10px 0 0 0;
        font-family: monospace;
        letter-spacing: 1px;
        font-size: 28px;
    }
    .valid { color: #2ecc71; }
    </style>
    ''', unsafe_allow_html=True)

    concessionarias = {
        'Ecovias Minas Goiás (Eco050) - EC5': 'EC5',
        'Ecovias Cerrado (EcoCerrado) - ECC': 'ECC',
    }

    tipos_obra = {
        'Duplicação (DPL)': 'DPL',
        'Drenagem (DRE)': 'DRE',
        'Obras de Artes Correntes (OAC)': 'OAC',
        'Obras de Artes Especiais (OAE)': 'OAE',
        'Passarela (PAS)': 'PAS',
        'Interseção (INT)': 'INT',
        'Melhorias Operacionais (MOP)': 'MOP',
        'Via Marginal (MAR)': 'MAR',
        'Terrapleno (TER)': 'TER',
        'Pavimento (PAV)': 'PAV',
        'Dispositivo em Desnível (DDE)': 'DDE',
        'Dispositivo em Nível (DNI)': 'DNI'
    }

    tipos_projeto = {
        'Projeto Executivo Sem Orçamento (EXE)': 'EXE',
        'Projeto Executivo Com Orçamento (EXO)': 'EXO',
        'Anteprojeto (ANT)': 'ANT',
        'Projeto Funcional (FUN)': 'FUN',
        'As Built (ASB)': 'ASB',
        'Estudo de Viabilidade (EVT)': 'EVT'
    }

    classes_doc = {
        'Desenhos (DE)': 'DE',
        'Relatório Técnico (RT)': 'RT',
        'Planilha (PL)': 'PL',
        'Memorial Descritivo (MD)': 'MD',
        'Memorial de Cálculo (MC)': 'MC',
        'Especificação Técnica (ET)': 'ET',
        'Nota de Servico (NS)': 'NS'
    }

    disciplinas = {
        'Projeto de Drenagem (H2)': 'H2',
        'Projeto Geométrico (F1)': 'F1',
        'Projeto Sinalização e Seg. (J1)': 'J1',
        'Projeto Terraplenagem (G1)': 'G1',
        'Projeto Pavimentação (I2)': 'I2',
        'Projeto Obras Complementares (J2)': 'J2',
        'Projeto Interferências (M1)': 'M1',
        'Projeto Desapropriação (Q1)': 'Q1',
        'Estudos Hidrológicos e Drenagem (H1)': 'H1',
        'Projeto Estrutural e Concreto (L2)': 'L2',
        'Termo de Referência (A1)': 'A1'
    }

    extensoes = ['.dwg', '.pdf', '.xls', '.xlsx', '.doc', '.docx', '.dxf', '.ctb', '.plt']

    col1, col2 = st.columns([1, 1])

    with col1:
        w_conc = st.selectbox("Concessionária:", list(concessionarias.keys()), index=0)
        w_rod = st.text_input("Rodovia/UF:", value="050MG", help="Ex: 050MG")
        w_loc = st.text_input("Localização:", value="084-100", help="Ex: 084-100 ou 507+925")
        w_obra = st.selectbox("Tipo de Obra:", list(tipos_obra.keys()), index=0)
        w_proj = st.selectbox("Tipo Projeto:", list(tipos_projeto.keys()), index=0)

    with col2:
        w_classe = st.selectbox("Classe Doc.:", list(classes_doc.keys()), index=0)
        w_disc = st.selectbox("Disciplina:", list(disciplinas.keys()), index=0)
        w_seq = st.text_input("Sequência:", value="001", help="Ex: 001")
        w_rev = st.text_input("Revisão (R):", value="00", help="Ex: 00, 01")
        w_ext = st.selectbox("Extensão:", extensoes, index=0)

    p_conc = concessionarias[w_conc].strip().upper()[:3]
    p_rod = w_rod.strip().upper().zfill(5)[:5]
    p_loc = w_loc.strip().upper().zfill(7)[:7]
    p_obra = tipos_obra[w_obra]
    p_proj = tipos_projeto[w_proj]
    p_classe = classes_doc[w_classe]
    p_disc = disciplinas[w_disc]
    p_seq = w_seq.strip().zfill(3)[:3] 
    p_rev = w_rev.strip().upper().zfill(2)[:2]
    p_ext = w_ext

    file_name = f"{p_conc}-{p_rod}-{p_loc}-{p_obra}-{p_proj}-{p_classe}-{p_disc}-{p_seq}-R{p_rev}{p_ext}"
    cor_classe = "valid"

    st.markdown(f'''
    <div class="output-box">
        <h4 class="output-title">Nome do Arquivo Gerado:</h4>
        <h2 class="output-name {cor_classe}">{file_name}</h2>
    </div>
    ''', unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Consultor SUROD 12", layout="wide")
    
    st.sidebar.title("Navegação - SUROD")
    st.sidebar.markdown("Escolha a ferramenta desejada:")
    pagina = st.sidebar.radio("", ["📚 Estruturação de Books", "⚙️ Renomeador de Arquivos"])
    
    if pagina == "📚 Estruturação de Books":
        render_books()
    elif pagina == "⚙️ Renomeador de Arquivos":
        render_renomeador()

if __name__ == "__main__":
    main()
