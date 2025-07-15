### System Design

---

User (Mobile UI)
    ↓
Chat Frontend (React or HTML/CSS/JS)
    ↓
Backend (Node.js / Flask / Express)
    ↓
Chatbot Engine (OpenAI API or rule-based logic)
    ↓
Optional: Language Translator API

---

### User Flow Diagram

[User visits chatbot page]
        ↓
[Greets user + language selection]
        ↓
[User types health-related question]
        ↓
[System processes input]
        ↓
[Chatbot returns answer]
        ↓
[User continues or exits]


---

### Wireframe (Frontend Structure)

-------------------------------------------------
| Chat Header - "HealthBot"                     |
-------------------------------------------------
| Chat History Window                           |
| > Bot: Welcome! What language do you prefer?  |
| > User: English                               |
| > Bot: How can I help you today?              |
| > User: I have a fever                        |
| > Bot: Please describe your symptoms          |
-------------------------------------------------
| [Text Input Box]   [Send Button]              |
-------------------------------------------------
