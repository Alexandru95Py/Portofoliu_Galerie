window.onload = function () {
    console.log("Script home.js a fost încărcat!");

    const typingElement = document.getElementById("typing-text");

    if (!typingElement) {
        console.error("Eroare: Nu am găsit elementul cu id='typing-text'");
        return;
    }

    console.log("Element typing-text găsit:", typingElement);

    const text = "Bine ai venit pe pagina mea!";
    let index = 0;

    function typeEffect() {
        if (index < text.length) {
            typingElement.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeEffect, 100);
        }
    }

    typeEffect();
};

