class AICommerceService:
    """
    AI services boundary:
    SEO generation,
    product scoring,
    recommendations,
    translation,
    forecasting.
    """

    def generate_seo(self, title: str, keywords: list[str]) -> dict[str, str]:
        joined = ", ".join(keywords[:8])

        return {
            "title": f"{title} | Fast Global Delivery",
            "description": (
                f"Buy {title} with verified suppliers, "
                "secure checkout and AI-personalized deals."
            ),
            "keywords": joined
        }

    def score_product(
        self,
        margin: float,
        demand: float,
        competition: float
    ) -> float:

        return round(
            (margin * 0.45)
            + (demand * 0.40)
            - (competition * 0.15),
            3
        )
