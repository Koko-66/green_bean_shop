// Adjust color of Coutry field in the form
// Code from CI Boutique Ado walkthrough project
let countrySelected = $('#default_country').val();
if(!countrySelected) {
    $('#default_country').css('color', '#6c757d');
};
$('#default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#6c757d');
    } else {
        $(this).css('color', '#000');
    }
});