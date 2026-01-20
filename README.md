# 🏗️ Calculadora de Aço Profissional (Versão 2026)

Uma ferramenta desktop robusta e intuitiva desenvolvida em **Python** para profissionais de Engenharia Civil e Serralheria. O software automatiza o cálculo de peso de armaduras de aço, permitindo a gestão rápida de listas de corte e dobra.

## ✨ Funcionalidades

*   **Cálculo Técnico Preciso:** Utiliza a fórmula padrão de mercado $(D²/162)$ para converter diâmetro e comprimento em peso (kg).
*   **Interface Dinâmica:** Adicione ou remova linhas de cálculo em tempo real conforme a necessidade do projeto.
*   **Resumo Inteligente:** Agrupamento automático de peso por bitola, facilitando a visualização para pedidos de compra.
*   **Tabela de Bitolas Padrão:** Pré-configurada com as medidas comerciais mais comuns (5.0mm a 25.0mm).
*   **Interface Moderna:** Desenvolvida com o tema `clam` do Tkinter para uma experiência visual limpa e profissional.

## 🚀 Como Executar

Para rodar este projeto em 2026, você precisa ter o **Python** instalado em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com
    ```

2.  **Acesse a pasta:**
    ```bash
    cd rebar-calculator
    ```

3.  **Execute o script:**
    ```bash
    python main.py
    ```

> **Nota:** Não é necessária a instalação de bibliotecas externas, pois o `tkinter` já vem integrado por padrão na maioria das distribuições Python.

## 📊 Regras de Cálculo

A aplicação segue o padrão normativo para cálculo de peso nominal de barras de aço CA-50/CA-60:

**Fórmula:**
$$Peso(kg) = \frac{Diâmetro(mm)^2}{162} \times Comprimento(m) \times Quantidade$$

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** [Python](https://www.python.org)
*   **GUI:** Tkinter / Ttk (Interface Gráfica)
*   **Paradigma:** Orientação a Objetos (POO)

## 📝 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---
*Desenvolvido para agilizar o levantamento de materiais em canteiros de obra e escritórios de engenharia.*
