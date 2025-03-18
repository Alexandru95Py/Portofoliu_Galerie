document.addEventListener("DOMCVontentLoaded", function () {
    var portofoliuCarousel = new bootstrap.Carousel(document.querySelector("#portofoliuCarousel"), {
       interval: 300,
       wrap: true, 
    });
});