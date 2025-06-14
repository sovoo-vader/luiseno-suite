
import streamlit as st

st.set_page_config(page_title="Luiseño Language Toolkit", layout="wide")
st.title("🌿 Luiseño Language Toolkit")
st.markdown("Select a tool from the sidebar to begin.")

tool = st.sidebar.selectbox("Choose a Tool", [
    "LuisenoMorphoEngine",
    "LuisenoSentenceSynth",
    "MorphemeClassifier",
    "LuisenoFlashBuilder",
    "LuisenoPronunciationSynth",
    "MorphGlossAligner"
])

if tool == "LuisenoMorphoEngine":
    st.header("🔡 Morpheme Analyzer & Generator")
    word = st.text_input("Enter Luiseño word to analyze:")
    if word:
        suffixes = ["lut", "kutum", "la", "ni", "qa", "muna"]
        enclitics = ["ku", "kam", "kun", "qay"]
        noun_suffixes = ["mal", "tum", "pi", "ka", "sh"]
        for form in suffixes + enclitics + noun_suffixes:
            if form in word:
                st.write(f"✅ Found morpheme '{form}'")

elif tool == "LuisenoSentenceSynth":
    st.header("🗣️ Sentence Synthesizer")
    subj = st.selectbox("Subject Pronoun", ["1sg", "2sg", "3sg"])
    verb = st.selectbox("Verb", ["see", "sing", "learn", "hear"])
    obj = st.selectbox("Object", ["bear", "song", "mother", "boy", None])
    tense = st.selectbox("Tense", ["present", "past", "future"])
    if st.button("Generate Sentence"):
        prefix = {"1sg": "no", "2sg": "'o", "3sg": "po"}[subj]
        verb_map = {"see": "qawaq", "sing": "heelaq", "learn": "pilaachaq", "hear": "naqmaq"}
        suffix_map = {"present": "qa", "past": "ni", "future": "lut"}
        verb_phrase = prefix + verb_map[verb] + suffix_map[tense]
        if obj:
            st.success(f"{prefix} {obj}pi {verb_phrase}")
        else:
            st.success(f"{prefix} {verb_phrase}")

elif tool == "MorphemeClassifier":
    st.header("🧬 Morpheme Classifier")
    morph = st.text_input("Enter morpheme:")
    morph_dict = {
        "qa": "Aspectual – present/hypothetical", "ni": "Tense – past",
        "lut": "Tense – future", "tum": "Plural", "pi": "Object case",
        "sh": "Instrumental", "mal": "Feminine noun", "ku": "Question",
        "kam": "Imperative", "kun": "Complementizer", "qay": "Negation",
        "muna": "Modal", "ka": "Locative", "no": "my", "po": "his", "yo": "your"
    }
    if morph:
        st.info(morph_dict.get(morph, "Unknown or unclassified morpheme"))

elif tool == "LuisenoFlashBuilder":
    st.header("🃏 Flashcard Trainer")
    vocab = {
        "person": "'ataax", "dog": "'avaal", "bird": "'ehengmay", "bear": "hunwut", "basket": "tukmal"
    }
    english = st.selectbox("Translate this:", list(vocab.keys()))
    user_input = st.text_input("Your Luiseño answer:")
    if user_input:
        if user_input == vocab[english]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Nope. It’s {vocab[english]}.")

elif tool == "LuisenoPronunciationSynth":
    st.header("🔊 Pronunciation Helper")
    word = st.text_input("Luiseño word:")
    phoneme_guide = {
        "aa": "like 'father'", "ee": "like 'bed'", "ii": "like 'machine'", "oo": "like 'bore'",
        "uu": "like 'moon'", "ch": "as in 'church'", "sh": "as in 'ship'", "ng": "as in 'sing'",
        "x": "rough h, like Spanish 'j'", "'": "glottal stop", "v": "like soft w", "r": "flap like Spanish r"
    }
    if word:
        for ph in phoneme_guide:
            if ph in word:
                st.markdown(f"🔹 **{ph}** → {phoneme_guide[ph]}")

elif tool == "MorphGlossAligner":
    st.header("🔠 Gloss Alignment")
    lw = st.text_input("Luiseño word (e.g. 'nohunwutqa'):")
    gloss = st.text_input("English gloss (e.g. 'my bear is'):")
    if lw and gloss:
        known = {"no": "my", "hunwut": "bear", "qa": "is", "ni": "was", "pi": "object marker"}
        found = [f"{k} → {v}" for k, v in known.items() if k in lw]
        if found:
            st.markdown("🔍 **Alignments Found:**")
            for f in found:
                st.write("🔸 " + f)
        else:
            st.warning("⚠️ No known morphemes found.")
