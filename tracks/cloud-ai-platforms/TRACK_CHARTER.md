# Track Charter — Cloud & AI Platforms

> **OU Lead:** Henrik Gütle (CVP, Cloud & AI Platforms)  
> **Americas SE&O:** Scott Prather

Cloud & AI Platforms SEs (formerly "Azure SEs") cover infrastructure, data, AI services, and application platform. This OU often partners with AI Business Process on joint architecture — Azure AI + D365 together is a powerful combined motion.

---

## Outcome statement

> **Cloud & AI Platforms SEs show customers that Azure isn't just infrastructure — it's the intelligent fabric that makes every business process smarter. AI services, Fabric analytics, and IoT + edge compute combine with D365 to create outcomes no other vendor can replicate.**

---

## Primary selling motions

| Motion | Key Products | Primary Demo Surface |
|---|---|---|
| **Azure AI & Foundry** | Azure OpenAI, AI Foundry, AI Search, AI Vision | Azure subscription |
| **Data & Analytics** | Microsoft Fabric, Azure SQL, Synapse, Power BI | Fabric workspace |
| **IoT & Edge** | Azure IoT Hub, IoT Edge, Azure Arc, Digital Twins | IoT demo environment |
| **Infrastructure** | Azure VM, AKS, Azure Stack HCI, Azure Arc | Azure subscription |
| **App Platform** | Azure Functions, Container Apps, Logic Apps, API Mgmt | Azure subscription |
| **Developer & GitHub** | GitHub Copilot, GitHub Actions, Dev Box | GitHub org |

---

## Industry verticals

| Vertical | Folder | What's different |
|---|---|---|
| **Discrete Manufacturing** | `verticals/discrete-mfg/` | IoT Hub, Fabric for OEE, Azure AI for predictive maint, Arc for edge |

> Azure is typically industry-agnostic at the infra layer but manufacturing has strong vertical-specific scenarios at the IoT/AI layer.

---

## Relationship with AI Business Process

Cloud & AI Platforms and AI Business Process frequently team on the same deal:

| | Cloud & AI Platforms | AI Business Process |
|---|---|---|
| **Primary product** | Azure (IaaS/PaaS/AI) | D365 (CRM/ERP) |
| **Copilot angle** | Azure OpenAI / custom agents | Copilot Studio + D365 Copilot |
| **Handoff point** | Azure AI model → | → Copilot Studio consumes it |

**Joint story:** Azure AI Foundry trains the model → Copilot Studio agent surfaces it in D365 → customer sees one intelligent business application.

---

## Key community touchpoints

- **CAIP SE Tribes** — Aakash Vats, Ravi Kumar Lingappa, Cloud & AI Platforms CoP
- **CE Solution Engineer Cross OU Collab** — cross-OU Teams channel
- **MSS Agentic Community of Practice** — Iro Stefopoulou
