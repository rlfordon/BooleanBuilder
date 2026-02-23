# Legal Boolean Search Builder

An interactive, single-page web tool designed to help law students, legal researchers, and practitioners build powerful and precise Boolean search strings for legal databases like Westlaw, LexisNexis, and Bloomberg Law.

This tool demystifies the process of creating complex queries by guiding the user through a logical, step-by-step workflow, inspired by best practices in legal research methodology.

Access at: [https://booleanbuilder.replit.app/](https://booleanbuilder.replit.app/).


## The Problem It Solves

Boolean search with terms and connectors is the gold standard for precision in legal research, but the syntax can be complex and unforgiving. Novice researchers often struggle with parentheses, proximity connectors, and truncation, leading to frustrating and inaccurate search results. This tool acts as an interactive "wizard," handling the syntax so the researcher can focus on the concepts.

## Features

-   **Step-by-Step Concept Building:** Break down a research question into core concepts, with each concept group automatically wrapped in parentheses `()`.
-   **Guided Brainstorming:** Contextual tips encourage users to add alternate terms and synonyms, which are automatically joined with the `OR` connector.
-   **Smart Phrase Suggestions:** Automatically converts multi-word phrases (e.g., "assumption of risk") into a more flexible proximity search (e.g., `(assumption /3 risk)`), filtering out common stop words.
-   **Interactive Truncation Helper:** A word-by-word helper assists users in finding the correct root for truncation (`!`), preventing overly broad or narrow stems.
-   **Clear Connector Choices:** A highly visible button-based interface with hover tips makes it easy to choose between `AND`, `/p` (same paragraph), and `/s` (same sentence).
-   **Live Search String Preview:** See your Boolean query being built in real-time in a dedicated output panel.
-   **Final Review Checklist:** An interactive checklist guides users through a final review of their search string to ensure proper grouping, truncation, and connector usage before running the search.
-   **Single-File Application:** The entire tool is self-contained in a single HTML file, requiring no installation or dependencies.

## How to Use

1.  **Open the File:** Download the `boolean_search_builder.html` file and open it in any modern web browser. Or access at [https://booleanbuilder.replit.app/](https://booleanbuilder.replit.app/).
2.  **Build Your First Concept:** Start by typing your first key term or phrase into the "Concept 1" input box.
3.  **Add Alternate Terms:** Use the `+ Add alternate term (OR)` button to add synonyms or related keywords for that concept.
4.  **Get Help with Truncation:** Click the `Build a Truncated Term` button to open a helper that suggests a truncated root based on variations you provide.
5.  **Add More Concepts:** Click the `+ Add Concept Group` button to create a new concept.
6.  **Connect Your Concepts:** Use the `AND`, `/p`, or `/s` buttons that appear between concept groups to define how they relate to each other.
7.  **Review Your String:** As you work, your complete Boolean search string is built in the "Your Search String" panel on the right.
8.  **Copy and Search:** Once you are satisfied, use the "Copy" button to copy the string to your clipboard and paste it into your legal research platform's advanced search bar.

## Technology Stack

-   **HTML5:** For the core structure of the application.
-   **Tailwind CSS:** For modern, responsive styling.
-   **JavaScript (ES6):** For all interactive logic and DOM manipulation, with no external libraries or frameworks.

## Acknowledgments

A special thank you Charlie Amiot and Debbie Ginsberg for their invaluable feedback, ideas, and testing that helped shape this tool. 

## Contributing

Suggestions, bug reports, and pull requests are welcome! If you have an idea for a new feature or an improvement, please open an issue to start a discussion.
