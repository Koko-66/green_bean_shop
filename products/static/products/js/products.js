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

    // Preselect the first color in the product detail and all products views
    $('.color-selector').each(function(index){
        $(this).find('*').filter(':input:first').attr("checked", true);
        $(this).find('*').filter(':input:first').attr("required", true);
    });
    // Preselect size M in the product detail and all products views
    $('.size-selector').each(function(index){
        // $(this).find('*').filter(':input:first').attr("checked", true);
        $(this).find('*').filter(':input[value="M"]').attr("checked", true);
        $(this).find('*').filter(':input:first').attr("required", true);
    });
    // clear selected filters in filters pop up
    $('#clear-filters').click(function(event){
        $("input[type='radio']").prop("checked", false);
    }) 
})