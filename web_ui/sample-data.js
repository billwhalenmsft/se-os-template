"use strict";

window.SEOS_SAMPLE_DATA = Object.freeze({
  meta: {
    owner: "Demo Operator",
    mode: "local",
    classification: "synthetic"
  },
  signals: [
    {
      id: "SIG-001",
      title: "Contoso dispatch delays",
      description: "A fictional service team wants to reduce the time between case creation and technician assignment.",
      status: "Needs framing",
      tags: ["Contoso", "Field Service", "synthetic"]
    },
    {
      id: "SIG-002",
      title: "Fabrikam knowledge search",
      description: "A fictional support team wants grounded answers from an approved article library.",
      status: "Needs framing",
      tags: ["Fabrikam", "Customer Service", "synthetic"]
    }
  ],
  decisions: [
    {
      id: "DEC-001",
      title: "Choose the first success measure",
      description: "Recommendation: measure median dispatch time before adding additional workflow metrics.",
      status: "Needs owner input",
      tags: ["review-and-go", "L1"]
    }
  ],
  builds: [
    {
      id: "BLD-001",
      title: "Outcome frame example",
      description: "Run the deterministic local agent and review its objective, measures, and guardrails.",
      status: "Ready",
      tags: ["local", "reversible", "Python"]
    }
  ],
  library: [
    {
      id: "LIB-001",
      title: "Contoso field-service demo pattern",
      description: "A synthetic five-beat demo guide for dispatch optimization.",
      status: "Reviewed",
      tags: ["demo", "Field Service", "synthetic"],
      url: "demos/contoso-field-service.html"
    },
    {
      id: "LIB-002",
      title: "Fabrikam customer-service demo pattern",
      description: "A synthetic demo guide for grounded knowledge assistance.",
      status: "Reviewed",
      tags: ["demo", "Customer Service", "synthetic"],
      url: "demos/fabrikam-customer-service.html"
    }
  ]
});
