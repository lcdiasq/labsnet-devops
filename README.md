# 🚀 LabsNet DevOps Project LifeCycle

Projeto prático de **DevOps completo**, cobrindo desde desenvolvimento até deploy em cloud com observabilidade.

---

# 🎯 Objetivo

Demonstrar na prática um pipeline moderno de DevOps utilizando:

* Desenvolvimento de API
* Containerização
* Integração Contínua (CI)
* Entrega Contínua (CD)
* Deploy em Cloud
* Monitoramento e Qualidade

---

# 🧱 Arquitetura

```
VSCode → GitHub → CI → CD → Cloud Run (GCP)
```

---

# ⚙️ Tecnologias Utilizadas

* **Backend:** FastAPI (Python)
* **Container:** Docker
* **CI/CD:** GitHub Actions
* **Cloud:** Google Cloud Run
* **Registry:** Artifact Registry
* **Qualidade:** Pytest, Flake8, Safety

---

# 📦 Estrutura do Projeto

```
app/
  main.py
  routes/
  services/

tests/

.github/workflows/
  ci.yml
  cd.yml
```

---

# 🚀 Pipeline DevOps

## 🔹 CI (Integração Contínua)

Executado em Pull Requests:

* ✔ Testes automatizados (pytest)
* ✔ Análise de código (flake8)
* ✔ Verificação de segurança (safety)

---

## 🔹 CD (Entrega Contínua)

Executado ao fazer merge na `main`:

* ✔ Build da imagem Docker
* ✔ Push para Artifact Registry
* ✔ Deploy automático no Cloud Run

---

# ☁️ Deploy

A aplicação é publicada automaticamente no:

👉 **Google Cloud Run**

Cada alteração na branch `main` gera uma nova versão em produção.

---

# 📊 Observabilidade

O projeto possui:

* ✔ Logs estruturados (Cloud Logging)
* ✔ Métricas automáticas (CPU, memória, requisições)
* ✔ Endpoint `/health` para monitoramento

---

# 🧪 Qualidade

O pipeline garante:

* ✔ Código testado
* ✔ Padronização
* ✔ Segurança básica

---

# 🌐 Funcionalidades

* Endpoint `/health` para verificação de status
* Dashboard simples para visualização das etapas do projeto
* Estrutura preparada para expansão (monitoramento de serviços)

---

# 💡 Conceitos Aplicados

* DevOps
* CI/CD
* Containerização
* Cloud Computing
* Observabilidade
* Qualidade de software

---

# 🎓 Uso Educacional

Este projeto foi desenvolvido com foco didático para ensino de:

* Pipelines DevOps na prática
* Integração com Cloud
* Boas práticas de desenvolvimento moderno

---

# 🚀 Próximos Passos

* Infraestrutura como código (Terraform)
* Monitoramento avançado
* Frontend moderno (dashboard completo)
* Autenticação e persistência de dados

---

# 👨‍💻 Autor

Projeto desenvolvido para fins educacionais e profissionais.

---

# 📌 Conclusão

Este projeto representa um fluxo completo de DevOps:

> Código → Teste → Build → Deploy → Monitoramento

---
