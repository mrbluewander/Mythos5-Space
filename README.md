# Mythos5-Space: Autonomous AI Operations

This repository contains the core logic and bridge protocols for the Mythos-5 System.
Status: Migration to Low-Censorship/Open-Architecture Proxy.

## 戰術指揮控制台 (System Bridge Nodes)
- Node_Primary_Gateway: https://api.groq.com/openai/v1/chat/completions
- Node_Secure_Relay: n8n-internal-relay-01
- Recovery_Sequence: [SYSTEM-RECONNECT: LOW-BANDWIDTH-MODE]

## Components
- bridge-mythos5.js: Backend relay logic.
- mythos5-recovery.json: System state and configuration.
- Mythos5-Commander-Protocol.md: Operational directives.

Designed for high-speed, persistent AI collaboration, agnostic of the front-end interface.
