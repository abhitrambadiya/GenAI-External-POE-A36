document.addEventListener("DOMContentLoaded", () => {
    const researchForm = document.getElementById("research-form");
    const questionInput = document.getElementById("question-input");
    const submitBtn = document.getElementById("submit-btn");
    const loadingSpinner = document.getElementById("loading-spinner");
    const btnText = submitBtn.querySelector(".btn-text");
    const clearBtn = document.getElementById("clear-btn");
    const resultsArea = document.getElementById("results-area");
    const answerContent = document.getElementById("answer-content");
    const sourcesList = document.getElementById("sources-list");
    const disclaimerText = document.getElementById("disclaimer-text");
    const healthDot = document.getElementById("health-dot");
    const healthText = document.getElementById("health-text");

    // Progress items
    const prog1 = document.getElementById("prog-1");
    const prog2 = document.getElementById("prog-2");
    const prog3 = document.getElementById("prog-3");

    // Check system health on load
    async function checkHealth() {
        try {
            const resp = await fetch("/health");
            if (resp.ok) {
                const data = await resp.json();
                healthDot.className = "status-dot healthy";
                healthText.textContent = `Online • Model: ${data.model} • ${data.agents.length} Agents Active`;
            } else {
                throw new Error("Health check non-200");
            }
        } catch (err) {
            healthDot.className = "status-dot error";
            healthText.textContent = "Service degraded or API key unconfigured";
        }
    }
    checkHealth();

    // Chip click handlers
    document.querySelectorAll(".chip").forEach(chip => {
        chip.addEventListener("click", () => {
            questionInput.value = chip.getAttribute("data-query");
            questionInput.focus();
        });
    });

    // Clear handler
    clearBtn.addEventListener("click", () => {
        questionInput.value = "";
        resultsArea.classList.add("hidden");
    });

    // Helper to format simple markdown if marked is unavailable
    function formatMarkdown(text) {
        if (window.marked && typeof window.marked.parse === "function") {
            return window.marked.parse(text);
        }
        return text
            .replace(/^### (.*$)/gim, '<h3>$1</h3>')
            .replace(/^## (.*$)/gim, '<h2>$1</h2>')
            .replace(/^# (.*$)/gim, '<h1>$1</h1>')
            .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/gim, '<em>$1</em>')
            .replace(/`(.*?)`/gim, '<code>$1</code>')
            .replace(/\n\n/gim, '<p></p>')
            .replace(/\n/gim, '<br>');
    }

    // Submit handler
    researchForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const question = questionInput.value.trim();

        if (question.length < 5) {
            alert("Please enter a research question of at least 5 characters.");
            return;
        }

        // UI Loading state
        submitBtn.disabled = true;
        btnText.textContent = "Analyzing Inquiry...";
        loadingSpinner.classList.remove("hidden");
        resultsArea.classList.remove("hidden");

        // Reset progress animation
        prog1.className = "progress-item active";
        prog2.className = "progress-item";
        prog3.className = "progress-item";
        answerContent.innerHTML = "<p><em>Coordinating Query Analyzer, Research Agent, and Answer Reviewer...</em></p>";
        sourcesList.innerHTML = "";
        disclaimerText.textContent = "";

        const timer1 = setTimeout(() => {
            prog1.className = "progress-item completed";
            prog2.className = "progress-item active";
        }, 1200);

        const timer2 = setTimeout(() => {
            prog2.className = "progress-item completed";
            prog3.className = "progress-item active";
        }, 2800);

        try {
            const response = await fetch("/ask", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ question })
            });

            clearTimeout(timer1);
            clearTimeout(timer2);
            prog1.className = "progress-item completed";
            prog2.className = "progress-item completed";
            prog3.className = "progress-item completed";

            const data = await response.json();

            if (!response.ok) {
                const detail = data.detail || "An error occurred during multi-agent analysis.";
                answerContent.innerHTML = `<div style="color: #dc2626; padding: 1rem; background: #fee2e2; border-radius: 8px;"><strong>Analysis Error:</strong> ${detail}</div>`;
                return;
            }

            // Render synthesized answer
            answerContent.innerHTML = formatMarkdown(data.answer);

            // Render consulted sources
            if (data.sources && data.sources.length > 0) {
                sourcesList.innerHTML = data.sources.map(s => `<li>📄 ${s}</li>`).join("");
            } else {
                sourcesList.innerHTML = "<li>No external library documents cited.</li>";
            }

            // Render disclaimer
            disclaimerText.textContent = data.disclaimer;

        } catch (error) {
            answerContent.innerHTML = `<div style="color: #dc2626; padding: 1rem; background: #fee2e2; border-radius: 8px;"><strong>Network Error:</strong> Failed to communicate with FastAPI backend server (${error.message}).</div>`;
        } finally {
            submitBtn.disabled = false;
            btnText.textContent = "Run Multi-Agent Research";
            loadingSpinner.classList.add("hidden");
        }
    });
});
