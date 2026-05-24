# Process Manufacturing — Cloud & AI Platforms Overlay

> **OU:** Cloud & AI Platforms
> **This file:** Azure services lens for process manufacturing customers
> **Primary D365 content:** `../../../ai-business-process/verticals/process-mfg/`
> **Shared industry context:** `../../../_shared/process-mfg/`

Process manufacturing generates massive volumes of sensor and batch data — ideal for Azure's IoT, analytics, and ML stack. The Azure motion here is often a landing pad before the D365 conversation, or an expansion play on top of an existing D365 footprint.

---

## Top scenarios (Azure lens)

| # | Scenario | Products | Business outcome |
|---|---|---|---|
| 1 | **Real-time batch monitoring** | Azure IoT Hub + Azure Stream Analytics | Catch out-of-spec conditions before batch fails |
| 2 | **Batch quality ML model** | Azure ML + Fabric | Predict yield from in-process variables |
| 3 | **OEE analytics on continuous lines** | Microsoft Fabric + Power BI + IoT telemetry | Real-time line efficiency |
| 4 | **Lot genealogy data lake** | Azure Data Lake + Fabric + D365 F&O | Full batch traceability for recall response |
| 5 | **Sustainability telemetry** | Azure IoT + Fabric + Sustainability Manager | Energy/water per batch, Scope 3 emissions |
| 6 | **MES/SCADA integration** | Azure IoT Edge + API Management | Connect legacy plant systems without ripping them out |
| 7 | **Regulatory compliance AI** | Azure AI + SharePoint (D365 QM data) | Auto-generate batch records for FDA/GMP audit |

---

## Joint motion with AI Business Process

```
Azure IoT Hub ← collects sensor data from fermenters, reactors, filling lines
    ↓
Azure ML / Fabric ← analyzes batch variables, flags anomaly
    ↓
D365 F&O ← creates quality non-conformance, triggers CAPA
    ↓
Copilot Studio agent ← notifies quality manager with context + recommended action
```

---

## Cross-reference

- D365 angle: `../../../ai-business-process/verticals/process-mfg/`
- M365/Teams angle: `../../../ai-workplace/verticals/process-mfg/`
- Shared industry context: `../../../_shared/process-mfg/`
