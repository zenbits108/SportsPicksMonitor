# Sports Picks Monitor

**Automated Telegram → OCR → Pick Intelligence Pipeline**

This project monitors sports-handicapper Telegram channels, extracts picks from image posts, 
and converts them into structured data for analysis.  

### 🔭 Design Philosophy
- **Transparency:** all steps from capture → parse → store → report are inspectable.  
- **Safety:** complies with Telegram ToS (read-only user account, throttled API calls).  
- **Expandability:** modular layout ready for future AI models, APIs, dashboards.  
- **Reproducibility:** deterministic Docker build for Linux/Mint/Ubuntu.  

Phase 1 → Capture & Parse  
Phase 2 → Scoring & Confidence Modeling  
Phase 3 → Dashboards & Reporting  

