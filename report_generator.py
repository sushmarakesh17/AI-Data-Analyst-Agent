import os
from datetime import datetime


class ReportGenerator:
    def __init__(self):
        self.output_dir = "outputs/reports"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_report(self, analysis_text):
        """
        Save AI analysis as a text report.
        """

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = os.path.join(
            self.output_dir,
            f"analysis_report_{timestamp}.txt"
        )

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(analysis_text)

        return file_path