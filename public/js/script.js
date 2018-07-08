//LOGIN
$('#login-button').on('click', function(){
    $('.login-modal-wrap').css('display', 'block')
    $('.login-modal').animate({
        marginTop: '15%'
    }, 500)
    $('.login-modal-wrap').animate({
        backgroundColor: 'rgba(0,0,0,0.7)'
    }, 500)
});

$('#login-button').on('mouseover', function(){
    $(this).css('cursor', 'pointer')
    $(this).css('text-decoration', 'underline')
})

loginmodal = document.getElementById('loginmodal')

window.onclick = function(event){
	if(event.target == loginmodal){
        $('.login-modal').animate({
            marginTop: '-800px'
        }, 300, function(){
            $('.login-modal-wrap').css('display', 'none')
        })
}}


//RATINGS
$('.category-ratings-wrap').on('click', function(){
    $(this).css('background-color', 'red')
})

//FIRST STEPS animation
$(document).ready(function(){
    setTimeout(function(){
        $('.first-first').css('display', 'block')
        $('.first-first').addClass('animated fadeInUp')},500);
    setTimeout(function(){
        $('.first-second').css('display', 'block')
        $('.first-second').addClass('animated fadeInUp')}, 1000);
    setTimeout(function(){
        $('.first-third').css('display', 'block')
        $('.first-third').addClass('animated fadeInUp')}, 1500);
    setTimeout(function(){
        $('.first-fourth').css('display', 'block')
        $('.first-fourth').addClass('animated fadeInUp')}, 2000)
    setTimeout(function(){
        $('.first-first').addClass('animated fadeOutUp')
        $('.first-second').addClass('animated fadeOutUp')
        $('.first-third').addClass('animated fadeOutUp')
        $('.first-fourth').addClass('animated fadeOutUp')
    }, 5000)
    setTimeout(function(){
        $('#call-to-action').css('display', 'block')
        $('.registration-button-animated').css('display', 'block')
        $('#call-to-action').animate({
            marginTop: '-40%'
        }, 500)
    }, 5750)
    setTimeout(function(){
        $('.stationary-cart').animate({
            opacity: '1'
        }, 1500)
    })

})


//ANIMATION FOR MI PERFIL
$('#firstImg').on("mouseover", function(){
    $(this).addClass('animated fadeOutUp')
    setTimeout(function(){$('#firstImg2').addClass('animated fadeInUp')}, 500)
    setTimeout(function(){$('#firstImg2').css('display', 'block')}, 675)
    $('#firstAdd').css('display', 'block')
    $('.btn-warning').css('display', 'block')
    $('#firstAdd').animate({
        marginTop: '-200px'
    }, 1000)

})



//RATING
//$('.rating-wrapper').on('click', function(){
    $(this).css('background-color', '#ff8702')
//})