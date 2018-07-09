const  submit = $('#post-submission');
const form = document.getElementById('post-form');

$('#post-form').submit(function(event) {
    event.preventDefault();

    const text = $('#post-input-text').val();
    const username =$('#author-username').val();
    console.log(text)

    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: "/submit",
        data:{
            'text': text,
            'author': username,
        },
        success: function (data) {
            console.log('you posted');
            text.val('');
            console.log(data)
        },
        fail: function () {
            console.log('posting failed')
        }
    });

});

