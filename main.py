import tkinter as tk
from tkinter import ttk

class CalculadoraAco:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Aço Profissional - 2026")
        self.root.geometry("850x650")

        # Lista de bitolas padrão de mercado
        self.bitolas_padrao = ["5.0", "6.3", "8.0", "10.0", "12.5", "16.0", "20.0", "25.0"]
        self.linhas = []

        tk.Label(root, text="Tabela de Cálculo de Aço", font=("Arial", 16, "bold")).pack(pady=10)

        # Container da Tabela
        self.frame_container = tk.Frame(root)
        self.frame_container.pack(padx=10, fill="both", expand=True)

        # Cabeçalhos
        headers = ["Bitola (mm)", "Comp. (m)", "Qtd (un)", "Peso Linha (kg)", "Ação"]
        for i, text in enumerate(headers):
            tk.Label(self.frame_container, text=text, font=("Arial", 10, "bold"), 
                     borderwidth=1, relief="solid", width=15).grid(row=0, column=i, sticky="nsew", padx=1)

        # Botão Adicionar
        tk.Button(root, text="+ Adicionar Nova Barra", command=self.adicionar_linha, 
                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

        # Seção de Resumo
        tk.Label(root, text="Resumo por Bitola:", font=("Arial", 11, "bold")).pack(pady=(10, 0))
        self.txt_resumo = tk.Text(root, height=6, width=60, font=("Consolas", 11), bg="#f8f8f8", state="disabled")
        self.txt_resumo.pack(pady=5)
        
        # Rodapé Total
        self.lbl_total_geral = tk.Label(root, text="Total Geral: 0.00 kg", font=("Arial", 14, "bold"), bg="#dcdcdc")
        self.lbl_total_geral.pack(fill="x", side="bottom", ipady=10)

        self.adicionar_linha()

    def adicionar_linha(self):
        # Variáveis de controle
        v_bitola = tk.StringVar(value="10.0")
        v_comp = tk.StringVar(value="12.0")
        v_qtd = tk.StringVar(value="1")
        
        row_idx = len(self.linhas) + 2 # +2 para pular cabeçalho e espaçamento
        
        # Widgets da linha
        # Substituindo Entry por Combobox para a Bitola
        cb_bitola = ttk.Combobox(self.frame_container, textvariable=v_bitola, values=self.bitolas_padrao, width=12, state="readonly")
        e_comp = tk.Entry(self.frame_container, textvariable=v_comp, width=15, justify="center")
        e_qtd = tk.Entry(self.frame_container, textvariable=v_qtd, width=15, justify="center")
        l_peso = tk.Label(self.frame_container, text="0.00 kg", width=15, font=("Arial", 10, "bold"))
        b_rem = tk.Button(self.frame_container, text="Remover", bg="#f44336", fg="white", 
                          command=lambda: self.remover_linha(dados))

        # Posicionamento Grid
        cb_bitola.grid(row=row_idx, column=0, pady=3)
        e_comp.grid(row=row_idx, column=1, pady=3)
        e_qtd.grid(row=row_idx, column=2, pady=3)
        l_peso.grid(row=row_idx, column=3, pady=3)
        b_rem.grid(row=row_idx, column=4, padx=5, pady=3)

        dados = {
            "vars": (v_bitola, v_comp, v_qtd), 
            "lbl": l_peso, 
            "widgets": (cb_bitola, e_comp, e_qtd, l_peso, b_rem)
        }
        
        # Eventos para atualizar cálculos
        v_bitola.trace_add("write", lambda *args: self.calcular())
        v_comp.trace_add("write", lambda *args: self.calcular())
        v_qtd.trace_add("write", lambda *args: self.calcular())
            
        self.linhas.append(dados)
        self.calcular()

    def remover_linha(self, dados):
        for w in dados["widgets"]: w.destroy()
        self.linhas.remove(dados)
        self.calcular()

    def calcular(self):
        total_geral = 0.0
        resumo_bitolas = {}

        for linha in self.linhas:
            try:
                # Pega os valores das variáveis
                b = float(linha["vars"][0].get())
                c = float(linha["vars"][1].get())
                q = float(linha["vars"][2].get())
                
                # Fórmula técnica: (D² / 162) * Comprimento * Quantidade
                peso = (b**2 / 162) * c * q
                linha["lbl"].config(text=f"{peso:.2f} kg")
                
                total_geral += peso
                
                # Agrupamento para o Resumo
                chave = f"{b:>4} mm"
                resumo_bitolas[chave] = resumo_bitolas.get(chave, 0) + peso
                
            except (ValueError, tk.TclError):
                linha["lbl"].config(text="Erro/Vazio")

        # Atualizar área de texto do Resumo
        self.txt_resumo.config(state="normal")
        self.txt_resumo.delete("1.0", tk.END)
        self.txt_resumo.insert(tk.END, f"{'BITOLA':<15} | {'PESO TOTAL':<15}\n")
        self.txt_resumo.insert(tk.END, "-" * 35 + "\n")
        
        for bitola in sorted(resumo_bitolas.keys(), key=lambda x: float(x.split()[0])):
            peso_sub = resumo_bitolas[bitola]
            self.txt_resumo.insert(tk.END, f"{bitola:<15} | {peso_sub:>10.2f} kg\n")
        
        self.txt_resumo.config(state="disabled")
        self.lbl_total_geral.config(text=f"TOTAL GERAL DO PROJETO: {total_geral:.2f} kg")

if __name__ == "__main__":
    root = tk.Tk()
    # Aplicar um tema visual mais moderno
    style = ttk.Style()
    style.theme_use('clam') 
    CalculadoraAco(root)
    root.mainloop()
