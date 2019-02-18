$(document).ready(function () {
    $('#appForm').on('submit', function (event) {
        event.preventDefault();
        var voiceData = $('#voiceInput').val();
        var textData = $('#textInput').val();

        $.ajax({
            url: "/speak",
            method: 'POST',
            data: {
                voice: voiceData,
                text: textData
            },
            success: function (data) {
                console.log('Success!');
            },
            error: function (error) {
                console.log('API request failed.');
            }
        });
    });
});