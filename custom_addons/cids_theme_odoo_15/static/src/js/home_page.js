odoo.define("cids_theme_odoo_15.cidsdes", function (require) {
    var ajax = require("web.ajax");
    var core = require('web.core');

   $(document).ready(function() {
            var nav = $('.nav-bar');
            $('#wrapwrap').scroll(function () {
                if ($(this).scrollTop() > 50) {
                    nav.addClass("f-nav");
                } else {
                    nav.removeClass("f-nav");
                }
            });
   })
   



          $(document).ready(function () {
            var owl = $('.owl-carousel.tpbanner');
            owl.owlCarousel({
                margin: 10,
                nav: true,
                autoplay: true,
                animateOut: 'zoomOut',
                animateIn: 'fadeIn',
                loop: true,
                autoplayTimeout: 4000,
                autoplaySpeed: 1500,

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

        $("document").ready(function () {
            $('.humburger').click(function(){
               $('.menu').toggleClass('mobileMenu');
               
            });
        });
        $(document).ready(function () {
            var owl4 = $('.owl-carousel.address');
            owl4.owlCarousel({
                margin: 10,
                nav: true,
                autoplay: false,
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
            $(".addholder .owl-prev").html('<img src="/cids_theme_odoo_15/static/src/img/images/footerLeft.png"/>');
            $(".addholder .owl-next").html('<img src="/cids_theme_odoo_15/static/src/img/images/footerRight.png"/>');
           
        });

        $(document).ready(function () {
            var owl5 = $('.owl-carousel.aboutcarsouel');
            owl5.owlCarousel({
                margin: 0,
                nav: true,
                autoplay: true,
                loop: true,
                slideTransition: 'linear',
            autoplayTimeout: 4000,
            autoplaySpeed: 1500,
            autoplayHoverPause: true,
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
        });

        $(document).ready(function () {
            var owl6 = $('.owl-carousel.hotelServicesCarsouel');
            owl6.owlCarousel({
                margin: 0,
                nav: true,
                autoplay: false,
                loop: true,

                responsive: {
                    0: {
                        items: 1
                    },
                    769: {
                        items: 3
                    },
                    1000: {
                        items: 4
                    }
                }
            });
            $(".hotel-services .owl-prev").html('<img src="/cids_theme_odoo_15/static/src/img/images/Left.png"/>');
            $(".hotel-services .owl-next").html('<img src="/cids_theme_odoo_15/static/src/img/images/Right.png"/>');
        });

        $(document).ready(function () {
            var owl7 = $('.owl-carousel.hotelCaseCarsouel');
            owl7.owlCarousel({
                margin: 32,
                nav: true,
                
                autoplay: false,
                loop: true,

                responsive: {
                    0: {
                        items: 1
                    },
                    769: {
                        items: 1,
                        stagePadding:0
                    },
                    1000: {
                        items: 1,
                        stagePadding: 170,
                    }
                }
            });
            $(".hotel-case .owl-prev").html('<img src="/cids_theme_odoo_15/static/src/img/images/Left.png"/>');
            $(".hotel-case .owl-next").html('<img src="/cids_theme_odoo_15/static/src/img/images/Right.png"/>');
        });

        $(document).ready(function () {
            var owl8 = $('.owl-carousel.hotelClientCarsouel');
            owl8.owlCarousel({
                margin: 150,
                nav: true,
                autoplay: true,
                loop: true,
                autoplayTimeout: 4000,
            autoplaySpeed: 3500,
            autoplayHoverPause: true,

                responsive: {
                    0: {
                        items: 3
                    },
                    769: {
                        items: 4
                    },
                    1000: {
                        items: 4
                    }
                }
            });
        });

        $(document).ready(function () {
            var owl9 = $('.owl-carousel.clientFeedbackCarsouel');
            owl9.owlCarousel({
                margin: 0,
                nav: true,
               
                autoplay: false,
                loop: true,

                responsive: {
                    0: {
                        items: 1
                    },
                    769: {
                        items: 1,
                        stagePadding:0
                    },
                    1000: {
                        items: 1,
                        stagePadding: 170,
                    }
                }
            });
            $(".client-feedback .owl-prev").html('<img src="/cids_theme_odoo_15/static/src/img/images/whiteLeft.png"/>');
            $(".client-feedback .owl-next").html('<img src="/cids_theme_odoo_15/static/src/img/images/whiteRight.png"/>');
        });

  
})
