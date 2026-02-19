class ResponseFormatter:

    @staticmethod
    def interpret_confidence(score):
        if score >= 0.65:
            return "High Semantic Grounding"
        elif score >= 0.55:
            return "Moderate Semantic Grounding"
        else:
            return "Low Semantic Grounding"

    @staticmethod
    def extract_theme(results):

        if not results:
            return "General Philosophical Teaching"

        chapters = [r["chapter"] for r in results]
        combined_text = " ".join([r["verse_text"].lower() for r in results])

        # Count frequency
        chapter_counts = {}
        for ch in chapters:
            chapter_counts[ch] = chapter_counts.get(ch, 0) + 1

        dominant_chapter = max(chapter_counts, key=chapter_counts.get)
        dominance_ratio = chapter_counts[dominant_chapter] / len(chapters)

    # ----------------------------
    # STRONG KEYWORD SIGNALS
    # ----------------------------

        if any(word in combined_text for word in ["cosmic form", "vishvarupa"]):
            return "Vishvarupa (Cosmic Form)"

        if any(word in combined_text for word in ["meditation", "meditating", "yoga practice"]):
            return "Meditation & Discipline"

        if any(word in combined_text for word in ["renunciation", "renounce"]):
        # Only if Chapter 18 dominates
            if dominant_chapter == 18 and dominance_ratio >= 0.4:
                return "Renunciation & Liberation"

        if any(word in combined_text for word in ["devotion", "devoted", "worship", "bhakti"]):
            return "Bhakti (Devotion)"

        if any(word in combined_text for word in ["action", "duty", "karma"]):
            return "Karma Yoga (Action)"

        if any(word in combined_text for word in ["eternal", "self", "atman", "immortal"]):
            return "Self-Realization (Atman)"

    # ----------------------------
    # FALLBACK TO CHAPTER DOMINANCE
    # ----------------------------

        if dominance_ratio >= 0.6:
            theme_map = {
                11: "Vishvarupa (Cosmic Form)",
                12: "Bhakti (Devotion)",
                6: "Meditation & Discipline",
                18: "Renunciation & Liberation",
                3: "Karma Yoga (Action)",
                2: "Self-Realization (Atman)"
            }
            return theme_map.get(dominant_chapter, "General Philosophical Teaching")

        return "General Philosophical Teaching"

    @staticmethod
    def build_structured_response(response):

        confidence_score = response["confidence"]
        results = response["results"]

        theme = ResponseFormatter.extract_theme(results)
        confidence_label = ResponseFormatter.interpret_confidence(confidence_score)

        return {
            "theme": theme,
            "confidence_score": confidence_score,
            "confidence_label": confidence_label,
            "verses": results
        }
