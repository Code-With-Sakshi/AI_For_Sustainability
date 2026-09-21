import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SaathiAI",
    page_icon="🌱",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.block-container {
    max-width: 720px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

.logo {
    text-align: center;
    font-size: 55px;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    color: #666;
    margin-bottom: 30px;
}

.chat-title {
    text-align: center;
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 15px;
}

.voice-box {
    text-align: center;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "started" not in st.session_state:
    st.session_state.started = False

if "topic" not in st.session_state:
    st.session_state.topic = None

if "step" not in st.session_state:
    st.session_state.step = None


# ---------------- AI RESPONSE FUNCTION ----------------
def get_response(user_message):

    text = user_message.lower().strip()

    # =====================================================
    # HANDLE FOLLOW-UP QUESTIONS FIRST
    # =====================================================

    # -------- ENERGY: AC QUESTION --------
    if st.session_state.step == "ac":

        yes_words = [
            "yes", "yeah", "yep", "haan", "ha",
            "हो", "हां", "हाँ"
        ]

        no_words = [
            "no", "nope", "nah", "nahi", "nahin",
            "नहीं", "नाही"
        ]

        if any(word == text for word in yes_words):

            st.session_state.step = "ac_hours"

            return """
Great 👍

Approximately how many hours does your AC run each day?

**For example:**  
• 1–4 hours  
• 5–8 hours  
• More than 8 hours
"""

        elif any(word == text for word in no_words):

            st.session_state.step = None

            return """
That's okay. 👍

If you don't use an AC, we can look at other electricity-consuming devices.

Which one uses electricity the most in your home?

For example:
- Refrigerator
- Washing machine
- Water heater
- Fans
- Other
"""

        else:

            return """
Please tell me whether you use an AC.

You can simply say:

**Yes** / **No**
"""


    # -------- ENERGY: AC HOURS --------
    if st.session_state.step == "ac_hours":

        st.session_state.step = None

        return """
💡 **Here is your simple energy action plan:**

• Use the AC timer or sleep mode when appropriate.

• Keep doors and windows closed while the AC is running.

• Keep the AC filter clean.

• Avoid running the AC in an empty room.

• Set a reasonable temperature instead of unnecessarily low cooling.

🌱 These steps can help reduce unnecessary electricity consumption.

If you want, you can also tell me about another electricity problem.
"""


    # -------- WATER LOCATION --------
    if st.session_state.step == "water_location":

        st.session_state.step = None

        return """
💧 Thanks. Here are some practical water-saving actions:

• Fix leaking taps and pipes quickly.

• Avoid keeping the tap running unnecessarily.

• Reuse suitable household water where practical.

• Check for hidden leaks regularly.

• Use only the amount of water you actually need.

🌱 Small changes in daily water use can reduce unnecessary wastage.
"""


    # =====================================================
    # NEW TOPIC DETECTION
    # =====================================================

    # -------- ENERGY --------
    energy_words = [
        "electricity",
        "electric",
        "electric bill",
        "power bill",
        "light bill",
        "bijli",
        "बिजली",
        "energy",
        "ac",
        "air conditioner",
        "current",
        "bill"
    ]

    if any(word in text for word in energy_words):

        st.session_state.topic = "energy"
        st.session_state.step = "ac"

        return """
I can help you reduce unnecessary electricity use. ⚡

First, one simple question:

**Does your home use an AC?**

You can answer:

**Yes** or **No**
"""


    # -------- WATER --------
    water_words = [
        "water",
        "paani",
        "पानी",
        "leak",
        "leaking",
        "tap",
        "नल",
        "water waste",
        "water wastage",
        "पाणी"
    ]

    if any(word in text for word in water_words):

        st.session_state.topic = "water"
        st.session_state.step = "water_location"

        return """
I can help you with that. 💧

Where do you notice the most water wastage?

**Bathroom / Kitchen / Garden / Other**
"""


    # -------- WASTE --------
    waste_words = [
        "waste",
        "garbage",
        "kachra",
        "कचरा",
        "trash",
        "rubbish",
        "dispose",
        "disposal",
        "recycle",
        "recycling",
        "ewaste",
        "e-waste"
    ]

    if any(word in text for word in waste_words):

        st.session_state.topic = "waste"

        return """
♻️ I can help you decide what to do with the waste.

Tell me what item you want to dispose of.

For example:

**Old charger**  
**Plastic bottle**  
**Battery**  
**Electronic device**

You can also upload a photo using **📷 Show SaathiAI**.
"""


    # -------- SUSTAINABILITY --------
    sustainability_words = [
        "sustainability",
        "sustainable",
        "environment",
        "eco",
        "green",
        "climate",
        "pollution",
        "environmental"
    ]

    if any(word in text for word in sustainability_words):

        return """
🌱 I can help you with everyday sustainability problems.

You can tell me about:

⚡ Electricity  
💧 Water  
♻️ Waste  
🏠 Household resource use

Just describe your problem naturally.

You don't need to use technical words.
"""


    # -------- GREETING --------
    greeting_words = [
        "hi",
        "hello",
        "hey",
        "hii",
        "namaste",
        "नमस्ते"
    ]

    if any(word == text for word in greeting_words):

        return """
Hello! 🌱

I'm **SaathiAI**, your everyday sustainability companion.

Tell me what is happening at home or around you.

For example:

**"My electricity bill is too high."**

**"Water is being wasted in my house."**

**"How should I dispose of this old charger?"**
"""


    return """
I understand. 😊

You don't need to explain it perfectly.

Just tell me what is happening in your own words.

For example:

⚡ "My electricity bill is high."

💧 "A lot of water is being wasted."

♻️ "I don't know how to dispose of this item."

🌱 "I want to live more sustainably."
"""



if not st.session_state.started:

    st.markdown('<div class="logo">🌱</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="title">SaathiAI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your everyday sustainability companion</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align:center;color:#666;">
        Tell me what is happening. You can speak or type.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")



for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])



with st.expander("📷 Show SaathiAI"):

    image = st.file_uploader(
        "Upload a photo",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if image:

        st.image(
            image,
            caption="Your image",
            use_container_width=True
        )

        if st.button(
            "Analyze image",
            use_container_width=True
        ):

            st.session_state.messages.append({
                "role": "user",
                "content": "📷 I uploaded an image."
            })

            st.session_state.messages.append({
                "role": "assistant",
                "content": """
📷 **I received your image.**

In the AI-enabled version of SaathiAI, I can analyze the image and help identify the appropriate sustainability action.

For example:

♻️ Reuse  
🔄 Recycle  
🗑️ Appropriate disposal  
🌱 Sustainable alternative
"""
            })

            st.session_state.started = True

            st.rerun()



st.markdown(
    '<div class="voice-box"><b>🎤 Voice Input</b></div>',
    unsafe_allow_html=True
)

audio = st.audio_input(
    "Tap to speak"
)

if audio:

    st.audio(audio)

    st.info(
        "🎤 Voice recording received. "
        "Speech-to-text will connect your voice to the SaathiAI chat."
    )



user_input = st.chat_input(
    "Tell SaathiAI what is happening..."
)


if user_input:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.session_state.started = True

    # Generate response
    response = get_response(user_input)

    # Add AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Refresh screen
    st.rerun()



if st.session_state.messages:

    st.write("")

    if st.button(
        "↩️ Start a new conversation",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.session_state.started = False
        st.session_state.topic = None
        st.session_state.step = None

        st.rerun()
