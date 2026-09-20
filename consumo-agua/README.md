# 💧 Classificador de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen?style=for-the-badge)

Programa em **Python** que classifica o perfil de consumo de água de um imóvel e emite alertas educativos, feito para uma campanha de conscientização ambiental de uma companhia de saneamento.

## 🎯 Objetivo

Receber o tipo de imóvel (comercial, casa ou apartamento) e o consumo mensal de água em m³, e retornar uma mensagem orientando o morador sobre seu padrão de consumo.

## 🛠️ Linguagem

Python 3.

## ▶️ Como executar

```bash
python3 app.py
```

O programa vai pedir:

1. O tipo de imóvel (`comercial`, `casa` ou `apartamento`)
2. O consumo mensal de água em m³

## 📋 Regras de classificação

| Tipo de imóvel      | Consumo        | Mensagem                  |
| ------------------- | -------------- | ------------------------- |
| Comercial           | qualquer       | Tarifa comercial aplicada |
| Apartamento         | < 10 m³        | Consumo econômico ✅      |
| Apartamento ou casa | até 25 m³      | Consumo moderado 🟡       |
| Qualquer            | acima de 25 m³ | Consumo excessivo ⚠️      |
