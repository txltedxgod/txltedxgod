<div align="center">

# 👋 Hi, I'm txltedxgod

### Senior Software & AI Infrastructure Engineer
**Distributed Systems · LLM & AI Infrastructure · High-Throughput Gateways · Cloud-Native Architecture**

<br/>

[![GitHub Stars](https://img.shields.io/github/stars/txltedxgod?style=for-the-badge&color=388bfd&labelColor=0d1117)](https://github.com/txltedxgod)
[![Public Repos](https://img.shields.io/badge/Public_Projects-70+-58a6ff?style=for-the-badge&logo=github&labelColor=0d1117)](https://github.com/txltedxgod?tab=repositories)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge&labelColor=0d1117)](https://opensource.org/licenses/MIT)

<br/>

```text
> Specialization : Distributed Systems, LLM Orchestration, Memory-Safe Microservices & Cloud-Native FinOps
> Primary Stacks : Python 3.12 · Go 1.22 · Rust · Modern C++17 · TypeScript · C# / .NET 8
> Infrastructure : Kubernetes · Docker · Kafka · Redis · PostgreSQL · Terraform · Prometheus · Grafana
```

</div>

---

## 🛠️ Core Technology Stack

<div align="center">

| Domain | Technologies & Frameworks |
| :--- | :--- |
| **Languages** | `Python` · `Go (Golang)` · `Rust` · `C++17` · `TypeScript` · `C# (.NET 8)` · `SQL` |
| **AI / ML & LLM** | `RAG (RRF / GraphRAG)` · `LoRA / QLoRA` · `DSPy` · `Vector Cache` · `LLM Guardrails` · `pgvector` · `PyTorch` |
| **Distributed Systems** | `Event-Driven (Kafka / CDC)` · `gRPC / Protobuf` · `CRDTs` · `Commit-Log Brokers` · `Message Queues` · `WebSockets` |
| **Cloud & DevOps** | `Kubernetes (K8s)` · `Docker & Compose` · `Helm 3` · `Terraform (IaC)` · `Ansible` · `GitHub Actions CI/CD` |
| **Databases & Caching** | `PostgreSQL (WAL/Partman)` · `Redis` · `SQLite` · `SQLAlchemy 2.0 (Async)` · `Alembic` · `In-Memory KV` |
| **Security & Observability**| `WebAuthn / Passkeys` · `JWT RBAC` · `Prometheus` · `Grafana` · `Loki` · `OpenTelemetry` · `WAF` |

</div>

---

## 🚀 Featured Engineering Projects

### 🧠 1. AI, LLM Infrastructure & RAG Systems

| Repository | Tech Stack | Highlights |
| :--- | :--- | :--- |
| ⚡ **[rag-fusion-engine](https://github.com/txltedxgod/rag-fusion-engine)** | `Python 3.12`, `FastAPI`, `NumPy`, `Docker` | Advanced RAG with Reciprocal Rank Fusion (RRF), multi-query expansion and cross-encoder reranking. |
| 🛡️ **[llm-eval-guard](https://github.com/txltedxgod/llm-eval-guard)** | `Python`, `FastAPI`, `Pydantic`, `Regex` | Production LLM evaluation & safety platform: hallucination detection, prompt injection defense, PII masking. |
| 💾 **[vector-cache-redis](https://github.com/txltedxgod/vector-cache-redis)** | `Python`, `Redis`, `Vector-Search`, `FastAPI` | Semantic vector cache for LLM queries with cosine similarity deduplication (80%+ cost reduction). |
| 🧠 **[polyagent-core](https://github.com/txltedxgod/polyagent-core)** | `Python`, `AsyncIO`, `FastAPI`, `DAG` | Autonomous multi-agent orchestration framework with DAG execution, vector memory and tool sandboxing. |
| 🕸️ **[graph-rag-navigator](https://github.com/txltedxgod/graph-rag-navigator)** | `Python`, `Neo4j`, `Knowledge-Graph`, `LLM` | Knowledge Graph-enhanced RAG engine with entity extraction, graph traversal, and multi-hop reasoning. |
| 📐 **[embeddings-quantizer](https://github.com/txltedxgod/embeddings-quantizer)** | `Python`, `Product-Quantization`, `SQ8` | High-performance vector quantization reducing embedding memory footprint by 75% without accuracy loss. |
| 🎯 **[prompt-optimizer-dsp](https://github.com/txltedxgod/prompt-optimizer-dsp)** | `Python`, `DSPy`, `LLM-Optimization` | Automated prompt optimization & DSPy self-refinement framework for production AI pipelines. |
| 🧪 **[synthetic-data-gen](https://github.com/txltedxgod/synthetic-data-gen)** | `Python`, `Differential-Privacy`, `Stats` | Privacy-preserving tabular synthetic data generator with Differential Privacy and validation reports. |
| 📄 **[docassist](https://github.com/txltedxgod/docassist)** | `FastAPI`, `pgvector`, `aiogram3`, `Docker` | Production RAG assistant over documents: async pgvector ingestion, semantic search and SSE streaming. |

---

### ⚡ 2. High-Performance Distributed Systems & Gateways

| Repository | Tech Stack | Highlights |
| :--- | :--- | :--- |
| 🛡️ **[zenith-gateway](https://github.com/txltedxgod/zenith-gateway)** | `Rust`, `Tokio`, `Axum`, `Tower` | Ultra-fast cloud-native API Gateway and WAF with dynamic rate limiting and JWT RBAC policies (150k+ QPS). |
| 📡 **[nexus-mq](https://github.com/txltedxgod/nexus-mq)** | `Go 1.22`, `gRPC`, `mmap`, `WebSocket` | Distributed commit-log message broker with consumer groups, automatic rebalancing & real-time dashboard. |
| 🔀 **[event-stream-cdc](https://github.com/txltedxgod/event-stream-cdc)** | `Python`, `PostgreSQL WAL`, `Kafka`, `Redis` | Real-time Change Data Capture (CDC) engine with Transactional Outbox pattern, DLQ and replay. |
| ⚙️ **[distributed-task-mesh](https://github.com/txltedxgod/distributed-task-mesh)** | `Python`, `DAG`, `Task-Queue`, `FastAPI` | Lightweight distributed task queue and worker mesh with DAG task dependencies and live UI. |
| 👑 **[distributed-cron-leader](https://github.com/txltedxgod/distributed-cron-leader)** | `Python`, `Leader-Election`, `Redis` | Distributed cron scheduler with leader election protocol and exactly-once task execution guarantees. |
| ⚡ **[turbokv](https://github.com/txltedxgod/turbokv)** | `Modern C++17`, `TCP`, `WAL`, `POSIX` | Fast in-memory key-value store with TTL, binary Write-Ahead Logging (WAL) crash recovery and TCP protocol. |
| 🎨 **[syncspace-crdt](https://github.com/txltedxgod/syncspace-crdt)** | `TypeScript`, `CRDTs`, `WebSockets`, `Canvas` | Collaborative infinite canvas engine with Conflict-Free Replicated Data Types & QuadTree spatial indexing. |
| 🦫 **[gocache-proxy](https://github.com/txltedxgod/gocache-proxy)** | `Go 1.22`, `LRU-Cache`, `Prometheus` | High-performance HTTP caching reverse proxy with concurrent thread-safe in-memory LRU. |
| 🔷 **[hookflow](https://github.com/txltedxgod/hookflow)** | `C# / .NET 8`, `EF Core`, `Workers` | High-throughput webhook delivery and retry engine with exponential backoff, HMAC signing & DLQ. |

---

### 🛡️ 3. Security, Authentication & Observability

| Repository | Tech Stack | Highlights |
| :--- | :--- | :--- |
| 🔑 **[auth-passkey-service](https://github.com/txltedxgod/auth-passkey-service)** | `Python 3.12`, `FastAPI`, `WebAuthn`, `FIDO2` | Modern passwordless WebAuthn / Passkey FIDO2 authentication microservice with cross-platform attestation. |
| 🔐 **[jwt-guard-rs](https://github.com/txltedxgod/jwt-guard-rs)** | `Rust`, `Axum`, `Redis`, `Serde` | High-speed JWT authentication and real-time token revocation gateway with sub-millisecond overhead. |
| 🕵️ **[secret-scanner-ci](https://github.com/txltedxgod/secret-scanner-ci)** | `Python`, `Entropy-Analysis`, `CI/CD` | High-speed pre-commit & CI secret scanner detecting leaked API keys, tokens and high-entropy secrets. |
| 📜 **[audit-trail-ledger](https://github.com/txltedxgod/audit-trail-ledger)** | `Python`, `Merkle-Tree`, `Crypto`, `FastAPI` | Cryptographically verifiable immutable audit log ledger with Merkle Tree hash verification. |
| 📈 **[observability-anomaly-detector](https://github.com/txltedxgod/observability-anomaly-detector)** | `Python`, `Prometheus`, `IsolationForest` | Real-time time-series anomaly detection on Prometheus metrics and logs using Isolation Forest. |
| ⏱️ **[cert-sentinel](https://github.com/txltedxgod/cert-sentinel)** | `Go`, `TLS / x509`, `Prometheus` | Automated SSL/TLS certificate expiry watcher and Prometheus exporter with webhook alerting. |

---

### ☁️ 4. Cloud, Kubernetes, FinOps & Infrastructure

| Repository | Tech Stack | Highlights |
| :--- | :--- | :--- |
| 💰 **[k8s-cost-optimizer](https://github.com/txltedxgod/k8s-cost-optimizer)** | `Python`, `Kubernetes API`, `FinOps` | Kubernetes resource rightsizing & FinOps cost optimization daemon: CPU/Memory waste detection. |
| ☸️ **[k8s-pod-autoscale](https://github.com/txltedxgod/k8s-pod-autoscale)** | `Go`, `client-go`, `Prometheus` | Custom Kubernetes controller for dynamic queue and metric-based pod autoscaling. |
| ☁️ **[tf-infra-modules](https://github.com/txltedxgod/tf-infra-modules)** | `Terraform HCL`, `AWS`, `GCP` | Production modular Infrastructure as Code blueprints: Multi-AZ VPC, EKS Cluster, Aurora RDS, IAM. |
| 📦 **[helm-charts-hub](https://github.com/txltedxgod/helm-charts-hub)** | `Helm 3`, `Kubernetes` | Curated production Helm charts for microservices, Redis Sentinel HA, and ingress controllers. |
| 📊 **[docker-compose-lab](https://github.com/txltedxgod/docker-compose-lab)** | `Prometheus`, `Grafana`, `Loki`, `Promtail` | Ready-to-use Docker Compose observability stack with custom dashboards and log shipping. |
| 🔒 **[ansible-hardening](https://github.com/txltedxgod/ansible-hardening)** | `Ansible`, `Linux Kernel Tuning` | Production Linux server security hardening, CIS benchmark compliance, and sysctl tuning. |

---

### 🏛️ 5. Clean Architecture Backend & Developer Tools

| Repository | Tech Stack | Highlights |
| :--- | :--- | :--- |
| 🏛️ **[fastapi-clean-template](https://github.com/txltedxgod/fastapi-clean-template)** | `FastAPI`, `SQLAlchemy 2.0`, `DDD`, `Alembic` | Enterprise Clean Architecture & Domain-Driven Design production boilerplate with JWT RBAC. |
| 🔍 **[database-query-optimizer](https://github.com/txltedxgod/database-query-optimizer)** | `Python`, `PostgreSQL EXPLAIN`, `AST` | Automated PostgreSQL query plan analyzer, EXPLAIN cost breakdown and index tuning advisor. |
| 🧩 **[pydantic-ast-generator](https://github.com/txltedxgod/pydantic-ast-generator)** | `Python`, `Pydantic v2`, `Python AST` | Dynamic schema compiler generating Pydantic v2 models and AST validation rules from SQL DDL. |
| 🗄️ **[pg-partman-py](https://github.com/txltedxgod/pg-partman-py)** | `Python`, `PostgreSQL`, `Timeseries` | Automated timeseries table partitioning and retention manager for PostgreSQL. |
| 🔗 **[url-shortener](https://github.com/txltedxgod/url-shortener)** | `FastAPI`, `PostgreSQL`, `Redis`, `Docker` | Production-grade URL shortener with analytics, Base62 codes, dynamic QR codes, and dashboard. |
| 🤖 **[telegram-store-bot](https://github.com/txltedxgod/telegram-store-bot)** | `Python`, `aiogram 3`, `PostgreSQL`, `Docker` | Full-featured ecommerce Telegram bot with cart, FSM checkout, orders, promo codes and admin panel. |

---

## 📊 GitHub Analytics & Profile Statistics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=txltedxgod&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=58A6FF&icon_color=58A6FF&text_color=C9D1D9" height="175" alt="GitHub Stats" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=txltedxgod&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=58A6FF&text_color=C9D1D9" height="175" alt="Top Languages" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=txltedxgod&theme=tokyonight&hide_border=true&background=0D1117&stroke=58A6FF&ring=58A6FF&fire=58A6FF&currStreakNum=C9D1D9" alt="Streak Stats" />

</div>

---

<div align="center">
  <sub>Engineered with production reliability, performance & cloud-native best practices</sub>
</div>
