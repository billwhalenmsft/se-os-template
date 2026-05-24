# Shared — Process Manufacturing Cross-OU Patterns

> **Purpose:** Industry context, buyer personas, demo environments, and talk tracks that apply regardless of which OU is leading a process manufacturing engagement. Start here before going to OU-specific content.

---

## What is Process Manufacturing?

Process manufacturers produce goods in **batches or continuous flows** — not countable discrete units. Think: chemicals mixed in a vat, food produced on a line, pharmaceuticals in a controlled batch. The product can't be disassembled back into its components.

**Key industries:**
- Food & Beverage (F&B) — breweries, dairy, packaged foods
- Chemicals & Specialty Chemicals
- Pharmaceuticals & Life Sciences
- Oil & Gas / Energy
- Paints, coatings, adhesives

**How they differ from Discrete Mfg:**
| | Discrete | Process |
|---|---|---|
| Unit | Countable (serial #12345) | Batch / lot / formula |
| BOM | Bill of Materials | Recipe / formula |
| Rework | Reassemble | Usually not possible |
| Quality | Inspection per unit | QC on batch/lot |
| ERP focus | D365 CE / SCM | D365 F&O with process mfg modules |

---

## Top pain points (universal across all OUs)

1. **Recipe / formula management** — versions, compliance, change control are manual
2. **Batch traceability** — recall readiness requires lot-level genealogy across ingredients
3. **Quality compliance** — FDA 21 CFR Part 11, ISO 22000, GMP documentation is manual
4. **OEE on continuous lines** — line efficiency is tracked in paper or legacy SCADA
5. **Demand-driven scheduling** — seasonal spikes, raw material availability drive constant replanning
6. **Sustainability / ESG** — scope 3 emissions, water/energy per batch increasingly required

---

## Buyer personas

| Persona | Title | What they care about | Key question to ask |
|---|---|---|---|
| **Plant Director** | VP/Director of Operations | OEE, batch yield, downtime | "What percentage of your batches require rework?" |
| **Quality Manager** | QA/QC Manager | Compliance, traceability, CAPA | "How long does a recall investigation take today?" |
| **Supply Chain VP** | VP Supply Chain / Procurement | Raw material costs, lead time | "How much buffer stock are you carrying?" |
| **R&D / Formulation** | Formulation Scientist / R&D Lead | Recipe iteration, scale-up | "How do you manage formula versions today?" |
| **IT Director** | CTO / IT Director | Integration, cloud migration | "What's running your MES/SCADA today?" |
| **CFO** | CFO / VP Finance | Cost per batch, waste, margin | "What's your batch yield variance costing you annually?" |

---

## Demo environment note

Process manufacturing scenarios typically require **D365 Finance & Operations** (not D365 CE) for deep recipe/batch scenarios. For field service and customer-facing scenarios, the **Master CE Mfg** environment can be adapted.

> No dedicated process mfg demo environment exists yet. See `../../ai-business-process/verticals/process-mfg/` for current demo status.

---

## Industry talk tracks

### Opening for a Food & Beverage audience
> "In food and beverage, your margin lives in two places: yield per batch and speed of response when something goes wrong. Today most manufacturers are stitching together a SCADA report, an Excel spreadsheet, and a quality system that only talks to itself. What we're going to show you is what it looks like when all of that becomes one intelligent platform."

### Opening for a Pharma / Life Sciences audience
> "In pharma, compliance isn't optional — and your systems have to prove it. The question isn't whether your process is compliant. It's whether your *data* can prove it fast enough when the FDA asks. Today we'll show you how Microsoft's platform handles batch genealogy, 21 CFR Part 11 signatures, and CAPA workflows without a roomful of consultants."

### Opening for an IT/CTO audience
> "Your MES or SCADA is probably not going away — and it shouldn't. But the data it generates stays siloed unless you connect it. Azure IoT and Microsoft Fabric let you pull that signal data into an analytics layer your operations team can actually use, alongside your ERP, your quality system, and your supplier data."
