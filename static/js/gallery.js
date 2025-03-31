document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript încărcat!");

    // Galerie zoom la hover
    document.querySelectorAll(".gallery-img").forEach(img => {
        img.addEventListener("mouseenter", function () {
            this.style.transform = "scale(1.05)";
            this.style.transition = "transform 0.9s ease-out";
        });
        img.addEventListener("mouseleave", function () {
            this.style.transform = "scale(1)";
        });
    });

    // Butoane de like
    document.querySelectorAll('.like-action').forEach(button => {
        button.addEventListener('click', function () {
            const tablouId = this.dataset.tablouId;
            // restul codului...
        
    
    
            console.log("DEBUG: tablouId =", tablouId);

            if (!tablouId) {
                console.error("EROARE: tablouId este undefined!");
                return;
            }

            let likeCount = document.querySelector(`#like-count-${tablouId}`);
            if (!likeCount) {
                console.error(`EROARE: Elementul #like-count-${tablouId} nu a fost găsit în DOM!`);
                return;
            }

            let csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
            let csrfToken = csrfTokenElement ? csrfTokenElement.value : "";

            fetch(`/galerie/like/${tablouId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                this.classList.toggle("liked", data.liked);
                likeCount.textContent = data.like_count;
            })
            .catch(error => {
                console.error("Eroare fetch:", error);
                alert("A apărut o eroare. Verifică consola pentru detalii.");
            });
        });
    });

    // Comentarii
    document.querySelectorAll(".comment-form").forEach(form => {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            let action = this.getAttribute("action");
            let tablouId = this.getAttribute("data-tablou-id") || action?.split("/").filter(Boolean).pop();

            if (!tablouId) {
                console.error("Eroare: tablouId nu a fost găsit.");
                return;
            }

            let formData = new FormData(this);
            let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]")?.value;

            if (!csrfToken) {
                console.error("Eroare: Tokenul CSRF nu a fost găsit.");
                return;
            }

            fetch(`/galerie/comentariu/${tablouId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    let container = document.querySelector(`#comments-${tablouId}`);
                    if (!container) {
                        console.error("Containerul de comentarii nu a fost găsit.");
                        return;
                    }

                    let nouComentariu = document.createElement("p");
                    nouComentariu.innerHTML = `<strong>${data.name}</strong>: ${data.text}`;
                    container.appendChild(nouComentariu);
                    form.reset();
                } else {
                    console.error("Eroare la trimitere:", data.error);
                }
            })
            .catch(error => console.error("Eroare AJAX:", error));
        });
    });
});