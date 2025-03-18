document.addEventListener("DOMContentLoaded" , function () {
    console.log("Galerie Incarcata!");

    let gallery = document.querySelector(".gallery-container");

    if(gallery) {
        gallery.style.display = "grid";
        gallery.style.gridTemplateColumns = "repeat(3, 1fr)";
        gallery.style.gap = "20px";
        gallery.style.JustifyContent = "center";
        gallery.style.paddingBottom = "30px";

        document.querySelectorAll(".gallery-img").forEach(img => {
           img.style.width ="100%";
           img.style.height = "400px";
           img.style.objectFit = "cover";
           img.style.objectPosition = "center";
           img.style.display = "block";
        });
    }
        document.querySelectorAll(".gallery-img").forEach(img => {
            img.addEventListener("mouseenter", function () {
                this.style.transform = "scale(1.05)";
                this.style.transition = "0.9 ease-to-out"

        });
        img.addEventListener("mouseleave", function () {
            this.style.transform = "scale(1)";
        });

        document.querySelector(".like-btn").addEventListener("click", function() {
            this.classList.toggle("liked");  //adauga sau elimina clasa liked

        });

    });
});

document.addEventListener("DOMContentLoaded", function () {
    console.log("Galerie încărcată!"); // ✅ Verifică dacă JavaScript-ul este încărcat

    document.querySelectorAll(".like-btn").forEach(button => {
        button.addEventListener("click", function () {
            let tablouId = this.dataset.tablouId;  // ✅ Extrage ID-ul tabloului
            console.log("DEBUG: tablouId =", tablouId); // ✅ Verifică în consolă dacă este corect

            if (!tablouId) {
                console.error("EROARE: tablouId este undefined!");
                return;  // 🚨 Oprire dacă tablouId nu există
            }

            let likeCount = document.querySelector(`#like-count-${tablouId}`);
            if (!likeCount) {
                console.error("EROARE: Elementul #like-count-${tablouId} nu a fost găsit în DOM!");
                return;
            }

            let csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
            let csrfToken = csrfTokenElement ? csrfTokenElement.value : "";

            console.log(`Trimit request la: /like/${tablouId}/`)
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
                if (data.liked) {
                    this.classList.add("liked");
                } else {
                    this.classList.remove("liked");
                }
                likeCount.textContent = data.like_count;  // ✅ Actualizează numărul de like-uri
            })
            .catch(error => {
                console.error("Eroare fetch:, error");
                alert("A apartu o eroare. Verifica consola pentru detalii");
            })
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Selectează toate formularele de comentarii
    document.querySelectorAll(".comment-form").forEach(form => {
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Previne reîncărcarea paginii la trimiterea formularului

            // Obține tablouId din action sau dintr-un data-atribut
            let action = this.getAttribute("action");
            let tablouId = this.getAttribute("data-tablou-id"); // Alternativ

            // Dacă nu există în action, încearcă să îl ia dintr-un data-atribut
            if (!tablouId && action) {
                tablouId = action.split("/").filter(Boolean).pop();
            }

            console.log("Action:", action);
            console.log("Tablou ID extras:", tablouId);

            if (!tablouId) {
                console.error("Eroare: Tablou ID nu a fost găsit.");
                return;
            }

            // Obține datele din formular
            let formData = new FormData(this);
            let csrfTokenElement = document.querySelector("[name=csrfmiddlewaretoken]");
            let csrfToken = csrfTokenElement? csrfTokenElement.value : null;
            
            if (!csrfToken) {
                console.error("Eroare: Tokenul csrf nu a fost gasit in HTML!");
                return;
            }

            // Trimite cererea AJAX către server
            console.log("Trimit date catre server:", {
                tablouId: tablouId,
                formData: Object.fromEntries(formData)
            })
            fetch(`/galerie/comentariu/${tablouId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log("Răspuns server:", data);  // ✅ Afișează răspunsul serverului în consolă
                if (data.success) {
                    let comentariiContainer = document.querySelector(`#comments-${tablouId}`);

                    console.log("Container de comentarii cautat:", `#comments-${tablouId}`);
                    console.log("Container de comentarii gasit:", comentariiContainer);

                    if (!comentariiContainer) {
                        console.error("Containerul de comentarii nu a fost găsit.");
                        return;
                    }
                    let nouComentariu = document.createElement("p");
                    nouComentariu.innerHTML = `<strong>${data.name}</strong>: ${data.text}`;

                    console.log("Container de comentarii gasit:", comentariiContainer);
                    if (!comentariiContainer) {
                        console.error("Eroare: Nu am gasit containerul de comentarii!");
                        return;
                    }
                    comentariiContainer.appendChild(nouComentariu);
            
                    form.reset(); // Șterge conținutul formularului după trimitere
                } else {
                    console.error("Eroare la trimitere:", data.error);
                }
            })
            .catch(error => console.error("Eroare AJAX:", error));
        });
    });
});