odoo.define("cids_theme_odoo_15.cidsdes", function (require) {
    var ajax = require("web.ajax");
    var core = require('web.core');
   $(document).ready(function (){
            var owl = $('.owl-carousel.tpbanner');
            owl.owlCarousel({
                margin: 10,
                nav: true,
                autoplay: true,
                animateOut: 'zoomOut',
                animateIn: 'fadeIn',
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

        });
   $(document).ready(function () {
            var owl5 = $('.owl-carousel.aboutcarsouel');
            owl5.owlCarousel({
                margin: 0,
                nav: true,
                autoplay: true,
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
            $(".owl-prev").html('<img src="/cids_theme_odoo_15/static/src/img/images/Left.png"/>');
            $(".owl-next").html('<img src="/cids_theme_odoo_15/static/src/img/images/Right.png"/>');
        });
   $(document).ready(function () {
            var owl7 = $('.owl-carousel.hotelCaseCarsouel');
            owl7.owlCarousel({
                margin: 32,
                nav: true,
                stagePadding: 170,
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
            $(".owl-prev").html('<img src="/cids_theme_odoo_15/static/src/img/images/Left.png"/>');
            $(".owl-next").html('<img src="/cids_theme_odoo_15/static/src/img/images/Right.png"/>');
        });
   $(document).ready(function () {
            var owl8 = $('.owl-carousel.hotelClientCarsouel');
            owl8.owlCarousel({
                margin: 150,
                nav: true,
                autoplay: false,
                loop: true,

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


})
   $(document).ready(function () {
            var owl9 = $('.owl-carousel.clientFeedbackCarsouel');
            owl9.owlCarousel({
                margin: 0,
                nav: true,
                stagePadding: 170,
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
            $(".client-feedback .owl-prev").html('<img src="/cids_theme_odoo_15/static/src/img/images/whiteLeft.png"/>');
            $(".client-feedback .owl-next").html('<img src="/cids_theme_odoo_15/static/src/img/images/whiteRight.png"/>');
        });

})
