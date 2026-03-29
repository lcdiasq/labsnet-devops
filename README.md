# 🚀 LabsNet DevOps Lifecycle

Projeto educacional focado no ciclo completo de DevOps/DevSecOps, desde o desenvolvimento até o deploy em cloud.

---

## 🎯 Objetivo

Demonstrar na prática:

- Desenvolvimento de API
- Testes automatizados
- Containerização com Docker
- Integração contínua (CI)
- Segurança (DevSecOps)
- Deploy contínuo (CD)
- Infraestrutura como Código (Terraform)
- Deploy no Google Cloud Run

---

## 🧱 Stack

- Python (FastAPI)
- Docker
- GitHub Actions
- Terraform
- Google Cloud Platform (Cloud Run)

---

## 🧠 Arquitetura de execução

O projeto é desenvolvido no Windows (VS Code), mas executado em ambiente Linux via Docker.

Isso garante compatibilidade com ambientes reais de produção.

---

## ▶️ Executar localmente (sem Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload