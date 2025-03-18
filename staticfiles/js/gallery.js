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
            img.style.width = "100%";
            img.style.height = "100%";
            img.style.ObjectPosition = "center";
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

