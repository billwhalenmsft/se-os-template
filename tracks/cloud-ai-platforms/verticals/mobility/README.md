# Mobility — Cloud & AI Platforms Overlay

> **OU:** Cloud & AI Platforms
> **This file:** Azure services lens for automotive OEMs, fleet operators, and connected vehicle scenarios
> **Primary D365 content:** `../../../ai-business-process/verticals/mobility/`
> **Shared industry context:** `../../../_shared/mobility/`

The Azure mobility story is strongest at the OEM and fleet operator level — connected vehicle data, telematics, and predictive maintenance powered by IoT and AI, feeding into D365 FS for dispatch.

---

## Top scenarios (Azure lens)

| # | Scenario | Products | Business outcome |
|---|---|---|---|
| 1 | **Connected vehicle telemetry** | Azure IoT Hub + Event Hubs + Stream Analytics | Real-time vehicle health monitoring |
| 2 | **Predictive fleet maintenance** | Azure ML + D365 Field Service | Predict failures before breakdown, schedule proactively |
| 3 | **Digital twin for vehicle** | Azure Digital Twins | "What-if" simulation for fleet lifecycle |
| 4 | **EV charging & range analytics** | Azure IoT + Maps + Fabric | Optimize charging routing, reduce range anxiety incidents |
| 5 | **Dealer inventory intelligence** | Microsoft Fabric + Power BI + D365 Sales data | OEM sees real-time dealer lot inventory + pipeline |
| 6 | **Recall impact analysis** | Azure Synapse + D365 CS data | Identify affected VINs, prioritize outreach in hours not weeks |
| 7 | **GitHub Copilot for vehicle software** | GitHub Copilot + Azure DevOps | OEM software team productivity (ADAS, infotainment) |

---

## Joint motion with AI Business Process

```
Azure IoT Hub ← telemetry from connected vehicles / fleet
    ↓
Azure ML ← predicts component failure (brake pads, battery, engine)
    ↓
D365 Field Service ← creates proactive work order, dispatches mobile tech
    ↓
Copilot Studio agent ← notifies vehicle owner / fleet manager with scheduling options
```

---

## Cross-reference

- D365 angle: `../../../ai-business-process/verticals/mobility/`
- M365/Teams angle: `../../../ai-workplace/verticals/mobility/`
- Shared industry context: `../../../_shared/mobility/`
