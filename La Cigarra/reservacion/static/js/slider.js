$(document).ready(function() {
    $(".slider").slick({
      dots: true,
      arrows: true,
      prevArrow: '<div class="slider-arrow prev"><i class="fas fa-arrow-left"></i></div>',
      nextArrow: '<div class="slider-arrow next"><i class="fas fa-arrow-right"></i></div>',
      autoplay: true,
      autoplaySpeed: 3000,
    });
  });
  