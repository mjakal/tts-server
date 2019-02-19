$(document).ready(function () {
    
    // Speak text api
    $('#appForm').on('submit', function (event) {
        event.preventDefault();
        var voiceData = $('#voiceInput').val();
        var textData = $('#textInput').val();

        $.ajax({
            url: "/api/v1/speak",
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

    // Get the list of installed voices api
    $.ajax({
        url: "/api/v1/voices",
        method: 'GET',
        success: function (voices) {
            var selectVoice = $("#voiceInput");
            
            selectVoice.append('<option value="">Select Voice</option>');
            voices.forEach(function (voice) {
                selectVoice.append('<option value="' + voice + '">' + voice + '</option>');
            });
        },
        error: function (error) {
            var selectVoice = $("#voiceInput");
            
            selectVoice.append('<option value="">No voices found...</option>');
        }
    });

});