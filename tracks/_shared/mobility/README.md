# Shared — Mobility Cross-OU Patterns

> **Purpose:** Industry context, buyer personas, and talk tracks for Mobility — automotive OEMs, dealers, fleet operators, and transportation-adjacent manufacturers. Start here before going to OU-specific content.

---

## What is Mobility?

Mobility covers organizations whose business revolves around **vehicles, transportation, or fleet operations**:

- **Automotive OEMs** — vehicle manufacturers (cars, trucks, EVs, heavy equipment)
- **Automotive dealers / dealer groups** — franchise dealerships selling new/used, service bays
- **Fleet operators** — companies operating large fleets (logistics, utilities, municipalities)
- **Transportation & logistics** — carriers, 3PLs, last-mile delivery
- **Aftermarket / parts distributors** — OEM parts, wholesale auto parts

**How Mobility relates to the other manufacturing sub-verticals:**
- Automotive OEMs build *discrete* units (vehicles have VINs) → see `../../discrete-mfg/` for plant floor scenarios
- Mobility focus here is post-manufacture: **sales, service, fleet management, and dealer network**

---

## Top pain points (universal across all OUs)

1. **Dealer network complexity** — OEM has limited visibility into dealer inventory, sales pipeline, customer satisfaction
2. **Service bay scheduling** — appointment booking, parts availability, and tech dispatch are siloed
3. **Vehicle lifecycle** — warranty, recall, service history scattered across OEM, dealer, and owner
4. **EV transition** — charging infrastructure, range anxiety, new service model (fewer moving parts but new tech issues)
5. **Fleet ROI** — fleet managers can't see total cost of ownership in real time
6. **Customer retention** — post-sale relationship gaps (dealer rarely contacts owner proactively)

---

## Buyer personas

| Persona | Title | What they care about | Key question to ask |
|---|---|---|---|
| **Dealer Principal** | Owner / GM of dealership | Revenue per service bay, floor plan cost | "What's your current service bay utilization rate?" |
| **Service Manager** | Service Director / Manager | RO throughput, technician productivity, CSI score | "What percentage of your appointments are first-time fix?" |
| **Fleet Manager** | VP Fleet / Fleet Operations | TCO, uptime, driver safety | "How do you track maintenance compliance across the fleet today?" |
| **OEM Channel Manager** | Regional Sales Manager (OEM side) | Dealer performance, market share, inventory | "How long does it take to see what's on dealer lots across your region?" |
| **Parts Manager** | Parts Director | Fill rates, obsolescence, parts margin | "What's your current parts obsolescence rate?" |
| **IT Director** | CTO / IT Director | DMS integration, cloud, data consolidation | "What's your current DMS? Are you on CDK, Reynolds, or Tekion?" |

---

## Demo environment note

Mobility scenarios primarily use **D365 Sales** (dealer/fleet CRM), **D365 Field Service** (service bay scheduling + tech dispatch), and **Copilot Studio** (dealer chat, appointment booking agents). **Master CE Mfg** can be adapted for mobility/dealer scenarios.

> See `../../ai-business-process/verticals/mobility/` for current demo status and customer builds.

---

## Industry talk tracks

### Opening for a dealer / dealer group
> "A vehicle customer walks into your store once every three to five years to buy. But they come in for service four or five times in between. The dealerships winning on retention aren't the ones with the best inventory — they're the ones who know their customer's history before the car pulls into the service lane. Let me show you what that looks like."

### Opening for a fleet operator
> "In fleet operations, every unplanned breakdown costs you in three ways: the repair itself, the driver downtime, and the missed commitment to your customer. What if your fleet could tell you three weeks before a breakdown that a specific vehicle needs attention — and automatically schedule the service around your dispatch calendar?"

### Opening for an automotive OEM
> "Your dealer network is your front line — but right now you're probably flying blind on what's happening at the store level until it shows up in monthly reports. What we're going to show you is a platform where you see pipeline, inventory, CSI, and service volume across every dealer in real time, and where your best-performing dealer's playbook can be deployed across all of them."
