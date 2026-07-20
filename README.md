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
-   **Clear Connector Choices:** A highly visible button-based interface makes it easy to choose between `AND`, `/p` (same paragraph), and `/s` (same sentence), with explanatory tips that appear on hover *or keyboard focus*.
-   **Live Search String Preview:** See your Boolean query being built in real-time in a dedicated output panel.
-   **Final Review Checklist:** An interactive checklist guides users through a final review of their search string to ensure proper grouping, truncation, and connector usage before running the search.
-   **Genuinely Single-File:** Markup, styles, and logic are self-contained in one HTML file. No installation, no build step to run it, and no network requests at all — it works offline, from a thumb drive, on a plane.
-   **Accessible:** Built to WCAG 2.1 AA. See below.

## How to Use

1.  **Open the File:** Download `index.html` and open it in any modern web browser — no install, no server, no internet connection required. Or access at [https://booleanbuilder.replit.app/](https://booleanbuilder.replit.app/).
2.  **Build Your First Concept:** Start by typing your first key term or phrase into the "Concept 1" input box.
3.  **Add Alternate Terms:** Use the `+ Add alternate term (OR)` button to add synonyms or related keywords for that concept.
4.  **Get Help with Truncation:** Click the `Build a Truncated Term` button to open a helper that suggests a truncated root based on variations you provide.
5.  **Add More Concepts:** Click the `+ Add Concept Group` button to create a new concept.
6.  **Connect Your Concepts:** Use the `AND`, `/p`, or `/s` buttons that appear between concept groups to define how they relate to each other.
7.  **Review Your String:** As you work, your complete Boolean search string is built in the "Your Search String" panel on the right.
8.  **Copy and Search:** Once you are satisfied, use the "Copy" button to copy the string to your clipboard and paste it into your legal research platform's advanced search bar.

## Technology Stack

-   **HTML5:** For the core structure of the application.
-   **Tailwind CSS (precompiled):** Only the ~180 utilities this page actually uses are generated and inlined, so there is no CDN runtime fetched at page load.
-   **JavaScript (ES6):** For all interactive logic and DOM manipulation, with no external libraries or frameworks.

## Accessibility

The tool targets **WCAG 2.1 Level AA**. This matters if you work at a public institution: DOJ's April 2024 Title II rule adopts WCAG 2.1 AA as the technical standard for state and local government entities, which includes public universities and government libraries.

-   Every control has a meaningful accessible name, including the dynamically generated term inputs, which are labelled by position ("Concept 2, alternate term 3") and renumber as concepts are added and removed.
-   The generated search string is announced through a polite live region, debounced so screen reader users hear the settled string rather than one fragment per keystroke.
-   All tips and explanations are reachable by keyboard, not hover only.
-   The truncation helper is a proper modal dialog: it traps Tab, closes on Escape, and returns focus to the control that opened it.
-   All text and focus indicators meet or exceed AA contrast.

**Caveat, stated plainly:** this was verified programmatically and by keyboard, *not* with a real screen reader. If you use NVDA, JAWS, VoiceOver, or anything else and something reads badly, please open an issue — that feedback is worth more than the audit.

## Development

The Tailwind utilities are generated at build time rather than fetched from a CDN. If you add or change a Tailwind class, regenerate the stylesheet:

```bash
printf '@tailwind base;\n@tailwind components;\n@tailwind utilities;\n' > in.css
npx tailwindcss@3 -i in.css -o out.css --minify --content index.html
```

then replace the contents of the generated `<style>` block in `index.html` with the new `out.css`.

## Acknowledgments

A special thank you Charlie Amiot and Debbie Ginsberg for their invaluable feedback, ideas, and testing that helped shape this tool. 

## Contributing

Suggestions, bug reports, and pull requests are welcome! If you have an idea for a new feature or an improvement, please open an issue to start a discussion.
