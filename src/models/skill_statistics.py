class SkillStatistics:

    def calculate(self, matched, missing):

        total = len(matched) + len(missing)

        if total == 0:
            return {
                "matched_count": 0,
                "missing_count": 0,
                "match_percent": 0
            }

        percent = round((len(matched) / total) * 100, 2)

        return {

            "matched_count": len(matched),

            "missing_count": len(missing),

            "match_percent": percent

        }