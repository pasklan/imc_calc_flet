# 📊 Calculadora de IMC

**Calculadora de IMC** é um aplicativo desenvolvido com [Flet](https://flet.dev/) que permite calcular o Índice de Massa Corporal (IMC) de forma prática e intuitiva. 
O app oferece uma interface amigável e visual para interpretar os resultados do IMC com base em imagens e mensagens personalizadas.

## 🛠️ Funcionalidades

- Calcula o IMC com base no peso e altura fornecidos.
- Suporte para seleção de gênero (Masculino ou Feminino).
- Exibe imagens e mensagens personalizadas conforme o resultado do IMC.
- Feedback claro em caso de campos incompletos ou valores inválidos.
- Design responsivo para dispositivos móveis e desktops.

---

## 📱 Prévia do App

![Preview](https://via.placeholder.com/400x300) <!-- Substitua com um link de imagem real ou captura de tela -->

---

## 🚀 Instalação e Uso

### 1. Requisitos

- **Python** 3.8+
- **Flet** instalado (`pip install flet`)
- Ferramentas de build (opcional para criar APKs)

### 2. Clonar o Repositório

```bash
git clone https://github.com/pasklan/imc_calc_flet.git
cd imc_calc_flet
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o App
```bash
flet run main.py
```

### 5. Gerar APK (Opcional)
```bash
flet pack main.py --platform android --ouput ./dist
```

## 🖼️ Estrutura do Projeto
```bash
imc_calc_flet/
├── main.py               # Código principal do aplicativo
├── pyproject.toml        # Configuração para Flet CLI
├── requirements.txt      # Dependências do projeto
├── assets/               # Imagens e outros recursos estáticos
└── README.md             # Documentação do projeto
```
## 🛠️ Tecnologias Utilizadas
- [Flet](https://www.flet.dev/) - Framework para criar apps multiplataforma com Python.
- Python 3.8+.
- Android SDK (para builds em APK)

## 🐛 Probkenas conhecidos
- Alguns dispositivos estão apresentando tela branca após a Splash Screen. Consulte documentação do Flet para depurar problemas.
- Erros de validação podem ocorrer ao inserir valores com vírgulas em vez de ponto.

## 📄 Licença
Este projeto está licenciado sob a MIT License.
