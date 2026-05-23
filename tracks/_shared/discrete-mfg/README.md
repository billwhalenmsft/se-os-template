# Shared — Discrete Manufacturing Cross-OU Patterns

> **Purpose:** Industry context, demo environments, and customer personas that are the same regardless of which OU is leading the engagement. Every SE demoing to a discrete manufacturer — whether they're AI BP, AI Workplace, or Azure — starts here.

---

## What lives here vs. in OU-specific files

| Content | Where it lives |
|---|---|
| Industry background, key pain points, buyer personas | **Here** (this folder) |
| D365 use cases (service, sales, field service) | `../../ai-business-process/verticals/discrete-mfg/` |
| Teams / M365 Copilot scenarios for mfg workers | `../../ai-workplace/verticals/discrete-mfg/` |
| Azure IoT, Fabric, predictive maintenance | `../../cloud-ai-platforms/verticals/discrete-mfg/` |
| OT/IT security, Defender for IoT | `../../security/` + coordinate here |

---

## Industry background (bring this to every call)

**What discrete manufacturers make:**  
Physical goods — industrial equipment, automotive parts, aerospace components, consumer products, electronics, building materials.

**How they're different from process manufacturers:**  
Discrete = countable units (you can track serial number #12345). Process = batches of fluids/chemicals. D365 demos default to discrete scenarios.

**Top pain points (universal across all OUs):**
1. **Fragmented systems** — ERP, CRM, field service, and quality are siloed
2. **Unplanned downtime** — reactive maintenance costs 5-10x more than preventive
3. **Dealer / distributor complexity** — indirect sales channel with poor visibility
4. **Talent pressure** — experienced technicians retiring; knowledge transfer is a crisis
5. **Customer expectations** — B2B buyers now expect B2C-level service transparency

---

## Buyer personas (bring these to every SE call)

| Persona | Title | What they care about | Key question to ask |
|---|---|---|---|
| **Service VP** | VP of Customer Service | CSAT, case volume, cost per resolution | "How many cases does your team handle per day?" |
| **Plant Manager** | VP/Director of Operations | OEE, downtime, maintenance cost | "What's your current unplanned downtime rate?" |
| **IT Director** | CTO / IT Director | Integration complexity, security, cloud | "What's your current CRM/ERP stack?" |
| **Field Tech** | Service Technician / FSE | Parts availability, dispatch clarity | (usually not in the room — but demo as this persona) |
| **Dealer/Distributor** | Channel Partner | Inventory visibility, case tracking | "Do your partners have a portal today?" |
| **CFO/Finance** | CFO / VP Finance | ROI, cost reduction, license consolidation | "What are you paying for today that's overlapping?" |

---

## Demo environments

| Environment | What it is | Who owns it | When to use |
|---|---|---|---|
| **Master CE Mfg** | Primary D365 CE demo org (Sales + CS + FS) | Bill Whalen (billwhalen@microsoft.com) | Any D365 demo for a manufacturer |
| **Mfg Gold Template** | Clean D365 baseline — clone for new customers | Bill Whalen | Starting point for new customer builds |

> **Request access:** ping Bill directly or open a GitHub issue with `env-access` label.

---

## Industry talk tracks (30-second intros)

### Opening for a CS/FS audience
> "Manufacturers have an invisible problem: their best service data is locked in systems that don't talk to each other. A tech in the field doesn't know the customer's history. The service manager doesn't see the open cases. And the plant director is looking at a report that's 48 hours old. What we're going to show you today is what it looks like when all of that becomes one connected, agent-driven experience."

### Opening for an IT/CTO audience
> "You've probably got Dynamics, a legacy CRM or homegrown system, SharePoint, and a few point solutions. The question isn't whether AI can help — it clearly can. The question is: do you want 10 different vendors' AI, or one platform that reasons across all your business data?"

### Opening for a joint AI BP + AI Workplace audience
> "Your knowledge workers use Microsoft 365 every day. Your operations run on Dynamics. Today we're going to show you what it looks like when Copilot connects both — so your service manager's Teams meeting and your field tech's D365 work order are part of the same intelligent thread."
