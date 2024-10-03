// informar o botão de avançar e retroceder 15segundos
const skipBackwardBtn = container.querySelector(".skip-backward");
const skipForwardBtn = container.querySelector(".skip-forward");

function showTooltip(btn, text) {
    const tooltip = document.createElement("div");
    tooltip.className = "tooltip";
    tooltip.innerText = text;
    btn.appendChild(tooltip);

    const rect = btn.getBoundingClientRect();
    tooltip.style.top = `${rect.top - tooltip.offsetHeight}px`;
    tooltip.style.left = `${rect.left + btn.offsetWidth / 2 - tooltip.offsetWidth / 2}px`;
}

function hideTooltip(btn) {
    const tooltip = btn.querySelector(".tooltip");
    if (tooltip) {
        btn.removeChild(tooltip);
    }
}

skipBackwardBtn.addEventListener("mouseenter", () => {
    showTooltip(skipBackwardBtn, "Retroceder 15 segundos");
});

skipBackwardBtn.addEventListener("mouseleave", () => {
    hideTooltip(skipBackwardBtn);
});

skipForwardBtn.addEventListener("mouseenter", () => {
    showTooltip(skipForwardBtn, "Avançar 15 segundos");
});

skipForwardBtn.addEventListener("mouseleave", () => {
    hideTooltip(skipForwardBtn);
});
