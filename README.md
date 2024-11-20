# Dolphin Sentiment Analyzer

Este projeto é uma aplicação Python que realiza análise de sentimentos de textos inseridos pelo usuário

## Funcionalidades

- **Análise de Sentimentos**: O programa analisa o sentimento de um texto inserido, utilizando o modelo TextBlob. O sentimento é classificado como "Extremamente Negativo", "Negativo", "Neutro", "Positivo", "Muito Positivo" ou "Extremamente Positivo".
- **Suporte a Múltiplas Línguas**: O programa detecta automaticamente o idioma do texto e o traduz para o inglês antes de realizar a análise de sentimentos.

## Como Funciona

1. O programa começa pedindo ao usuário para inserir um texto.
2. O texto será automaticamente traduzido para o inglês.
3. Após a tradução (se necessário), o texto é analisado quanto ao seu sentimento.
4. O resultado da análise é mostrado ao usuário.

## Pré-Requisitos

Antes de rodar o programa, certifique-se de que as seguintes bibliotecas Python estão instaladas:

- `deep-translator`
- `textblob`
- `colorama`

Você pode instalar as dependências usando o `pip`:

```bash
pip install deep-translator textblob colorama