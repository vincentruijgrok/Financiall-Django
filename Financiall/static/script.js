function markAllNegativeAmountsRed() {
    document.querySelectorAll(".amount").forEach((element) => {
        if (element.innerHTML.includes("€-")) {
            element.style.color="red";
        }
    })
}

document.addEventListener("DOMContentLoaded", () => {
    markAllNegativeAmountsRed();
})
