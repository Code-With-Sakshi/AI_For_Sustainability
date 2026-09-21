# 🌱 SaathiAI

### Just tell us. We'll help you act sustainably.

SaathiAI is a low-effort, multimodal AI sustainability assistant designed to help users make everyday sustainable decisions through simple **voice, text, and image-based interaction**.

The project focuses on people who may have limited digital literacy or may prefer simple, conversational interaction instead of complex forms and menus.

---

## 🎯 Problem Statement

Sustainability information is widely available, but many people still find it difficult to turn that information into everyday action.

Common barriers include:

- Complex digital interfaces
- Difficulty typing detailed questions
- Language and communication barriers
- Information overload
- Lack of personalized guidance
- Uncertainty about what action to take next

SaathiAI addresses this gap by allowing users to explain a problem naturally and guiding them toward a simple, practical action.

---

## 💡 Solution

SaathiAI follows a human-centered AI workflow:

```text
User Input
Voice / Text / Image
        ↓
AI Understanding
Intent + Context
        ↓
Agent Logic
        ↓
Ask Question / Retrieve Knowledge / Analyze Image
        ↓
RAG Layer
Trusted Sustainability Knowledge
        ↓
Personalized Recommendation
        ↓
Sustainable Action
```

### Core principle

> Don't make people learn technology. Make technology understand people.

---

## 🤖 AI Components

### 1. Natural Language Understanding

SaathiAI accepts everyday language instead of requiring users to use technical terms.

Example:

> "Mera electricity bill bahut zyada aa raha hai."

The system identifies this as an energy-related problem.

### 2. Agent Logic

The agent decides what should happen next.

For example:

```text
Electricity problem
       ↓
Does the user use AC?
       ↓
Yes
       ↓
How many hours?
       ↓
Retrieve relevant knowledge
       ↓
Generate recommendation
```

The prototype uses state-based decision logic to demonstrate this workflow.

### 3. RAG — Retrieval-Augmented Generation

SaathiAI retrieves relevant information from a curated sustainability knowledge base before producing guidance.

```text
User Question
     ↓
Retrieve Relevant Knowledge
     ↓
Trusted Context
     ↓
Generate Response
```

This helps ground recommendations in predefined sustainability information instead of relying only on general model knowledge.

### 4. Multimodal Interaction

The planned system supports:

- 🎤 Voice
- 💬 Text
- 📷 Images

The current prototype demonstrates voice recording and image upload interfaces. Speech-to-text and production-grade image understanding can be connected in a later stage.

---

## 📚 Knowledge Base

The project includes `knowledge_base.txt`.

It contains sustainability information covering:

- Energy conservation
- Water conservation
- Waste management
- Electronic waste
- Sustainable consumption

For a production system, the knowledge base should be expanded using reliable sources such as official government, UN, and other verified sustainability resources.

---

## 🧠 Example User Flow

### Example 1 — Energy

**User:**

> My electricity bill is very high.

**SaathiAI:**

> Does your home use an AC?

**User:**

> Yes.

**SaathiAI:**

> Approximately how many hours does your AC run each day?

**User:**

> 8 hours.

**SaathiAI:**

> Provides a personalized energy-saving action plan.

---

### Example 2 — Water

**User:**

> A lot of water is being wasted in my house.

**SaathiAI:**

> Where do you notice the most water wastage — bathroom, kitchen, garden, or somewhere else?

The system then provides relevant water-saving actions.

---

### Example 3 — Waste

**User:**

> I don't know how to dispose of my old charger.

SaathiAI can identify the problem as an electronic-waste question and guide the user toward appropriate e-waste handling.

---

## 🛠️ Technology Stack

- Python
- Streamlit
- Scikit-learn
- TF-IDF based retrieval for the RAG prototype
- Streamlit session state for conversation/agent state
- Text knowledge base

### Planned / extendable AI layer

The prototype architecture can be extended with:

- IBM Granite or another approved LLM
- Speech-to-text
- Multilingual interaction
- Vision/image understanding
- More advanced vector search
- Production RAG pipeline

---

## 📁 Project Structure

```text
SaathiAI/
│
├── app.py
├── rag_demo.py
├── agent_demo.py
├── knowledge_base.txt
├── requirements.txt
└── README.txt
```

If the agent and RAG demos are combined into one application, the files can be merged into a single Streamlit application.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SaathiAI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the main application

```bash
streamlit run app.py
```

### 4. Run the RAG demonstration

```bash
streamlit run rag_demo.py
```

### 5. Run the Agent Logic demonstration

```bash
streamlit run agent_demo.py
```

---

## 🌱 SDG Alignment

### Primary SDG

**SDG 12 — Responsible Consumption and Production**

SaathiAI encourages responsible use of:

- Electricity
- Water
- Household resources
- Consumer products
- Electronic waste

### Supporting SDGs

**SDG 6 — Clean Water and Sanitation**

Encourages responsible water use.

**SDG 7 — Affordable and Clean Energy**

Provides guidance for reducing unnecessary energy consumption.

**SDG 11 — Sustainable Cities and Communities**

Supports sustainable everyday practices within households and communities.

---

## 👥 Target Users

SaathiAI is designed for:

- People with limited digital literacy
- Voice-first users
- Users who prefer local-language interaction
- Households seeking practical sustainability guidance
- Users who find complex applications difficult to navigate
- People who want simple, actionable sustainability advice

---

## 🔐 Responsible AI

### Privacy

Only necessary information should be collected. Personal conversations and images should not be unnecessarily stored.

### Fairness and Accessibility

The system should not assume that all users have the same language, digital skills, resources, or living conditions.

### Transparency

Users should know when recommendations are AI-generated.

### Reliable Information

Recommendations should be grounded in a curated and verified knowledge base where possible.

### Human Control

SaathiAI provides decision support. The final decision remains with the user.

---

## 📊 Expected Impact

### Environmental

- Encourage responsible water use
- Encourage efficient energy use
- Promote appropriate waste handling
- Encourage sustainable consumption

### Social

- Reduce barriers caused by complex digital interfaces
- Make sustainability guidance easier to access
- Support conversational interaction

### Behavioral

Convert:

```text
"I have a problem"
        ↓
"I understand the problem"
        ↓
"I know what to do"
        ↓
"I can take action"
```

---

## 📈 Possible Evaluation Metrics

The prototype can be evaluated using:

- Number of interactions needed to reach useful guidance
- User understanding
- User satisfaction
- Successful completion of recommended actions
- Reported change in resource-use behavior
- Accuracy/relevance of retrieved knowledge

---

## ⚠️ Prototype Limitations

This is a prototype and not a production sustainability advisory system.

Current limitations include:

- Voice recording is demonstrated, but speech-to-text requires an additional service/model.
- Image upload is demonstrated, but full image understanding requires a vision model.
- The RAG prototype uses TF-IDF retrieval rather than a production vector database.
- Agent behavior is demonstrated using state-based logic.
- The knowledge base is intentionally small for demonstration.
- Sustainability recommendations should be validated against authoritative local guidance before real-world deployment.

---

## 🔮 Future Scope

- IBM Granite integration
- Speech-to-text and text-to-speech
- Hindi and Marathi support
- Multimodal image understanding
- Vector database and semantic retrieval
- Source citations in answers
- Personalized sustainability history
- Follow-up tracking
- Local sustainability guidelines
- Human escalation for uncertain or high-impact cases

---

## 👩‍💻 Project

**Project:** SaathiAI  
**Theme:** AI + Sustainability  
**Primary SDG:** SDG 12 — Responsible Consumption and Production

Built as an AI + Sustainability prototype demonstrating human-centered AI, RAG, agent logic, and multimodal interaction.
