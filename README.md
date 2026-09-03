# Consultor SUROD 12/2025 - Padrão ANTT

Aplicação interativa desenvolvida em [Streamlit](https://streamlit.io/) para otimizar a organização de entregáveis e a padronização de nomenclatura de arquivos técnicos em projetos de engenharia rodoviária. O sistema foi construído com base nas diretrizes do **Art. 7º e Anexo da Portaria SUROD nº 12/2025 da ANTT**.

## 🚀 Funcionalidades (Single Page Application)

Através de um menu lateral de navegação integrado, o usuário tem acesso a duas ferramentas principais:

*   **📚 Estruturação de Books de Projeto:** 
    *   Consulta rápida da composição de volumes exigida para cada tipo de projeto (EVTEA, Funcional, Anteprojeto, Projeto Executivo e As Built).
    *   Listagem automática de documentos obrigatórios transversais em todos os protocolos (Declaração de Veracidade, Check-list do PER, ART, Caderno de Respostas, etc.).
*   **⚙️ Configurador de Nomenclatura:** 
    *   Gerador do nome oficial de arquivos (desenhos, memórias, planilhas) seguindo a rigorosa máscara de 31 caracteres da ANTT.
    *   Formatação automatizada utilizando preenchimento de zeros (`.zfill`), padronização de letras maiúsculas e regras de hifenização para Concessionária, Rodovia, Localização, Obra, Projeto, Classe, Disciplina, Sequência e Revisão.

## 📁 Estrutura do Repositório

*   `app_surod_completo.py`: Código-fonte principal contendo a interface e a lógica das duas ferramentas unificadas.
*   `requirements.txt`: Arquivo de dependências para o ambiente de execução.

## 💻 Como executar localmente

1. Faça o clone deste repositório:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
