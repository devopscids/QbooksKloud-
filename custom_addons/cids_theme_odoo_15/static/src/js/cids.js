odoo.define("cids_theme_odoo_15.cidsdes", function (require) {
    var ajax = require("web.ajax");
    var core = require('web.core');
   $(document).ready(function() {
   console.log("aman");
                var owl = $('.owl-carousel.designwork');
                owl.owlCarousel({
                  margin: 10,
                  nav: true,
                  autoplay:true,
                  loop: true,
                  responsive: {
                    0: {
                      items: 2
                    },
                    600: {
                      items: 3
                    },
                    1000: {
                      items: 4
                    }
                  }
                })
              });

               $(document).ready(function() {
                var owl1 = $('.owl-carousel.testimonial');
                owl1.owlCarousel({
                  margin: 10,
                  nav: true,
                  autoplay:true,
                  loop: true,
                  responsive: {
                    0: {
                      items: 1
                    },
                    600: {
                      items: 1
                    },
                    1000: {
                      items: 1
                    }
                  }
                });
                 $( ".owl-prev").html('<img src="https://dev.cids.design/web/image/1433-e2b28c47/Element-arrow-2.svg"/>');
   $( ".owl-next").html('<img src="https://dev.cids.design/web/image/1433-e2b28c47/Element-arrow-2.svg"/>');
              });

               $(document).ready(function() {
                 var owl2 = $('.owl-carousel.services');
                owl2.owlCarousel({
                 center:true,
                 margin: 20,
                 nav: true,



  items:2,
  loop:true,
  margin:10,
  animateOut: 'slideInLeft',
  animateIn: 'slideOutRight',
  stagePadding: 50,
                  responsive: {
                    0: {
                      items: 1
                    },
                    600: {
                      items: 2
                    },
                    1000: {
                      items: 2
                    }
                  }
                  })
              });



               $(document).ready(function() {
                var owl3 = $('.owl-carousel.luxuryCarsiuel');
                owl3.owlCarousel({
                  margin: 10,
                  nav: true,
                  autoplay:true,
                  loop: true,
                  responsive: {
                    0: {
                      items: 1
                    },
                    600: {
                      items: 1
                    },
                    1000: {
                      items: 1
                    }
                  }
                });
                 $( ".owl-prev").html('<img src="https://dev.cids.design/web/image/1433-e2b28c47/Element-arrow-2.svg"/>');
   $( ".owl-next").html('<img src="https://dev.cids.design/web/image/1433-e2b28c47/Element-arrow-2.svg"/>');
              });

              $(document).ready(function() {
                var owl4 = $('.owl-carousel.address');
                owl4.owlCarousel({
                  margin: 10,
                  nav: true,
                  autoplay:false,
                  loop: true,

                  responsive: {
                    0: {
                      items: 1
                    },
                    769: {
                      items: 1
                    },
                    1000: {
                      items: 1
                    }
                  }
                });
                 $( ".owl-prev").html('<img src="https://dev.cids.design/web/image/1433-e2b28c47/Element-arrow-2.svg"/>');
   $( ".owl-next").html('<img src="https://dev.cids.design/web/image/1433-e2b28c47/Element-arrow-2.svg"/>');
              });



               $(document).ready(function() {
                var owl5 = $('.owl-carousel.bannerwork');
                owl5.owlCarousel({
                  margin: 10,
                  nav: true,
                  autoplay:true,
                  loop: true,
                  responsive: {
                    0: {
                      items: 1
                    },
                    600: {
                      items: 1
                    },
                    1000: {
                      items: 1
                    }
                  }
                })
              });

               $(document).ready(function() {

               $('.humburger').click(function(){

               	$('.header-links a').each(function(index, element) {
			    	    $(element).delay(index*100).hide().fadeToggle(2000);
			    	    });

			    	  $('.header-links').toggleClass('swichmenu');

               });
               });

               $(document).ready(function() {
                var owl5 = $('.owl-carousel.bannerwork');
                owl5.owlCarousel({
                  margin: 10,
                  nav: true,
                  autoplay:true,
                  loop: true,
                  responsive: {
                    0: {
                      items: 1
                    },
                    600: {
                      items: 1
                    },
                    1000: {
                      items: 1
                    }
                  }
                });
                 $( ".owl-prev").html('<img src="https://dev.cids.design/web/image/1433-e2b28c47/Element-arrow-2.svg"/>');
   $( ".owl-next").html('<img src="https://dev.cids.design/web/image/1433-e2b28c47/Element-arrow-2.svg"/>');
              });

            $(document).ready(function() {
                var owl5 = $('.owl-carousel.happyclients');
                owl5.owlCarousel({
                  margin: 10,
                  nav: true,
                  autoplay:true,
                  loop: true,
                  responsive: {
                    0: {
                      items: 1
                    },
                    600: {
                      items: 1
                    },
                    1000: {
                      items: 1
                    }
                  }
                });
                 $( ".owl-prev").html('<img src="https://dev.cids.design/web/image/1985-a075e29e/abutarrow.png"/>');
   $( ".owl-next").html('<img src="https://dev.cids.design/web/image/1985-a075e29e/abutarrow.png"/>');
              });


 $(document).ready(function() {
    $('.gallery').mauGallery({
        columns: {
            xs: 1,
            sm: 2,
            md: 3,
            lg: 4,
            xl: 3
        },
        lightBox: true,
        lightboxId: 'myAwesomeLightbox',
        showTags: true,
        tagsPosition: 'top'
    });
});

})