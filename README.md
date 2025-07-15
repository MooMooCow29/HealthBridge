# HealthBridge
A chatbot and clinic locator for healthcare-scarce regions

---

### Problem Background

---

#### Problem

Sub-Saharan Africa faces a persistent healthcare crisis. Over **600 million people** lack access to essential medical services \[6]. Despite holding **16% of the world’s population**, the region receives only **1% of global health expenditure** while carrying **23% of the global disease burden** \[6]\[7]. Structural challenges — such as limited infrastructure, understaffed facilities, and rural isolation — severely restrict access to timely care \[6].

---

#### Existing Solutions

Digital health tools, particularly **AI-powered chatbots**, are emerging as scalable, cost-effective ways to extend basic healthcare access across underserved regions. These chatbots are capable of delivering:

* Symptom triage
* Health education
* Chronic condition support (e.g., diabetes, hypertension)
* Mental health first aid

A successful case is the *GREAT4Diabetes* WhatsApp chatbot deployed in South Africa during COVID-19. Over **8,000 patients** used the service, and **71%** of engaged users reported improved diabetes self-care \[2]. **88%** felt more confident managing their condition, and healthcare providers observed reduced pressure on clinics \[2].

---

#### Gaps & Opportunities

Despite early successes, chatbot adoption across Africa remains sparse. A 2023 scoping review found **only 12 published studies** from 2017 to 2022 that focused on health chatbots in Africa \[1]. Most were informational, with few measuring health outcomes.

Key barriers include:

* Limited digital access and poor internet coverage \[1]
* Low trust in AI-driven tools \[1]\[5]
* Lack of local language support \[1]
* Data privacy and governance issues \[3]\[4]

Nevertheless, recent literature emphasizes the potential for community-oriented, culturally sensitive, and low-data chatbot systems to bridge the healthcare gap — especially when designed with equity, accessibility, and trust in mind \[4]\[5].

---

### Solution Summary

This project introduces a lightweight, AI-powered chatbot designed to improve access to basic healthcare services in underserved regions of Sub-Saharan Africa. The chatbot delivers multilingual support for health education, symptom triage, and chronic disease self-management—tailored for users with limited digital literacy and poor connectivity. It is accessible via mobile-optimized web chat and aims to reduce the burden on local clinics by empowering individuals with self-care tools.

---

### Who It Helps

* Rural and low-income communities in Sub-Saharan Africa with limited access to clinics or hospitals
* Patients with chronic illnesses who need reliable guidance but cannot frequently visit healthcare providers
* Non-English speakers needing local language support for health information
* Health workers and NGOs looking for scalable digital tools to reach wider populations
* Governments and policy makers seeking data-driven insights to understand healthcare needs and gaps

---


### Key Features (MVP focus)

---

| Feature                       | Priority | Notes                                              |
| ----------------------------- | -------- | -------------------------------------------------- |
| Symptom Checker Chatbot       | ✅ High   | Based on simple yes/no Q\&A; no complex NLP needed |
| Clinic Locator (by location)  | ✅ High   | Hardcoded or static JSON-based data if needed      |
| Responsive Frontend UI        | ✅ High   | Mobile-first design, text-based UI                 |
| Clear Guidance/Emergency Info | ✅ High   | Simple messages like “Call emergency services”     |
| README & Docs                 | ✅ High   | Explain setup + use case clearly                   |
| 5-Minute Video                | ✅ High   | Explain what, who, how, why, and short demo        |

---

### Tech Stack (Lean + Fast)

---

| Layer         | Tech                         | Reason                                    |
| ------------- | ---------------------------- | ----------------------------------------- |
| Frontend      | HTML/CSS/JavaScript          | Fast to build, responsive for all devices |
| Backend       | Python (Flask or FastAPI)    | Simple routing, fast API dev              |
| Chatbot Logic | Python Decision Tree         | No AI, simple rules = faster execution    |
| Location API  | OpenStreetMap/Nominatim      | Free & easy location search               |
| Hosting       | GitHub Pages + Replit/Render | Free + quick deploy options               |
| Data Storage  | JSON or SQLite               | Keep it static for MVP                    |


---

### References

1. Phiri, B., & Munoriyarwa, A. (2023). *Health Chatbots in Africa: A Scoping Review*. JMIR Human Factors, 10, e41229. [https://doi.org/10.2196/41229](https://doi.org/10.2196/41229)
2. Mash, B., et al. (2022). *Evaluation of a WhatsApp Chatbot for Diabetes Care During COVID-19 in South Africa*. Journal of Medical Internet Research, 24(9), e38972. [https://doi.org/10.2196/38972](https://doi.org/10.2196/38972)
3. Njei, B., et al. (2023). *Artificial Intelligence in African Healthcare: A Scientometric Analysis*. Healthcare (Basel), 11(1), 82. [https://doi.org/10.3390/healthcare11010082](https://doi.org/10.3390/healthcare11010082)
4. Abdulsalam, Y. A., et al. (2025). *Challenges and Opportunities for AI in African Health Systems*. African Journal of Health Informatics. \[Preprint]
5. Laymouna, A., et al. (2024). *Roles and Limitations of Chatbots in Global Health*. Healthcare (Basel), 12(3), 271. [https://doi.org/10.3390/healthcare12030271](https://doi.org/10.3390/healthcare12030271)
6. WHO Africa. (2022). *Universal Health Coverage in Africa: A Framework for Action*. World Health Organization. [https://www.afro.who.int](https://www.afro.who.int)
7. World Bank. (2023). *Healthcare Access and Quality in Sub-Saharan Africa: An Overview*. [https://www.worldbank.org/en/topic/health](https://www.worldbank.org/en/topic/health)

---
