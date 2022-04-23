// Adjust color of Coutry field in the form
// Code from CI Boutique Ado walkthrough project
let countrySelected = $('.default-country').val();
console.log(countrySelected);
if(!countrySelected) {
    $('.default-country').css('color', '#6c757d');
};
$('.default-country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#6c757d');
    } else {
        $(this).css('color', '#000');
    }
});