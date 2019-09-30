$(document).ready(function() {

    var score = 0;
    $(".btn").click(function(e) {
        
        $.ajax ({
            data: {
                button_name: this.name,
                image_src: $('img').attr('src')
            },
            type: 'POST',
            url: '/process'
        }).done(function(data) {
            if (data.button_name != data.image_name) {
                // if the user lost
                alert('Your score was ' + score + '. Press OK to play again.');
                location.reload();   
            }
            else {
                // increment score if the user choose the right button
                score = score + 1;
                $('img').attr('src', data.next_picture);
            }
        });
    });   
});