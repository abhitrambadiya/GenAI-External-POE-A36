"""Sample Grounding Documents and Research Library for Research Analyst Agents.

Contains authentic research benchmarks, macroeconomic data, semiconductor market forecasts,
enterprise software metrics, clean tech economics, and biotech pipeline valuations.
"""

from typing import Any, Dict, List

SAMPLE_DOCUMENTS: List[Dict[str, Any]] = [
    {
        "id": "semi-ai-infra-2024",
        "title": "Global Semiconductor & AI Infrastructure Market Outlook (2024-2028)",
        "category": "Semiconductors & AI Hardware",
        "keywords": [
            "semiconductor",
            "gpu",
            "ai",
            "hardware",
            "tsmc",
            "nvidia",
            "datacenter",
            "capex",
            "hbm",
            "advanced packaging",
            "cowos",
            "silicon",
        ],
        "summary": (
            "Comprehensive market analysis on hyperscaler CapEx allocation, GPU accelerator demand, "
            "High Bandwidth Memory (HBM3e/HBM4) supply elasticity, and advanced packaging constraints."
        ),
        "content": (
            "Key Industry Metrics & Findings:\n"
            "1. Hyperscaler CapEx Growth: Aggregate capital expenditure among Tier-1 cloud service providers "
            "(Microsoft, Google, AWS, Meta) increased by 42% YoY in 2024 to surpass $180B, with over 55% "
            "specifically allocated to AI server infrastructure and networking.\n"
            "2. Accelerator Market Sizing: The AI accelerator total addressable market (TAM) is projected to expand "
            "from $65B in 2023 to $280B by 2028, representing a compound annual growth rate (CAGR) of 34.2%.\n"
            "3. Supply Chain Bottlenecks: Advanced packaging capacity (TSMC CoWoS) remains the primary critical path. "
            "Capacity expansions from 35,000 wafers/month in early 2024 are on track to exceed 75,000 wafers/month by 2026.\n"
            "4. Memory Density: HBM3e and next-gen HBM4 content per server node is growing at 68% annually, driving "
            "record gross margins for memory suppliers (SK Hynix, Micron, Samsung).\n"
            "5. Strategic Risk: Power density limits (40-100 kW per rack) are shifting data center construction bottlenecks "
            "from chip availability to grid interconnection queues and liquid cooling adoption."
        ),
    },
    {
        "id": "saas-valuation-benchmarks",
        "title": "Enterprise SaaS Benchmarks: Net Retention, Rule of 40 & Valuation Multiples",
        "category": "Software & Cloud Services",
        "keywords": [
            "saas",
            "software",
            "net retention",
            "arr",
            "rule of 40",
            "churn",
            "valuation",
            "ev/revenue",
            "gross margin",
            "cac payback",
            "multiples",
        ],
        "summary": (
            "Empirical study analyzing median and upper-quartile B2B software performance, CAC payback velocity, "
            "and Enterprise Value to Next-Twelve-Months (EV/NTM) revenue multiple adjustments."
        ),
        "content": (
            "Key Valuation & Operational Metrics:\n"
            "1. Multiple Compression & Normalization: Median public B2B SaaS multiples have stabilized at 6.1x EV/NTM Revenue, "
            "down from the 2021 historical peak of 17.4x, reflecting higher cost of capital and focus on free cash flow.\n"
            "2. Top-Quartile Performance: Elite software businesses (>15x EV/NTM) consistently demonstrate: "
            "Net Revenue Retention (NRR) >= 120%, Gross Margins >= 78%, and Free Cash Flow (FCF) margins >= 22%.\n"
            "3. Rule of 40 Metric: The median across 120 surveyed public software firms is 36% (Revenue Growth % + FCF Margin %). "
            "Firms surpassing the 40% threshold trade at a 65% valuation premium compared to peers below 30%.\n"
            "4. Unit Economics: Median Customer Acquisition Cost (CAC) payback period is 18.5 months for mid-market and "
            "24.0 months for enterprise contracts. Annual churn rates remain bounded at 4.5% to 7.0% for mission-critical core platforms.\n"
            "5. Efficiency Ratios: Average ARR generated per full-time employee (ARR/FTE) for high-performing operators stands at $340,000."
        ),
    },
    {
        "id": "macro-monetary-policy-2024",
        "title": "Macroeconomic Bulletin: Interest Rate Cycles, Central Bank Policy & Liquidity",
        "category": "Macroeconomics & Monetary Policy",
        "keywords": [
            "macroeconomic",
            "inflation",
            "interest rate",
            "fed",
            "ecb",
            "liquidity",
            "yield curve",
            "treasury",
            "monetary policy",
            "quantitative tightening",
            "gdp",
        ],
        "summary": (
            "Quarterly macroeconomic assessment of Federal Reserve interest rate pathways, sovereign yield curve "
            "dynamics, balance sheet runoff (QT), and cross-asset liquidity transmission."
        ),
        "content": (
            "Macroeconomic Analysis & Empirical Indicators:\n"
            "1. Neutral Rate (r*) Dynamics: The real neutral rate of interest is estimated to have shifted upward from 0.5% "
            "pre-pandemic to approximately 1.25%-1.50%, suggesting a nominal policy terminal floor of 3.25%-3.50%.\n"
            "2. Yield Curve Transmission: The 2Y/10Y U.S. Treasury spread disinversion signifies late-cycle transition rather than "
            "immediate monetary easing, with term premium returning to positive territory (+35 to +50 bps).\n"
            "3. Balance Sheet Roll-off: Quantitative tightening (QT) has withdrawn over $1.7T in banking system liquidity, with "
            "Overnight Reverse Repo (ON RRP) facility balances stabilizing near baseline friction thresholds ($150B-$250B).\n"
            "4. Corporate Debt Maturity Wall: An estimated $1.9T in corporate speculative-grade debt matures through 2026, "
            "creating an average refinancing headwind of +210 bps in debt service costs.\n"
            "5. Global Growth Outlook: Global real GDP expansion is modeled at 3.1% YoY, constrained by demographic headwinds "
            "and structural energy transition capital reallocation."
        ),
    },
    {
        "id": "clean-energy-battery-economics",
        "title": "Global Clean Energy Transition & Battery Technology Economics",
        "category": "Energy & Industrial Technology",
        "keywords": [
            "clean energy",
            "battery",
            "ev",
            "lithium",
            "solar",
            "storage",
            "grid",
            "lcoe",
            "renewable",
            "bess",
            "energy transition",
        ],
        "summary": (
            "Techno-economic review of battery cell pack cost curves ($/kWh), Levelized Cost of Energy (LCOE), "
            "and utility-scale Battery Energy Storage Systems (BESS) project IRR."
        ),
        "content": (
            "Key Industry Metrics & Cost Curves:\n"
            "1. Battery Pack Cost Curve: Volume-weighted average lithium-ion battery pack prices declined to $118/kWh in 2024, "
            "driven by lithium carbonate price normalization ($14,000/ton) and rapid adoption of cathode-efficient LFP chemistries.\n"
            "2. Levelized Cost of Energy (LCOE): Utility-scale photovoltaic solar + 4-hour battery storage achieved an unsubsidized "
            "LCOE of $52-$68/MWh, outcompeting open-cycle gas peakers ($110-$180/MWh) in major wholesale electricity markets.\n"
            "3. Utility-Scale Storage Deployment: Global BESS capacity additions are growing at 38% CAGR, with installations "
            "forecast to exceed 160 GWh annually by 2027.\n"
            "4. Manufacturing Capacity Distribution: Mainland China retains 74% of global cathode active material processing, while "
            "U.S. and European domestic content mandates (IRA Section 45X) are incentivizing localized supply chain capex.\n"
            "5. Project Financials: Standard 100MW/400MWh merchant BESS assets in deregulated grids (ERCOT, CAISO) yield levered IRRs "
            "between 13.5% and 17.0%, driven by ancillary service revenue stacking and day-ahead wholesale price arbitrage."
        ),
    },
    {
        "id": "cybersecurity-zero-trust-intel",
        "title": "Cybersecurity Market Intelligence: Zero Trust & AI-Driven Threat Defense",
        "category": "Cybersecurity & Enterprise Infrastructure",
        "keywords": [
            "cybersecurity",
            "zero trust",
            "siem",
            "soc",
            "endpoint",
            "security",
            "threat",
            "ransomware",
            "cloud security",
            "xdr",
            "identity",
        ],
        "summary": (
            "Strategic industry forecast analyzing enterprise cyber budget resilience, vendor consolidation into platforms, "
            "and AI-assisted incident response efficacy."
        ),
        "content": (
            "Market Findings & Spend Distribution:\n"
            "1. Spending Durability: Enterprise cybersecurity budgets exhibited zero net shrinkage in 2024, maintaining 11.8% YoY growth "
            "and representing 12.5% of overall corporate IT expenditure.\n"
            "2. Platform Consolidation Wave: Over 71% of enterprise CISOs surveyed actively report consolidating point security solutions "
            "into unified XDR (Extended Detection & Response) and SASE (Secure Access Service Edge) architecture.\n"
            "3. Market Sizing: The global cybersecurity market is on track to expand from $190B in 2023 to $310B by 2028 (10.3% CAGR).\n"
            "4. AI-Augmented Operations: Automated AI threat triage has demonstrated a 45% reduction in mean time to detect (MTTD) "
            "and a 58% reduction in mean time to remediate (MTTR) high-severity ransomware incursions.\n"
            "5. Identity as the Perimeter: Identity and Access Management (IAM) and Privileged Access Management (PAM) represent "
            "the fastest-growing sub-segments at 15.6% CAGR, catalyzed by credential theft in hybrid cloud deployments."
        ),
    },
    {
        "id": "biotech-pharma-pipeline-valuation",
        "title": "Biotechnology & Pharmaceutical R&D Pipeline Valuation Frameworks",
        "category": "Life Sciences & Healthcare Biotechnology",
        "keywords": [
            "biotech",
            "pharma",
            "clinical trials",
            "fda",
            "pipeline",
            "valuation",
            "r&d",
            "patents",
            "glp-1",
            "oncology",
            "rnpv",
        ],
        "summary": (
            "Methodology for risk-adjusted Net Present Value (rNPV) modeling, phase probability transitions, "
            "and patent exclusivity cliffs in commercial biopharmaceuticals."
        ),
        "content": (
            "Pipeline Valuation Parameters & Clinical Metrics:\n"
            "1. Cumulative Approval Probability: Across all indications, the cumulative probability of clinical phase success from "
            "Phase I to FDA regulatory approval is 8.2% (Oncology lowest at 5.3%, Rare Diseases highest at 16.4%).\n"
            "2. rNPV Discount Parameters: Industry cost of capital (WACC) applied to pre-commercial clinical pipelines ranges from "
            "11.5% to 14.0%, incorporating binary developmental, regulatory, and patent trial outcomes.\n"
            "3. Weight-Loss & Metabolic Expansion: The global GLP-1 receptor agonist market is projected to reach $115B by 2030, "
            "with cardiovascular and sleep apnea label expansions adding $28B in incremental peak sales.\n"
            "4. Patent Exclusivity Cliff: Large-cap pharmaceutical manufacturers face $185B in worldwide revenue exposure through 2028 "
            "due to Loss of Exclusivity (LoE) on marquee biologics, driving accelerated M&A premiums (median 55% over undisturbed equity value).\n"
            "5. R&D Capital Productivity: Average fully capitalized cost to bring a novel molecular entity to market currently stands at "
            "$2.18B, inclusive of post-approval safety commitments and pipeline abandonment costs."
        ),
    },
]

# Aliases for compatibility
SAMPLE_RESEARCH_DOCUMENTS = SAMPLE_DOCUMENTS
