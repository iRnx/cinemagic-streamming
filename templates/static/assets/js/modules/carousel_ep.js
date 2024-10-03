$('.slick-carousel').slick({
    infinite: false,
    slidesToShow: 5,
    slidesToScroll: 5,
    responsive: [
{
    breakpoint: 1500,
    settings: {
    slidesToShow: 4,
    slidesToScroll: 4,
    infinite: false,
    }
},

{
    breakpoint: 1300,
    settings: {
    slidesToShow: 3,
    slidesToScroll: 3,
    infinite: false,
    }
},

{
    breakpoint: 992,
    settings: {
    slidesToShow: 2,
    slidesToScroll: 2,
    infinite: false,
    }
},

{
    breakpoint: 595,
    settings: {
    slidesToShow: 1,
    slidesToScroll: 1,
    infinite: false,
    }
},

]
});
