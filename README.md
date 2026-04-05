# ESG Cost Exposure Model: Electricity + Carbon Pricing

## Overview

This project models electricity cost exposure across a multi-site portfolio and evaluates how carbon pricing affects total operating costs.

It integrates:
- Electricity cost (baseline operational expense)
- Carbon pricing scenarios (transition risk)
- QA/QC-validated datasets

The objective is to translate energy and emissions data into **financially material ESG risk insights**.

---

## Key Findings

- **Top cost exposure site**  
  DC_VA_01 → ~$1.8M total annual cost  
  Driven by both high electricity demand and carbon cost contribution

- **Transition risk concentration**  
  Industrial and data center sites (VA, TX, IL) show significant cost increases under carbon pricing scenarios (greater than 30%)

- **Lower exposure sites**  
  Smaller facilities (e.g., FARM_WI_01) remain primarily electricity-driven with limited carbon cost impact

---

## Analytical Insight

Electricity costs dominate baseline operations across all sites. However, carbon pricing significantly alters cost structures for high-load, high-emission facilities.

This creates two distinct exposure profiles:
- **Operational cost exposure** → electricity-driven
- **Transition risk exposure** → emissions and policy-driven

This distinction supports:
- ESG reporting (Scope 2 and transition risk)
- Capital allocation and prioritization
- Decarbonization strategy development

---

## Visualization

### Portfolio Transition Cost Exposure

![Electricity vs Carbon Cost](outputs/portfolio_transition_cost_exposure.png)

This visualization separates:
- Electricity cost (baseline)
- Carbon cost (policy-driven impact under mid scenario)

---

## Data Sources

- Portfolio electricity cost dataset (processed)
- State-level electricity price data (QA/QC validated)
- Carbon pricing scenario (mid-case assumption)

---

## Project Structure
