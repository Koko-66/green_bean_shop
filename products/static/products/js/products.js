
console.log('hello world')
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

})
