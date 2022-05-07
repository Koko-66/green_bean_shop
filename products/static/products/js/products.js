
// Code taken and adapted from CI Boutique Ado walkthrough
$(document).ready(function () {
    // scroll to the top (from Boutique Ado walkthrough)
    $(".btt-link").click(function(e){
        window.scrollTo(0,0)
    }) 
    // sort the content based on criteria passed in the url
    // (from Boutique Ado walkthrough)
    $("#sort-selector").change(function() {
        let selector = $(this);
        let currentUrl = new URL(window.location);

        let selectedValue = selector.val();
        console.log(selectedValue)
        if(selectedValue != "reset"){
            let sort_type = selectedValue.split("-")[0];
            let direction = selectedValue.split("-")[1];

            currentUrl.searchParams.set("sort", sort_type);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.set("sort");
            currentUrl.searchParams.set("direction");
            window.location.replace(currentUrl);
        }
    })

    // $('.circle').hover(function() {
    //     $(this).toggleClass('outline');
    // });
    // Preselect the first size and color in the product detai view
    $('.color-selector').each(function(index){
        $(this).find('*').filter(':input:first').attr("checked", true);
        $(this).find('*').filter(':input:first').attr("required", true);
    });

    $('.size-selector').each(function(index){
        // $(this).find('*').filter(':input:first').attr("checked", true);
        $(this).find('*').filter(':input[value="M"]').attr("checked", true);
        $(this).find('*').filter(':input:first').attr("required", true);
    });
})