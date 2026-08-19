# Discrete Manufacturing — Cloud & AI Platforms Overlay

> **OU:** Cloud & AI Platforms  
> **This file:** Azure services lens on discrete manufacturing customers  
> **Primary content:** `../../../ai-business-process/verticals/discrete-mfg/`

Discrete manufacturing has some of the richest Azure scenarios of any industry — real-time IoT data from plant floor equipment, predictive maintenance ML models, and edge compute for disconnected factory environments. This overlay captures scenarios where **Azure** is the primary hero.

---

## Top scenarios (Azure lens)

| # | Scenario | Products | Business outcome |
|---|---|---|---|
| 1 | **Predictive maintenance** | Azure IoT Hub + Azure ML + D365 FS | Reduce unplanned downtime |
| 2 | **OEE analytics dashboard** | Microsoft Fabric + Power BI + IoT telemetry | Real-time line efficiency |
| 3 | **Digital twin for plant floor** | Azure Digital Twins + IoT Edge | "What-if" simulation |
| 4 | **Edge ML at the machine** | Azure Arc + IoT Edge + ONNX | Inference without cloud connectivity |
| 5 | **AI-powered quality inspection** | Azure AI Vision + custom model | Defect detection on the line |
| 6 | **Supply chain intelligence** | Microsoft Fabric + D365 SCM + Synapse | Demand sensing |
| 7 | **GitHub Copilot for factory automation code** | GitHub Copilot + Azure DevOps | Developer productivity |

---

## Joint motion with AI Business Process

The strongest discrete mfg pitch combines Azure + D365:

```
Azure IoT Hub → collects machine data
    ↓
Fabric / Azure ML → analyzes patterns, triggers alert
    ↓
D365 Field Service → creates work order, dispatches tech
    ↓
Copilot Studio agent → guides tech on mobile with AI assist
```

Use `../../../_shared/discrete-mfg/` for shared demo environment context before coordinating with the AI BP SE.

---

## Cross-reference

- D365 angle: `../../../ai-business-process/verticals/discrete-mfg/`
- M365 Copilot/Teams angle: `../../../ai-workplace/verticals/discrete-mfg/`
- Shared environments + personas: `../../../_shared/discrete-mfg/`
