const text = $('#post-input-text').val();
const username =$('#author-username').val();
const  submit = $('#post-submission');
const form = $('#post-form');
form.submit(function (event) {
    console.log(text)
    //event.preventDefault();
    $.ajax({
        data:{
            'text': text,
            'author': username
        },
        url: "/submit-post",
        success: function () {
            console.log('you posted');
            text.val('')
        },
        fail: function () {
            console.log('posting failed')
        }
    }
    )

});

