# Ferramenta de Numeração de Páginas de PDF

Esta ferramenta web permite adicionar números às páginas de arquivos PDF de maneira fácil e intuitiva. O usuário pode escolher a posição do número nas páginas e a página a partir da qual a contagem deve começar.

## Funcionalidades

- Upload de arquivos PDF.
- Escolha da posição do número nas páginas:
  - Direita Superior
  - Direita Inferior
  - Esquerda Superior
  - Esquerda Inferior
- Definição da página inicial para a contagem.
- Download automático do PDF numerado após o processamento.

## Tecnologias Utilizadas

- Django: Framework web para o backend.
- Bootstrap: Biblioteca CSS para estilização.
- JavaScript: Para funcionalidades dinâmicas.
- Python: Para manipulação de PDFs.
- **HTML**: Para estruturação da interface.
- **CSS**: Para estilização e layout da interface.

## Pré-requisitos

- Python 3.8 ou superior
- Django 3.2 ou superior

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/numerar-pdf.git
   cd numerar-pdf

2. Crie um ambiente virtual e ative-o:
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`

3. Instale as dependências:

    ```bash
   pip install -r requirements.txt

4. Aplique as migrações do banco de dados:

    ```bash
   python manage.py migrate

5. Inicie o servidor de desenvolvimento:

    ```bash
   python manage.py runserver

6. Acesse a aplicação no navegador:

    ```bash
   http://127.0.0.1:8000

   

